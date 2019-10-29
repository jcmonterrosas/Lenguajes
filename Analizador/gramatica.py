gramatica = {
    ############################### productions & actions ###############################
    "component" : 
        [
            ["comp_kwd", "tk_id", "component_p"], ##Se podria reducir mas cambiando comp_kwd por sus producciones
            ["tk_body", "tk_id", "body_stmt_ls", "end_id", "tk_punto_coma"],
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

    ############################### spec/body contents ###############################
    "spec_stmt_ls": ## quite recursividad por izquierda REVISAR
        [
            ["spec_stmt","spec_stmt_ls_p"],
           
        ],
        
    "spec_stmt_ls_p":
        [
            ["tk_punto_coma","spec_stmt","spec_stmt_ls_p"],
            ["e"]
        ],
        
    "spec_stmt":
        [
            ["common_stmt"],
            ["extend_clause"],
            ["body_only"],
        ],

    "body_stmt_ls":  ## quite recursividad por izquierda REVISAR
        [
            ["body_stmt","body_stmt_ls_p"],
        ],

    "body_stmt_ls_p":
        [
            ["tk_punto_coma","body_stmt","body_stmt_ls_p"],
            ["e"]
        ],

    "body_stmt":
        [
            ["common_stmt"],
            ["expr"],
            ["body_only"],
            ["extend_clause"],
        ],
    
    "body_only":
        [
            ["stmt"],
            ["proc"],
            ["process"],
            ["procedure"],
            ["initial_block"],
            ["final_block"],
        ],
        
    "common_stmt":
        [
            ["decl"],
            ["import_clause"],
            ["e"],
        ],

    "import_clause":
        [
            ["tk_import", "import_list"],
        ],

    "extend_clause": ## REVISAR EN GRAMATICA (IF)
        [
            ["tk_extend", "import_list"],
        ],

    "import_list": ## quite recursividad por izquierda REVISAR
        [
            ["tk_id", "import_list_p"],
        ],

    "import_list_p":
        [
            ["tk_coma", "tk_id", "import_list_p"],
            ["e"]
        ],
    
    ############################### top-level body stmtents ###############################
    "op_decl":
        [
            ["op_or_ext","oper_def_lp"]
        ],

    "op_or_ext":
        [
            ["tk_op"],
            ["tk_external"],
        ],

    "oper_def_lp": ## quite recursividad por izquierda REVISAR
        [
            ["oper_def", "oper_def_lp_p"],
        ],
    
    "oper_def_lp_p":
        [
            ["tk_coma","oper_def","oper_def_lp_p"],
            ["e"]
        ],

    "oper_def": ##Factor comun por izquierda
        [
            ["id_subs_lp","oper_def_p"]
        ],

    "oper_def_p":
        [
            ["op_prototype"],
            ["colon_opt", "qualified_id"]
        ],

    "colon_opt":
        [
            ["tk_dos_puntos"],
            ["e"]
        ],

    "sem_decl":
        [
            ["tk_sem","sem_def_lp"],
        ],

    "sem_def_lp": ## quite recursividad por izquierda REVISAR
        [
            ["sem_def","sem_def_lp_p"]
        ],

    "sem_def_lp_p":
        [
           ["tk_coma","sem_def","sem_def_lp_p"],
           ["e"],
        ],
    
    "sem_def":
        [
            ["id_subs","sem_proto","sem_init"]
        ],

    "sem_proto":
        [
            ["return_spec_null"]
        ],
    
    "sem_init":
        [
            ["tk_asignacion","expr"],
            ["e"]
        ],

    "proc":
        [
            ["tk_proc", "tk_id", "param_names", "block", "end_id"],
        ],

    "procedure":
        [
            ["tk_procedure","tk_id","prototype","block","end_id"],

        ],

    "process":
        [
            ["tk_process","tk_id","return_spec_null","quantifiers_opt","block","end_id"],
        ],

    "initial_block":
        [
            ["tk_initial","block","tk_end","initial_opt"],

        ],

    "initial_opt":
        [
            ["tk_initial"],
            ["e"]
        ],

    "final_block":
        [
            ["tk_final","block","tk_end","final_opt"],

        ],
    
    "final_opt":
        [
            ["tk_final"],
            ["e"]
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

    ############################### declaration ###############################  ---Revisar (Revisado)
    "decl":
        [
            ["tk_punto_coma"], 
            ["type_decl"],
            ["obj_decl"],
            ["optype_decl"],
            ["sem_decl"],
            ["op_decl"],

        ],

    "type_decl":
        [
            ["tk_type", "tk_id", "tk_igual", "type_gram", "type_restriction"]
        ],
    
    "type_restriction":
        [
            ["tk_corchete_izquierdo","tk_id","tk_corchete_derecho"],
            ["e"],
        ],
    
    "obj_decl":
        [
            ["var_or_const","var_def_lp"]
        ],

    "var_or_const":
        [
            ["tk_var"],
            ["tk_const"]
        ],

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

    "var_att":  ##¡¡¡REVISAR!!!  
        [
            ["tk_dos_puntos","type_gram","var_att_p"],
            ["tk_asignacion", "expr"],
            ["tk_punto_coma"]
        ],

    "var_att_p": 
        [
            ["tk_asignacion", "expr"],
            ["e"],
        ],


    ############################### type specification ############################### -- Revisar
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
            ["op_prototype"],
            ["tk_sem", "sem_proto"],
            ["tk_vm"]
        ],

    ############################### optype ###############################  (Revisado)

    "optype_decl":
        [
            ["tk_optype","tk_id","eq_opt","op_prototype"],
        ],

    "op_prototype":
        [
            ["prototype","op_restriction_opt"]
        ],

    "eq_opt":
        [
            ["tk_igual"],
            ["e"],
        ],
    
    "op_restriction_opt":
        [
            ["tk_corchete_izquierdo","op_restriction","tk_corchete_derecho"],
            ["e"],
        ],

    "op_restriction": #quitar factor comun por izquierda
        [
            ["tk_call", "op_restriction_p"],
            ["tk_send", "op_restriction_p_p"],

        ],

    "op_restriction_p":
        [
            ["tk_coma", "tk_send"],
            ["e"],
        ],

    "op_restriction_p_p":
        [
            ["tk_coma", "tk_call"],
            ["e"],
        ],

    ############################### blocks and statements ############################### (Revisado)

    "block":
        [
            ["block_items"]
        ],

    "block_items": # Recursion por izquierda
        [
            ["block_item","block_items_p"],
        ],

    "block_items_p":
        [
            ["tk_punto_coma","block_item","block_items_p"],
            ["e"]
        ],

    "block_item":
        [
            ["decl"],
            ["stmt"],
            ["expr"],
            ["import_clause"],
            ["e"],
        ],
    
    "stmt":
        [
            ["tk_skip"],
            ["stop_stmt"],
            ["tk_exit"],
            ["tk_next"],
            ["tk_return"],
            ["tk_reply"],
            ["tk_forward", "invocation"],
            ["send_stmt"],
            ["explicit_call"],
            ["tk_destroy", "expr"],
            ["tk_begin", "block", "tk_end"],
            ["tk_if", "guarded_cmd_lp", "else_cmd_opt", "tk_fi"],
            ["tk_do", "guarded_cmd_lp", "else_cmd_opt", "tk_od"],
            ["tk_fa", "quantifier_lp", "tk_ejecuta", "block", "tk_af"],
            ["tk_V", "tk_parentesis_izquierdo", "expr", "tk_parentesis_derecho"],
            ["input_stmt"],
            ["tk_receive", "expr", "paren_list"],
            ["tk_P", "tk_parentesis_izquierdo", "expr", "tk_parentesis_derecho"],
            ["concurrent_stmt"],
        ],

    "stop_stmt":
        [
            ["tk_stop","exit_code_opt"]
        ],

    "exit_code_opt":
        [ 
            ["tk_parentesis_izquierdo","expr","tk_parentesis_derecho"],
            ["e"],
        ],
        
    "send_stmt":
        [
            ["tk_send","invocation"],
        ],

    "explicit_call":
        [
            ["tk_call","invocation"]
        ],
        
    "guarded_cmd_lp": #Recursion izquierda
        [
            ["guarded_cmd","guarded_cmd_lp_p"],
        ],
    
    "guarded_cmd_lp_p": 
        [
            ["tk_separa","guarded_cmd","guarded_cmd_lp_p"],
            ["e"]
        ],

    "guarded_cmd":
        [
            ["expr","tk_ejecuta","block"],
        ],
    
    "else_cmd_opt":
        [
            ["tk_separa","tk_else","tk_ejecuta","block"],
            ["e"]
        ],
    
    
    ############################### input statement ###############################
    "input_stmt":
        [
            ["tk_in","in_cmd_lp","else_cmd_opt","tk_ni"] 
        ],
        
    "in_cmd_lp": #recursividad por izquierda
        [
            ["in_cmd","in_cmd_lp_p"]
        ],
        
    "in_cmd_lp_p":
        [
            ["tk_separa","in_cmd","in_cmd_lp_p"],
            ["e"]
        ],

    "in_cmd":
        [
            ["quantifiers_opt", "in_spec", "sync_expr_opt", "sched_expr_opt", "tk_ejecuta", "block"]
        ],

    "in_spec":
        [
            ["in_op","param_names"]
        ],
    
    "in_op": #factor comun por izuierda
        [
            ["qualified_id", "in_op_p"],
        ],

    "in_op_p":
        [
            ["subscripts"],
            ["e"],
        ],

    "sync_expr_opt": ## Se añade regla ya que existen dos tk_and
        [
            ["tk_and", "expr"],
            ["tk_y", "expr"],
            ["tk_suchthat","expr"],
            ["e"]
        ],
    
    "sched_expr_opt":
        [
            ["tk_by","expr"],
            ["e"]
        ],

    ############################### co statement ###############################
    "concurrent_stmt":
        [
            ["tk_co", "concurrent_cmd_lp", "tk_oc"]
        ],

    "concurrent_cmd_lp": ###Se quita recursividad por izquierda
        [
            ["concurrent_cmd", "concurrent_cmd_lp_p"]
        ],

    "concurrent_cmd_lp_p":
        [
            ["tk_paralela", "concurrent_cmd" "concurrent_cmd_lp_p"], 
            ["e"] 
        ],

    "concurrent_cmd":
        [
            ["quantifiers_opt", "separator_opt", "concurrent_invocation", "post_processing_opt"]
        ],

    "separator_opt": ## Se quita recursividad por izquierda Revisar!!
        [
            ["tk_punto_coma", "separator_opt"],
            ["e"]
        ],

    "concurrent_invocation":
        [
            ["explicit_call"],
            ["send_stmt"],
            ["expr"]
        ],

    "post_processing_opt":
        [
            ["tk_ejecuta", "block"],
            ["e"]
        ],

    ############################### quantifier ###############################
    "quantifiers_opt" :
        [
            ["tk_parentesis_izquierdo", "quantifier_lp", "tk_parentesis_derecho"],
            ["e"]
        ],

    "quantifier_lp" : ###Se quita recursividad por izquierda
        [
            ["quantifier", "quantifier_lp_p"]
        ],

    "quantifier_lp_p" :
        [
            ["tk_coma", "quantifier", "quantifier_lp_p"],
            ["e"]
        ],

    "quantifier" :
        [
            ["tk_id", "tk_asignacion", "expr", "direction", "expr", "step_opt", "such_that_opt"]
        ],

    "direction" :
        [
            ["tk_to"],
            ["tk_downto"]
        ],

    "step_opt" :
        [
            ["tk_by", "expr"],
            ["e"]
        ],

    "such_that_opt" :
        [
            ["tk_suchthat", "expr"],
            ["e"]
        ],

    ############################### expression ###############################
    "expr" :
        [
            ["tk_id", "expr_pp"],
            #literales
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
            # create_expr
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
            # invocation
            ["paren_list"]
        ],

    "new_item":
        [
            ["unsub_type"],
            ["tk_sem","sem_proto"],
            ["tk_op","op_prototype"]
        ],

    "paren_expr":
        [
            ["tk_parentesis_izquierdo", "expr", "tk_parentesis_derecho"]
        ],

    "invocation" :
        [
            ["expr", "paren_list"]
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
            ["tk_on", "expr"],
            ["e"]
        ],

    ############################### miscellaneous ############################### -- Revisar - (Revisado)
    "qualified_id": #terminos en comun por izquierda
        [
            ["tk_id", "qualified_id_p"]
        ],
    
    "qualified_id_p":
        [
            ["tk_punto", "tk_id"],
            ["e"]
        ],

    "end_id":
        [
            ["tk_end","id_opt"]
        ],

    "id_opt":
        [
            ["tk_id"],
            ["e"]
        ],
    
    "id_ls":
        [
            ["id_lp"],
            ["e"]
        ],
    
    "id_lp" : #recursion por izq
        [
            ["tk_id", "id_lp_p"]
        ],

    "id_lp_p":
        [
            ["tk_coma", "tk_id","id_lp_p"],
            ["e"]
        ],

    "id_subs_lp" : #recursion por izq
        [
            ["id_subs", "id_subs_lp_p"]
        ],
        
    "id_subs_lp_p":
        [
            ["tk_coma", "id_subs","id_subs_lp_p"],
            ["e"]
        ],

    "id_subs": #factor comun por izquierda
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

    "bound_lp": #recursividad por izquierda
        [
            ["bounds", "bound_lp_p"]
        ],
    
    "bound_lp_p":
        [
            ["tk_coma", "bounds","bound_lp_p"],
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
