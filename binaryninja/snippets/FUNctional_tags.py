# create common tags for function attributes like leaf, loop, stub, etc

# See below for the tags variable for the various tag types created/added
large = 40
complex = 40

def init_tags():
	for tagType in tags:
		if tagType['name'] not in bv.tag_types.keys():
			bv.create_tag_type(tagType['name'], tagType['emoji'])

def cc(fn):
	nodes = len(fn.basic_blocks)
	edges = sum(len(x.outgoing_edges) for x in fn.basic_blocks)
	connected = 1 #always 1 for binary control flow graphs, kinda the whole point
	return edges - nodes + 2 * connected
		
def iscomplex(fn):
	return cc(fn) > complex

def isleaf(fn):
	return len(fn.callees) == 0

def islarge(fn):
	return len(fn.basic_blocks) >= large

def isstub(fn):
	"""Returns true if a function is likely only a stub"""
	if len(fn.basic_blocks) > 1 or len(fn.llil.basic_blocks) > 1:
		return False
	if fn.llil.basic_blocks[0].has_undetermined_outgoing_edges or len(fn.callees) == 1:
		return True
	return False

def hasloop(fn):
	"""Returns true if a function has a 'strange loop' (ignore this, inside joke)"""
	for bb in fn.basic_blocks:
		if bb in bb.dominance_frontier:
			return True
	return False

tags = [ \
{'emoji': '🍃', 'name': 'Leaf Function', 'description': 'Leaf function (does not call anything else)', 'fn': isleaf},
{'emoji': '🔄', 'name': 'Loop Function', 'description': 'Function contains a loop', 'fn': hasloop},
{'emoji': '🥾', 'name': 'Stub Function', 'description': 'Function is likely a stub (only contains one basic block and one call or indirect jump)', 'fn': isstub},
{'emoji': '🐘', 'name': 'Large Function', 'description': 'Function is "large" (IE, it has more than the blocks defined above)', 'fn': islarge},
{'emoji': '🤯', 'name': 'Complex Function', 'description': 'Function is "complex" (IE, it has a cyclomatic complexity greater than a defined constant)', 'fn': iscomplex},

]

init_tags()

for fn in bv.functions:
	for tagType in tags:
		if tagType['fn'](fn):
			fn.create_user_function_tag(bv.tag_types[tagType['name']], '', unique=True)