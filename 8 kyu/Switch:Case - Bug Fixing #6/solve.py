def eval_object(v):
    return eval('{}{}{}'.format(v['a'], v['operation'], v['b']))
