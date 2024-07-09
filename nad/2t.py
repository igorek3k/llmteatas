def create_str(string_, n1, n2):
    if (n1 <= 0 or n1 > len(string_)):
        raise ValueError("Error! Invalid Value!")

    if (n2 <= 0 or n2 > len(string_)):
        raise ValueError("Error! Invalid Value!")

    str = string_[:n1] + string_[n2:]
    return str


test = "Карл у Клары украл кораллы"
try:
    result = create_str(test, 4, 12)
except ValueError as e:
    print(e)
    
if result == "Карл украл кораллы": #n1 = 4; n2 = 12
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")


test = "Error test"
try:
    result = create_str(test, 0, 4) #n1 = 0
    print("Test 2: FAIL")
except ValueError as e:
    print("Test 2: PASS")
    

test = "Error test"
try:
    result = create_str(test, 100, 4) #n1 = 100
    print("Test 3: FAIL")
except ValueError as e:
    print("Test 3: PASS")