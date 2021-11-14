# uidf example
#
# This snippet graciously provided by https://twitter.com/xmppwocky as an
# example of a workflow leveraging the User-Informed-Data-Flow system
# (https://binary.ninja/2020/09/10/user-informed-dataflow.html).
# 
# Used to handle C++ classes with virtual methods but no subclasses

vt_ty_field = TextLineField("vtable type")
vt_addr_field = AddressField("vtable address")
assert get_form_input([vt_ty_field, vt_addr_field], "hello")
vt_type = bv.get_type_by_name(vt_ty_field.result)
vt_addr = vt_addr_field.result
assert vt_type is not None
def proc_fn(fn):
    candidates = []
    for var in fn.vars:
        if var.type.target == vt_type:
            candidates.append((fn, var))
    return candidates
candidates = []
for fn in bv.functions:
    candidates += proc_fn(fn)
if get_choice_input(
    "Set value of {} variables?".format(len(candidates)),
    "Confirm", ["Yes", "No"]) == 1:
        raise Exception("cancelled")
for fn, var in candidates:
    for defn in fn.mlil.get_var_definitions(var):
        # could double-check that this comes from a vtable
        # field here, if we wanted...
        fn.set_user_var_value(var, defn.address,
            PossibleValueSet.constant_ptr(vt_addr))