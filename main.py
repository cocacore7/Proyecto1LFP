import Automatas
import AutomataPrincipal

print("-------------------------------------------")
print("              ---Comandos---               ")
print("1) CREATE SET")
print("2) LOAD INTO -.- FILES -.-")
print("3) USE SET")
print("4) SELECT || SELECT -.- WHERE -.-")
print("5) LIST ATTRIBUTES")
print("6) PRINT IN")
print("7) MAX")
print("8) MIN")
print("9) SUM")
print("10) COUNT")
print("11) REPORT TO")
print("12) SCRIPT")
print("13) REPORT TOKENS")
print("14) SALIR")
print("-------------------------------------------")
print("")


def inicio():
    entrada = input("Introducir Comando: ")
    aux = entrada.lower()
    comando = Automatas.inicio(aux)
    identificadorNombre = []
    identificadorDatos = []
    identificadorEstruc = []
    memoriaActual = []
    EstrucActual = []
    tokens = []
    if comando == "createset":
        AutomataPrincipal.createset(aux, identificadorNombre, identificadorDatos, identificadorEstruc, memoriaActual,
                                    EstrucActual, tokens)

    elif comando == "loadinto":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "useset":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "select":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "listattributes":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "printin":
        Automatas.printin(aux, tokens)
        print("No hay -sets- cargados")
        inicio()

    elif comando == "max":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "min":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "sum":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "count":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "reportto":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "script":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "reporttokens":
        print("No hay -sets- cargados")
        inicio()

    elif comando == "salir" or comando == "sali":
        print("Hasta la proxima! :D")

    else:
        print("Comando Invalido")
        inicio()


inicio()
