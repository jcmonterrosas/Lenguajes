gramatica = {
    ############################### productions & actions ###############################
    "component" : 
        [
            ["comp_kwd", "tk_id", "component_p"], ##Se podria reducir mas cambiando comp_kwd por sus producciones
            ["tk_body", "tk_id", "body_stmt_ls", "end_id", "tk_punto_coma"],
            ["e"]
        ],
    
    "component_p" :
        [
            ["spec_stmt_ls", "spec_body", "tk_punto_coma"],
            ["comp_params", "body_stmt_ls", "end_id", "tk_punto_coma"]
        ],

    "comp_kwd" :
        [
            ["tk_global"],
            ["tk_resource"]
        ],

    "spec_body" :
        [
            ["end_id"],
            ["tk_body", "tk_id", "maybe_params", "spec_body_p"]
        ],
    
    "spec_body_p" :
        [
            ["body_stmt_ls", "end_id"],
            ["tk_punto_coma"]
        ],

    "maybe_params" :
        [
            ["comp_params"],
            ["e"]
        ],

    "comp_params" :
        [
            ["parameters"]
        ],
    
    "separate_body" :
        [
            ["tk_body", "tk_id", "body_stmt_ls", "end_id"]
        ],

    ############################### spec/body contents ###############################

    ############################### top-level body stmtents ###############################
    "sem_proto":
        [
            ["return_spec_null"]
        ],

    ############################### parameters ###############################
    "prototype" :
        [
            ["parameters", "return_spec_opt"]
        ],

    "parameters" :
        [
            ["tk_parentesis_izquierdo", "param_spec_ls", "tk_parentesis_derecho"]
        ],

    "param_spec_ls" :
        [
            ["param_spec_lp"],
            ["e"]
        ],

    "param_spec_lp" :
        [
            ["param_spec", "param_spec_lp_p"]
        ],

    "param_spec_lp_p" :
        [
            ["tk_punto_coma", "param_spec_lp_p_p"],
            ["e"]
        ],

    "param_spec_lp_p_p" :
        [
            ["param_spec_lp"],
            ["e"]
        ],

    "param_spec" :
        [
            ["param_kind_opt", "param_spec_p"]
        ],

    "param_spec_p" :
        [
            ["type_gram"],
            ["id_subs_lp", "tk_dos_puntos", "type_gram"]
        ],

    "param_kind_opt" :
        [
            ["tk_val"],
            ["tk_var"],
            ["tk_res"],
            ["tk_ref"],
            ["e"]
        ],

    "return_spec_opt" :
        [
            ["return_spec_null"],
            ["tk_returns", "return_spec_opt_p"]
        ],

    "return_spec_opt_p" :
        [
            ["type_gram"],
            ["id_subs", "tk_dos_puntos", "type_gram"],
            ["tk_id"] ##, "TK_BOGUS" no me parecio necesario ¡¡¡REVISAR!!!
        ],

    "return_spec_null" :
        [
            ["e"]
        ],

    "param_names" :
        [
            ["tk_parentesis_izquierdo", "id_ls", "tk_parentesis_derecho", "return_name_opt"]
        ],

    "return_name_opt" :
        [
            ["tk_returns", "tk_id"],
            ["e"]
        ],

    ############################### declaration ###############################
    "var_def_lp":
        [
            ["var_def", "var_def_lp_p"]
        ],

    "var_def_lp_p":
        [
            ["tk_coma", "var_def", "var_def_lp_p"],
            ["e"]
        ],

    "var_def":
        [
            ["id_subs_lp", "var_att"]
        ],

    "var_att":  ##¡¡¡REVISAR!!!  tiene factores comunes por la izq
        [
            ["tk_dos_puntos", "type_gram"],
            ["tk_dos_puntos", "type_gram", "tk_asignacion", "expr"],
            ["tk_asignacion", "expr"],
            ["tk_punto_coma"]
        ],

    ############################### type specification ###############################
    "type_gram" :
        [
            ["subscripts", "unsub_type"],
            ["unsub_type"]
        ],
        
    "unsub_type" :
        [
            ["basic_type"],
            ["string_def"],
            ["enum_def"],
            ["pointer_def"],
            ["record_def"],
            ["union_def"],
            ["capability_def"],
            ["qualified_id"]
        ],
    
    "basic_type" :
        [
            ["tk_bool"],
            ["tk_char"],
            ["tk_int"],
            ["tk_file"],
            ["tk_real"]
        ],

    "string_def" :
        [
            ["tk_cadena", "string_def_p"]
        ],
    
    "string_def_p" :
        [
            ["tk_parentesis_cuad_izquierdo", "string_lim", "tk_parentesis_cuad_derecho"],
            ["tk_parentesis_izquierdo", "string_lim", "tk_parentesis_derecho"]
        ],

    "string_lim" :
        [
            ["expr"],
            ["tk_multiplicacion"]
        ],

    "enum_def":
        [
            ["tk_enum","tk_parentesis_izquierdo","id_lp","tk_parentesis_derecho"]    
        ],

    "pointer_def":
        [
            ["tk_ptr","pointer_def_p"]
        ],

    "pointer_def_p":
        [
            ["type_gram"],
            ["tk_any"]
        ],

    "record_def":
        [
            ["tk_rec","tk_parentesis_izquierdo","field_lp","tk_parentesis_derecho"]
        ],

    "union_def":
        [
            ["tk_union","tk_parentesis_izquierdo","field_lp","tk_parentesis_derecho"]
        ],  

    "field_lp":
        [
            ["field","field_lp_p"]
        ],

    "field_lp_p":
        [
            ["tk_punto_coma","field_lp_p_p"],
            ["e"]
        ],

    "field_lp_p_p":
        [
            ["field_lp"],
            ["e"]
        ],

    "field":
        [
            ["var_def_lp"]
        ],

    "capability_def":
        [
            ["tk_cap","cap_for"]
        ],  

    "cap_for" : 
        [
            ["qualified_id"],
            #["op_prototype"],
            ["tk_sem", "sem_proto"],
            ["tk_vm"]
        ],

    ############################### optype ###############################

    ############################### blocks and statements ###############################

    ############################### input statement ###############################

    ############################### co statement ###############################

    ############################### quantifier ###############################

    ############################### expression ###############################
    "expr" :
        [
            #literales
            ["tk_id", "expr_pp"],
            ["tk_numero", "expr_pp"],
            ["blit", "expr_pp"],
            ["tk_cadena", "expr_pp"],
            ["tk_null", "expr_pp"],
            #constructor
            ["tk_parentesis_izquierdo", "constr_item_lp", "tk_parentesis_derecho", "expr_pp"],
            #prefijos
            ["tk_no", "expr"],
            ["tk_mas", "expr"],
            ["tk_menos", "expr"],
            ["tk_arroba", "expr"],
            ["tk_interrogacion", "expr"],
            ["tk_incremento", "expr"],
            ["tk_decremento", "expr"],
            ["basic_type", "paren_expr", "expr_pp"],
            ["tk_cadena", "paren_expr", "expr_pp"],
            ["tk_low", "tk_parentesis_izquierdo", "type_gram", "tk_parentesis_derecho", "expr_pp"],
            ["tk_high", "tk_parentesis_izquierdo", "type_gram", "tk_parentesis_derecho", "expr_pp"],
            ["tk_new", "tk_parentesis_izquierdo", "subscripts_opt", "new_item", "tk_parentesis_derecho", "expr_pp"],
            ["tk_create", "create_call", "location_opt", "expr_pp"]
        ],

    "blit" :
        [
            ["tk_true"],
            ["tk_false"]
        ],

    "expr_pp" :
        [
            ["expr_p", "expr_pp"],
            ["e"]
        ],

    "expr_p":
        [
            # binary_expr
            ["tk_exponente", "expr"],
            ["tk_multiplicacion", "expr"],
            ["tk_division", "expr"],
            ["tk_mod", "expr"],
            ["tk_modulo", "expr"],
            ["tk_mas", "expr"],
            ["tk_menos", "expr"],
            ["tk_concatenacion", "expr"],
            ["tk_igual", "expr"],
            ["tk_diferente", "expr"],
            ["tk_mayor_igual", "expr"],
            ["tk_menor_igual", "expr"],
            ["tk_mayor", "expr"],
            ["tk_menor", "expr"],
            ["tk_y", "expr"],
            ["tk_o", "expr"],
            ["tk_xor", "expr"],
            ["tk_desplazar_der", "expr"],
            ["tk_desplazar_izq", "expr"],
            ["tk_swap", "expr"],
            ["tk_asignacion", "expr"],
            # suffix_expr
            ["tk_incremento"],
            ["tk_decremento"],
            ["tk_elevado"],
            ["tk_punto", "tk_id"],
            ["tk_parentesis_cuad_izquierdo", "bound_lp", "tk_parentesis_cuad_derecho"],
            ["paren_list"]
        ],

    "paren_list":
        [
            ["tk_parentesis_izquierdo","paren_item_ls","tk_parentesis_derecho"]
        ],

    "paren_item_ls":
        [
            ["expr_lp"],
            ["e"]
        ],
        
    "expr_lp":
        [
            ["expr","expr_lp_p"]
        ],
        
    "expr_lp_p":
        [
            ["tk_coma","expr","expr_lp_p"],
            ["e"]
        ],

    "constr_item_lp":
        [
            ["constr_item", "constr_item_lp_p"],
        ],

    "constr_item_lp_p":
        [
            ["tk_coma", "constr_item", "constr_item_lp_p"],
            ["e"]
        ],

    "constr_item":
        [
            ["expr"],
            ["tk_parentesis_cuad_izquierdo", "expr", "tk_parentesis_cuad_derecho", "expr"]
        ],
    
    "paren_expr":
        [
            ["tk_parentesis_izquierdo", "expr", "tk_parentesis_derecho"]
        ],

    "new_item":
        [
            ["unsub_type"],
            ["tk_sem","sem_proto"],
            ["tk_op","op_prototype"]
        ],

    "create_call":
        [
            ["rsrc_name","paren_list"]
        ],
        
    "rsrc_name":
        [
            ["tk_id"],
            ["tk_vm"]
        ],

    "location_opt":
        [
            ["tk_on"],
            ["e"]
        ],

    ############################### miscellaneous ###############################
    "qualified_id":
        [
            ["tk_id", "qualified_id_p"]
        ],

    "qualified_id_p":
        [
            ["tk_punto", "tk_id"],
            ["e"]
        ],
    
    "id_lp" :
        [
            ["tk_id", "id_lp_p"]
        ],

    "id_lp_p":
        [
            ["tk_coma", "tk_id"],
            ["e"]
        ],

    "id_subs_lp" :
        [
            ["id_subs", "id_subs_lp_p"]
        ],
        
    "id_subs_lp_p":
        [
            ["tk_coma", "id_subs"],
            ["e"]
        ],

    "id_subs":
        [
            ["tk_id", "id_subs_p"]
        ],
    
    "id_subs_p" :
        [
            ["subscripts"],
            ["e"]
        ],

    "subscripts":
        [
            ["bracketed_list", "subscripts_opt"]
        ],

    "subscripts_opt":
        [   
            ["subscripts"],
            ["e"]
        ],
    
    "bracketed_list":
        [
            ["tk_parentesis_cuad_izquierdo", "bound_lp", "tk_parentesis_cuad_derecho"]
        ],

    "bound_lp":
        [
            ["bounds", "bound_lp_p"]
        ],
    
    "bound_lp_p":
        [
            ["tk_coma", "bounds"],
            ["e"]
        ],

    "bounds":
        [
            ["bound", "bounds_p"]
        ],

    "bounds_p":
        [
            ["tk_punto_coma", "bound"],
            ["e"]
        ],

    "bound":
        [
            ["expr"],
            ["tk_multiplicacion"]
        ]
}
