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
    27 : ["tk_division", 1],
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
    52 : ["tk_multiplicacion", 1],
    53 : ["tk_no",0],
    54 : ["tk_arroba",0],
    55 : ["tk_interrogacion",0],
    56 : ["tk_decremento",1],
    58 : ["tk_concatenacion",0],
    61 : ["tk_diferente",0],
    63 : ["tk_desplazar_izq",1],
    64 : ["tk_desplazar_der",1],
    65 : ["tk_elevado",0],
    66 : ["tk_paralela",0],
    69 : ["tk_aug_mas", 0],
    71 : ["tk_aug_menos", 0],
    73 : ["tk_aug_multiplicacion", 0],
    75 : ["tk_aug_division", 0],
    77 : ["tk_aug_modulo", 0],
    79 : ["tk_aug_exponencial", 0],
    81 : ["tk_aug_o", 0],
    83 : ["tk_aug_y", 0],
    90 : ["tk_modulo", 1],
    91 : ["tk_exponente", 1],
    92 : ["tk_o", 1],
    93 : ["tk_y", 1],
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
            return 67
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
        elif caracter == '~':
            return 62     
        elif caracter == '@':
            return 54 
        elif caracter == '?':
            return 55
        elif caracter == '|':
            return 57   
        elif caracter == '&':
            return 60 
        elif caracter == "^":
            return 65    
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
        elif caracter == ':':
            return 68
        else:
            return 22
    elif estado == 23:
        if caracter == '>':
            return 24
        elif caracter == '-':
            return 56
        elif re.match("\d", caracter):
            return 4
        elif caracter == ':':
            return 70
        else:
            return 25
    elif estado == 26:
        if caracter == "*":
            return 51
        elif caracter == ':':
            return 72
        else:
            return 52
    elif estado == 28:
        if caracter == ':':
            return 76
        else:
            return 90
    elif estado == 33:
        if caracter == '=':
            return 34
        elif caracter == "<":
            return 63    
        else:
            return 35
    elif estado == 36:
        if caracter == '=':
            return 37
        elif caracter == '>':
            return 86   
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
    elif estado == 51:
        if caracter == ':':
            return 78
        else:
            return 91
    elif estado == 57:
        if caracter == "|":
            return 84
        elif caracter == ':':
            return 80
        else:
            return 92   
    elif estado == 60:
        if caracter == ":":
            return 82
        else:
            return 93
    elif estado == 62:
        if caracter == "=":
            return 61
        else:
            return 53    
    elif estado == 67:
        if caracter == "/":
            return 66
        elif caracter == ':':
            return 74
        else: 
            return 27   
    elif estado == 68:
        if caracter == "=":
            return 69
        else: 
            return -1
    elif estado == 70:
        if caracter == "=":
            return 71
        else:
            return -1
    elif estado == 72:
        if caracter == "=":
            return 73
        else:
            return -1
    elif estado == 74:
        if caracter == "=":
            return 75
        else:
            return -1
    elif estado == 76:
        if caracter == "=":
            return 77
        else:
            return -1
    elif estado == 78:
        if caracter == "=":
            return 79
        else:
            return -1
    elif estado == 80:
        if caracter == "=":
            return 81
        else:
            return -1
    elif estado == 82:
        if caracter == "=":
            return 83
        else:
            return -1
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
                            lexema = "tk_" + lexema
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
    if lexema == "V" or lexema == "P":
        return True
    elif len(lexema) < 2:
        return False
    else:
        with open('reservadas.txt') as archivo:
            flag = False
            for line in archivo:
                if lexema in line:
                    flag = True
            return flag

#main()

    
