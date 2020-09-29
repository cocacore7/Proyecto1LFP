def logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual):
    if signo1 == "=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    elif signo1 == "<":
        contador = 0
        for i in range(0, len(memoriaActual)):
            suma1 = 0
            suma2 = 0
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
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
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
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
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    elif signo1 == ">":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
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
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
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
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    elif signo1 == "<=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    elif signo1 == ">=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    elif signo1 == "!=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                contador = contador + 1

    else:
        print("Signo de consulta erroneo")


def logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar):
    if signo1 == "=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    elif signo1 == "<":
        contador = 0
        for i in range(0, len(memoriaActual)):
            suma1 = 0
            suma2 = 0
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
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
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
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
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    elif signo1 == ">":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
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
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
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
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    elif signo1 == "<=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    elif signo1 == ">=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    elif signo1 == "!=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                contador = contador + 1

    else:
        print("Signo de consulta erroneo")


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


def ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2):
    if signo2 == "=":
        imprimirigual(i, estrucActual, memoriaActual, condicion2, comparar2)

    elif signo2 == "<":
        imprimirmenor(i, estrucActual, memoriaActual, condicion2, comparar2)

    elif signo2 == ">":
        imprimirmayor(i, estrucActual, memoriaActual, condicion2, comparar2)

    elif signo2 == "<=":
        imprimirmenorI(i, estrucActual, memoriaActual, condicion2, comparar2)

    elif signo2 == ">=":
        imprimirmayorI(i, estrucActual, memoriaActual, condicion2, comparar2)

    if signo2 == "!=":
        imprimirnoigual(i, estrucActual, memoriaActual, condicion2, comparar2)


def ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar):
    if signo2 == "=":
        imprimirigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)

    elif signo2 == "<":
        imprimirmenor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)

    elif signo2 == ">":
        imprimirmayor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)

    elif signo2 == "<=":
        imprimirmenorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)

    elif signo2 == ">=":
        imprimirmayorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)

    if signo2 == "!=":
        imprimirnoigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)


def imprimir(posauxiliar, estrucActual, memoriaActual):
    for z in estrucActual:
        print(z + ": " + memoriaActual[posauxiliar])
        posauxiliar = posauxiliar + 1
    print("")


def imprimir2(posauxiliar, estrucActual, memoriaActual, auxiliar):
    aux = posauxiliar
    for u in auxiliar:
        posauxiliar = aux
        for z in estrucActual:
            if u == z:
                print(u + ": " + memoriaActual[posauxiliar])
                posauxiliar = posauxiliar + 1
            else:
                posauxiliar = posauxiliar + 1
    print("")


def imprimirigual(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    datos = posauxiliar
    for z in estrucActual:
        if z == condicion2 and memoriaActual[posauxiliar] == comparar2:
            imprimir(datos, estrucActual, memoriaActual)
        posauxiliar = posauxiliar + 1
    print("")


def imprimirigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    datos = posauxiliar
    for z in estrucActual:
        if z == condicion2 and memoriaActual[posauxiliar] == comparar2:
            imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posauxiliar = posauxiliar + 1
    print("")


def imprimirmenor(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "False" and comparar2 == "True":
                imprimir(datos, estrucActual, memoriaActual)
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) < float(comparar2):
                        imprimir(datos, estrucActual, memoriaActual)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 < suma4:
                        imprimir(datos, estrucActual, memoriaActual)
        posaux = posaux + 1


def imprimirmenor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "False" and comparar2 == "True":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) < float(comparar2):
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 < suma4:
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posaux = posaux + 1


def imprimirmayor(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                imprimir(datos, estrucActual, memoriaActual)
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) > float(comparar2):
                        imprimir(datos, estrucActual, memoriaActual)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 > suma4:
                        imprimir(datos, estrucActual, memoriaActual)
        posaux = posaux + 1


def imprimirmayor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) > float(comparar2):
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 > suma4:
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posaux = posaux + 1


def imprimirmenorI(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                imprimir(datos, estrucActual, memoriaActual)
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                imprimir(datos, estrucActual, memoriaActual)
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) <= float(comparar2):
                        imprimir(datos, estrucActual, memoriaActual)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 <= suma4:
                        imprimir(datos, estrucActual, memoriaActual)
        posaux = posaux + 1


def imprimirmenorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                print("")
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) <= float(comparar2):
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 <= suma4:
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posaux = posaux + 1


def imprimirmayorI(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                imprimir(datos, estrucActual, memoriaActual)
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                imprimir(datos, estrucActual, memoriaActual)
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) >= float(comparar2):
                        imprimir(datos, estrucActual, memoriaActual)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 >= suma4:
                        imprimir(datos, estrucActual, memoriaActual)
        posaux = posaux + 1


def imprimirmayorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posaux = posdata - posestruc
    datos = posaux
    for z in estrucActual:
        suma3 = 0
        suma4 = 0
        if z == condicion2:
            if memoriaActual[posaux] == "True" and comparar2 == "False":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) >= float(comparar2):
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 >= suma4:
                        imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posaux = posaux + 1


def imprimirnoigual(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    datos = posauxiliar
    for z in estrucActual:
        if z == condicion2 and memoriaActual[posauxiliar] != comparar2:
            imprimir(datos, estrucActual, memoriaActual)
        posauxiliar = posauxiliar + 1
    print("")


def imprimirnoigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    datos = posauxiliar
    for z in estrucActual:
        if z == condicion2 and memoriaActual[posauxiliar] != comparar2:
            imprimir2(datos, estrucActual, memoriaActual, auxiliar)
        posauxiliar = posauxiliar + 1
    print("")
