# load borland map
# 
# loads function and data variable symbols from Borland MAP files (https://community.embarcadero.com/article/technical-articles/149-tools/14524-understanding-linker-generated-32bit-map-files)

import re
import os

#Load symbols from a MAP file
mapfile = get_open_filename_input("filename:", "All Files (*)")
if mapfile is not None and os.access(mapfile, os.R_OK):
	with open(mapfile, "r+", encoding="utf-8") as f:
			data = f.readlines()
else:
	log_error("Unable to parse specified map file.")
	data = []

mylog = log_debug
#uncomment to enable debugging even if BN debugging is off
#mylog = log_info

segments = {}
symcount = 0
for line in data:
	line = line.strip()
	if line.startswith("0"):
		index = line.split(":")[0]
		if index in segments.keys(): #this is a record for a segment we know about
			offset = int(line.split(" ")[0].split(":")[1], 16)
			addr = offset + segments[index][0]
			symbol = line.split(" ")[-1]
			symtype=SymbolType.DataSymbol
			if symbol.endswith("()"):
				symbol = symbol[0:-2]
			if symbol.startswith("<-"):
				symbol = symbol[2:]
				symtype=SymbolType.FunctionSymbol
				contain = bv.get_functions_containing(addr)
				makenew = True
				for fn in contain: 
					if fn.start == addr: #there should not be other functions around this
						makenew = False
					else:
						mylog(f'Removed bogus prior function at {hex(fn.start)}')
						bv.remove_user_function(fn)
				if makenew:
					mylog(f'Created function at {hex(addr)}')
					bv.create_user_function(addr)
			if symbol.startswith("->:"): #call to a function, name destination
				symbol = symbol[3:]
				symtype=SymbolType.FunctionSymbol
				dest = bv.get_callees(addr)
				if len(dest) == 0: #current function hasn't been analyzed yet, extract destination from disasssembly and create destination function and symbol
					destaddr = int(bv.get_disassembly(addr).split(' ')[-1], 16)
					bv.create_user_function(destaddr)
					bv.define_user_symbol(Symbol(symtype, destaddr, symbol))
					mylog(f'Created function at {hex(destaddr)}')
					continue
				else:
					destfn = bv.get_function_at(dest[0])
					destfn.name = symbol
					mylog(f'Renamed function {symbol} as destination of call at {hex(addr)}')
			if symbol.startswith("->"):
				symbol = symbol[2:]
				continue #just a pointer to an import, skip
			if symbol.startswith("*"):
				symbol = symbol[1:]
			bv.define_user_symbol(Symbol(symtype, addr, symbol))
			mylog(f'Creating symbol {symbol} at {hex(addr)}')
			symcount += 1
		else: #new memory segment
			records = re.split('\s+', line[5:])
			base = int(records[0], 16)
			size = int(records[1][:-1], 16)
			try:
				name = records[2]
			except IndexError:
				name = 'name'
			try:
				cls = records[3]
			except IndexError:
				cls = 'class'
			if name.endswith("END") or name.endswith("END_"):
				continue
			segments[index] = [ base, size, name, cls ]
		
log_info(f'Updated {symcount} total symbols')