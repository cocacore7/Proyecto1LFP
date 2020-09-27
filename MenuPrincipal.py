import Automatas
import Select


def cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual):
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
    print("------------------------------------------------------------")
    entrada = input("Introducir Comando: ")
    aux = entrada.lower()
    comando = Automatas.inicio(aux)
    if comando == "createset":
        Automatas.createset(aux, identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual,
                            estrucActual)

    elif comando == "loadinto":
        Automatas.loadinto(aux, identificadorNombre, identificadorDatos, identificadorEstruc)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "useset":
        memoria = Automatas.usesetD(aux, identificadorNombre, identificadorDatos)
        estructura = Automatas.usesetE(aux, identificadorNombre, identificadorEstruc)
        if memoria != "":
            memoriaActual = memoria
            estrucActual = estructura
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "select":
        Select.select(entrada, memoriaActual, estrucActual)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "listattributes":
        if len(memoriaActual) != 0:
            for i in memoriaActual:
                print(i)
        else:
            print("No se a cargado ninguna memoria creada, usar comando -use set-")
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "printin":
        Automatas.printin(aux)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "max":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "min":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "sum":
        Automatas.sum(entrada, memoriaActual, estrucActual)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "count":
        Automatas.count(entrada, memoriaActual, estrucActual)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "reportto":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "script":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "reporttokens":
        print(comando)
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)

    elif comando == "salir" or comando == "sali":
        print("Hasta la proxima! :D")

    else:
        print("Comando Invalido")
        cargaA(identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual, estrucActual)
