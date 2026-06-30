from src.models.desiguinacaoSimples.variaveis import x
from pulp import LpRestriction

for i in I:
    for j in J:
        # Restrição de alocação de itens aos centros
        # Cada item i deve ser alocado a exatamente um centro j
        constraint = LpRestriction(e=x[i,j], sense=1, rhs=1, name=f"allocation_constraint_{i}_{j}")