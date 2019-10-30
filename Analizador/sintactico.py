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
        print("error sintactico, token esperado: " + token_esperado + "\n"
                "token recibido: " + token)

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
# productions & actions
def component():
    global token
    print("component")
    if token in predicciones.predicciones["component"][0]:
        comp_kwd()
        token = emparejar("tk_id")
        component_p()
    elif token in predicciones.predicciones["component"][1]:
        token = emparejar("tk_body")
        token = emparejar("tk_id")
        body_stmt_ls()
        end_id()
        #token = emparejar("tk_punto_coma")
    else:
        error(predicciones.predicciones["component"])

def component_p():
    global token
    print("component_p")
    if token in predicciones.predicciones["component_p"][0]:
        spec_stmt_ls()
        spec_body()
        #token = emparejar("tk_punto_coma")
    elif token in predicciones.predicciones["component_p"][1]:
        comp_params()
        body_stmt_ls()
        end_id()
        #token = emparejar("tk_punto_coma")
    else:
        error(predicciones.predicciones["component_p"])

def comp_kwd():
    global token
    print("comp_kwd")
    if token in predicciones.predicciones["comp_kwd"][0]:
        token = emparejar("tk_global")
    elif token in predicciones.predicciones["comp_kwd"][1]:
        token = emparejar("tk_resource")
    else:
        error(predicciones.predicciones["comp_kwd"])

def spec_body():
    global token
    print("spec_body")
    if token in predicciones.predicciones["spec_body"][0]:
        end_id()
    elif token in predicciones.predicciones["spec_body"][1]:
        token = emparejar("tk_body")
        token = emparejar("tk_id")
        maybe_params()
        spec_body_p()
    else:
        error(predicciones.predicciones["spec_body"])

def spec_body_p():
    global token
    print("spec_body_p")
    if token in predicciones.predicciones["spec_body_p"][0]:
        body_stmt_ls()
        end_id()
    #elif token in predicciones.predicciones["spec_body_p"][1]:
        #token = emparejar("tk_punto_coma")
    else:
        error(predicciones.predicciones["spec_body_p"])

def maybe_params():
    global token
    print("maybe_params")
    if token in predicciones.predicciones["maybe_params"][0]:
        comp_params()
    elif token not in predicciones.predicciones["maybe_params"][1]:
        error(predicciones.predicciones["maybe_params"])

def comp_params():
    global token
    print("comp_params")
    if token in predicciones.predicciones["comp_params"][0]:
        parameters()
    else:
        error(predicciones.predicciones["comp_params"])


# spec/body contents
def spec_stmt_ls():
    global token
    print("spec_stmt_ls")
    if token in predicciones.predicciones["spec_stmt_ls"][0]:
        spec_stmt()
        spec_stmt_ls_p()
    else:
        error(predicciones.predicciones["spec_stmt_ls"])

def spec_stmt_ls_p():
    global token
    print("spec_stmt_ls_p")
    if token in predicciones.predicciones["spec_stmt_ls_p"][0]:
        token = emparejar("tk_punto_coma")
        spec_stmt()
        spec_stmt_ls_p()
    elif token not in predicciones.predicciones["spec_stmt_ls_p"][1]:
        error(predicciones.predicciones["spec_stmt_ls_p"])

def spec_stmt():
    global token
    print("spec_stmt")
    if token in predicciones.predicciones["spec_stmt"][0]:
        common_stmt()
    elif token in predicciones.predicciones["spec_stmt"][1]:
        extend_clause()
    elif token in predicciones.predicciones["spec_stmt"][2]:
        body_only()
    else:
        error(predicciones.predicciones["spec_stmt"])

def body_stmt_ls():
    global token
    print("body_stmt_ls")
    if token in predicciones.predicciones["body_stmt_ls"][0]:
        body_stmt()
        body_stmt_ls_p()
    else:
        error(predicciones.predicciones["body_stmt_ls"])

def body_stmt_ls_p():
    global token
    print("body_stmt_ls_p")
    if token in predicciones.predicciones["body_stmt_ls_p"][0]:
        token = emparejar("tk_punto_coma")
        body_stmt()
        body_stmt_ls_p()
    elif token not in predicciones.predicciones["body_stmt_ls_p"][1]:
        error(predicciones.predicciones["body_stmt_ls_p"])

def body_stmt():
    global token
    print("body_stmt")
    if token in predicciones.predicciones["body_stmt"][0]:
        common_stmt()
    elif token in predicciones.predicciones["body_stmt"][1]:
        expr()
    elif token in predicciones.predicciones["body_stmt"][2]:
        body_only()
    elif token in predicciones.predicciones["body_stmt"][3]:
        extend_clause()
    else:
        error(predicciones.predicciones["body_stmt"])

def body_only():
    global token
    print("body_only")
    if token in predicciones.predicciones["body_only"][0]:
        stmt()
    elif token in predicciones.predicciones["body_only"][1]:
        proc()
    elif token in predicciones.predicciones["body_only"][2]:
        process()
    elif token in predicciones.predicciones["body_only"][3]:
        procedure()
    elif token in predicciones.predicciones["body_only"][4]:
        initial_block()
    elif token in predicciones.predicciones["body_only"][5]:
        final_block()
    else:
        error(predicciones.predicciones["body_only"])

def common_stmt():
    global token
    print("common_stmt")
    if token in predicciones.predicciones["common_stmt"][0]:
        decl()
    elif token in predicciones.predicciones["common_stmt"][1]:
        import_clause()
    elif token not in predicciones.predicciones["common_stmt"][2]:
        error(predicciones.predicciones["common_stmt"])

def import_clause():
    global token
    print("import_clause")
    if token in predicciones.predicciones["import_clause"][0]:
        token = emparejar("tk_import")
        import_list()
    else:
        error(predicciones.predicciones["import_clause"])

def extend_clause():
    global token
    print("extend_clause")
    if token in predicciones.predicciones["extend_clause"][0]:
        token = emparejar("tk_extend")
        import_list()
    else:
        error(predicciones.predicciones["extend_clause"])

def import_list():
    global token
    print("import_list")
    if token in predicciones.predicciones["import_list"][0]:
        token = emparejar("tk_id")
        import_list_p()
    else:
        error(predicciones.predicciones["import_list"])

def import_list_p():
    global token
    print("import_list_p")
    if token in predicciones.predicciones["import_list_p"][0]:
        token = emparejar("tk_coma")
        token = emparejar("tk_id")
        import_list_p()
    elif token not in predicciones.predicciones["import_list_p"][1]:
        error(predicciones.predicciones["import_list_p"])


# top-level body stmtents
def op_decl():
    global token
    print("op_decl")
    if token in predicciones.predicciones["op_decl"][0]:
        op_or_ext()
        oper_def_lp()
    else:
        error(predicciones.predicciones["op_decl"])

def op_or_ext():
    global token
    print("op_or_ext")
    if token in predicciones.predicciones["op_or_ext"][0]:
        token = emparejar("tk_op")
    elif token in predicciones.predicciones["op_or_ext"][1]:
        token = emparejar("tk_external")
    else:
        error(predicciones.predicciones["op_or_ext"])

def oper_def_lp():
    global token
    print("oper_def_lp")
    if token in predicciones.predicciones["oper_def_lp"][0]:
        oper_def()
        oper_def_lp_p()
    else:
        error(predicciones.predicciones["oper_def_lp"])

def oper_def_lp_p():
    global token
    print("oper_def_lp_p")
    if token in predicciones.predicciones["oper_def_lp_p"][0]:
        token = emparejar("tk_coma")
        oper_def()
        oper_def_lp_p()
    elif token not in predicciones.predicciones["oper_def_lp_p"][1]:
        error(predicciones.predicciones["oper_def_lp_p"])

def oper_def():
    global token
    print("oper_def")
    if token in predicciones.predicciones["oper_def"][0]:
        id_subs_lp()
        oper_def_p()
    else:
        error(predicciones.predicciones["oper_def"])

def oper_def_p():
    global token
    print("oper_def_p")
    if token in predicciones.predicciones["oper_def_p"][0]:
        op_prototype()
    elif token in predicciones.predicciones["oper_def_p"][1]:
        colon_opt()
        qualified_id()
    else:   
        error(predicciones.predicciones["oper_def_p"])

def colon_opt():
    global token
    print("colon_opt")
    if token in predicciones.predicciones["colon_opt"][0]:
        token = emparejar("tk_dos_puntos")
    elif token not in predicciones.predicciones["colon_opt"][1]:
        error(predicciones.predicciones["colon_opt"])

def sem_decl():
    global token
    print("sem_decl")
    if token in predicciones.predicciones["sem_decl"][0]:
        token = emparejar("tk_sem")
        sem_def_lp()
    else:
        error(predicciones.predicciones["sem_decl"])

def sem_def_lp():
    global token
    print("sem_def_lp")
    if token in predicciones.predicciones["sem_def_lp"][0]:
        sem_def()
        sem_def_lp_p()
    else:
        error(predicciones.predicciones["sem_def_lp"])

def sem_def_lp_p():
    global token
    print("sem_def_lp_p")
    if token in predicciones.predicciones["sem_def_lp_p"][0]:
        token = emparejar("tk_coma")
        sem_def()
        sem_def_lp_p()
    elif token not in predicciones.predicciones["sem_def_lp_p"][1]:
        error(predicciones.predicciones["sem_def_lp_p"])

def sem_def():
    global token
    print("sem_def")
    if token in predicciones.predicciones["sem_def"][0]:
        id_subs()
        sem_proto()
        sem_init()
    else:
        error(predicciones.predicciones["sem_def"])

def sem_proto():
    global token
    print("sem_proto")
    if token in predicciones.predicciones["sem_proto"][0]:
        return_spec_null()
    else:
        error(predicciones.predicciones["sem_proto"])

def sem_init():
    global token
    print("sem_init")
    if token in predicciones.predicciones["sem_init"][0]:
        token = emparejar("tk_asignacion")
        expr()
    elif token not in predicciones.predicciones["sem_init"][1]:
        error(predicciones.predicciones["sem_init"])

def proc():
    global token
    print("proc")
    if token in predicciones.predicciones["proc"][0]:
        token = emparejar("tk_proc")
        token = emparejar("tk_id")
        param_names()
        block()
        end_id()
    else:
        error(predicciones.predicciones["proc"])

def procedure():
    global token
    print("procedure")
    if token in predicciones.predicciones["procedure"][0]:
        token = emparejar("tk_procedure")
        token = emparejar("tk_id")
        prototype()
        block()
        end_id()
    else:
        error(predicciones.predicciones["procedure"])

def process():
    global token
    print("process")
    if token in predicciones.predicciones["process"][0]:
        token = emparejar("tk_process")
        token = emparejar("tk_id")
        return_spec_null()
        quantifiers_opt()
        block()
        end_id()
    else:
        error(predicciones.predicciones["process"])

def initial_block():
    global token
    print("initial_block")
    if token in predicciones.predicciones["initial_block"][0]:
        token = emparejar("tk_initial")
        block()
        token = emparejar("tk_end")
        initial_opt()
    else:
        error(predicciones.predicciones["initial_block"])

def initial_opt():
    global token
    print("initial_opt")
    if token in predicciones.predicciones["initial_opt"][0]:
        token = emparejar("tk_initial")
    elif token not in predicciones.predicciones["initial_opt"][1]:
        error(predicciones.predicciones["initial_opt"])

def final_block():
    global token
    print(predicciones.predicciones["final_block"][0])
    if token in predicciones.predicciones["final_block"][0]:
        token = emparejar("tk_final")
        block()
        token = emparejar("tk_end")
        final_opt()
    else:
        error(predicciones.predicciones["final_block"])

def final_opt():
    global token
    print("final_opt")
    if token in predicciones.predicciones["final_opt"][0]:
        token = emparejar("tk_final")
    elif token not in predicciones.predicciones["final_opt"][1]:
        error(predicciones.predicciones["final_opt"])


# parameters

def prototype():
    global token
    print("prototype")
    if token in predicciones.predicciones["prototype"][0]:
        parameters()
        return_spec_opt()
    else:
        error(predicciones.predicciones["prototype"])

def parameters():
    global token
    print("parameters")
    if token in predicciones.predicciones["parameters"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        param_spec_ls()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["parameters"])

def param_spec_ls():
    global token
    print("param_spec_ls")
    if token in predicciones.predicciones["param_spec_ls"][0]:
        param_spec_lp()
    elif token not in predicciones.predicciones["param_spec_ls"][1]:
        error(predicciones.predicciones["param_spec_ls"])

def param_spec_lp():
    global token
    print("param_spec_lp")
    if token in predicciones.predicciones["param_spec_lp"][0]:
        param_spec()
        param_spec_lp_p()
    else:
        error(predicciones.predicciones["param_spec_lp"])

def param_spec_lp_p():
    global token
    print("param_spec_lp_p")
    if token in predicciones.predicciones["param_spec_lp_p"][0]:
        token = emparejar("tk_punto_coma")
        param_spec_lp_p_p()
    elif token not in predicciones.predicciones["param_spec_lp_p"][1]:
        error(predicciones.predicciones["param_spec_lp_p"])

def param_spec_lp_p_p():
    global token
    print("param_spec_lp_p_p")
    if token in predicciones.predicciones["param_spec_lp_p_p"][0]:
        param_spec_lp()
    elif token not in predicciones.predicciones["param_spec_lp_p_p"][1]:
        error(predicciones.predicciones["param_spec_lp_p_p"])

def param_spec():
    global token
    print("param_spec")
    if token in predicciones.predicciones["param_spec"][0]:
        param_kind_opt()
        param_spec_p()
    else:
        error(predicciones.predicciones["param_spec"])

def param_spec_p():
    global token
    print("param_spec_p")
    if token in predicciones.predicciones["param_spec_p"][0]:
        type_gram()
    elif token in predicciones.predicciones["param_spec_p"][1]:
        id_subs_lp()
        token = emparejar("tk_dos_puntos")
        type_gram()
    else:
        error(predicciones.predicciones["param_spec_p"])

def param_kind_opt():
    global token
    print("param_kind_opt")
    if token in predicciones.predicciones["param_kind_opt"][0]:
        token = emparejar("tk_val")
    elif token in predicciones.predicciones["param_kind_opt"][1]:
        token = emparejar("tk_var")
    elif token in predicciones.predicciones["param_kind_opt"][2]:
        token = emparejar("tk_res")
    elif token in predicciones.predicciones["param_kind_opt"][3]:
        token = emparejar("tk_ref")
    elif token not in predicciones.predicciones["param_kind_opt"][4]:
        error(predicciones.predicciones["param_kind_opt"])

def return_spec_opt():
    global token
    print("return_spec_opt")
    if token in predicciones.predicciones["return_spec_opt"][0]:
        return_spec_null()
    elif token in predicciones.predicciones["return_spec_opt"][1]:
        token = emparejar("tk_returns")
        return_spec_opt_p()
    else:
        error(predicciones.predicciones["return_spec_opt"])

def return_spec_opt_p():
    global token
    print("return_spec_opt_p")
    if token in predicciones.predicciones["return_spec_opt_p"][0]:
        type_gram()
    elif token in predicciones.predicciones["return_spec_opt_p"][1]:
        id_subs()
        token = emparejar("tk_dos_puntos")
        type_gram()
    elif token in predicciones.predicciones["return_spec_opt_p"][2]:
        token = emparejar("tk_id")
    else:
        error(predicciones.predicciones["return_spec_opt_p"])

def return_spec_null():
    global token
    print("return_spec_null")
    if token not in predicciones.predicciones["return_spec_null"][0]:
        error(predicciones.predicciones["return_spec_null"])

def param_names():
    global token
    print("param_names")
    if token in predicciones.predicciones["param_names"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        id_ls()
        token = emparejar("tk_parentesis_derecho")
        return_name_opt()
    else:
        error(predicciones.predicciones["param_names"])

def return_name_opt():
    global token
    print("return_name_opt")
    if token in predicciones.predicciones["return_name_opt"][0]:
        token = emparejar("tk_returns")
        token = emparejar("tk_id")
    elif token not in predicciones.predicciones["return_name_opt"][1]:
        error(predicciones.predicciones["return_name_opt"])


# declaration
def decl():
    global token
    print("decl")
    if token in predicciones.predicciones["decl"][0]:
        type_decl()
    elif token in predicciones.predicciones["decl"][1]:
        obj_decl()
    elif token in predicciones.predicciones["decl"][2]:
        optype_decl()
    elif token in predicciones.predicciones["decl"][3]:
        sem_decl()
    elif token in predicciones.predicciones["decl"][4]:
        op_decl()
    else:
        error(predicciones.predicciones["decl"])

def type_decl():
    global token
    print("type_decl")
    if token in predicciones.predicciones["type_decl"][0]:
        token = emparejar("tk_type")
        token = emparejar("tk_id")
        token = emparejar("tk_igual")
        type_gram()
        type_restriction()
    else:
        error(predicciones.predicciones["type_decl"])

def type_restriction():
    global token
    print("type_restriction")
    if token in predicciones.predicciones["type_restriction"][0]:
        token = emparejar("tk_corchete_izquierdo")
        token = emparejar("tk_id")
        token = emparejar("tk_corchete_derecho")
    elif token not in predicciones.predicciones["type_restriction"][1]:
        error(predicciones.predicciones["type_restriction"])

def obj_decl():
    print("obj_decl")
    global token
    if token in predicciones.predicciones["obj_decl"][0]:
        var_or_const()
        var_def_lp()
    else:
        error(predicciones.predicciones["obj_decl"])

def var_or_const():
    print("var_or_const")
    global token
    if token in predicciones.predicciones["var_or_const"][0]:
        token = emparejar("tk_var")
    elif token in predicciones.predicciones["var_or_const"][1]:
        token = emparejar("tk_const")
    else:
        error(predicciones.predicciones["var_or_const"])

def var_def_lp():
    global token
    print("var_def_lp")
    if token in predicciones.predicciones["var_def_lp"][0]:
        var_def()
        var_def_lp_p()
    else:
        error(predicciones.predicciones["var_def_lp"])

def var_def_lp_p():
    print("var_def_lp_p")
    global token
    if token in predicciones.predicciones["var_def_lp_p"][0]:
        token = emparejar("tk_coma")
        var_def()
        var_def_lp_p()
    elif token not in predicciones.predicciones["var_def_lp_p"][1]:
        error(predicciones.predicciones["var_def_lp_p"])

def var_def():
    global token
    print("var_def")
    if token in predicciones.predicciones["var_def"][0]:
        id_subs_lp()
        var_att()
    else:
        error(predicciones.predicciones["var_def"])

def var_att():
    print("var_att")
    global token
    if token in predicciones.predicciones["var_att"][0]:
        token = emparejar("tk_dos_puntos")
        type_gram()
        var_att_p()
    elif token in predicciones.predicciones["var_att"][1]:
        token = emparejar("tk_asignacion")
        expr()
    elif token in predicciones.predicciones["var_att"][2]:
        token = emparejar("tk_punto_coma")
    elif token not in predicciones.predicciones["var_att"][3]:
        error(predicciones.predicciones["var_att"])

def var_att_p():
    global token
    print("var_att_p")
    if token in predicciones.predicciones["var_att_p"][0]:
        token = emparejar("tk_asignacion")
        expr()
    elif token not in predicciones.predicciones["var_att_p"][1]:
        error(predicciones.predicciones["var_att_p"])


# type specification
def type_gram():
    global token
    print("type_gram")
    if token in predicciones.predicciones["type_gram"][0]:
        subscripts()
        unsub_type()
    elif token in predicciones.predicciones["type_gram"][1]:
        unsub_type()
    else:
        error(predicciones.predicciones["type_gram"])

def unsub_type():
    global token
    print("unsub_type")
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
    print("basic_type")
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
    print("string_def")
    if token in predicciones.predicciones["string_def"][0]:
        token = emparejar("tk_cadena")
        string_def_p()
    else:
        error(predicciones.predicciones["string_def"])

def string_def_p():
    global token
    print("string_def_p")
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
    print("string_lim")
    if token in predicciones.predicciones["string_lim"][0]:
        expr()
    elif token in predicciones.predicciones["string_lim"][1]:
        token = emparejar("tk_multiplicacion")
    else:
        error(predicciones.predicciones["string_lim"])

def enum_def():
    global token
    print("enum_def")
    if token in predicciones.predicciones["enum_def"][0]:
        token = emparejar("tk_enum")
        token = emparejar("tk_parentesis_izquierdo")
        id_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["enum_def"])

def pointer_def():
    global token
    print("pointer_def")
    if token in predicciones.predicciones["pointer_def"][0]:
        token = emparejar("tk_ptr")
        pointer_def_p()
    else:
        error(predicciones.predicciones["pointer_def"])

def pointer_def_p():
    global token
    print("pointer_def_p")
    if token in predicciones.predicciones["pointer_def_p"][0]:
        type_gram()
    elif token in predicciones.predicciones["pointer_def_p"][1]:
        token = emparejar("tk_any")
    else:
        error(predicciones.predicciones["pointer_def_p"])

def record_def():
    global token
    print("record_def")
    if token in predicciones.predicciones["record_def"][0]:
        token = emparejar("tk_rec")
        token = emparejar("tk_parentesis_izquierdo")
        field_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["record_def"])

def union_def():
    global token
    print("union_def")
    if token in predicciones.predicciones["union_def"][0]:
        token = emparejar("tk_union")
        token = emparejar("tk_parentesis_izquierdo")
        field_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["union_def"])

def field_lp():
    global token
    print("field_lp")
    if token in predicciones.predicciones["field_lp"][0]:
        field()
        field_lp_p()
    else:
        error(predicciones.predicciones["field_lp"])

def field_lp_p():
    global token
    print("field_lp_p")
    if token in predicciones.predicciones["field_lp_p"][0]:
        token = emparejar("tk_punto_coma")
        field_lp_p_p()
    elif token not in predicciones.predicciones["field_lp_p"][1]:
        error(predicciones.predicciones["field_lp_p"])

def field_lp_p_p():
    global token
    print("field_lp_p_p")
    if token in predicciones.predicciones["field_lp_p_p"][0]:
        field_lp()
    elif token not in predicciones.predicciones["field_lp_p_p"][1]:
        error(predicciones.predicciones["field_lp_p_p"])

def field():
    global token
    print("field")
    if token in predicciones.predicciones["field"][0]:
        var_def_lp()
    else:
        error(predicciones.predicciones["field"])

def capability_def():
    global token
    print("capability_def")
    if token in predicciones.predicciones["capability_def"][0]:
        token = emparejar("tk_cap")
        cap_for()
    else:
        error(predicciones.predicciones["capability_def"])

def cap_for():
    global token
    print("cap_for")
    if token in predicciones.predicciones["cap_for"][0]:
        qualified_id()
    elif token in predicciones.predicciones["cap_for"][1]:
        op_prototype()
    elif token in predicciones.predicciones["cap_for"][2]:
        token = emparejar("tk_sem")
        sem_proto()
    elif token in predicciones.predicciones["cap_for"][3]:
        token = emparejar("tk_vm")
    else:
        error(predicciones.predicciones["cap_for"])


# optype
def optype_decl():
    global token
    print("optype_decl")
    if token in predicciones.predicciones["optype_decl"][0]:
        token = emparejar("tk_optype")
        token = emparejar("tk_id")
        eq_opt()
        op_prototype()
    else:
        error(predicciones.predicciones["optype_decl"])

def op_prototype():
    global token
    print("op_prototype")
    if token in predicciones.predicciones["op_prototype"][0]:
        prototype()
        op_restriction_opt()
    else:
        error(predicciones.predicciones["op_prototype"])

def eq_opt():
    global token
    print("eq_opt")
    if token in predicciones.predicciones["eq_opt"][0]:
        token = emparejar("tk_igual")
    elif token not in predicciones.predicciones["eq_opt"][1]:
        error(predicciones.predicciones["eq_opt"])

def op_restriction_opt():
    global token
    print("op_restriction_opt")
    if token in predicciones.predicciones["op_restriction_opt"][0]:
        token = emparejar("tk_corchete_izquierdo")
        op_restriction()
        token = emparejar("tk_corchete_derecho")
    elif token not in predicciones.predicciones["op_restriction_opt"][1]:
        error(predicciones.predicciones["op_restriction_opt"])

def op_restriction():
    global token
    print("op_restriction")
    if token in predicciones.predicciones["op_restriction"][0]:
        token = emparejar("tk_call")
        op_restriction_p()
    elif token in predicciones.predicciones["op_restriction"][1]:
        token = emparejar("tk_send")
        op_restriction_p_p()
    else:
        error(predicciones.predicciones["op_restriction"])

def op_restriction_p():
    global token
    print("op_restriction_p")
    if token in predicciones.predicciones["op_restriction_p"][0]:
        token = emparejar("tk_coma")
        token = emparejar("tk_send")
    elif token not in predicciones.predicciones["op_restriction_p"][1]:
        error(predicciones.predicciones["op_restriction_p"])

def op_restriction_p_p():
    global token
    print("op_restriction_p_p")
    if token in predicciones.predicciones["op_restriction_p_p"][0]:
        token = emparejar("tk_coma")
        token = emparejar("tk_call")
    elif token not in predicciones.predicciones["op_restriction_p_p"][1]:
        error(predicciones.predicciones["op_restriction_p_p"])


# blocks and statements
def block():
    global token
    print("block")
    if token in predicciones.predicciones["block"][0]:
        block_items()
    elif token not in predicciones.predicciones["block"][1]:
        error(predicciones.predicciones["block"])

def block_items():
    global token
    print("block_items")
    if token in predicciones.predicciones["block_items"][0]:
        block_item()
        block_items_p()
    else:
        error(predicciones.predicciones["block_items"])

def block_items_p():
    global token
    print("block_items_p")
    if token in predicciones.predicciones["block_items_p"][0]:
        token = emparejar("tk_punto_coma")
        block_item()
        block_items_p()
    elif token not in predicciones.predicciones["block_items_p"][1]:
        error(predicciones.predicciones["block_items_p"])

def block_item():
    global token
    print("block_item")
    if token in predicciones.predicciones["block_item"][0]:
        decl()
    elif token in predicciones.predicciones["block_item"][1]:
        stmt()
    elif token in predicciones.predicciones["block_item"][2]:
        expr()
    elif token in predicciones.predicciones["block_item"][3]:
        import_clause()
    elif token not in predicciones.predicciones["block_item"][4]:
        error(predicciones.predicciones["block_item"])

def stmt():
    global token
    print("stmt")
    if token in predicciones.predicciones["stmt"][0]:
        token = emparejar("tk_skip")
    elif token in predicciones.predicciones["stmt"][1]:
        stop_stmt()
    elif token in predicciones.predicciones["stmt"][2]:
        token = emparejar("tk_exit")
    elif token in predicciones.predicciones["stmt"][3]:
        token = emparejar("tk_next")
    elif token in predicciones.predicciones["stmt"][4]:
        token = emparejar("tk_return")
    elif token in predicciones.predicciones["stmt"][5]:
        token = emparejar("tk_reply")
    elif token in predicciones.predicciones["stmt"][6]:
        token = emparejar("tk_forward")
        invocation()
    elif token in predicciones.predicciones["stmt"][7]:
        send_stmt()
    elif token in predicciones.predicciones["stmt"][8]:
        explicit_call()
    elif token in predicciones.predicciones["stmt"][9]:
        token = emparejar("tk_destroy")
        expr()
    elif token in predicciones.predicciones["stmt"][10]:
        token = emparejar("tk_begin")
        block()
        token = emparejar("tk_end")
    elif token in predicciones.predicciones["stmt"][11]:
        token = emparejar("tk_if")
        guarded_cmd_lp()
        else_cmd_opt()
        token = emparejar("tk_fi")
    elif token in predicciones.predicciones["stmt"][12]:
        token = emparejar("tk_do")
        guarded_cmd_lp()
        else_cmd_opt()
        token = emparejar("tk_od")
    elif token in predicciones.predicciones["stmt"][13]:
        token = emparejar("tk_fa")
        quantifier_lp()
        token = emparejar("tk_ejecuta")
        block()
        token = emparejar("tk_af")
    elif token in predicciones.predicciones["stmt"][14]:
        token = emparejar("tk_V")
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        token = emparejar("tk_parentesis_derecho")
    elif token in predicciones.predicciones["stmt"][15]:
        input_stmt()
    elif token in predicciones.predicciones["stmt"][16]:
        token = emparejar("tk_receive")
        expr()
        paren_list()
    elif token in predicciones.predicciones["stmt"][17]:
        token = emparejar("tk_P")
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        token = emparejar("tk_parentesis_derecho")
    elif token in predicciones.predicciones["stmt"][18]:
        concurrent_stmt()
    else:
        error(predicciones.predicciones["stmt"])

def stop_stmt():
    global token
    print("stop_stmt")
    if token in predicciones.predicciones["stop_stmt"][0]:
        token = emparejar("tk_stop")
        exit_code_opt()
    else:
        error(predicciones.predicciones["stop_stmt"])

def exit_code_opt():
    global token
    print("exit_code_opt")
    if token in predicciones.predicciones["exit_code_opt"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        token = emparejar("tk_parentesis_derecho")
    elif token not in predicciones.predicciones["exit_code_opt"][1]:
        error(predicciones.predicciones["exit_code_opt"])

def send_stmt():
    global token
    print("send_stmt")
    if token in predicciones.predicciones["send_stmt"][0]:
        token = emparejar("tk_send")
        invocation()
    else:
        error(predicciones.predicciones["send_stmt"])

def explicit_call():
    global token
    print("explicit_call")
    if token in predicciones.predicciones["explicit_call"][0]:
        token = emparejar("tk_call")
        invocation()
    else:
        error(predicciones.predicciones["explicit_call"])

def guarded_cmd_lp():
    global token
    print("guarded_cmd_lp")
    if token in predicciones.predicciones["guarded_cmd_lp"][0]:
        guarded_cmd()
        guarded_cmd_lp_p()
    else:
        error(predicciones.predicciones["guarded_cmd_lp"])

def guarded_cmd_lp_p():
    global token
    print("guarded_cmd_lp_p")
    if token in predicciones.predicciones["guarded_cmd_lp_p"][0]:
        token = emparejar("tk_separa")
        guarded_cmd()
        guarded_cmd_lp_p()
    elif token not in predicciones.predicciones["guarded_cmd_lp_p"][1]:
        error(predicciones.predicciones["guarded_cmd_lp_p"])

def guarded_cmd():
    global token
    print("guarded_cmd")
    if token in predicciones.predicciones["guarded_cmd"][0]:
        expr()
        token = emparejar("tk_ejecuta")
        block()
    else:
        error(predicciones.predicciones["guarded_cmd"])

def else_cmd_opt():
    global token
    print("else_cmd_opt")
    if token in predicciones.predicciones["else_cmd_opt"][0]:
        token = emparejar("tk_separa")
        token = emparejar("tk_else")
        token = emparejar("tk_ejecuta")
        block()
    elif token not in predicciones.predicciones["else_cmd_opt"][1]:
        error(predicciones.predicciones["else_cmd_opt"])


# input statement
def input_stmt():
    global token
    print("input_stmt")
    if token in predicciones.predicciones["input_stmt"][0]:
        token = emparejar("tk_in")
        in_cmd_lp()
        else_cmd_opt()
        token = emparejar("tk_ni")
    else:
        error(predicciones.predicciones["input_stmt"])

def in_cmd_lp():
    global token
    print("in_cmd_lp")
    if token in predicciones.predicciones["in_cmd_lp"][0]:
        in_cmd()
        in_cmd_lp_p()
    else:
        error(predicciones.predicciones["in_cmd_lp"])

def in_cmd_lp_p():
    global token
    print("in_cmd_lp_p")
    if token in predicciones.predicciones["in_cmd_lp_p"][0]:
        token = emparejar("tk_separa")
        in_cmd()
        in_cmd_lp_p()
    elif token not in predicciones.predicciones["in_cmd_lp_p"][1]:
        error(predicciones.predicciones["in_cmd_lp_p"])

def in_cmd():
    global token
    print("in_cmd")
    if token in predicciones.predicciones["in_cmd"][0]:
        quantifiers_opt()
        in_spec()
        sync_expr_opt()
        sched_expr_opt()
        token = emparejar("tk_ejecuta")
        block()
    else:
        error(predicciones.predicciones["in_cmd"])

def in_spec():
    global token
    print("in_spec")
    if token in predicciones.predicciones["in_spec"][0]:
        in_op()
        param_names()
    else:
        error(predicciones.predicciones["in_spec"])

def in_op():
    global token
    print("in_op")
    if token in predicciones.predicciones["in_op"][0]:
        qualified_id()
        in_op_p()
    else:
        error(predicciones.predicciones["in_op"])

def in_op_p():
    global token
    print("in_op_p")
    if token in predicciones.predicciones["in_op_p"][0]:
        subscripts()
    elif token not in predicciones.predicciones["in_op_p"][1]:
        error(predicciones.predicciones["in_op_p"])

def sync_expr_opt():
    global token
    print("sync_expr_opt")
    if token in predicciones.predicciones["sync_expr_opt"][0]:
        token = emparejar("tk_and")
        expr()
    elif token in predicciones.predicciones["sync_expr_opt"][1]:
        token = emparejar("tk_y")
        expr()
    elif token in predicciones.predicciones["sync_expr_opt"][2]:
        token = emparejar("tk_suchthat")
        expr()
    elif token not in predicciones.predicciones["sync_expr_opt"][3]:
        error(predicciones.predicciones["sync_expr_opt"])

def sched_expr_opt():
    global token
    print("sched_expr_opt")
    if token in predicciones.predicciones["sched_expr_opt"][0]:
        token = emparejar("tk_by")
        expr()
    elif token not in predicciones.predicciones["sched_expr_opt"][1]:
        error(predicciones.predicciones["sched_expr_opt"])

        
##############co statement

def concurrent_stmt():
    global token
    print("concurrent_stmt")
    if token in predicciones.predicciones["concurrent_stmt"][0]:
        token = emparejar("tk_co")
        concurrent_cmd_lp()
        token = emparejar("tk_oc")
    else:
        error(predicciones.predicciones["concurrent_stmt"])

def concurrent_cmd_lp():
    global token
    print("concurrent_cmd_lp")
    if token in predicciones.predicciones["concurrent_cmd_lp"][0]:
        concurrent_cmd()
        concurrent_cmd_lp_p()
    else:
        error(predicciones.predicciones["concurrent_cmd_lp"])

def concurrent_cmd_lp_p():
    global token
    print("concurrent_cmd_lp_p")
    if token in predicciones.predicciones["concurrent_cmd_lp_p"][0]:
        token = emparejar("tk_paralela")
        concurrent_cmd()
        concurrent_cmd_lp_p()
    elif token not in predicciones.predicciones["concurrent_cmd_lp_p"][1]:
        error(predicciones.predicciones["concurrent_cmd_lp_p"])

def concurrent_cmd():
    global token
    print("concurrent_cmd")
    if token in predicciones.predicciones["concurrent_cmd"][0]:
        quantifiers_opt()
        separator_opt()
        concurrent_invocation()
        post_processing_opt()
    else:
        error(predicciones.predicciones["concurrent_cmd"])

def separator_opt():
    global token
    print("separator_opt")
    if token in predicciones.predicciones["separator_opt"][0]:
        token = emparejar("tk_punto_coma")
        separator_opt()
    elif token not in predicciones.predicciones["separator_opt"][1]:
        error(predicciones.predicciones["separator_opt"])

def concurrent_invocation():
    global token
    print("concurrent_invocation")
    if token in predicciones.predicciones["concurrent_invocation"][0]:
        explicit_call()
        send_stmt()
        expr()
    else:
        error(predicciones.predicciones["concurrent_invocation"])

def post_processing_opt():
    global token
    print("post_processing_opt")
    if token in predicciones.predicciones["post_processing_opt"][0]:
        token = emparejar("tk_ejectuta")
        block()
    elif token not in predicciones.predicciones["post_processing_opt"][1]:
        error(predicciones.predicciones["post_processing_opt"])

##############quantifier
def quantifiers_opt():
    global token
    print("quantifiers_opt, " + token)
    if token in predicciones.predicciones["quantifiers_opt"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        quantifier_lp()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["quantifiers_opt"])

def quantifier_lp():
    global token
    print("quantifier_lp, " + token)
    if token in predicciones.predicciones["quantifier_lp"][0]:
        quantifier()        
        quantifier_lp_p()   
    elif token not in predicciones.predicciones["quantifier_lp"][1]:
        error(predicciones.predicciones["quantifier_lp"])

def quantifier_lp_p():
    global token
    print("quantifier_lp_p")
    if token in predicciones.predicciones["quantifier_lp_p"][0]:
        token = emparejar("tk_coma")
        quantifier()
        quantifier_lp_p()
    elif token not in predicciones.predicciones["quantifier_lp_p"][1]:
        error(predicciones.predicciones["quantifier_lp_p"])


def quantifier():
    global token
    print("quantifier")
    if token in predicciones.predicciones["quantifier"][0]:
        token = emparejar("tk_id")
        token = emparejar("tk_asignacion")
        expr()
        direction()
        expr()
        step_opt()
        such_that_opt()
    else:
        error(predicciones.predicciones["quantifier"])

def direction():
    global token
    print("direction")
    if token in predicciones.predicciones["direction"][0]:
        token = emparejar("tk_to")
    elif token in predicciones.predicciones["direction"][1]:
        token = emparejar("tk_downto")
    else:
        error(predicciones.predicciones["direction"])

def step_opt():
    global token
    print("step_opt")
    if token in predicciones.predicciones["step_opt"][0]:
        token = emparejar("tk_by")
        expr()
    elif token not in predicciones.predicciones["step_opt"][1]:
        error(predicciones.predicciones["step_opt"])

def such_that_opt():
    global token
    print("such_that_opt")
    if token in predicciones.predicciones["such_that_opt"][0]:
        token = emparejar("tk_suchthat")
        expr()
    elif token not in predicciones.predicciones["such_that_opt"][1]:
        error(predicciones.predicciones["such_that_opt"])


##############expresions
def expr():
    global token
    print("expr")
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
    print("blit")
    if token in predicciones.predicciones["blit"][0]:
        token = emparejar("tk_true")
    elif token in predicciones.predicciones["blit"][1]:
        token = emparejar("tk_false")
    else:
        error(predicciones.predicciones["blit"])

def expr_pp():
    global token
    print("expr_pp")
    if token in predicciones.predicciones["expr_pp"][0]:
        expr_p()
        expr_pp()
    elif token not in predicciones.predicciones["expr_pp"][1]:
        error(predicciones.predicciones["expr_pp"])


def expr_p():
    global token
    print("expr_p")
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
        token = emparejar("tk_aug_mas")
        expr()
    elif token in predicciones.predicciones["expr_p"][22]:
        token = emparejar("tk_aug_menos")
        expr()
    elif token in predicciones.predicciones["expr_p"][23]:
        token = emparejar("tk_aug_multiplicacion")
        expr()
    elif token in predicciones.predicciones["expr_p"][24]:
        token = emparejar("tk_aug_division")
        expr()
    elif token in predicciones.predicciones["expr_p"][25]:
        token = emparejar("tk_aug_modulo")
        expr()
    elif token in predicciones.predicciones["expr_p"][26]:
        token = emparejar("tk_aug_exponencial")
        expr()
    elif token in predicciones.predicciones["expr_p"][27]:
        token = emparejar("tk_aug_o")
        expr()
    elif token in predicciones.predicciones["expr_p"][28]:
        token = emparejar("tk_aug_y")
        expr()
    elif token in predicciones.predicciones["expr_p"][29]:
        token = emparejar("tk_incremento")
    elif token in predicciones.predicciones["expr_p"][30]:
        token = emparejar("tk_decremento")
    elif token in predicciones.predicciones["expr_p"][31]:
        token = emparejar("tk_elevado")
    elif token in predicciones.predicciones["expr_p"][32]:
        token = emparejar("tk_punto")
        token = emparejar("tk_id")
    elif token in predicciones.predicciones["expr_p"][33]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        bound_lp()
        token = emparejar("tk_parentesis_cuad_derecho")
    elif token in predicciones.predicciones["expr_p"][34]:
        paren_list()
    else:
        error(predicciones.predicciones["expr_p"])

def new_item():
    global token
    print("new_item")
    if token in predicciones.predicciones["new_item"][0]:
        unsub_type()
    elif token in predicciones.predicciones["new_item"][1]:  
        token = emparejar("tk_sem")
        sem_proto()
    elif token in predicciones.predicciones["new_item"][2]:  
        token = emparejar("tk_op")
        op_prototype()
    else:
        error(predicciones.predicciones["new_item"])

def parent_expr():
    global token
    print("parent_expr")
    if token in predicciones.predicciones["parent_expr"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        token = emparejar("tk_parentesis_derecho")
    else:
        error(predicciones.predicciones["parent_expr"])

def invocation():
    global token
    print("invocation")
    if token in predicciones.predicciones["invocation"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        expr()
        paren_list()
    else:
        error(predicciones.predicciones["invocation"])

def paren_list():
    global token
    print("paren_list")
    if token in predicciones.predicciones["paren_list"][0]:
        token = emparejar("tk_parentesis_izquierdo")
        paren_item_ls()
        token = emparejar("tk_parentesis_derecho") 
    else:
        error(predicciones.predicciones["paren_list"])

def paren_item_ls():
    global token
    print("paren_item_ls")
    if token in predicciones.predicciones["paren_item_ls"][0]:
        expr_lp()
    elif token not in predicciones.predicciones["paren_item_ls"][1]:
        error(predicciones.predicciones["paren_item_ls"])

def expr_lp():
    global token
    print("expr_lp")
    if token in predicciones.predicciones["expr_lp"][0]:
        expr()
        expr_lp_p()
    else:
        error(predicciones.predicciones["expr_lp"])

def expr_lp_p():
    global token
    print("expr_lp_p")
    if token in predicciones.predicciones["expr_lp_p"][0]:
        token = emparejar("tk_coma")
        expr()
        expr_lp_p()
    elif token not in predicciones.predicciones["expr_lp_p"][1]:
        error(predicciones.predicciones["expr_lp_p"])


def constr_item_lp():
    global token
    print("constr_item_lp")
    if token in predicciones.predicciones["constr_item_lp"][0]:
        constr_item()
        constr_item_lp_p()
    else:
        error(predicciones.predicciones["constr_item_lp"])

def constr_item_lp_p():
    global token
    print("constr_item_lp_p")
    if token in predicciones.predicciones["constr_item_lp_p"][0]:
        token = emparejar("tk_coma")
        constr_item()
        constr_item_lp_p()
    elif token not in predicciones.predicciones["constr_item_lp_p"][1]:
        error(predicciones.predicciones["constr_item_lp_p"])

def constr_item():
    global token
    print("constr_item")
    if token in predicciones.predicciones["constr_item"][0]:
        expr()
    elif token in predicciones.predicciones["constr_item"][1]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        expr()
        token = emparejar("tk_parentesis_cuad_derecho")
        expr()
    else:
        error(predicciones.predicciones["constr_item"])

def create_call():
    global token
    print("create_call")
    if token in predicciones.predicciones["create_call"][0]:
        rsrc_name()
        paren_list()
    else:
        error(predicciones.predicciones["create_call"])

def rsrc_name():
    global token
    print("rsrc_name")
    if token in predicciones.predicciones["rsrc_name"][0]:
        token = emparejar("tk_id")
    elif token in predicciones.predicciones["rsrc_name"][1]:  
        token = emparejar("tk_vm")
    else:
        error(predicciones.predicciones["rsrc_name"])

def location_opt():
    global token
    print("location_opt")
    if token in predicciones.predicciones["location_opt"][0]:
        token = emparejar("tk_on")
    elif token not in predicciones.predicciones["location_opt"][1]:
        error(predicciones.predicciones["location_opt"])

##############miscellaneous

def qualified_id():
    global token
    print("qualified_id")
    if token in predicciones.predicciones["qualified_id"][0]:
        token = emparejar("tk_id")
        qualified_id_p()
    else:
        error(predicciones.predicciones["qualified_id"])

def qualified_id_p():
    global token
    print("qualified_id_p")
    if token in predicciones.predicciones["qualified_id_p"][0]:
        token = emparejar("tk_dos_puntos")
        token = emparejar("tk_id")
    elif token not in predicciones.predicciones["qualified_id_p"][1]:
        error(predicciones.predicciones["qualified_id_p"])

def end_id():
    global token
    print("end_id")
    if token in predicciones.predicciones["end_id"][0]:
        token = emparejar("tk_end")
        id_opt()
    else:
        error(predicciones.predicciones["end_id"])

def id_opt():
    global token
    print("id_opt")
    if token in predicciones.predicciones["id_opt"][0]:
        token = emparejar("tk_id")
    elif token not in predicciones.predicciones["id_opt"][1]:
        error(predicciones.predicciones["id_opt"])
        
def id_ls():
    global token
    print("id_ls")
    if token in predicciones.predicciones["id_ls"][0]:
        id_lp()
    elif token not in predicciones.predicciones["id_ls"][1]:
        error(predicciones.predicciones["id_ls"])

def id_lp():
    global token
    print("id_lp")
    if token in predicciones.predicciones["id_lp"][0]:
        token = emparejar("tk_id")
        id_lp_p()  
    else:
        error(predicciones.predicciones["id_lp"])

def id_lp_p():
    global token
    print("id_lp_p")
    if token in predicciones.predicciones["id_lp_p"][0]:
        token = emparejar("tk_coma")
        token = emparejar("tk_id")
        id_lp_p()
    elif token not in predicciones.predicciones["id_lp_p"][1]:
        error(predicciones.predicciones["id_lp_p"])


def id_subs_lp():
    print("id_subs_lp")
    global token
    if token in predicciones.predicciones["id_subs_lp"][0]:
        id_subs()
        id_subs_lp_p()  
    else:
        error(predicciones.predicciones["id_subs_lp"])

def id_subs_lp_p():
    print("id_subs_lp_p")
    global token
    if token in predicciones.predicciones["id_subs_lp_p"][0]:
        token = emparejar("tk_coma")
        id_subs()
        id_subs_lp_p()
    elif token not in predicciones.predicciones["id_subs_lp_p"][1]:
        error(predicciones.predicciones["id_subs_lp_p"])

def id_subs():
    print("id_subs")
    global token
    if token in predicciones.predicciones["id_subs"][0]:
        token = emparejar("tk_id")
        id_subs_p()  
    elif token in predicciones.predicciones["id_subs"][1]:
        expr()
    else:
        error(predicciones.predicciones["id_subs"])

def id_subs_p():
    print("id_subs_p")
    global token    
    if token in predicciones.predicciones["id_subs_p"][0]:
        subscripts()
    elif token not in predicciones.predicciones["id_subs_p"][1]:
        error(predicciones.predicciones["id_subs_p"])

def subscripts():
    print("subscripts")
    global token
    if token in predicciones.predicciones["subscripts"][0]:
        bracketed_list()
        subscripts_opt()
    else:
        error(predicciones.predicciones["subscripts"])

def subscripts_opt():
    print("subscripts_opt")
    global token
    if token in predicciones.predicciones["subscripts_opt"][0]:
        subscripts()
    elif token not in predicciones.predicciones["subscripts_opt"][1]:
        error(predicciones.predicciones["subscripts_opt"])

def bracketed_list():
    global token
    print("bracketed_list")
    if token in predicciones.predicciones["bracketed_list"][0]:
        token = emparejar("tk_parentesis_cuad_izquierdo")
        bound_lp()
        token = emparejar("tk_parentesis_cuad_derecho")
    else:
        error(predicciones.predicciones["bracketed_list"])

def bound_lp():
    global token
    print("bound_lp")
    if token in predicciones.predicciones["bound_lp"][0]:
        bounds()
        bound_lp_p()
    else:
        error(predicciones.predicciones["bound_lp"])

def bound_lp_p():
    global token
    print("bound_lp_p")
    if token in predicciones.predicciones["bound_lp_p"][0]:
        token = emparejar("tk_coma")
        bounds()
        bound_lp_p()
    elif token not in predicciones.predicciones["bound_lp_p"][1]:
        error(predicciones.predicciones["bound_lp_p"])

def bounds():
    global token
    print("bounds")
    if token in predicciones.predicciones["bounds"][0]:
        bound()
        bounds_p()
    else:
        error(predicciones.predicciones["bounds"])

def bounds_p():
    global token
    print("bounds_p")
    if token in predicciones.predicciones["bounds_p"][0]:
        token = emparejar("tk_punto_coma")
        bound()
    elif token not in predicciones.predicciones["bounds_p"][1]:
        error(predicciones.predicciones["bounds_p"])

def bound():
    print("bound")
    global token
    if token in predicciones.predicciones["bound"][0]:
        expr()
    elif token in predicciones.predicciones["bound"][1]:  
        token = emparejar("tk_multiplicacion")
    else:
        error(predicciones.predicciones["bound"])



def main():
    global token 
    lexico.main()
    print("\n")
    for v in lexico.tokens_list:
        print(v.token_string())
    print("\n")
    predicciones.main()
    token = getNextToken()
    component()
    print("\nEl analisis sintactico ha finalizado exitosamente")

main()
