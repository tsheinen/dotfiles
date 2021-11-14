# creates executable sections
# 
# Useful snippet for binaries without sections but executable (and writable) 
# segments. Also demonstrates triggering an analysis module after load. 
# 
# Note that the last line is unnecessary in the python console since the UI 
# triggers it after each command entered anyway.
counter=0
for seg in bv.segments:
	if seg.executable and seg.writable:
		bv.add_user_section("section_%d"%counter, seg.start, seg.end-seg.start, SectionSemantics.ReadOnlyCodeSectionSemantics)
		bv.add_analysis_option("linearsweep")
	counter += 1

bv.update_analysis()