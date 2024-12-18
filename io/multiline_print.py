# the output is multiline print
def multiline_print():
    var_1 = 1
    var_2 = 2  
    var_3 = 3
    print(f'''
    this is a test of multiline print,
    var_1 = {var_1},
    var_2 = {var_2},
    var_3 = {var_3}
    ''')
    
# the output is single line print
def multiline_input():
    var_1 = 1
    var_2 = 2
    var_3 = 3
    print(
        "this is a test of multiline input,"
        f"var_1 = {var_1},"
        f"var_2 = {var_2},"
        f"var_3 = {var_3}")

multiline_print() 
''' output: 
    this is a test of multiline print,
    var_1 = 1,
    var_2 = 2,
    var_3 = 3 '''
multiline_input()
''' output: 
    this is a test of multiline input,var_1 = 1,var_2 = 2,var_3 = 3 '''