# get the selected variable
# 
# Uses the UIContext to get the variable the user has currently selected, copied from https://twitter.com/josh_watson/status/1352319354663178240

ctx = UIContext.activeContext()
h = ctx.contentActionHandler()
a = h.actionContext()
token_state = a.token
selectedVar = Variable.from_identifier(current_function, token_state.token.value)
