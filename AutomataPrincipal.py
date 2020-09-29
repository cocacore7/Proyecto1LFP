import MenuPrincipal


def createset(cadena, identificadorNombre, identificadorDato, identificadorEstruc, memoriaActual, EstrucActual, tokens):
    comando = ""
    palabra = ""
    auxiliar = []
    inicial = ""
    for i in cadena:
        if i != " " and comando != "createset":
            if i == "c" or i == "r" or i == "e" or i == "a" or i == "t" or i == "s":
                comando = comando + i
        else:
            if i != " " or i == "_" or i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" \
                    or i == "g" or i == "h" or i == "i" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" \
                    or i == "ñ" or i == "o" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "u" \
                    or i == "v" or i == "w" or i == "x" or i == "y" or i == "z" or i == "0" or i == "1" or i == "2" \
                    or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                if inicial == "":
                    palabra = palabra + i
                    inicial = i
                else:
                    palabra = palabra + i
    if inicial == "_" or inicial == "a" or inicial == "b" or inicial == "c" or inicial == "d" or \
            inicial == "e" or inicial == "f" or inicial == "g" or inicial == "h" or inicial == "i" or \
            inicial == "j" or inicial == "k" or inicial == "l" or inicial == "m" or inicial == "n" or \
            inicial == "ñ" or inicial == "o" or inicial == "p" or inicial == "q" or inicial == "r" or \
            inicial == "s" or inicial == "t" or inicial == "u" or inicial == "v" or inicial == "w" or \
            inicial == "x" or inicial == "y" or inicial == "z":
        identificadorNombre.append(palabra)
        identificadorDato.append(auxiliar)
        identificadorEstruc.append(auxiliar)
        tokens.append("tk: CREATE SET (Palabra Reservada)")
        tokens.append("tk: " + palabra + " (Identificador)")
        MenuPrincipal.cargaA(identificadorNombre, identificadorDato, identificadorEstruc, memoriaActual, EstrucActual,
                             tokens)
    else:
        print("Identificador Invalido")
        print("------------------------------------")
        MenuPrincipal.cargaA(identificadorNombre, identificadorDato, identificadorEstruc, memoriaActual, EstrucActual,
                             tokens)
