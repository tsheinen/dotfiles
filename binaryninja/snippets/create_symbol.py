# create a symbol
#
# Used to create a symbol when you don't want to define a type at a particular location

sym_name = get_text_line_input("Symbol name:", "Symbol Name")
if sym_name not in [None, b'']:
  bv.define_user_symbol(Symbol(SymbolType.DataSymbol, here, sym_name))