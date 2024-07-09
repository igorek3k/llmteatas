def translit(str):
    uppercase_letters = {
    1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D',
    1045: 'E', 1025: 'Yo', 1046: 'Zh', 1047: 'Z',
    1048: 'I', 1049:'Y', 1050: 'K', 1051: 'L', 1052: 'M',
    1053: 'N', 1054:'O', 1055: 'P', 1056: 'R', 1057: 'S',
    1058: 'T', 1059:'U', 1060: 'F', 1061: 'H', 1062: 'C',
    1063: 'Ch', 1064: 'Sh', 1065: 'Sch', 1066: '"',
    1067: 'I', 1068: '\'', 1069: 'E', 1070: 'Yu', 1071: 'Ya'
    }

    lowercase_letters = {
        1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd',
        1077: 'e', 1105: 'yo', 1078: 'zh', 1079: 'z', 1080: 'i',
        1081: 'y', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n',
        1086: 'o', 1087: 'p', 1088: 'r', 1089: 's', 1090: 't',
        1091: 'u', 1092: 'f', 1093: 'h', 1094: 'c',  1095: 'ch',
        1096: 'sh', 1097: 'sch', 1098: '"', 1099: 'i', 1100:'\'',
        1101: 'e', 1102: 'yu', 1103: 'ya'
    }
    
    result = ""
    for i in range (0, len(str)):
        code = ord(str[i])
        if (code >= 1072 and code <= 1103 or code == 1105):
            result += lowercase_letters[code]
        elif (code >= 1040 and code <= 1071 or code == 1025):
            char = uppercase_letters[code]
            if (len(str) > i+1):
                if (ord(str[i+1]) >= 1040 and ord(str[i+1]) <= 1071 or ord(str[i+1]) == 1025):
                    char = uppercase_letters[code].upper()
            else:
                char = uppercase_letters[code].upper()
            result += char
        else:
            result += str[i]
    return result
                        
test = "Я обожаю программировать на Турбо Паскале!"
correct = "Ya obozhayu programmirovat' na Turbo Paskale!"
if translit(test) == correct:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")
    
test = "ЮЛЯ"
correct = "YULYA"
if translit(test) == correct:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")
    
test = "Юля"
correct = "Yulya"
if translit(test) == correct:
    print("Test 3: PASS")
else:
    print("Test 3: FAIL")
   
test = "ЗАкутоК"
correct = "ZAkutoK"
if translit(test) == correct:
    print("Test 4: PASS")
else:
    print("Test 4: FAIL")
    
test = "АлЁнушка"
correct = "AlYonushka"
if translit(test) == correct:
    print("Test 5: PASS")
else:
    print("Test 5: FAIL")
   
test = "АлЁНушка"
correct = "AlYONushka"
if translit(test) == correct:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

