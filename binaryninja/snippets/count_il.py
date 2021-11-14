# IL instruction counts for a given function
#
# Walks all IL instructions at different layers, counting unique operations

from binaryninja.lowlevelil import LowLevelILInstruction 
from binaryninja.mediumlevelil import MediumLevelILInstruction 
from binaryninja.highlevelil import HighLevelILInstruction 

def visit(illest, expr, operations):
	for field in operations[expr.operation]:
		if field[1] == "expr":
			visit(illest, getattr(expr, field[0]), operations)
	illest.add(expr.operation)

llillest = set(())
mlillest = set(())
hlillest = set(())

if current_llil:
	fnname = current_function.name
	for ins in current_llil.instructions:
		visit(llillest, ins, LowLevelILInstruction.ILOperations)

if current_mlil:
	for ins in current_mlil.instructions:
		visit(mlillest, ins, MediumLevelILInstruction.ILOperations)

if current_hlil:
	for ins in current_hlil.instructions:
		visit(hlillest, ins, HighLevelILInstruction.ILOperations)

log_info("%s LLIL (%d): " % (fnname, len(llillest)))
log_info(str(llillest))
log_info("%s MLIL (%d): " % (fnname, len(mlillest)))
log_info(str(mlillest))
log_info("%s HLIL (%d): " % (fnname, len(hlillest)))
log_info(str(hlillest))
