import gramatica
import lexico

i = 0

def getNextToken() :
    global i
    if i < len(lexico.tokens_list):
        return_token = lexico.tokens_list[i].tipo
        i += 1
        return return_token
    else:
        return "e"

def emparejar(token, tokens_esperados) :
    if token in tokens_esperados :
        return getNextToken()
    else :
        print ("error sintactico: token no esperado")

def Exp_m1(token) :
    if token in predicciones["Exp_m1"][0] : 
        Exp_m2(token)
        Exp_m1_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m1_prima(token) :
    if token in predicciones["Exp_m1_prima"][0] :
        token = emparejar(token, ["tk_mas"])
        Exp_m2(token)
        Exp_m1_prima(token)
    elif token in predicciones["Exp_m1_prima"][1] :
        token = emparejar(token, predicciones["Exp_m1_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m2(token) :
    if token in predicciones["Exp_m2"][0] : 
        Exp_m3(token)
        Exp_m2_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m2_prima(token) :
    if token in predicciones["Exp_m2_prima"][0] :
        token = emparejar(token, ["tk_menos"])
        Exp_m3(token)
        Exp_m2_prima(token)
    elif token in predicciones["Exp_m2_prima"][1] :
        token = emparejar(token, predicciones["Exp_m2_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m3(token) :
    if token in predicciones["Exp_m3"][0] : 
        Exp_m4(token)
        Exp_m3_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m3_prima(token) :
    if token in predicciones["Exp_m3_prima"][0] :
        token = emparejar(token, ["tk_exponente"])
        Exp_m4(token)
        Exp_m3_prima(token)
    elif token in predicciones["Exp_m3_prima"][1] :
        token = emparejar(token, predicciones["Exp_m3_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m4(token) :
    if token in predicciones["Exp_m4"][0] : 
        Exp_m5(token)
        Exp_m4_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m4_prima(token) :
    if token in predicciones["Exp_m4_prima"][0] :
        token = emparejar(token, ["tk_exponente"])
        Exp_m5(token)
        Exp_m4_prima(token)
    elif token in predicciones["Exp_m4_prima"][1] :
        token = emparejar(token, predicciones["Exp_m4_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m5(token) :
    if token in predicciones["Exp_m5"][0] : 
        Exp_m6(token)
        Exp_m5_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m5_prima(token) :
    if token in predicciones["Exp_m5_prima"][0] :
        token = emparejar(token, ["tk_exponente"])
        Exp_m6(token)
        Exp_m5_prima(token)
    elif token in predicciones["Exp_m5_prima"][1] :
        token = emparejar(token, predicciones["Exp_m5_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m6(token) :
    if token in predicciones["Exp_m6"][0] : 
        Exp_m7(token)
        Exp_m6_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m6_prima(token) :
    if token in predicciones["Exp_m6_prima"][0] :
        token = emparejar(token, ["tk_exponente"])
        Exp_m7(token)
        Exp_m6_prima(token)
    elif token in predicciones["Exp_m6_prima"][1] :
        token = emparejar(token, predicciones["Exp_m6_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m7(token) :
    if token in predicciones["Exp_m7"][0] : 
        Exp_m8(token)
        Exp_m7_prima(token)    
    else :
        print ("error sintactico: token no esperado")

def Exp_m7_prima(token) :
    if token in predicciones["Exp_m7_prima"][0] :
        token = emparejar(token, ["tk_exponente"])
        Exp_m8(token)
        Exp_m7_prima(token)
    elif token in predicciones["Exp_m7_prima"][1] :
        token = emparejar(token, predicciones["Exp_m7_prima"][1])
    else :
        print ("error sintactico: token no esperado")

def Exp_m8(token) :
    if token in predicciones["Exp_m8"][0] : 
        token = emparejar(token, ["tk_id"])
    elif token in predicciones["Exp_m8"][1] : 
        token = emparejar(token, ["tk_numero"])
    else :
        print ("error sintactico: token no esperado")

def main() :
    lexico.main()
    token = getNextToken()
    Exp_m1(token)
    