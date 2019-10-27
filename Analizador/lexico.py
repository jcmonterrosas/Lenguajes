import re

tokens_list = []
estados_aceptacion = {
    3 : ["tk_id", 1],
    5 : ["tk_numero", 1],
    7 : ["tk_numero", 2],
    9 : ["tk_numero", 1],
    10 : ["tk_parentesis_izquierdo", 0],
    11 : ["tk_parentesis_derecho", 0],
    13 : ["tk_separa", 0],
    14 : ["tk_parentesis_cuad_izquierdo", 1],
    15 : ["tk_parentesis_cuad_derecho", 0],
    17 : ["tk_asignacion", 1],
    18 : ["tk_dos_puntos", 1],
    19 : ["tk_coma", 0],
    21 : ["tk_incremento", 0],
    22 : ["tk_mas", 1],
    24 : ["tk_ejecuta", 0],
    25 : ["tk_menos", 1],
    27 : ["tk_division", 0],
    28 : ["tk_modulo", 0],
    29 : ["tk_punto_coma", 0],
    30 : ["tk_punto", 0],
    31 : ["tk_corchete_izquierdo", 0],
    32 : ["tk_corchete_derecho", 0],
    34 : ["tk_menor_igual", 0],
    35 : ["tk_menor", 1],
    37 : ["tk_mayor_igual",0],
    38 : ["tk_mayor",1],
    40 : ["tk_comparacion", 0],
    41 : ["tk_igual", 1],
    43 : ["tk_cadena", 0],
    47 : ["tk_diferente", 0],
    48 : ["tk_menos",0],
    50 : ["tk_swap",0],
    51 : ["tk_exponente", 0],
    52 : ["tk_multiplicacion", 1],
}



tiene_lexema = [3, 5, 7, 9, 43]

class Token:
    def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def token_string(self):
        if self.lexema != "":
            res_string = "<{},{},{},{}>".format(self.tipo, self.lexema, self.fila, self.columna)
        else:   
            res_string = "<{},{},{}>".format(self.tipo, self.fila, self.columna)
        return res_string
        

#\d - digitos, \w - alfanumerico, [a-zA-Z] - letras 
def dt(estado, caracter):
    #print(estado, caracter)
    if estado == 1:
        if re.match("[a-zA-Z]", caracter):
            return 2
        elif re.match("\d", caracter):
            return 4
        elif caracter == "\n" or caracter == " " or caracter == "\t":
            return 1
        elif  caracter == '(':
            return 10
        elif caracter == ')':
            return 11
        elif caracter == '[':
            return 12
        elif caracter == ']':
            return 15
        elif caracter == ':':
            return 16
        elif caracter == ',':
            return 19
        elif caracter == '+':
            return 20
        elif caracter == '-':
            return 23
        elif caracter == '*':
            return 26
        elif caracter == '/':
            return 27
        elif caracter == '%':
            return 28
        elif caracter == ';':
            return 29
        elif caracter == '.':
            return 30
        elif caracter == '{':
            return 31
        elif caracter == '}':
            return 32
        elif caracter == '<':
            return 33
        elif caracter == '>':
            return 36
        elif caracter == '=':
            return 39
        elif caracter == '"':
            return 42   
        elif caracter == '#':
            return 44    
        elif caracter == '!':
            return 46           
        else:
            return -1
    elif estado == 2:
        if re.match("\w", caracter) or caracter == '_':
            return 2
        else:
            return 3
    elif estado == 4:
        if re.match("\d", caracter):
            return 4
        elif caracter == '.':
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
    elif estado == 12:
        if caracter == ']':
            return 13
        else:
            return 14
    elif estado == 16:
        if caracter == '=':
            return 49
        else:
            return 18
    elif estado == 20:
        if caracter == '+':
            return 21
        else:
            return 22
    elif estado == 23:
        if caracter == '>':
            return 24
        elif re.match("\d", caracter):
            return 4
        else:
            return 25
    elif estado == 26:
        if caracter == "*":
            return 51
        else:
            return 52
    elif estado == 33:
        if caracter == '=':
            return 34
        else:
            return 35
    elif estado == 36:
        if caracter == '=':
            return 37
        else:
            return 38
    elif estado == 39:
        if caracter == '=':
            return 40
        else:
            return 41
    elif estado == 42:
        if caracter == '"':
            return 43
        else:
            return 42
    elif estado == 44:
        if caracter == '\n':
            return 45
        else:
            return 44
    elif estado == 46:
        if caracter == '=':
            return 47
        else:
            return -1
    elif estado == 49:
        if caracter == ':':
            return 50
        else:
            return 17
    else:
        return -1

    
def main():
    filepath = 'ejemplo.txt'
    fila = 0

    with open(filepath,encoding="utf-8") as archivo:   
        for linea in archivo:
            estado = 1
            lexema = ""
            i = 0
            fila += 1
            linea += "\n"
            while i < len(linea):  
                if estado == 1: columna = i + 1
                lexema += linea[i]

                estado = dt(estado, linea[i])

                if estado == 23 and i>0 and i<len(linea):
                    if re.match("\w", linea[i-1]): 
                        if linea[i+1] !='>':
                            estado = 48 
                        else:
                            estado = 23    
                        

                if estado == 45: estado = 1

                if estado in estados_aceptacion:
                    i -= estados_aceptacion[estado][1]
                    if estado in tiene_lexema:
                        if estado != 43:
                            lexema = lexema[:-estados_aceptacion[estado][1]]
                            lexema = lexema.replace(" ", "")
                            lexema = lexema.replace("\t", "")
                    else:
                        lexema = ""

                    if estado == 3:
                        if clasificar_identificador(lexema):
                            appendToken(lexema, "", fila, columna)
                        else:
                            appendToken(estados_aceptacion[estado][0], lexema, fila, columna)
                    else:
                        appendToken(estados_aceptacion[estado][0], lexema, fila, columna)
                        
                    estado = 1
                    lexema = ""
                if estado == -1:
                    tokens_list.append("Error lexico(linea:{},posicion:{})".format(fila,columna))
                    break
                
                i += 1

            if estado == 42:
                tokens_list.append("Error lexico(linea:{},posicion:{})".format(fila,columna))

    # for i in range(len(tokens_list)):
    #     print(tokens_list[i])

def appendToken(token,lexema,fila,columna):
    token = Token(token, lexema, fila, columna)
    #tokens_list.append(token.token_string())
    tokens_list.append(token)

def clasificar_identificador(lexema):
    if len(lexema) < 2:
        return False
    with open('reservadas.txt') as archivo:
        flag = False
        for line in archivo:
            if lexema in line:
                flag = True
        return flag

#main()

    
