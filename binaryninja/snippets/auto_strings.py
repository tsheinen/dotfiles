# auto strings
#
# automatically create string types at all detected strings

count = 0
for s in bv.strings:
	bv.define_user_data_var(s.start, Type.array(Type.char(), s.length))

	if bv.get_symbol_at(s.start) is None:
		sym = Symbol(types.SymbolType.DataSymbol, s.start, "str_{}".format(s.value))
		bv.define_user_symbol(sym)
		count += 1

interaction.show_message_box(
	"Auto-Rename strings", 
	f"Completed renaming variables based {count} strings!"
)