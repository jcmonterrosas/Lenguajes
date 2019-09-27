import re

tokens_list = []
estados_aceptacion = {
    3 : ["tk_id", 1],
    5 : ["tk_numero", 1],
    7 : ["tk_numero", 2],
    9 : ["tk_numero", 1],
}

class Token:
    def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def token_string(self):
        res_string = "<{},{},{},{}>".format(self.tipo, self.lexema, self.fila, self.columna)
        return res_string

#\d - digitos, \w - alfanumerico, [a-zA-Z] - letras  re.match("", caracter):

def dt(estado, caracter):
    if estado == 1:
        if re.match("[a-zA-Z]", caracter):
            return 2
        elif re.match("\d", caracter):
            return 4
        else:
            return -1
    elif estado == 2:
        if re.match("\w", caracter):
            return 2
        else:
            return 3
    elif estado == 4:
        if re.match("\d", caracter):
            return 4
        elif re.match("[.]", caracter):
            return 6
        else:
            return 5
    elif estado == 6:
        if re.match("\d", caracter):
            return 8
        else:
            return 7
    elif estado == 8:
        if re.match("\d", caracter):
            return 8
        else:
            return 9
    else:
        return -1

    
def main():
    archivo = open("ejemplo.txt","r")
    texto_codigo = archivo.read()
    archivo.close()
    estado = 1
    lexema = ""
    fila = 1
    columna = 1
    print(texto_codigo)
    for i in range(len(texto_codigo)):  
        if re.match("$", texto_codigo[i]):
            fila += 1
            columna = 1

        print(i)
        lexema += texto_codigo[i]
        estado = dt(estado, texto_codigo[i])
        columna += 1
        
        if estado in estados_aceptacion:
            i -= (estados_aceptacion[estado][1] + 2)
            token_column = columna - len(lexema) 
            lexema = lexema[:-estados_aceptacion[estado][1]]
            token = Token(estados_aceptacion[estado][0], lexema, fila, token_column)
            tokens_list.append(token.token_string())
            estado = 1
            lexema = ""
        if estado == -1:
            tokens_list.append("Error lexico(linea:{},posicion:{})".format(fila,columna))
            break
        
    

    for i in range(len(tokens_list)):
        print(tokens_list[i])
    # print(tokens_list)

# def identificar_token(estado):
#     if estado == 3

main()

    
