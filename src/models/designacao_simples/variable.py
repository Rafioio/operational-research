import gurobipy as gp

def create_variable(model, data):
    I =  data['I']
    J = data['J']

    vars = {}

    vars['x'] = model.addVars(I, J, vtype=gp.GRB.BINARY, name="x")

    return vars
