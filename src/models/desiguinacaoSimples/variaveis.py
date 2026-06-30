from pulp import LpVariable
import json

with open("data/desiguinicao.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

i = []
j = []

x = LpVariable("x",(i,j), cat="Binary")
#Xij = 1 se o item i é alocado ao centro j, 0 caso contrário

