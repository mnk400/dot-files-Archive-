def Exec(exp, global_vars, local_vars=None):
    if local_vars is not None:
        exec exp in global_vars, local_vars
    else:
        exec exp in global_vars