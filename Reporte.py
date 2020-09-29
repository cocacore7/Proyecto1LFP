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
                palabra = palabra + i
        elif estado == 1:
            if i != " ":
                palabra = palabra + i
            elif i == " " and palabra != "":
                archivo = palabra
                tokens.append("tk: " + palabra + " (Archivo Reportado)")
                palabra = ""
                estado = 2
        elif estado == 2:
            if i == " " and palabra != "":
                if comando == "":
                    comando = palabra
                cadaux = cadaux + " " + palabra
            else:
                palabra = palabra + i

    if comando == "select":
        tokens.append("tk: SELECT (Palabra Reservada)")
        final = ReporteSelect.select(cadaux, memoriaActual, estrucActual, tokens)
        if len(final) != 0:
            archivo(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "max":
        tokens.append("tk: MAX (Palabra Reservada)")
        final = AutomatasReportes.maximo(cadaux, memoriaActual, estrucActual, tokens)
        if len(final) != 0:
            archivo(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "min":
        tokens.append("tk: MIN (Palabra Reservada)")
        final = AutomatasReportes.minimo(cadaux, memoriaActual, estrucActual, tokens)
        if len(final) != 0:
            archivo(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "sum":
        tokens.append("tk: SUM (Palabra Reservada)")
        final = AutomatasReportes.sum(cadaux, memoriaActual, estrucActual, tokens)
        if len(final) != 0:
            archivo(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "count":
        tokens.append("tk: COUNT (Palabra Reservada)")
        final = AutomatasReportes.count(cadaux, memoriaActual, estrucActual, tokens)
        if len(final) != 0:
            archivo(archivo, final)
            print("Reporte Realizado con exito")
        else:
            print("No se encontraron Datos")

    elif comando == "reporttokens":
        if len(tokens) != 0:
            archivo(archivo, tokens)
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

        for i in memoria:
            arch.write("   <h4>" + i + "</h4>" + "\n")

        arch.write('</center>' + "\n")
        arch.write('</body>' + "\n")
        arch.write('</html>')
        arch.close()
        print("Reporte Creado")
        webbrowser.open("reporte.html")
