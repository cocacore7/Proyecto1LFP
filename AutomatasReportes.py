def count(cadena, memoriaActual, estrucActual, tokens):
    estado = 0
    total = 0
    contador = 0
    palabra = ""
    auxiliar = ""
    final = []
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
                for z in estrucActual:
                    if palabra == "*":
                        tokens.append("tk: " + z + " (Identificador)")
                    elif palabra == z:
                        tokens.append("tk: " + z + " (Identificador)")
                auxiliar = auxiliar + " " + palabra
                if i == ",":
                    tokens.append("tk: ',' (Separador)")
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.lower().split()

    if len(estrucAux) != 0:
        if estrucAux[0] == "*":
            for _ in memoriaActual:
                total = total + 1
            final.append("Total: " + str(total))
            return final
        else:
            for u in estrucAux:
                total = 0
                for _ in memoriaActual:
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == u:
                            total = total + 1
                        contador = 0
                    else:
                        if estrucActual[contador] == u:
                            total = total + 1
                        contador = contador + 1

                for z in estrucActual:
                    if z == u:
                        final.append(u + ": " + str(total))
            return final
    else:
        print("No se ingresaron consultas para contar")


def sum(cadena, memoriaActual, estrucActual, tokens):
    contador = 0
    estado = 0
    palabra = ""
    auxiliar = ""
    final = []
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
                for z in estrucActual:
                    if palabra == "*":
                        tokens.append("tk: * (Identificador)")
                    elif palabra == z:
                        tokens.append("tk: " + z + " (Identificador)")
                if i == ",":
                    tokens.append("tk: ',' (Separador)")
                auxiliar = auxiliar + " " + palabra
                palabra = ""
    auxiliar = auxiliar + " " + palabra
    estrucAux = auxiliar.lower().split()
    if len(estrucAux) != 0:
        if estrucAux[0] == "*":
            for z in estrucActual:
                num = 0
                for i in memoriaActual:
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == z:
                            bandera = numero(i)
                            if bandera:
                                num = num + float(i)
                        contador = 0
                    else:
                        if estrucActual[contador] == z:
                            bandera = numero(i)
                            if bandera:
                                num = num + float(i)
                        contador = contador + 1
                if num != 0:
                    final.append(z + " = " + str(num))
        else:
            for z in estrucAux:
                num = 0
                for i in memoriaActual:
                    if contador == len(estrucActual) - 1:
                        if estrucActual[contador] == z:
                            bandera = numero(i)
                            if bandera:
                                num = num + float(i)
                        contador = 0
                    else:
                        if estrucActual[contador] == z:
                            bandera = numero(i)
                            if bandera:
                                num = num + float(i)
                        contador = contador + 1
                if num != 0:
                    final.append(z + " = " + str(num))
        return final
    else:
        print("No se ingresaron consultas para sumar")


def maximo(cadena, memoriaActual, estrucActual, tokens):
    estado = 0
    palabra = ""
    auxiliar = ""
    cadenas = []
    numeros = []
    tipos = []
    final = []
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
    estrucAux = auxiliar.lower().split()
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
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            for u in numeros[i]:
                if u == 1:
                    final.append(reemplazo[i] + ": True" + " (Tipo: Booleano)")
        elif tipos[i] == "string":
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            mayor = max(numeros[i])
            posicion = 0
            posicion2 = 0
            for u in numeros[i]:
                if u == mayor:
                    for a in cadenas[i]:
                        if posicion == posicion2:
                            final.append(reemplazo[i] + ": " + a + " (Tipo: Cadena)")
                        posicion2 = posicion2 + 1
                posicion = posicion + 1
        elif tipos[i] == "numero":
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            mayor = max(numeros[i])
            final.append(reemplazo[i] + ": " + str(mayor) + " (Tipo: Numerico)")
    return final


def minimo(cadena, memoriaActual, estrucActual, tokens):
    estado = 0
    palabra = ""
    auxiliar = ""
    cadenas = []
    numeros = []
    tipos = []
    final = []
    for i in cadena:
        if estado == 0:
            if palabra == "min":
                tokens.append("tk: MIN (Palabra Reservada)")
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
    estrucAux = auxiliar.lower().split()
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
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            for u in numeros[i]:
                if u == 0:
                    final.append(reemplazo[i] + ": False" + " (Tipo: Booleano)")
        elif tipos[i] == "string":
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            mayor = min(numeros[i])
            posicion = 0
            posicion2 = 0
            for u in numeros[i]:
                if u == mayor:
                    for a in cadenas[i]:
                        if posicion == posicion2:
                            final.append(reemplazo[i] + ": " + a + " (Tipo: Cadena)")
                        posicion2 = posicion2 + 1
                posicion = posicion + 1
        elif tipos[i] == "numero":
            tokens.append("tk: " + reemplazo[i] + " (Identificador)")
            mayor = min(numeros[i])
            final.append(reemplazo[i] + ": " + str(mayor) + " (Tipo: Numerico)")
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
