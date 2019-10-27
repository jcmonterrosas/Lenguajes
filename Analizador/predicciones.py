import re

primeros = {} 
siguientes = {}  
predicciones = {}
epsilon = {"e"}



def inicializar_primeros():
    for key in gramatica.keys():
        content = []
        for rule in range(1, len(gramatica.get(key))+1):
            content.append(set())
        primeros.update({key:content})
       

def inicializar_siguientes():
    for key in gramatica.keys():
        siguientes.update({key:set()})

def inicializar_predicciones():
    for key in gramatica.keys():
        content = []
        for rule in range(1, len(gramatica.get(key))+1):
            content.append(set())
        predicciones.update({key:content})

""" gramatica ={
    "A" :[["B","C"],["ant", "A", "all"]],
    "B" :[["big","C"],["bus", "A", "boss"],["e"]],
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
                                primerosk= calcular_primeros(regla[k])
                                aux = primeros.get(inicial)
                                for l in primerosk:
                                    temporal =aux[contador].union(l)
                                    aux[contador] = temporal
                                primeros.update({inicial:aux})

        contador = contador +1
    return primeros.get(inicial)

def calcular_siguientes(NoTerminal):
    if(NoTerminal == simbolo_inicial):
        aux = siguientes.get(NoTerminal)
        aux.add("$")
        siguientes.update({NoTerminal:aux})
    for NT in gramatica.keys():
        for rule in range(0, len(gramatica.get(NT))):
            if(NoTerminal in gramatica.get(NT)[rule]):  
                rango = len(gramatica.get(NT)[rule])
                for x in range(0,rango):                  
                    if(gramatica.get(NT)[rule][x] == NoTerminal):                               
                        if(x == rango-1):
                            if(NT == NoTerminal):
                                return siguientes.get(NoTerminal)
                            else:
                                siguientes_B = calcular_siguientes(NT)
                                aux = siguientes.get(NoTerminal)
                                aux = aux.union(siguientes_B)
                                siguientes.update({NoTerminal:aux})
                        else:       
                            if(isNotTerminal(gramatica.get(NT)[rule][x+1])):
                                primeros_beta = primeros.get(gramatica.get(NT)[rule][x+1])
                                total = siguientes.get(NoTerminal)
                                for w in primeros_beta:
                                    total = total.union(w.difference(epsilon))
                                siguientes.update({NoTerminal:total})
                                for q in primeros_beta:
                                    if("e" in q):
                                        siguientes_B = calcular_siguientes(NT)
                                        aux = siguientes.get(NoTerminal)
                                        aux = aux.union(siguientes_B)
                                        siguientes.update({NoTerminal:aux})
                            elif(not isNotTerminal(gramatica.get(NT)[rule][x+1])):
                                aux = siguientes.get(NoTerminal)
                                aux.add(gramatica.get(NT)[rule][x+1])
                                siguientes.update({NoTerminal:aux})
    return siguientes.get(NoTerminal)

def calcular_predicciones():
    for NT in gramatica.keys():
        for numregla in range(0,len(gramatica.get(NT))):
            print(numregla)
            if("e" in gramatica.get(NT)[numregla]):
                aux_primeros = primeros.get(NT)[numregla].difference(epsilon)
                aux_siguientes = siguientes.get(NT)
                aux_predicciones = predicciones.get(NT)
                aux_predicciones[numregla] = aux_predicciones[numregla].union(aux_primeros.union(aux_siguientes))
                predicciones.update({NT:aux_predicciones})
            else:
                aux_primeros = primeros.get(NT)[numregla].difference(epsilon)
                aux_predicciones = predicciones.get(NT)
                aux_predicciones[numregla] = aux_predicciones[numregla].union(aux_primeros)
                predicciones.update({NT:aux_predicciones})

    
def isNotTerminal(symbol):
    if "Exp" in symbol:
        return True
    else:
        return False
        
   
""" def isNotTerminal(symbol):
     return re.match("[A-Z]",symbol[0]) """ 
    
simbolo_inicial = "Exp_m1"
inicializar_primeros()
inicializar_siguientes()
inicializar_predicciones()
for u in gramatica.keys():
    calcular_primeros(u) 
for w in gramatica.keys():
    calcular_siguientes(u) 
calcular_predicciones()
print("Primeros")
print(primeros)
print("Siguientes")
print(siguientes)
print("Predicciones")
print(predicciones)




