import gramatica
import lexico
import predicciones
import sys

i = 0
token = ""

def getNextToken():
    global i
    if i < len(lexico.tokens_list):
        return_token = lexico.tokens_list[i].tipo
        i += 1
        return return_token
    else:
        return "EOF"


def emparejar(token_esperado):
    global token
    if token == token_esperado:
        return getNextToken()
    else:
        print("error sintactico: token no esperado" + "emparejar")

def error(predicciones):
    global i
    error_token = ""
    error_token = lexico.tokens_list[i-1]
    print("\n<" + str(error_token.fila) + "," + str(error_token.columna) + ">" + 
        " Error sintactico, se encontro: " + error_token.tipo +
        "\nSe esperaba: " + ''.join("\n\"" + (str(e)).replace("{", "").replace("}", "").replace("\'","") + "\"," for e in predicciones))
    sys.exit()

'''
funcion para no terminal sin epsilon:

def name():
    global token
    if token in predicciones.predicciones["name"][0]:
        
    else:
        error(predicciones.predicciones["name"])


funcion para no terminal con epsilon:

def name():
    global token
    if token in predicciones.predicciones["name"][0]:
        
    elif token not in predicciones.predicciones["name"][ultimo]:
        error(predicciones.predicciones["name"])


Para emparejar:

token = emparejar("tk_esperado")
'''

def expr():
    global token
    if token in predicciones.predicciones["expr"][0]:
        token = emparejar("tk_id")
        expr_pp()
    elif token in predicciones.predicciones["expr"][1]:
        token = emparejar("tk_numero")
        expr_pp()
    elif token in predicciones.predicciones["expr"][2]:
        blit()
        expr_pp()
    elif token in predicciones.predicciones["expr"][3]:
        token = emparejar("tk_cadena")
        expr_pp()
    elif token in predicciones.predicciones["expr"][4]:
        token = emparejar("tk_null")
        expr_pp()
    elif token in predicciones.predicciones["expr"][5]:
        token = emparejar("tk_parentesis_izquierdo")
        constr_item_lp()
        token = emparejar("tk_parentesis_derecho")
        expr_pp()
    elif token in predicciones.predicciones["expr"][6]:
        token = emparejar("tk_no")
        expr()
    elif token in predicciones.predicciones["expr"][7]:
        token = emparejar("tk_mas")
        expr()
    elif token in predicciones.predicciones["expr"][8]:
        token = emparejar("tk_menos")
        expr()
    elif token in predicciones.predicciones["expr"][9]:
        token = emparejar("tk_arroba")
        expr()
    elif token in predicciones.predicciones["expr"][10]:
        token = emparejar("tk_interrogacion")
        expr()
    elif token in predicciones.predicciones["expr"][11]:
        token = emparejar("tk_incremento")
        expr()
    elif token in predicciones.predicciones["expr"][12]:
        token = emparejar("tk_decremento")
        expr()
    elif token in predicciones.predicciones["expr"][13]:
        basic_type()
        parent_expr()
        expr_pp()
    elif token in predicciones.predicciones["expr"][14]:
        token = emparejar("tk_cadena")
        parent_expr()
        expr_pp()
    elif token in predicciones.predicciones["expr"][15]:
        token = emparejar("tk_low")
        token = emparejar("tk_parentesis_izquierdo")
        type_gram()
        token = emparejar("tk_parentesis_derecho")
        expr_pp()
    elif token in predicciones.predicciones["expr"][16]:
        token = emparejar("tk_high")
        token = emparejar("tk_parentesis_izquierdo")
        type_gram()
        token = emparejar("tk_parentesis_derecho")
        expr_pp()
    elif token in predicciones.predicciones["expr"][17]:
        token = emparejar("tk_new")
        token = emparejar("tk_parentesis_izquierdo")
        subscripts_opt()
        new_item()
        token = emparejar("tk_parentesis_derecho")
        expr_pp()
    elif token in predicciones.predicciones["expr"][18]:
        token = emparejar("tk_create")
        create_call()
        location_opt() 
        expr_pp()
    else:
        error(predicciones.predicciones["expr"])

def blit():
    global token
    if token in predicciones.predicciones["blit"][0]:
        token = emparejar("tk_true")
    elif token in predicciones.predicciones["blit"][1]:
        token = emparejar("tk_false")
    else:
        error(predicciones.predicciones["blit"])

def expr_pp():
    global token
    if token in predicciones.predicciones["expr_pp"][0]:
        expr_p()
        expr_pp()
    elif token not in predicciones.predicciones["expr_pp"][1]:
        error(predicciones.predicciones["expr_pp"])


def expr_p():
    global token
    if token in predicciones.predicciones["expr_p"][0]:
        token = emparejar("tk_exponente")
        expr()
    elif token in predicciones.predicciones["expr_p"][1]:
        token = emparejar("tk_multiplicacion")
        expr()
    elif token in predicciones.predicciones["expr_p"][2]:
        token = emparejar("tk_division")
        expr()
    elif token in predicciones.predicciones["expr_p"][3]:
        token = emparejar("tk_mod")
        expr()
    elif token in predicciones.predicciones["expr_p"][4]:
        token = emparejar("tk_modulo")
        expr()
    elif token in predicciones.predicciones["expr_p"][5]:
        token = emparejar("tk_mas")
        expr()
    elif token in predicciones.predicciones["expr_p"][6]:
        token = emparejar("tk_menos")
        expr()
    elif token in predicciones.predicciones["expr_p"][7]:
        token = emparejar("tk_concatenacion")
        expr()
    elif token in predicciones.predicciones["expr_p"][8]:
        token = emparejar("tk_igual")
        expr()
    elif token in predicciones.predicciones["expr_p"][9]:
        token = emparejar("tk_diferente")
        expr()
    elif token in predicciones.predicciones["expr_p"][10]:
        token = emparejar("tk_mayor_igual")
        expr()
    elif token in predicciones.predicciones["expr_p"][11]:
        token = emparejar("tk_menor_igual")
        expr()
    elif token in predicciones.predicciones["expr_p"][12]:
        token = emparejar("tk_mayor")
        expr()
    elif token in predicciones.predicciones["expr_p"][13]:
        token = emparejar("tk_menor")
        expr()
    elif token in predicciones.predicciones["expr_p"][14]:
        token = emparejar("tk_y")
        expr()
    elif token in predicciones.predicciones["expr_p"][15]:
        token = emparejar("tk_o")
        expr()
    elif token in predicciones.predicciones["expr_p"][16]:
        token = emparejar("tk_xor")
        expr()
    elif token in predicciones.predicciones["expr_p"][17]:
        token = emparejar("tk_desplazar_der")
        expr()
    elif token in predicciones.predicciones["expr_p"][18]:
        token = emparejar("tk_desplazar_izq")
        expr()
    elif token in predicciones.predicciones["expr_p"][19]:
        token = emparejar("tk_swap")
        expr()
    elif token in predicciones.predicciones["expr_p"][20]:
        token = emparejar("tk_asignacion")
        expr()
    elif token in predicciones.predicciones["expr_p"][21]:
        token = emparejar("tk_incremento")
    elif token in predicciones.predicciones["expr_p"][22]:
        token = emparejar("tk_decremento")
    elif token in predicciones.predicciones["expr_p"][23]:
        token = emparejar("tk_elevado")
    elif token in predicciones.predicciones["expr_p"][24]:
        token = emparejar("tk_punto")
        token = emparejar("tk_id")
    elif token in predicciones.predicciones["expr_p"][25]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        bound_lp()
        token = emparejar("tk_parentesis_cuad_derecho")
    elif token in predicciones.predicciones["expr_p"][26]:
        paren_list()
    else:
        error(predicciones.predicciones["expr_p"])

def constr_item_lp():
    global token
    if token in predicciones.predicciones["constr_item_lp"][0]:
        constr_item()
        constr_item_lp_p()
    else:
        error(predicciones.predicciones["constr_item_lp"])

def constr_item_lp_p():
    global token
    if token in predicciones.predicciones["constr_item_lp_p"][0]:
        token = emparejar("tk_coma")
        constr_item()
        constr_item_lp_p()
    elif token not in predicciones.predicciones["constr_item_lp_p"][1]:
        error(predicciones.predicciones["constr_item_lp_p"])

def constr_item():
    global token
    if token in predicciones.predicciones["constr_item"][0]:
        expr()
    elif token in predicciones.predicciones["constr_item"][1]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        expr()
        token = emparejar("tk_parentesis_cuad_derecho")
        expr()
    else:
        error(predicciones.predicciones["constr_item"])


def parent_expr():
    global token
    if token in predicciones.predicciones["parent_expr"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["parent_expr"])

def subscripts_opt():
    global token
    if token in predicciones.predicciones["subscripts_opt"][0]:
        subscripts()
    elif token not in predicciones.predicciones["subscripts_opt"][1]:
        error(predicciones.predicciones["subscripts_opt"])

def subscripts():
    global token
    if token in predicciones.predicciones["subscripts"][0]:
        bracketed_list()
        subscripts_opt()
    else:
        error(predicciones.predicciones["subscripts"])

def bracketed_list():
    global token
    if token in predicciones.predicciones["bracketed_list"][0]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        bound_lp()
        token = emparejar("tk_parentesis_cuad_derecho")
    else:
        error(predicciones.predicciones["bracketed_list"])

def bound_lp():
    global token
    if token in predicciones.predicciones["bound_lp"][0]:
        bounds()
        bound_lp_p()
    else:
        error(predicciones.predicciones["bound_lp"])

def bound_lp_p():
    global token
    if token in predicciones.predicciones["bound_lp_p"][0]:
        token = emparejar("tk_coma")
        bounds()
    elif token not in predicciones.predicciones["bound_lp_p"][1]:
        error(predicciones.predicciones["bound_lp_p"])

def bounds():
    global token
    if token in predicciones.predicciones["bounds"][0]:
        bound()
        bounds_p()
    else:
        error(predicciones.predicciones["bounds"])

def bounds_p():
    global token
    if token in predicciones.predicciones["bounds_p"][0]:
        token = emparejar("tk_punto_coma")
        bound()
    elif token not in predicciones.predicciones["bounds_p"][1]:
        error(predicciones.predicciones["bounds_p"])

def bound():
    global token
    if token in predicciones.predicciones["bound"][0]:
        expr()
    elif token in predicciones.predicciones["bound"][1]:  
        token = emparejar("tk_multiplicacion")
    else:
        error(predicciones.predicciones["bound"])

def new_item():
    global token
    if token in predicciones.predicciones["new_item"][0]:
        unsub_type()
    elif token in predicciones.predicciones["new_item"][1]:  
        token = emparejar("tk_sem")
        sem_proto()
    elif token in predicciones.predicciones["new_item"][2]:  
        token = emparejar("tk_op")
        #op_prototype()
    else:
        error(predicciones.predicciones["new_item"])

def create_call():
    global token
    if token in predicciones.predicciones["create_call"][0]:
        rsrc_name()
        paren_list()
    else:
        error(predicciones.predicciones["create_call"])

def rsrc_name():
    global token
    if token in predicciones.predicciones["rsrc_name"][0]:
        token = emparejar("tk_id")
    elif token in predicciones.predicciones["rsrc_name"][1]:  
        token = emparejar("tk_vm")
    else:
        error(predicciones.predicciones["rsrc_name"])

def location_opt():
    global token
    if token in predicciones.predicciones["location_opt"][0]:
        token = emparejar("tk_on")
    elif token not in predicciones.predicciones["location_opt"][1]:
        error(predicciones.predicciones["location_opt"])

def paren_list():
    global token
    if token in predicciones.predicciones["paren_list"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        paren_item_ls()
        token = emparejar("tk_parentesis_derecho") 
    else:
        error(predicciones.predicciones["paren_list"])

def paren_item_ls():
    global token
    if token in predicciones.predicciones["paren_item_ls"][0]:
        expr_lp()
    elif token not in predicciones.predicciones["paren_item_ls"][1]:
        error(predicciones.predicciones["paren_item_ls"])

def expr_lp():
    global token
    if token in predicciones.predicciones["expr_lp"][0]:
        expr()
        expr_lp_p()
    else:
        error(predicciones.predicciones["expr_lp"])

def expr_lp_p():
    global token
    if token in predicciones.predicciones["expr_lp_p"][0]:
        token = emparejar("tk_coma")
        expr()
        expr_lp_p()
    elif token not in predicciones.predicciones["expr_lp_p"][1]:
        error(predicciones.predicciones["expr_lp_p"])

def type_gram():
    global token
    if token in predicciones.predicciones["type_gram"][0]:
        subscripts()
        unsub_type()
    elif token in predicciones.predicciones["type_gram"][1]:  
        unsub_type()
    else:
        error(predicciones.predicciones["type_gram"])

def unsub_type():
    global token
    if token in predicciones.predicciones["unsub_type"][0]:
        basic_type()
    elif token in predicciones.predicciones["unsub_type"][1]:  
        string_def()
    elif token in predicciones.predicciones["unsub_type"][2]:  
        enum_def()
    elif token in predicciones.predicciones["unsub_type"][3]:  
        pointer_def()
    elif token in predicciones.predicciones["unsub_type"][4]:  
        record_def()
    elif token in predicciones.predicciones["unsub_type"][5]:  
        union_def()
    elif token in predicciones.predicciones["unsub_type"][6]:  
        capability_def()
    elif token in predicciones.predicciones["unsub_type"][7]:  
        qualified_id()
    else:
        error(predicciones.predicciones["unsub_type"])

def basic_type():
    global token
    if token in predicciones.predicciones["basic_type"][0]:
        token = emparejar("tk_bool")
    elif token in predicciones.predicciones["basic_type"][1]:  
        token = emparejar("tk_char")
    elif token in predicciones.predicciones["basic_type"][2]:  
        token = emparejar("tk_int")
    elif token in predicciones.predicciones["basic_type"][3]:  
        token = emparejar("tk_file")
    elif token in predicciones.predicciones["basic_type"][4]:  
        token = emparejar("tk_real")
    else:
        error(predicciones.predicciones["basic_type"])

def string_def():
    global token
    if token in predicciones.predicciones["string_def"][0]:
        token = emparejar("tk_cadena")
        string_def_p()
    else:
        error(predicciones.predicciones["string_def"])

def string_def_p():
    global token
    if token in predicciones.predicciones["string_def_p"][0]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        string_lim()
        token = emparejar("tk_parentesis_cuad_derecho")
    elif token in predicciones.predicciones["string_def_p"][1]:  
        token = emparejar("tk_parentesis_izquierdo")
        string_lim()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["string_def_p"])

def string_lim():
    global token
    if token in predicciones.predicciones["string_lim"][0]:
        expr()
    elif token in predicciones.predicciones["string_lim"][1]:  
        token = emparejar("tk_multiplicacion")
    else:
        error(predicciones.predicciones["string_lim"])

def enum_def():
    global token
    if token in predicciones.predicciones["enum_def"][0]:
        token = emparejar("tk_enum")
        token = emparejar("tk_parentesis_izquierdo")
        id_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["enum_def"])

def id_lp():
    global token
    if token in predicciones.predicciones["id_lp"][0]:
        token = emparejar("tk_id")
        id_lp_p()  
    else:
        error(predicciones.predicciones["id_lp"])

def id_lp_p():
    global token
    if token in predicciones.predicciones["id_lp_p"][0]:
        token = emparejar("tk_coma")
        token = emparejar("tk_id")
    elif token not in predicciones.predicciones["id_lp_p"][1]:
        error(predicciones.predicciones["id_lp_p"])

def id_subs_lp():
    global token
    if token in predicciones.predicciones["id_subs_lp"][0]:
        id_subs()
        id_subs_lp_p()  
    else:
        error(predicciones.predicciones["id_subs_lp"])

def id_subs_lp_p():
    global token
    if token in predicciones.predicciones["id_subs_lp_p"][0]:
        token = emparejar("tk_coma")
        id_subs()
    elif token not in predicciones.predicciones["id_subs_lp_p"][1]:
        error(predicciones.predicciones["id_subs_lp_p"])

def id_subs():
    global token
    if token in predicciones.predicciones["id_subs"][0]:
        token = emparejar("tk_id")
        id_subs_p()  
    else:
        error(predicciones.predicciones["id_subs"])

def id_subs_p():
    global token
    if token in predicciones.predicciones["id_subs_p"][0]:
        subscripts()
    elif token not in predicciones.predicciones["id_subs_p"][1]:
        error(predicciones.predicciones["id_subs_p"])
        
def pointer_def():
    global token
    if token in predicciones.predicciones["pointer_def"][0]:
        token = emparejar("tk_ptr")
        pointer_def_p()
    else:
        error(predicciones.predicciones["pointer_def"])

def pointer_def_p():
    global token
    if token in predicciones.predicciones["pointer_def_p"][0]:
        type_gram()
    elif token in predicciones.predicciones["pointer_def_p"][1]:  
        token = emparejar("tk_any")
    else:
        error(predicciones.predicciones["pointer_def_p"])

def record_def():
    global token
    if token in predicciones.predicciones["record_def"][0]:
        token = emparejar("tk_rec")
        token = emparejar("tk_parentesis_izquierdo")
        field_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["record_def"])

def union_def():
    global token
    if token in predicciones.predicciones["union_def"][0]:
        token = emparejar("tk_union")
        token = emparejar("tk_parentesis_izquierdo")
        field_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["union_def"])

def field_lp():
    global token
    if token in predicciones.predicciones["field_lp"][0]:
        field()
        field_lp_p()
    else:
        error(predicciones.predicciones["field_lp"])
        
def field_lp_p():
    global token
    if token in predicciones.predicciones["field_lp_p"][0]:
        token = emparejar("tk_punto_coma")
        field_lp_p_p()
    elif token not in predicciones.predicciones["field_lp_p"][1]:
        error(predicciones.predicciones["field_lp_p"])

def field_lp_p_p():
    global token
    if token in predicciones.predicciones["field_lp_p_p"][0]:
        field_lp()
    elif token not in predicciones.predicciones["field_lp_p_p"][1]:
        error(predicciones.predicciones["field_lp_p_p"])

def field():
    global token
    if token in predicciones.predicciones["field"][0]:
        var_def_lp()
    else:
        error(predicciones.predicciones["field"])

def capability_def():
    global token
    if token in predicciones.predicciones["capability_def"][0]:
        token = emparejar("tk_cap")
        cap_for()
    else:
        error(predicciones.predicciones["capability_def"])

def cap_for():
    global token
    if token in predicciones.predicciones["cap_for"][0]:
        qualified_id()
    #elif token in predicciones.predicciones["cap_for"][1]:  
    #    op_prototype()
    elif token in predicciones.predicciones["cap_for"][2]:  
        token = emparejar("tk_sem")
        sem_proto()
    elif token in predicciones.predicciones["cap_for"][3]:  
        token = emparejar("tk_vm")
    else:
        error(predicciones.predicciones["cap_for"])

def sem_proto():
    global token
    if token in predicciones.predicciones["sem_proto"][0]:
       return_spec_null() 
    else:
        error(predicciones.predicciones["sem_proto"])

def return_spec_null():
    global token
    if token not in predicciones.predicciones["return_spec_null"][0]:
        error(predicciones.predicciones["return_spec_null"])

def qualified_id():
    global token
    if token in predicciones.predicciones["qualified_id"][0]:
        token = emparejar("tk_id")
        qualified_id_p()
    else:
        error(predicciones.predicciones["qualified_id"])

def qualified_id_p():
    global token
    if token in predicciones.predicciones["qualified_id_p"][0]:
        token = emparejar("tk_punto")
        token = emparejar("tk_id")
    elif token not in predicciones.predicciones["qualified_id_p"][1]:
        error(predicciones.predicciones["qualified_id_p"])

def var_def_lp():
    global token
    if token in predicciones.predicciones["var_def_lp"][0]:
        var_def()
        var_def_lp_p()
    else:
        error(predicciones.predicciones["var_def_lp"])

def var_def_lp_p():
    global token
    if token in predicciones.predicciones["var_def_lp_p"][0]:
        token = emparejar("tk_coma")
        var_def()
        var_def_lp_p()
    elif token not in predicciones.predicciones["var_def_lp_p"][1]:
        error(predicciones.predicciones["var_def_lp_p"])

def var_def():
    global token
    if token in predicciones.predicciones["var_def"][0]:
        id_subs_lp()
        var_att()
    else:
        error(predicciones.predicciones["var_def"])

def var_att():
    global token
    if token in predicciones.predicciones["var_att"][0]:
        token = emparejar("tk_dos_puntos")
        type_gram()
    elif token in predicciones.predicciones["var_att"][1]:
        token = emparejar("tk_dos_puntos")
        type_gram()
        token = emparejar("tk_asignacion")
        expr()
    elif token in predicciones.predicciones["var_att"][2]:
        token = emparejar("tk_asignacion")
        expr()
    elif token in predicciones.predicciones["var_att"][3]:
        token = emparejar("tk_punto_coma")
    else:
        error(predicciones.predicciones["var_att"])

def main():
    global token 
    lexico.main()
    print("\n")
    for v in lexico.tokens_list:
        print(v.tipo)
    print("\n")
    predicciones.main()
    token = getNextToken()
    expr()
    print("\nEl analisis sintactico ha finalizado exitosamente")

main()
