# SimpleQL CLI
Simple QL es una aplicación de consola "Key Insensitive" para el manejo de informacion de archivos .aon y siql, orientado a la implementacion de Automatas Finitos Deterministas "AFD", definiendo una estructura de lenguaje capaz de almacenar, manejar y reportar datos en tiempo de ejecución de la aplicación.
## Menu Principal
Se mostraran los comandos disponibles de la aplicacion:
* CREATE SET
* LOAD INTO ... FILES ...
* USE SET
* SELECT ... | SELECT ... WHERE ... [REGEX | AND | OR | XOR]
* LIST ATTRIBUTES
*  PRINT IN
* MAX
* MIN
* SUM
* COUNT
* REPORT TO
* SCRIPT
* REPORT TOKENS
* SALIR
Luego la consola solicitara el comando deseado, el primer comando siempre debera ser la carga de archivos, ya que si no se encuentran archivos cargados, al intentar ejecutar un comando distinto al de "CREATE SET", se mostrara la siguiente advertencia: "No hay -sets- cargados" y regresara al menu de comandos. Estos espacios de memoria son denominados "identificadores"
### 1) Comando "CREATE SET"
Este comando permite al usuario crear espacios de memoria donde se almacenaran datos almacenados en archivos con estructura de lenguaj .aon
### 2) Comando LOAD INTO ... FILES ...
Este comando permite al usuario leer archivos de estructura .aon, obteniendo la estructura del archivo actual y sus datos, almacenando ambos en los espacios de memoria solicitados o "identificadores" previamente creados con el comando "CREATE SET".
### 3) Comando USE SET
Este comando permite al usuario cargar uno de los identificadores creados, sobre el cual ejecutara todas la funciones de la aplicacion. cargando la estructura y datos obtenidos del archivo .aon previamente cargado al identificador solicitado.
### 4) Comando SELECT ... | SELECT ... WHERE ... [REGEX | AND | OR | XOR]
Este comando permite al usuario realizar consultas sobre los datos del identificador actual, cargado con el comando "USE SET".
Permite varios tipos de consultas:
* Consultas Especificas: Luego de la palabra "SELECT" se ingresan los campos del archivo .aon que se desean visualizar, mostrando todos los datos correspondientes a dicho campo, o utilizar un "*", mostrando todos los datos cargados con sus respectivos campos.
* Consultas Especificas: Este tipo de consultas admite dos tipos, consultas de una condicion y consultas de dos condiciones:
  - Una Condicion: Luego de especificar los campos que se desean visualizar se escribe el comando "WHERE", luego especificar una condicion para los datos deseados, puede ser de tipo texto, booleana o numerica.
  - Dos Condiciones: Luego de especificar los campos que se desean visualizar se escribe el comando "WHERE", especificando la primera condicion para los datos deseados, continuando con el tipo de anexo para la segunda condiciones con los operadores logicos "AND", "OR" y "XOR", por ultimo se especifica la ultima condicion para los datos solicitados.
 * Consultas REGEX: Este tipo de consultas responden a un lenguaje especifico, que al solicitar los campos que se desean visualizar y escribir el comando "WHERE", se escribe el campo de la condicion seguido de la palabra REGEX, solicitando el tipo de condiciones validas implementadas por REGEX.
### 5) Comando LIST ATTRIBUTES
Este comando permite al usuario listar los campos o atributos (Estructura), sobre la cual esta trabajando el espacio en memoria actual.
### 6) Comando PRINT IN
Este comando permite al usuario especificar el color de letra con el cual se imprimiran los datos y comandos en consola.
### 7) Comando MAX
Este comando permite al usuario obtener el valor maximo del campo solicitado, sea este booleano, texto o numerico. 
### 8) Comando MIN
Este comando permite al usuario obtener el valor minimo del campo solicitado, sea este booleano, texto o numerico. 
### 9) Comando SUM
Este comando permite al usuario obtener la suma total de los valores dentro de un campo solicitado, admitiendo solo datos de tipo numerico. 
### 10) Comando COUNT
Este comando permite al usuario obtener la cantidad de datos para cada campo solicitado.
### 11) Comando REPORT TO
Este comando permite al usuario crear reportes .HTML sobre el tipo de consulta solicitado, luego de especificar el nombre del reporte a crear, se coloca el comando que se reportara.
### 12) Comando SCRIPT
Este comando permite al usuario cargar un archivo de tipo .siql, ejecutando los comando dentro del archivo de ser validos.
### 13) Comando Salir
Este comando permite al usuario finalizar la ejecuacion de la aplicacion.
