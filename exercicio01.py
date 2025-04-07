nummeses = int(input("Digite um numero"))

if nummeses >= 1 and nummeses <=12:

    if nummeses == 1:
        print("janeiro")
    elif nummeses == 2:
        print("fevereiro")
    elif nummeses == 3:
        print("marco")
    elif nummeses == 4:
        print("abril")
    elif nummeses == 5:
        print("maio")
    elif nummeses == 6:
        print("junho")
    elif nummeses == 7:
        print("julho")
    elif nummeses == 8:
        print("agosto")
    elif nummeses == 9:
        print("setembro")
    elif nummeses == 10:
        print("outubro")
    elif nummeses == 11:
        print("novembro")
    else:
        print("dezembro")
else:
    print ("valor invalido")
