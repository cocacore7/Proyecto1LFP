def inicio(cadena):
    estado = 0
    palabra = ""
    for i in cadena:
        if i != " ":
            if estado == 0:
                if i == "c" or i == "l" or i == "u" or i == "s" or i == "p" or i == "m" or i == "r":
                    palabra = palabra + i
                    estado = 1
                else:
                    return "Comando Invalido"

            elif estado == 1:
                if i == "r" or i == "o" or i == "s" or i == "e" or i == "i" or i == "a" or i == "u" or i == "c":
                    palabra = palabra + i
                    estado = 2
                else:
                    return "Comando Invalido"

            elif estado == 2:
                if i == "e" or i == "a" or i == "l" or i == "s" or i == "i" or i == "x" or i == "m" or i == "u" \
                        or i == "p" or i == "r" or i == "n":
                    palabra = palabra + i
                    if palabra == "max" or palabra == "min" or palabra == "sum":
                        return palabra
                    else:
                        estado = 3
                else:
                    return "Comando Invalido"

            elif estado == 3:
                if i == "a" or i == "s" or i == "e" or i == "t" or i == "n" or i == "o" or i == "i" or i == "d":
                    palabra = palabra + i
                    estado = 4
                else:
                    return "Comando Invalido"

            elif estado == 4:
                if i == "t" or i == "i" or i == "e" or i == "c" or i == "a" or i == "r" or i == "p":
                    palabra = palabra + i
                    if palabra == "count" or palabra == "salir":
                        return palabra
                    else:
                        estado = 5
                else:
                    return "Comando Invalido"

            elif estado == 5:
                if i == "e" or i == "n" or i == "t" or i == "i":
                    palabra = palabra + i
                    if palabra == "script" or palabra == "select" or palabra == "useset":
                        return palabra
                    else:
                        estado = 6
                else:
                    return "Comando Invalido"

            elif estado == 6:
                if i == "s" or i == "t" or i == "n":
                    palabra = palabra + i
                    if palabra == "printin" or palabra == "loadinto":
                        return palabra
                    else:
                        estado = 7
                else:
                    return "Comando Invalido"

            elif estado == 7:
                if i == "e" or i == "o" or i == "r":
                    palabra = palabra + i
                    if palabra == "loadinto":
                        return palabra
                    else:
                        estado = 8
                else:
                    return "Comando Invalido"

            elif estado == 8:
                if i == "t" or i == "i" or i == "k":
                    palabra = palabra + i
                    if palabra == "createset":
                        return palabra
                    else:
                        estado = 9
                elif palabra == "reportto":
                    return palabra
                else:
                    return "Comando Invalido"

            elif estado == 9:
                if i == "b" or i == "e":
                    palabra = palabra + i
                    estado = 10
                else:
                    return "Comando Invalido"

            elif estado == 10:
                if i == "u" or i == "n":
                    palabra = palabra + i
                    estado = 11
                else:
                    return "Comando Invalido"

            elif estado == 11:
                if i == "t" or i == "s":
                    palabra = palabra + i
                    if palabra == "reporttokens":
                        return palabra
                    else:
                        estado = 12
                else:
                    return "Comando Invalido"

            elif estado == 12:
                if i == "e":
                    palabra = palabra + i
                    estado = 13
                else:
                    return "Comando Invalido"

            elif estado == 13:
                if i == "s":
                    palabra = palabra + i
                    if palabra == "listattributes":
                        return palabra
                    else:
                        return "Comando Invalido"


def loadinto(cadena, identificadorNombre, identificadorDato, identificadorEstruc):
    print("------------------------------------")
    # Variables
    ingresar = False
    bandera = False
    bandera2 = False
    estructura = ""
    comando = ""
    archivos = []
    palabra = ""
    memoria = ""
    estado = 0

    # reconocer lenguaje en cadena
    for i in cadena:
        if estado == 0:
            if palabra == "loadinto":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i
        elif estado == 1:
            if i != " ":
                palabra = palabra + i
            elif i == " " and palabra != "":
                memoria = palabra
                palabra = ""
                estado = 2
        elif estado == 2:
            if palabra == "files":
                comando = palabra
                palabra = ""
                estado = 3
            elif i != " ":
                palabra = palabra + i
        elif estado == 3:
            if i != " " and i != ",":
                palabra = palabra + i
            elif i != " " and palabra != "":
                archivos.append(palabra)
                palabra = ""

    archivos.append(palabra)
    palabra = ""
    estado = 0

    # Ingresar estructura del set solicitado
    for i in range(0, len(identificadorNombre)):
        if memoria == identificadorNombre[i] and comando == "files" and archivos[0] != "":
            try:
                with open(archivos[0], 'r') as miarchivo:
                    data = miarchivo.read()
                    miarchivo.close()
                    for letra in data:
                        if estado == 0:
                            if letra == "<":
                                estado = 1
                        elif estado == 1:
                            if letra == "[":
                                estado = 2
                        elif estado == 2:
                            if letra == "[":
                                palabra = ""
                            elif letra == "]":
                                estructura = estructura + " " + palabra
                                palabra = ""
                            elif letra == ">":
                                estado = 3
                            else:
                                palabra = palabra + letra.lower()
                        elif estado == 3:
                            if len(identificadorEstruc[i]) == 0:
                                identificadorEstruc[i] = estructura.split()
                                estado = 4
                            else:
                                estructura = ""
                                for z in identificadorEstruc[i]:
                                    estructura = estructura + " " + z
                        elif estado == 4:
                            continue
            except(OSError, IOError):
                print("Estructura no definida")
                print("------------------------------------")

            # Ingresar Datos en set
            for u in range(0, len(archivos)):
                try:
                    with open(archivos[u], 'r') as miarchivo:
                        data = miarchivo.read()
                        miarchivo.close()
                        estado = 0
                        comparar = estructuraload(data)
                        if estructura == comparar:
                            for letra in data:
                                if estado == 0:
                                    if letra == "<":
                                        estado = 1
                                elif estado == 1:
                                    if letra == "[":
                                        estado = 2
                                        palabra = ""
                                elif estado == 2:
                                    if letra == "[":
                                        if ingresar:
                                            identificadorDato[i].append(palabra)
                                        bandera = False
                                        bandera2 = False
                                        palabra = ""
                                    elif letra == "]":
                                        if len(identificadorEstruc[i]) != 0:
                                            for a in identificadorEstruc[i]:
                                                if a == palabra.lower():
                                                    ingresar = True
                                        palabra = ""
                                    elif letra == "=":
                                        bandera = True
                                        palabra = ""
                                    elif letra == '"':
                                        if bandera2:
                                            bandera2 = False
                                        else:
                                            bandera2 = True
                                    elif bandera2:
                                        if letra != " " and letra != "\n" and letra != "," and letra != "<" \
                                                and letra != ">" and letra != "(" and letra != ")":
                                            palabra = palabra + letra
                                    elif bandera:
                                        if letra != " " and letra != "\n" and letra != "," and letra != "<" \
                                                and letra != ">" and letra != "(" and letra != ")":
                                            palabra = palabra + letra
                                    else:
                                        palabra = palabra + letra
                            identificadorDato[i].append(palabra)
                        else:
                            print("Archivo -" + archivos[u] + "- no cumple con la estructura " + memoria)
                            print("------------------------------------")
                except(OSError, IOError):
                    print("Archivo -" + archivos[u] + "- no encontrado")
                    print("------------------------------------")
        else:
            print("No existe el identificador solicitado, usar comando create set...")


def estructuraload(data):
    estructura = ""
    palabra = ""
    estado = 0
    for letra in data:
        if estado == 0:
            if letra == "<":
                estado = 1
        elif estado == 1:
            if letra == "[":
                estado = 2
        elif estado == 2:
            if letra == "[":
                palabra = ""
            elif letra == "]":
                estructura = estructura + " " + palabra
                palabra = ""
            elif letra == ">":
                estado = 3
            else:
                palabra = palabra + letra.lower()
        elif estado == 3:
            return estructura


def usesetD(cadena, identificadorNombre, identificadorDato):
    estado = 0
    palabra = ""
    bandera = False
    posicion = 0
    for i in cadena:
        if estado == 0:
            if palabra == "useset":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i
        elif estado == 1:
            if i != " ":
                palabra = palabra + i
    for i in range(0, len(identificadorNombre)):
        if palabra == identificadorNombre[i]:
            bandera = True
            posicion = i
    if bandera:
        if len(identificadorDato[posicion]) != 0:
            return identificadorDato[posicion]
        else:
            print("Identificador vacío, usar comando load into...")
            return ""
    else:
        print("No existe el identificador solicitado")
        return ""


def usesetE(cadena, identificadorNombre, identificadorEstruc):
    estado = 0
    palabra = ""
    bandera = False
    posicion = 0
    for i in cadena:
        if estado == 0:
            if palabra == "useset":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i
        elif estado == 1:
            if i != " ":
                palabra = palabra + i
    for i in range(0, len(identificadorNombre)):
        if palabra == identificadorNombre[i]:
            bandera = True
            posicion = i
    if bandera:
        if len(identificadorEstruc[posicion]) != 0:
            return identificadorEstruc[posicion]


def printin(cadena):
    estado = 0
    palabra = ""
    for i in cadena:
        if estado == 0:
            if palabra == "printin":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i
        elif estado == 1:
            if i != " ":
                palabra = palabra + i
    if palabra == "blue":
        print("\x1b[1;34m")
    elif palabra == "red":
        print("\x1b[1;31m")
    elif palabra == "green":
        print("\x1b[1;32m")
    elif palabra == "yellow":
        print("\x1b[1;33m")
    elif palabra == "orange":
        print("\x1b[1;37m")
    elif palabra == "pink":
        print("\x1b[1;37m")
    else:
        print("Color invalido")


def count(cadena, memoriaActual, estrucActual):
    estado = 0
    total = 0
    contador = 0
    palabra = ""
    auxiliar = ""
    for i in cadena:
        if estado == 0:
            if palabra == "count":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if i != " " and i != ",":
                palabra = palabra + i
            elif i == " " or i == ",":
                auxiliar = auxiliar + " " + palabra
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.split()
    if len(estrucAux) != 0:
        if estrucAux[0] == "*":
            for _ in memoriaActual:
                total = total + 1
            print("Total: " + str(total))
        else:
            for u in estrucAux:
                total = 0
                for _ in memoriaActual:
                    if contador != len(estrucActual) - 1:
                        if estrucActual[contador] == u:
                            contador = contador + 1
                            total = total + 1
                        else:
                            contador = contador + 1
                    else:
                        contador = 0
                for z in estrucActual:
                    if z == u:
                        print(u + ": " + str(total))
    else:
        print("No se ingresaron consultas para contar")


def sum(cadena, memoriaActual, estrucActual):
    estado = 0
    contador = 0
    palabra = ""
    auxiliar = ""
    for i in cadena:
        if estado == 0:
            if palabra == "sum":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if i != " " and i != ",":
                palabra = palabra + i
            elif i == " " or i == ",":
                auxiliar = auxiliar + " " + palabra
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.split()
    if len(estrucAux) != 0:
        if estrucAux[0] == "*":
            for z in estrucActual:
                bandera = True
                palabra = ""
                num = 0
                for i in memoriaActual:
                    if contador != len(estrucActual) - 1:
                        if estrucActual[contador] == z:
                            contador = contador + 1
                            estado = 0
                            for u in i:
                                if estado == 0:
                                    if bandera:
                                        if u != "0" and u != "1" and u != "2" and u != "3" and u != "4" and u != "5" \
                                                and u != "6" and u != "7" and u != "8" and u != "9" and u != ".":
                                            bandera = False
                                        elif u == ".":
                                            estado = 1
                                            palabra = palabra + u
                                        else:
                                            palabra = palabra + u
                                    else:
                                        palabra = ""
                                elif estado == 1:
                                    if u != "0" and u != "1" and u != "2" and u != "3" and u != "4" and u != "5" and u \
                                            != "6" and u != "7" and u != "8" and u != "9":
                                        bandera = False
                                    else:
                                        palabra = palabra + u
                            if bandera and estado == 1:
                                num = num + float(palabra)
                                palabra = ""
                            elif bandera and estado == 0:
                                num = num + int(palabra)
                                palabra = ""
                        else:
                            contador = contador + 1
                    else:
                        contador = 0
                if num != 0:
                    print(z + " = " + str(num))

        else:
            for z in estrucAux:
                bandera = True
                palabra = ""
                num = 0
                for i in memoriaActual:
                    if contador != len(estrucActual) - 1:
                        if estrucActual[contador] == z:
                            contador = contador + 1
                            estado = 0
                            for u in i:
                                if estado == 0:
                                    if bandera:
                                        if u != "0" and u != "1" and u != "2" and u != "3" and u != "4" and u != "5" \
                                                and u != "6" and u != "7" and u != "8" and u != "9" and u != ".":
                                            bandera = False
                                        elif u == ".":
                                            estado = 1
                                            palabra = palabra + u
                                        else:
                                            palabra = palabra + u
                                    else:
                                        palabra = ""
                                elif estado == 1:
                                    if u != "0" and u != "1" and u != "2" and u != "3" and u != "4" and u != "5" and u \
                                            != "6" and u != "7" and u != "8" and u != "9":
                                        bandera = False
                                    else:
                                        palabra = palabra + u
                            if bandera and estado == 1:
                                num = num + float(palabra)
                                palabra = ""
                            elif bandera and estado == 0:
                                num = num + int(palabra)
                                palabra = ""
                        else:
                            contador = contador + 1
                    else:
                        contador = 0
                if num != 0:
                    print(z + " = " + str(num))
    else:
        print("No se ingresaron consultas para sumar")


def maximo(cadena, memoriaActual, estrucActual):
    estado = 0
    palabra = ""
    auxiliar = ""
    cadenas = []
    numeros = []
    tipos = []
    for i in cadena:
        if estado == 0:
            if palabra == "max":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if i != " " and i != ",":
                palabra = palabra + i
            elif i == " " or i == ",":
                auxiliar = auxiliar + " " + palabra
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.split()
    reemplazo = []
    for u in estrucAux:
        cadaux = []
        numaux = []
        tipo = ""
        reemplazoaux = ""
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == u:
                    if reemplazoaux == "":
                        reemplazoaux = estrucActual[contador]
                    if memoriaActual[i] == "True":
                        cadaux.append(memoriaActual[i])
                        numaux.append(1)
                        tipo = "bool"
                    elif memoriaActual[i] == "False":
                        cadaux.append(memoriaActual[i])
                        numaux.append(0)
                        tipo = "bool"
                    else:
                        estado = numero(memoriaActual[i])
                        if estado:
                            numaux.append(memoriaActual[i])
                            cadaux.append("")
                            tipo = "numero"
                        else:
                            suma1 = 0
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            numaux.append(suma1)
                            cadaux.append(memoriaActual[i])
                            tipo = "string"
                contador = 0
            else:
                if estrucActual[contador] == u:
                    if reemplazoaux == "":
                        reemplazoaux = estrucActual[contador]
                    if memoriaActual[i] == "True":
                        cadaux.append(memoriaActual[i])
                        numaux.append(1)
                        tipo = "bool"
                    elif memoriaActual[i] == "False":
                        cadaux.append(memoriaActual[i])
                        numaux.append(0)
                        tipo = "bool"
                    else:
                        estado = numero(memoriaActual[i])
                        if estado:
                            numaux.append(memoriaActual[i])
                            cadaux.append("")
                            tipo = "numero"
                        else:
                            suma1 = 0
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            numaux.append(suma1)
                            cadaux.append(memoriaActual[i])
                            tipo = "string"
                contador = contador + 1
        if len(cadaux) != 0:
            cadenas.append(cadaux)
            numeros.append(numaux)
            tipos.append(tipo)
            reemplazo.append(reemplazoaux)

    for i in range(0, len(cadenas)):
        if tipos[i] == "bool":
            for u in numeros[i]:
                if u == 1:
                    print(reemplazo[i] + ": True" + " (Tipo: Booleano)")
        elif tipos[i] == "string":
            mayor = max(numeros[i])
            posicion = 0
            posicion2 = 0
            for u in numeros[i]:
                if u == mayor:
                    for a in cadenas[i]:
                        if posicion == posicion2:
                            print(reemplazo[i] + ": " + a + " (Tipo: Cadena)")
                        posicion2 = posicion2 + 1
                posicion = posicion + 1
        elif tipos[i] == "numero":
            mayor = max(numeros[i])
            print(reemplazo[i] + ": " + str(mayor) + " (Tipo: Numerico)")


def minimo(cadena, memoriaActual, estrucActual):
    estado = 0
    palabra = ""
    auxiliar = ""
    cadenas = []
    numeros = []
    tipos = []
    for i in cadena:
        if estado == 0:
            if palabra == "min":
                palabra = ""
                estado = 1
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if i != " " and i != ",":
                palabra = palabra + i
            elif i == " " or i == ",":
                auxiliar = auxiliar + " " + palabra
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.split()
    reemplazo = []
    for u in estrucAux:
        cadaux = []
        numaux = []
        tipo = ""
        reemplazoaux = ""
        contador = 0
        for i in range(0, len(memoriaActual)):
            if contador == len(estrucActual) - 1:
                if estrucActual[contador] == u:
                    if reemplazoaux == "":
                        reemplazoaux = estrucActual[contador]
                    if memoriaActual[i] == "True":
                        cadaux.append(memoriaActual[i])
                        numaux.append(1)
                        tipo = "bool"
                    elif memoriaActual[i] == "False":
                        cadaux.append(memoriaActual[i])
                        numaux.append(0)
                        tipo = "bool"
                    else:
                        estado = numero(memoriaActual[i])
                        if estado:
                            numaux.append(memoriaActual[i])
                            cadaux.append("")
                            tipo = "numero"
                        else:
                            suma1 = 0
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            numaux.append(suma1)
                            cadaux.append(memoriaActual[i])
                            tipo = "string"
                contador = 0
            else:
                if estrucActual[contador] == u:
                    if reemplazoaux == "":
                        reemplazoaux = estrucActual[contador]
                    if memoriaActual[i] == "True":
                        cadaux.append(memoriaActual[i])
                        numaux.append(1)
                        tipo = "bool"
                    elif memoriaActual[i] == "False":
                        cadaux.append(memoriaActual[i])
                        numaux.append(0)
                        tipo = "bool"
                    else:
                        estado = numero(memoriaActual[i])
                        if estado:
                            numaux.append(memoriaActual[i])
                            cadaux.append("")
                            tipo = "numero"
                        else:
                            suma1 = 0
                            for a in memoriaActual[i]:
                                suma1 = suma1 + ord(a)
                            numaux.append(suma1)
                            cadaux.append(memoriaActual[i])
                            tipo = "string"
                contador = contador + 1
        if len(cadaux) != 0:
            cadenas.append(cadaux)
            numeros.append(numaux)
            tipos.append(tipo)
            reemplazo.append(reemplazoaux)

    for i in range(0, len(cadenas)):
        if tipos[i] == "bool":
            for u in numeros[i]:
                if u == 0:
                    print(reemplazo[i] + ": False" + " (Tipo: Booleano)")
        elif tipos[i] == "string":
            mayor = min(numeros[i])
            posicion = 0
            posicion2 = 0
            for u in numeros[i]:
                if u == mayor:
                    for a in cadenas[i]:
                        if posicion == posicion2:
                            print(reemplazo[i] + ": " + a + " (Tipo: Cadena)")
                        posicion2 = posicion2 + 1
                posicion = posicion + 1
        elif tipos[i] == "numero":
            mayor = min(numeros[i])
            print(reemplazo[i] + ": " + str(mayor) + " (Tipo: Numerico)")


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
