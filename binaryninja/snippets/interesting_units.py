# interesting units
#
# Log interesting components like the function and basic blocks with most incoming or outgoing edges

log_info("Most connected function: " + repr(max(bv.functions, key=lambda x: len(x.callees) + len(x.callers))))
log_info("Most connected bblock:   " + repr(max(bv.basic_blocks, key=lambda x: len(x.incoming_edges) + len(x.outgoing_edges))))
log_info("Highest xrefs: " + repr(max(bv.functions, key=lambda x: len(x.callers))))