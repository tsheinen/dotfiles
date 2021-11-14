# toggle arm thumb
#
# ARM/Thumb have an odd quirk where the same architecture module handles both and
# uses the lowest bit of the address to determine the correct architecture, so
# the normal API usage of specifing the optional platform will not work. Here's a
# quick snippet to show how to toggle the architecture of the current function by
# removing/creating it

func = current_function

if not func and (current_address & 1) == 0:
    address = current_address + 1
    funcs = bv.get_functions_at(address)
    func = funcs[0] if funcs else None

if not func:
    log_error(f'Cannot find a function at current_address {current_address:#x}')
else:
    address = func.start

    if func.arch == Architecture['armv7']:
        new_platform = Platform['thumb2']
        address |= 1
    elif func.arch == Architecture['thumb2']:
        new_platform = Platform['armv7']
        address &= ~3
    else:
        raise AttributeError("This snippet only works on thumb or armv7 functions")

    bv.remove_user_function(func)
    bv.create_user_function(address, new_platform)
    platform_name = str(new_platform)
    article = 'an' if platform_name[0].lower() in 'aeiou' else 'a'
    log_info(f"Creating {article} {str(new_platform)} function at {(address - (address % 2)):#x}")
