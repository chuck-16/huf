def interpret(code):
    code = str(code)
    out = ''
    tempchr = 0
    multchar = 0
    loc = -1
    closeout = False
    multiplying = False
    for sighn in code:
        loc+=1
        if not multiplying:
            if sighn == '+':
                tempchr +=1
            elif sighn == ">":
                multchar = 0
                out += chr(tempchr)
                tempchr = 0
            elif sighn == "|":
                multchar = 0
                multiplying = True
            else:
                return f"Whats going on here?  MARK_>{loc}<"
        else:
            if sighn == '+':
                multchar += 1
            elif sighn == "!":
                tempchr *= multchar
                multchar = 0
                multiplying = False
    return out

data = ''
with open(input("Name Of File: "), 'r') as file:
    data = file.read().replace('\n', '')
print(interpret(data))







