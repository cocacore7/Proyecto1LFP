def logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual):
    if signo1 == "=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    return final
                contador = contador + 1

    elif signo1 == "<":
        contador = 0
        for i in range(0, len(memoriaActual)):
            suma1 = 0
            suma2 = 0
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
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
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
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
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = contador + 1

    elif signo1 == ">":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
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
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
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
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = contador + 1

    elif signo1 == "<=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = contador + 1

    elif signo1 == ">=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                                return final
                contador = contador + 1

    elif signo1 == "!=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    final = ultimo(signo2, i, estrucActual, memoriaActual, comparar2, condicion2)
                    return final
                contador = contador + 1

    else:
        print("Signo de consulta erroneo")


def logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar):
    if signo1 == "=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                    final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    return final
                contador = contador + 1

    elif signo1 == "<":
        contador = 0
        for i in range(0, len(memoriaActual)):
            suma1 = 0
            suma2 = 0
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
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
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
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
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 < suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final

    elif signo1 == ">":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
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
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
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
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 > suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = contador + 1

    elif signo1 == "<=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) <= float(comparar1):
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 <= suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = contador + 1

    elif signo1 == ">=":
        contador = 0
        suma1 = 0
        suma2 = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "True" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1:
                    if memoriaActual[i] == "False" and comparar1 == "True":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "False" and comparar1 == "False":
                        final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                        return final
                    elif memoriaActual[i] == "True" and comparar1 == "True":
                        print("")
                    elif memoriaActual[i] == "True" and comparar1 == "False":
                        print("")
                    else:
                        num = numero(memoriaActual[i])
                        if num:
                            if float(memoriaActual[i]) >= float(comparar1):
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                        else:
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            for a in comparar1:
                                suma2 = suma2 + ord(a)
                            if suma1 >= suma2:
                                final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                                return final
                contador = contador + 1

    elif signo1 == "!=":
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    return final
                contador = 0
            else:
                if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                    final = ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar)
                    return final
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
        final = imprimirigual(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final

    elif signo2 == "<":
        final = imprimirmenor(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final

    elif signo2 == ">":
        final = imprimirmayor(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final
    elif signo2 == "<=":
        final = imprimirmenorI(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final

    elif signo2 == ">=":
        final = imprimirmayorI(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final

    elif signo2 == "!=":
        final = imprimirnoigual(i, estrucActual, memoriaActual, condicion2, comparar2)
        return final


def ultimo2(signo2, i, estrucActual, memoriaActual, comparar2, condicion2, auxiliar):
    if signo2 == "=":
        final = imprimirigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final

    elif signo2 == "<":
        final = imprimirmenor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final

    elif signo2 == ">":
        final = imprimirmayor2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final
    elif signo2 == "<=":
        final = imprimirmenorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final

    elif signo2 == ">=":
        final = imprimirmayorI2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final

    elif signo2 == "!=":
        final = imprimirnoigual2(i, estrucActual, memoriaActual, condicion2, comparar2, auxiliar)
        return final


def imprimir(posauxiliar, estrucActual, memoriaActual):
    final = []
    for z in estrucActual:
        final.append(z + ": " + memoriaActual[posauxiliar])
        posauxiliar = posauxiliar + 1
    return final


def imprimir2(posauxiliar, estrucActual, memoriaActual, auxiliar):
    aux = posauxiliar
    final = []
    for u in auxiliar:
        posauxiliar = aux
        for z in estrucActual:
            if u == z:
                final.append(u + ": " + memoriaActual[posauxiliar])
                posauxiliar = posauxiliar + 1
            else:
                posauxiliar = posauxiliar + 1
    return final


def imprimirigual(i, estrucActual, memoriaActual, condicion2, comparar2):
    posestruc = i
    posdata = i
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    datos = posauxiliar
    for z in estrucActual:
        if z == condicion2 and memoriaActual[posauxiliar] == comparar2:
            final = imprimir(datos, estrucActual, memoriaActual)
            return final
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
            final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            return final
        posauxiliar = posauxiliar + 1


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
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
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
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 < suma4:
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
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
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
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
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 < suma4:
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
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
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
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
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 > suma4:
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
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
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
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
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 > suma4:
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
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
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) <= float(comparar2):
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 <= suma4:
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
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
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) <= float(comparar2):
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 <= suma4:
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
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
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                final = imprimir(datos, estrucActual, memoriaActual)
                return final
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) >= float(comparar2):
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 >= suma4:
                        final = imprimir(datos, estrucActual, memoriaActual)
                        return final
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
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
            elif memoriaActual[posaux] == "True" and comparar2 == "True":
                final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                return final
            elif memoriaActual[posaux] == "False" and comparar2 == "True":
                print("")
            elif memoriaActual[posaux] == "False" and comparar2 == "False":
                print("")
            else:
                num = numero(memoriaActual[posaux])
                if num:
                    if float(memoriaActual[posaux]) >= float(comparar2):
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
                else:
                    for a in memoriaActual[posaux]:
                        suma3 = suma3 + ord(a)
                    for a in comparar2:
                        suma4 = suma4 + ord(a)
                    if suma3 >= suma4:
                        final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
                        return final
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
            final = imprimir(datos, estrucActual, memoriaActual)
            return final
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
            final = imprimir2(datos, estrucActual, memoriaActual, auxiliar)
            return final
        posauxiliar = posauxiliar + 1
    print("")
