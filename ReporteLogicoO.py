def logico(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual):
    final = []
    opcion1 = True
    opcion2 = True
    for w in range(1, 2):
        if opcion1:
            if signo1 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir(i, estrucActual, memoriaActual)
                            opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir(i, estrucActual, memoriaActual)
                            opcion1 = False
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
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
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
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
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
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
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
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir(i, estrucActual, memoriaActual)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir(i, estrucActual, memoriaActual)
                                        opcion1 = False
                        contador = contador + 1

            elif signo1 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir(i, estrucActual, memoriaActual)
                            opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir(i, estrucActual, memoriaActual)
                            opcion1 = False
                        contador = contador + 1

            else:
                print("Signo Invalido")

        if opcion2:
            if signo2 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] == comparar2:
                            final2 = imprimir(i, estrucActual, memoriaActual)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] == comparar2:
                            final2 = imprimir(i, estrucActual, memoriaActual)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = contador + 1

            elif signo2 == "<":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    suma1 = 0
                    suma2 = 0
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == ">":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == "<=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == ">=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "True":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir(i, estrucActual, memoriaActual)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar2):
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final2 = imprimir(i, estrucActual, memoriaActual)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] != comparar2:
                            final2 = imprimir(i, estrucActual, memoriaActual)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] != comparar2:
                            final2 = imprimir(i, estrucActual, memoriaActual)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = contador + 1

            else:
                print("Signo Invalido")
    return final


def logico2(signo1, signo2, comparar1, comparar2, condicion1, condicion2, memoriaActual, estrucActual, auxiliar):
    final = []
    opcion1 = True
    opcion2 = True
    for w in range(1, 2):
        if opcion1:
            if signo1 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] == comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            opcion1 = False
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
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
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
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
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
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
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
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
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
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "True" and comparar1 == "True":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "True" and comparar1 == "False":
                                final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                opcion1 = False
                            elif memoriaActual[i] == "False" and comparar1 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar1 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar1):
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar1:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        opcion1 = False
                        contador = contador + 1

            elif signo1 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            opcion1 = False
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1 and memoriaActual[i] != comparar1:
                            final = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            opcion1 = False
                        contador = contador + 1
        if opcion2:
            if signo2 == "=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] == comparar2:
                            final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] == comparar2:
                            final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = contador + 1

            elif signo2 == "<":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    suma1 = 0
                    suma2 = 0
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) < float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 < suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == ">":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) > float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 > suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == "<=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion1:
                            if memoriaActual[i] == "False" and comparar2 == "True":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) <= float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 <= suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == ">=":
                contador = 0
                suma1 = 0
                suma2 = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "True":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2:
                            if memoriaActual[i] == "True" and comparar2 == "True":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "True" and comparar2 == "False":
                                final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                if len(final) != 0:
                                    for y in final:
                                        final2.append(y)
                                return final2
                            elif memoriaActual[i] == "False" and comparar2 == "True":
                                print("")
                            elif memoriaActual[i] == "False" and comparar2 == "False":
                                print("")
                            else:
                                num = numero(memoriaActual[i])
                                if num:
                                    if float(memoriaActual[i]) >= float(comparar2):
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                                else:
                                    for a in memoriaActual[i]:
                                        suma1 = suma1 + ord(a)
                                    for a in comparar2:
                                        suma2 = suma2 + ord(a)
                                    if suma1 >= suma2:
                                        final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                                        if len(final) != 0:
                                            for y in final:
                                                final2.append(y)
                                        return final2
                        contador = contador + 1

            elif signo2 == "!=":
                contador = 0
                for i in range(0, len(memoriaActual)):
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] != comparar2:
                            final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
                        contador = 0
                    else:
                        if estrucActual[contador] == condicion2 and memoriaActual[i] != comparar2:
                            final2 = imprimir2(i, estrucActual, memoriaActual, auxiliar)
                            if len(final) != 0:
                                for y in final:
                                    final2.append(y)
                            return final2
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
