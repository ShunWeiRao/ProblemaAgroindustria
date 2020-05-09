from gurobipy import *

#Conjuntos y parámetros
productos = ["palta","uva","manzana","pera","aceituna","uvav","aceite"]
P = {"palta":2640, "uva":650, "manzana":120, "pera":345, "aceituna":1485, "uvav":2750, "aceite":4500}
C = {"palta":1584, "uva":422.5, "manzana":96, "pera":227, "aceituna":1039, "uvav":1237, "aceite":2925}
W = {"palta":1981, "uva":422, "manzana":822, "pera":922, "aceituna":900, "uvav":869, "aceite":14431}
MOD = {"palta":0.74, "uva":2.48, "manzana":2.88, "pera":3.35, "aceituna":1.04, "uvav":1.16, "aceite":0.22}
RE = {"palta":10, "uva":25, "manzana":58, "pera":45, "aceituna":7, "uvav":7.8, "aceite":1}
Th = 34749.49
Tp = 28600
Wa = 10**6

#Modelo
model = Model("Problema de agro")

#Variables
hectareas = model.addVars(productos, vtype=GRB.INTEGER,lb=0.0, name="hectareas")

#Restricciones
model.addConstr(quicksum(hectareas[p] for p in productos) <= Th, name="campo")
model.addConstr(quicksum(hectareas[p] * W[p] * RE[p] for p in productos) <= Wa, name="agua")
model.addConstr(quicksum(hectareas[p] * MOD[p] for p in productos) <= Tp, name="personal")

#Función objetivo
obj = quicksum(hectareas[p] * RE[p] * (P[p] - C[p]) for p in productos)
model.setObjective(obj, GRB.MAXIMIZE)
model.optimize()


#Atributos
print(model.getAttr("X"))
