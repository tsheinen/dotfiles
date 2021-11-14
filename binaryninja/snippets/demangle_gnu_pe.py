# demangle gnu pe
#
# Will attempt to demangle GNU mangled C++ names in a PE file since that is not automatically done

for func_sym in bv.get_symbols_of_type(SymbolType.FunctionSymbol):
	log_debug(f"Attempting to demangle {func_sym}")
	symtype, symname = demangle_gnu3(Architecture['x86'], func_sym.name)
	if symname != func_sym.name:
		log_info(f"Successfully demangled {func_sym.name}")
		if type(symname) == str:
			full_name = symname
		else:
			full_name = '::'.join(map(str, symname))
		new_sym = binaryninja.types.Symbol(SymbolType.FunctionSymbol, func_sym.address, short_name=symname[-1], full_name=full_name, raw_name=func_sym.name)
		bv.define_user_symbol(new_sym)