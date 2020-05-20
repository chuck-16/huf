def error(loc, clause):
    if clause == 'M#':
        print(f"At MARK_>{loc}< Missing '#'")
    elif clause == "US":
        print(f"At MARK_>{loc}< Unrecognized symbol")


def interpret(code):
    code = str(code)
    outchr = ''
    temp = 0
    mult_temp = 0
    loc = -1
    print_ = False
    multiplying = False
    for sighn in code:
        loc+=1
        if not multiplying:
            if sighn == '+':
                temp +=1
            elif sighn == ">":
                if print_:
                    outchr += chr(temp)
                mult_temp = 0
                temp = 0
            elif sighn == "|":
                mult_temp = 0
                multiplying = True
            elif sighn == "#":
                print_ = True
            elif sighn == "@":
                if print_:
                    print(outchr)
                else:
                    error(loc, "M#")
                print_ = False
                outchr = ''

            else:
                error(loc, "US")
        else:
            if sighn == '+':
                mult_temp += 1
            elif sighn == "!":
                temp *= mult_temp
                mult_temp = 0
                multiplying = False



with open(input("Name Of File: "), 'r') as file:
    data = file.read().replace('\n', '')
interpret(data)








