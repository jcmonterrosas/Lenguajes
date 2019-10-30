import re
import gramatica

primeros = {} 
primeros_aux = {}
siguientes = {} 
siguientes_aux = {} 
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
        siguientes_aux.update({key:set("aux")})

def inicializar_predicciones():
    for key in gramatica.keys():
        content = []
        for rule in range(1, len(gramatica.get(key))+1):
            content.append(set())
        predicciones.update({key:content})

gramatica = gramatica.gramatica

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
                 #aca
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
                                if(isNotTerminal(regla[k])):
                                    #aca
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
        aux.add("EOF")
        siguientes.update({NoTerminal:aux})
    for NT in gramatica.keys():
        for rule in range(0, len(gramatica.get(NT))):
            if(NoTerminal in gramatica.get(NT)[rule]):  
                rango = len(gramatica.get(NT)[rule])
                for x in range(0,rango):                  
                    if(gramatica.get(NT)[rule][x] == NoTerminal):                               
                        if(x == rango-1): # Beta = e
                            # si A y B son distintos
                            if(siguientes.get(NoTerminal) != siguientes_aux.get(NoTerminal)):
                                aux2 = siguientes.get(NoTerminal)
                                siguientes_aux.update({NoTerminal:aux2})
                                
                                siguientes_B = calcular_siguientes(NT) # NT -> alfa NoTerminal beta
                                aux = siguientes.get(NoTerminal)
                                aux = aux.union(siguientes_B)
                                siguientes.update({NoTerminal:aux})
                        else:   # Beta != e 
                            if(isNotTerminal(gramatica.get(NT)[rule][x+1])): # Si Beta es un no terminal
                                primeros_beta = primeros.get(gramatica.get(NT)[rule][x+1])
                                total = siguientes.get(NoTerminal)
                                for w in primeros_beta:
                                    total = total.union(w.difference(epsilon))
                                siguientes.update({NoTerminal:total})
                                for q in primeros_beta:
                                    if("e" in q):
                                        if(siguientes.get(NoTerminal) != siguientes_aux.get(NoTerminal)):
                                            aux2 = siguientes.get(NoTerminal)
                                            siguientes_aux.update({NoTerminal:aux2})
                                            siguientes_B = calcular_siguientes(NT)
                                            aux = siguientes.get(NoTerminal)
                                            aux = aux.union(siguientes_B)
                                            siguientes.update({NoTerminal:aux})
                            elif(not isNotTerminal(gramatica.get(NT)[rule][x+1])): # Si Beta es un terminal
                                aux = siguientes.get(NoTerminal)
                                aux.add(gramatica.get(NT)[rule][x+1])
                                siguientes.update({NoTerminal:aux})
    return siguientes.get(NoTerminal)

def calcular_predicciones():
    for NT in gramatica.keys():
        for numregla in range(0,len(gramatica.get(NT))):
            
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
        #print(NT)
        #print(predicciones.get(NT))
        #print("primeros")
        #print(primeros.get(NT))
        #print("siguientes")
        #print(siguientes.get(NT))
        #   print(" ")

""" def isNotTerminal(symbol):
    if "Exp" in symbol:
        return True
    else:
        return False """
        
def isNotTerminal(symbol):
    if(symbol[0]=='t' and symbol[1]=='k'):
        return False
    else:
        return True
   
""" def isNotTerminal(symbol):
     return re.match("[A-Z]",symbol[0]) """ 

simbolo_inicial = "component"
def main():
    inicializar_primeros()
    inicializar_siguientes()
    
    inicializar_predicciones()
    for u in gramatica.keys():
        calcular_primeros(u) 
    for w in gramatica.keys():
        calcular_siguientes(w) 
    calcular_predicciones()

    aux = predicciones.get("id_opt")
    aux2 = predicciones.get("body_stmt_ls")
    aux[1] = aux[1].union(aux2[0])
    predicciones.update({"id_opt":aux})
