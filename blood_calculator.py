def interface():
    print("BLood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice:")
        if choice == "9":
            return 
        elif choice =="1":
            HDL_driver()
        elif choice =="2":
            LDL_driver()
        elif choice =="3":
            cholesterol_driver()

def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif HDL_value >=40:
        return "Borderline Low"
    else:
        return "Low"

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

    # LDL Functions Below 
def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)

def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

def check_LDL(LDL_value):
    if LDL_value >= 190:
        return "Very High"
    elif LDL_value >=160:
        return "High"
    elif LDL_value >=130:
        return "Borderline High"
    else:
        return "Normal"

def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))
    
    # LDL Functions Below 
def cholesterol_driver():
    chol_value = input_chol()
    answer = check_chol(chol_value)
    output_chol_result(chol_value, answer)

def input_chol():
    chol_input = input("Enter the cholesterol value:")
    return int(chol_input)

def check_chol(chol_value):
    if chol_value >=240:
        return "High"
    elif chol_value >=200:
        return "Borderline High"
    else:
        return "Normal"

def output_chol_result(chol_value, charac):
    print("The results for a cholesterol value of {} is {}".format(chol_value, charac))



if __name__ == '__main__':
    interface()