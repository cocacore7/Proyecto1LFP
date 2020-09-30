import ReporteLogicoI
import ReporteLogicoO
import ReporteLogicoX


def select(cadena, memoriaActual, estrucActual, tokens):
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
                tokens.append("tk: WHERE (Palabra Reservada)")
                bandera = True
                estado = 2
                palabra = ""
            if i != " " and i != ",":
                palabra = palabra + i.lower()
            elif i == " " or i == ",":
                if i == ",":
                    tokens.append("tk: , (Separador)")
                for z in estrucActual:
                    if palabra == "*":
                        tokens.append("tk: * (Identificador)")
                    elif palabra == z:
                        tokens.append("tk: " + z + " (Identificador)")
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
                        tokens.append("tk: " + condicion1 + " (Identificador)")
                        palabra = ""
                    elif condicion1 != "" and condicion2 == "":
                        signo1 = signo1 + i
                elif signo == 2:
                    if condicion1 != "" and condicion2 == "":
                        signo2 = signo2 + i
                        condicion2 = palabra
                        tokens.append("tk: " + condicion2 + " (Identificador)")
                        palabra = ""
                    elif condicion1 != "" and condicion2 != "":
                        signo2 = signo2 + i
            elif i == " " and not comillas:
                if condicion1 != "" and comparar1 == "" and condicion2 == "" and comparar2 == "":
                    comparar1 = palabra
                    if comparar1 != "":
                        tokens.append("tk: " + signo1 + " (Signo)")
                        comprobar = numero(comparar1)
                        if comprobar:
                            tokens.append("tk: " + comparar1 + " (Valor)")
                        else:
                            if comparar1 != "True" or comparar1 != "False":
                                tokens.append('tk: " (Texto)')
                                tokens.append("tk: " + comparar1 + " (Valor)")
                                tokens.append('tk: " (Texto)')
                            else:
                                tokens.append("tk: " + comparar1 + " (Valor)")
                    palabra = ""
                elif palabra == "and":
                    tokens.append("tk: AND (Palabra Reservada)")
                    logicoI = True
                    signo = 2
                    palabra = ""
                elif palabra == "or":
                    tokens.append("tk: OR (Palabra Reservada)")
                    logicoO = True
                    signo = 2
                    palabra = ""
                elif palabra == "xor":
                    tokens.append("tk: XOR (Palabra Reservada)")
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
            comprobar = numero(comparar1)
            if comprobar:
                tokens.append("tk: " + comparar1 + " (Valor)")
            else:
                if comparar1 != "True" or comparar1 != "False":
                    tokens.append('tk: " (Texto)')
                    tokens.append("tk: " + comparar1 + " (Valor)")
                    tokens.append('tk: " (Texto)')
                else:
                    tokens.append("tk: " + comparar1 + " (Valor)")
        elif comparar2 == "":
            comparar2 = palabra
            tokens.append("tk: " + signo2 + " (Signo)")
            tokens.append("tk: " + comparar2 + " (Valor)")
    else:
        estrucaux = estrucaux + " " + palabra
    auxiliar = estrucaux.split()

    # Estructura de la busqueda de datos
    if auxiliar[0] == "*":
        if bandera:
            if logicoI:
                final = ReporteLogicoI.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual)
                return final
            elif logicoO:
                final = ReporteLogicoO.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual)
                return final
            elif logicoX:
                final = ReporteLogicoX.logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual)
                return final
            else:
                if signo1 == "=":
                    contador = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                                final = imprimir(i, estrucActual, memoriaActual)
                                return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                                final = imprimir(i, estrucActual, memoriaActual)
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
                                    final = imprimir(i, estrucActual, memoriaActual)
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
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 < suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    final = imprimir(i, estrucActual, memoriaActual)
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
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 < suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
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
                                    final = imprimir(i, estrucActual, memoriaActual)
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
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 > suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "False":
                                    final = imprimir(i, estrucActual, memoriaActual)
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
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 > suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
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
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) <= float(comparar1):
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 <= suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "False" and comparar1 == "True":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) <= float(comparar1):
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 <= suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
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
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "True" and comparar1 == "True":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) >= float(comparar1):
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 >= suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1:
                                if memoriaActual[i] == "True" and comparar1 == "True":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "True" and comparar1 == "False":
                                    final = imprimir(i, estrucActual, memoriaActual)
                                    return final
                                elif memoriaActual[i] == "False" and comparar1 == "True":
                                    print("")
                                elif memoriaActual[i] == "False" and comparar1 == "False":
                                    print("")
                                else:
                                    num = numero(memoriaActual[i])
                                    if num:
                                        if float(memoriaActual[i]) >= float(comparar1):
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                                    else:
                                        for a in memoriaActual[i]:
                                            suma1 = suma1 + ord(a)
                                        for a in comparar1:
                                            suma2 = suma2 + ord(a)
                                        if suma1 >= suma2:
                                            final = imprimir(i, estrucActual, memoriaActual)
                                            return final
                            contador = contador + 1

                elif signo1 == "!=":
                    contador = 0
                    for i in range(0, len(memoriaActual)):
                        if contador == len(estrucActual) - 1:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                                final = imprimir(i, estrucActual, memoriaActual)
                                return final
                            contador = 0
                        else:
                            if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                                final = imprimir(i, estrucActual, memoriaActual)
                                return final
                            contador = contador + 1
                else:
                    print("Signo de consulta incorrecto")
        else:
            return memoriaActual
    else:
        if bandera:
            if logicoI:
                final = ReporteLogicoI.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar)
                return final
            elif logicoO:
                final = ReporteLogicoO.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar)
                return final
            elif logicoX:
                final = ReporteLogicoX.logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar)
                return final
            elif signo1 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
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
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                return final
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        return final
                        contador = contador + 1

            elif signo1 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            return final
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            return final
                        contador = contador + 1

            else:
                print("Signo de consulta incorrecto")
        else:
            final = []
            for u in auxiliar:
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == u:
                            final.append(u + ": " + memoriaActual[i])
                        contador = 0
                    else:
                        if estrucActual[contador] == u:
                            final.append(u + ": " + memoriaActual[i])
                        contador = contador + 1
            return final


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
    final = []
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    posauxiliar = posdata - posestruc
    for z in estrucActual:
        final.append(z + ": " + memoriaActual[posauxiliar])
        posauxiliar = posauxiliar + 1
    return final


def imprimir2(i, estrucActual, memoriaActual, auxiliar):
    posestruc = i
    posdata = i
    final = []
    while posestruc >= len(estrucActual):
        posestruc = posestruc - len(estrucActual)
    for u in auxiliar:
        posauxiliar = posdata - posestruc
        for z in estrucActual:
            if u == z:
                final.append(u + ": " + memoriaActual[posauxiliar])
                posauxiliar = posauxiliar + 1
            else:
                posauxiliar = posauxiliar + 1
    return final
