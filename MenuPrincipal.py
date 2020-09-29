import Automatas
import Select
import AutomataPrincipal


def cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens):
    print("------------------------------------------------------------")
    print("Nombres:")
    print(identificadorNombre)
    print("Datos:")
    print(identificadorDatos)
    print("Estructuras:")
    print(identificadorEstruc)
    print("Set Actual")
    print(memoriaActual)
    print("Estructura Actual")
    print(estrucActual)
    print("Tokens Realizados")
    print(tokens)
    print("------------------------------------------------------------")
    entrada = input("Introducir Comando: ")
    aux = entrada.lower()
    comando = Automatas.inicio(aux)
    if comando == "createset":
        AutomataPrincipal.createset(aux, identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual,
                                    estrucActual, tokens)

    elif comando == "loadinto":
        Automatas.loadinto(aux, identificadorNombre, identificadorDatos, identificadorEstruc, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "useset":
        memoria = Automatas.usesetD(aux, identificadorNombre, identificadorDatos, tokens)
        estructura = Automatas.usesetE(aux, identificadorNombre, identificadorEstruc)
        if memoria != "":
            memoriaActual = memoria
            estrucActual = estructura
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "select":
        Select.select(entrada, memoriaActual, estrucActual, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "listattributes":
        if len(memoriaActual) != 0:
            for i in memoriaActual:
                print(i)
        else:
            print("No se a cargado ninguna memoria creada, usar comando -use set-")
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "printin":
        Automatas.printin(aux, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "max":
        Automatas.maximo(entrada, memoriaActual, estrucActual, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "min":
        Automatas.minimo(entrada, memoriaActual, estrucActual, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "sum":
        Automatas.sum(entrada, memoriaActual, estrucActual, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "count":
        Automatas.count(aux, memoriaActual, estrucActual, tokens)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "reportto":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "script":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "reporttokens":
        for i in tokens:
            print(i)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)

    elif comando == "salir" or comando == "sali":
        print("Hasta la proxima! :D")

    else:
        print("Comando Invalido")
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual, tokens)
