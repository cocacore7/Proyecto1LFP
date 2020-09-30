import webbrowser
import AutomatasReportes
import ReporteSelect


def reportar(cadena, memoriaActual, estrucActual, tokens):
    estado = 0
    archivo = ""
    cadaux = ""
    comando = ""
    palabra = ""
    for i in cadena:
        if estado == 0:
            if palabra == "reportto":
                palabra = ""
                estado = 1
                tokens.append("tk: REPORT TO (Palabra Reservada)")
            elif i != " ":
                palabra = palabra + i.lower()
        elif estado == 1:
            if i != " ":
                palabra = palabra + i.lower()
            elif i == " " and palabra != "":
                archivo = palabra
                tokens.append("tk: " + palabra + " (Archivo Reportado)")
                palabra = ""
                estado = 2
        elif estado == 2:
            if i == " " and palabra != "":
                if comando == "":
                    comando = palabra.lower()
                cadaux = cadaux + " " + palabra
                palabra = ""
            else:
                palabra = palabra + i
    cadaux = cadaux + " " + palabra

    if comando == "select":
        tokens.append("tk: SELECT (Palabra Reservada)")
        final = ReporteSelect.select(cadaux, memoriaActual, estrucActual, tokens)
        if final is not None:
            reporte(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "max":
        tokens.append("tk: MAX (Palabra Reservada)")
        final = AutomatasReportes.maximo(cadaux.lower(), memoriaActual, estrucActual, tokens)
        if final is not None:
            reporte(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "min":
        tokens.append("tk: MIN (Palabra Reservada)")
        final = AutomatasReportes.minimo(cadaux.lower(), memoriaActual, estrucActual, tokens)
        if final is not None:
            reporte(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "sum":
        tokens.append("tk: SUM (Palabra Reservada)")
        final = AutomatasReportes.sum(cadaux.lower(), memoriaActual, estrucActual, tokens)
        if final is not None:
            reporte(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "count":
        tokens.append("tk: COUNT (Palabra Reservada)")
        final = AutomatasReportes.count(cadaux.lower(), memoriaActual, estrucActual, tokens)
        if final is not None:
            reporte(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "listattributes" or comando == "listattribute" or comando == "list":
        tokens.append("tk: LIST ATTRIBUTES (Palabra Reservada)")
        if estrucActual is not None:
            reporte(archivo, estrucActual)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "script":
        tokens.append("tk: LIST ATTRIBUTES (Palabra Reservada)")
        if estrucActual is not None:
            reporte(archivo, estrucActual)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "reporttokens" or comando == "reporttoken" or comando == "report":
        if tokens is not None:
            reporte(archivo, tokens)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "salir" or comando == "sali":
        print("Hasta la proxima! :D")

    else:
        print("Comando Invalido")


def reporte(nombre, memoria):
    with open(nombre + '.html', 'w') as arch:
        arch.write('<!DOCTYPE html>' + "\n")
        arch.write('<html lang="en">' + "\n")
        arch.write('<head>' + "\n")
        arch.write('   <meta charset="UTF-8">' + "\n")
        arch.write('   <title>Document</title>' + "\n")
        arch.write('   <style type="text/css">' + "\n")
        arch.write('       body{background: url(fondo.jpg);background-size: 100%;}' + "\n")
        arch.write('h4{width: 400px;height: 40px;line-height: 60px;text-align: center;background: yellow;}'
                   + "\n")
        arch.write('h3{width: 400px;height: 40px;line-height: 60px;text-align: center;background: SkyBlue;}'
                   + "\n")
        arch.write('   </style>' + "\n")
        arch.write('</head>' + "\n")
        arch.write('<body>' + "\n")
        arch.write('<center>' + "\n")

        contador = 1
        for i in memoria:
            arch.write("   <h4>" + str(contador) + ") " + i + "</h4>" + "\n")
            contador = contador + 1

        arch.write('</center>' + "\n")
        arch.write('</body>' + "\n")
        arch.write('</html>')
        arch.close()
        print("Reporte Creado")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(nombre+".html")
