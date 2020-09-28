import LogicoI
import LogicoO
import LogicoX


def select(cadena, memoriaActual, estrucActual):
    estado = 0
    signo = 1
    palabra = ""
    estrucaux = ""
    condicion1 = ""
    condicion2 = ""
    comparar1 = ""
    comparar2 = ""
    signo1 = ""
    signo2 = ""
    logicoI = False
    logicoO = False
    logicoX = False
    bandera = False
    comillas = False

    # Obtener estructura de la cadena
    for i in cadena:
        if estado == 0:
            if palabra == "select":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if palabra == "where":
                bandera = True
                estado = 2
                palabra = ""
            if i != " " and i != ",":
                palabra = palabra + i.lower()
            elif i == " " or i == ",":
                estrucaux = estrucaux + " " + palabra
                palabra = ""
        elif estado == 2:
            if i == '"':
                if comillas:
                    comillas = False
                else:
                    comillas = True
            elif i == "<" or i == ">" or i == "!" or i == "=":
                if signo == 1:
                    if condicion1 == "" and condicion2 == "":
                        signo1 = signo1 + i
                        condicion1 = palabra
                        palabra = ""
                    elif condicion1 != "" and condicion2 == "":
                        signo1 = signo1 + i
                elif signo == 2:
                    if condicion1 != "" and condicion2 == "":
                        signo2 = signo2 + i
                        condicion2 = palabra
                        palabra = ""
                    elif condicion1 != "" and condicion2 != "":
                        signo2 = signo2 + i
            elif i == " " and not comillas:
                if condicion1 != "" and comparar1 == "" and condicion2 == "" and comparar2 == "":
                    comparar1 = palabra
                    palabra = ""
                elif palabra == "and":
                    logicoI = True
                    signo = 2
                    palabra = ""
                elif palabra == "or":
                    logicoO = True
                    signo = 2
                    palabra = ""
                elif palabra == "xor":
                    logicoX = True
                    signo = 2
                    palabra = ""
            else:
                if comillas:
                    if i != " ":
                        palabra = palabra + i
                else:
                    if condicion1 == "" and comparar1 == "" and condicion2 == "" and comparar2 == "" and i != " ":
                        palabra = palabra + i.lower()
                    elif condicion1 != "" and comparar1 == "" and condicion2 == "" and comparar2 == "" and i != " ":
                        if i != '"':
                            palabra = palabra + i
                    elif condicion1 != "" and comparar1 != "" and condicion2 == "" and comparar2 == "" and i != " ":
                        palabra = palabra + i.lower()
                    elif condicion1 != "" and comparar1 != "" and condicion2 != "" and comparar2 == "" and i != " ":
                        if i != '"':
                            palabra = palabra + i

    if bandera:
        if comparar1 == "":
            comparar1 = palabra
        elif comparar2 == "":
            comparar2 = palabra
    else:
        estrucaux = estrucaux + " " + palabra
    auxiliar = estrucaux.split()

    # Estructura de la busqueda de datos
    if auxiliar[0] == "*":
        if bandera:
            if logicoI:
                LogicoI.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                               estrucActual)
            elif logicoO:
                LogicoO.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                               estrucActual)
            elif logicoX:
                LogicoX.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                               estrucActual)
            else:
                if signo1 == "=":
                    contador = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                                imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                                imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1

                elif signo1 == "<":
                    contador = 0
                    for i in range(0, len(memoriaActual)):
                        suma1 = 0
                        suma2 = 0
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "False" and comparar1 == "True":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) < float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 < suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) < float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 < suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1

                elif signo1 == ">":
                    contador = 0
                    suma1 = 0
                    suma2 = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) > float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 > suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) > float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 > suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1

                elif signo1 == "<=":
                    contador = 0
                    suma1 = 0
                    suma2 = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "False" and comparar1 == "True":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) <= float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 <= suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "False" and comparar1 == "True":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) <= float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 <= suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1

                elif signo1 == ">=":
                    contador = 0
                    suma1 = 0
                    suma2 = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) >= float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 >= suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "True":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    imprimir(i, estrucActual, memoriaActual)
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) >= float(comparar1):
                                            imprimir(i, estrucActual, memoriaActual)
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 >= suma2:
                                            imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1

                elif signo1 == "!=":
                    contador = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                                imprimir(i, estrucActual, memoriaActual)
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                                imprimir(i, estrucActual, memoriaActual)
                            contador = contador + 1
                else:
                    print("Signo de consulta incorrecto")
        else:
            for i in memoriaActual:
                print(i)
    else:
        if bandera:
            if logicoI:
                LogicoI.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                                estrucActual, auxiliar)
            elif logicoO:
                LogicoO.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                                estrucActual, auxiliar)
            elif logicoX:
                LogicoX.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual,
                                estrucActual, auxiliar)
            elif signo1 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            elif signo1 == "<":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    suma1 = 0
                    suma2 = 0
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            elif signo1 == ">":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            elif signo1 == "<=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            elif signo1 == ">=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "True":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            elif signo1 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            imprimir2(i, estrucActual, memoriaActual, auxiliar)
                        contador = contador + 1

            else:
                print("Signo de consulta incorrecto")
        else:
            for u in auxiliar:
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == u:
                            print(u + ": " + memoriaActual[i])
                        contador = 0
                    else:
                        if estrucActual[contador] == u:
                            print(u + ": " + memoriaActual[i])
                        contador = contador + 1


def numero(cadena):
    bandera = False
    estado = 0
    for i in cadena:
        if estado == 0:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or \
                    i == "8" or i == "9":
                bandera = True
            elif i == ".":
                bandera = True
                estado = 1
            else:
                bandera = False
                return bandera
        elif estado == 1:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or \
                    i == "8" or i == "9":
                bandera = True
            elif i == ".":
                bandera = False
                return bandera
            else:
                bandera = False
                return bandera
    return bandera


def imprimir(i, estrucActual, memoriaActual):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    for z in estrucActual:
        print(z + ": " + memoriaActual[posauxiliar])
        posauxiliar = posauxiliar + 1
    print("")


def imprimir2(i, estrucActual, memoriaActual, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    for u in auxiliar:
        posauxiliar = posdata - posestruc
        for z in estrucActual:
            if u == z:
                print(u + ": " + memoriaActual[posauxiliar])
                posauxiliar = posauxiliar + 1
            else:
                posauxiliar = posauxiliar + 1
        print("")
