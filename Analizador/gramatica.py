gramatica = {
    "Exp_m1" : [["Exp_m2","Exp_m1_prima"]],
    "Exp_m1_prima" : [["tk_mas", "Exp_m2", "Exp_m1_prima"],["e"]],
    "Exp_m2" : [["Exp_m3","Exp_m2_prima"]],
    "Exp_m2_prima" : [["tk_menos", "Exp_m3", "Exp_m2_prima"],["e"]],
    "Exp_m3" : [["Exp_m4","Exp_m3_prima"]],
    "Exp_m3_prima" : [["tk_exponente", "Exp_m4", "Exp_m3_prima"],["e"]],
    "Exp_m4" : [["Exp_m5","Exp_m4_prima"]],
    "Exp_m4_prima" : [["tk_multiplicacion", "Exp_m5", "Exp_m4_prima"],["e"]],
    "Exp_m5" : [["Exp_m6","Exp_m5_prima"]],
    "Exp_m5_prima" : [["tk_division", "Exp_m6", "Exp_m5_prima"],["e"]],
    "Exp_m6" : [["Exp_m7","Exp_m6_prima"]],
    "Exp_m6_prima" : [["tk_modulo", "Exp_m7", "Exp_m6_prima"],["e"]],
    "Exp_m7" : [["Exp_m8","Exp_m7_prima"]],
    "Exp_m7_prima" : [["mod", "Exp_m8", "Exp_m7_prima"],["e"]],
    "Exp_m8" : [["tk_id"],["tk_numero"]]
}

