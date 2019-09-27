import re

tokens_list = []
estados_aceptacion = {
    
}


class Token:
     def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

def dt(estado, caracter):
    if estado == 1:
        
        print(estado)
        return 2
    if estado == 2:
        print(estado)
        return 3
    if estado == 3:
        print(estado)
        return 3
    
def main():
    archivo = open("ejemplo.txt","r")
    texto_codigo = archivo.read()
    estado = 1
    lexema = ""
    for i in range(len(texto_codigo)):
        lexema.append(texto_codigo[i])
        estado = dt(estado, texto_codigo[i])
        if estado in estados_aceptacion:
            i -= estados_aceptacion[estado][1]
            lexema = lexema[:-estados_aceptacion[estado][1]]
            tokens_list.append(Token(estados_aceptacion[estado][0], lexema, 1, 1))
    archivo.close()

def identificar_token(estado):
    if estado == 3

main()

    
