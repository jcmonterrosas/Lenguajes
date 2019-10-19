import re

""" primeros = {
    "A" :[set(),set()],
    "B" :[set(),set()],
    "C" :[set(),set()],
} """

primeros ={
    "Exp_m1" : [set()],
    "Exp_m1_prima" : [set(),set()],
    "Exp_m2" : [set()],
    "Exp_m2_prima" : [set(),set()],
    "Exp_m3" : [set()],
    "Exp_m3_prima" : [set(),set()],
    "Exp_m4" : [set()],
    "Exp_m4_prima" : [set(),set()],
    "Exp_m5" : [set()],
    "Exp_m5_prima" : [set(),set()],
    "Exp_m6" : [set()],
    "Exp_m6_prima" : [set(),set()],
    "Exp_m7" : [set()],
    "Exp_m7_prima" : [set(),set()],
    "Exp_m8" : [set(),set()]
} 
nexts = {}  
epsilon = {"e"}
""" gramatica ={
    "A" :[["B","C"],["bad"]],
    "B" :[["big","C","boss"],["e"]],
    "C" :[["cat"],["cow"]],
} """

gramatica = {
    "Exp_m1" : [["Exp_m2","Exp_m1_prima"]],
    "Exp_m1_prima" : [["tk_mas", "Exp_m2", "Exp_m1_prima"],["e"]],
    "Exp_m2" : [["Exp_m3","Exp_m2_prima"]],
    "Exp_m2_prima" : [["tk_menos", "Exp_m3", "Exp_m2_prima"],["e"]],
    "Exp_m3" : [["Exp_m4","Exp_m3_prima"]],
    "Exp_m3_prima" : [["tk_exponente", "Exp_m4", "Exp_m3_prima"],["e"]],
    "Exp_m4" : [["Exp_m5","Exp_m4_prima"]],
    "Exp_m4_prima" : [["tk_multiplicacion", "Exp_m5", "Exp_m4_prima"],["e"]],
    "Exp_m5" : [["Exp_m6","Exp_m5_prima"]],
    "Exp_m5_prima" : [["tk_division", "Exp_m6", "Exp_m5_prima"],["e"]],
    "Exp_m6" : [["Exp_m7","Exp_m6_prima"]],
    "Exp_m6_prima" : [["tk_modulo", "Exp_m7", "Exp_m6_prima"],["e"]],
    "Exp_m7" : [["Exp_m8","Exp_m7_prima"]],
    "Exp_m7_prima" : [["mod", "Exp_m8", "Exp_m7_prima"],["e"]],
    "Exp_m8" : [["tk_id"],["tk_numero"]]
} 


def calcular_primeros(inicial):
   
    contador = 0
    for regla in gramatica[inicial]:
        if(len(regla)==1 and regla[0]=="e"):
            aux = primeros.get(inicial)
            aux[contador].add("e")
            primeros.update({inicial:aux})
        else:
            if(not isNotTerminal(regla[0])):
                aux = primeros.get(inicial)
                aux[contador].add(regla[0])
                primeros.update({inicial:aux})
            
            elif(isNotTerminal(regla[0])):
                primerosa1 = calcular_primeros(regla[0])
                aux = primeros.get(inicial)
                for i in primerosa1:
                    temporal = aux[contador].union(i.difference(epsilon))
                    aux[contador] = temporal
                primeros.update({inicial:aux})
                for j in primerosa1:
                    if("e" in j):
                        if(len(regla)==1):
                            aux = primeros.get(inicial)
                            aux[contador].add("e")
                            primeros.update({inicial:aux})
                        else:
                            for k in range(1, len(regla)):
                                print(k)
                                primerosk= calcular_primeros(regla[k])
                                aux = primeros.get(inicial)
                                for l in primerosk:
                                    temporal =aux[contador].union(l)
                                    aux[contador] = temporal
                                primeros.update({inicial:aux})

        contador = contador +1
    return primeros.get(inicial)




    

            
def isNotTerminal(symbol):
    if "Exp" in symbol:
        return True
    else:
        return False
        
"""     return re.match("[A-Z]",symbol[0])
 """

for u in gramatica.keys():
    print(u)
    calcular_primeros(u) 

print(primeros)