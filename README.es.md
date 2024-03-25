<h1 align="center"><p align="center">Compresor de Longitud Variable LZ78</h1></h1>
<p align="center" id="badges">
    <a href="https://github.com/monp4r/lz78_varlen_compressor/blob/master/LICENSE"><img src="https://img.shields.io/github/license/monp4r/lz78_varlen_compressor" alt="Licencia"></a>
    <a href="#"><img src="https://img.shields.io/github/languages/code-size/monp4r/lz78_varlen_compressor" alt="Tamaño del código"></a>
    <a href="https://github.com/monp4r/lz78_varlen_compressor/commits"><img src="https://img.shields.io/github/last-commit/monp4r/lz78_varlen_compressor" alt="Último commit"></a>
</p>

> Creado por **Juan Francisco Montero** (<https://github.com/monp4r/>) y **Luis Alfonso Martínez**

## Introducción
Bienvenido al Compresor de Longitud Variable LZ78, donde la eficiencia se encuentra con la simplicidad en el mundo de la compresión de archivos de texto.

Basado en el algoritmo de compresión de datos sin pérdidas LZ78 publicado por Abraham Lempel y Jacob Ziv, consiste en un único programa ejecutable que puede ser utilizado tanto como compresor como descompresor, dependiendo de las opciones de menú seleccionadas. Proporciona ratios de compresión óptimos manteniendo la facilidad de uso.

El Compresor de Longitud Variable LZ78 ha sido desarrollado como proyecto final para el examen de Procesamiento Automático de la Información en el programa de Doble Grado en Matemáticas e Informática en la Universidad de Valladolid.

## Características:
- **Compresión Eficiente:** Utiliza el avanzado algoritmo LZ78 para lograr altos ratios de compresión.
- **Soporte de Hasta 12 Bits:** Manejo preciso de la codificación de longitud variable, admitiendo hasta 12 bits para una compresión óptima.
- **Interfaz Amigable para el Usuario:** Interfaz de línea de comandos simple para operaciones de compresión sin problemas.
- **Manejo Robusto de Errores:** Asegura confiabilidad y robustez durante la compresión, brindándote tranquilidad.

¿Listo para experimentar una compresión ultrarrápida sin comprometer la calidad? ¡Comencemos!

## Empezar:

Para comenzar con el Compresor de Longitud Variable LZ78 usando el IDE Spyder, sigue estos pasos:

1. **Clonar el Repositorio:**

   Clona el repositorio del Compresor de Longitud Variable LZ78 en tu máquina local usando Git. Abre una terminal o Git Bash y ejecuta el siguiente comando:
   
       git clone https://github.com/monp4r/lz78_varlen_compressor.git

    Abre el IDE Spyder (o en python CI) en tu máquina local. Navega al directorio donde clonaste el repositorio del Compresor de Longitud Variable LZ78 usando el explorador de archivos o la terminal.

3. **Explorar y Ejecutar el Código**

    Una vez que el proyecto esté abierto (en Spyder), puedes explorar los archivos de código fuente. El archivo principal, `lz78_varlen_compressor.py`, contiene la implementación del Compresor de Longitud Variable LZ78.

4. **Ejecutar el Compresor**

    Para comprimir un archivo de texto usando el Compresor de Longitud Variable LZ78, puedes seleccionar la primera opción para especificar la ruta de tu archivo de texto de entrada después de ejecutar el script. Puedes hacer esto haciendo clic en el botón verde de "reproducir" en la barra de herramientas del IDE Spyder o presionando F5 (invocar python.exe en la línea de comandos).

5. **Ver Resultados de Compresión**

    Después de ejecutar el compresor, puedes ver la salida comprimida en la consola o terminal. La salida comprimida consistirá en una serie de índices y frases generadas por el Compresor de Longitud Variable LZ78.

6. **Descomprimir Archivos (Opcional)**

    Si lo deseas, también puedes descomprimir archivos usando la funcionalidad de descompresión proporcionada en el archivo `lz78_varlen_compressor.py`. Sigue pasos similares para seleccionar una opción diferente y ejecutar el script para descomprimir un archivo de texto comprimido.

Siguiendo estos pasos, puedes empezar fácilmente con el Compresor de Longitud Variable LZ78 usando el IDE Spyder.

## Precaución:

Por favor, ten en cuenta que en el proceso de comprimir un archivo de texto, el formato predeterminado del archivo de texto en cuestión será '.txt' en esta versión del programa. Esto es para evitar posibles errores en el programa y para mantener la concepción de diseño propuesta desde el inicio de la creación del programa.

Finalmente, es recomendable guardar el contenido de cada operación de codificación o decodificación que realices, para evitar perder el contenido.

## ¿Cómo funciona?:

El Compresor de Longitud Variable LZ78 funciona analizando el archivo de texto de entrada e identificando patrones recurrentes. Aquí tienes una visión general del proceso de compresión y descompresión paso a paso:

1. **Compresión:**
   - **Construcción del Diccionario:** El compresor lee el archivo de texto de entrada y construye un diccionario de frases encontradas en el texto.
   - **Codificación de Longitud Variable:** A cada frase en el diccionario se le asigna un índice único, y el compresor reemplaza cada ocurrencia de una frase con su índice correspondiente. Los índices se codifican utilizando codificación de longitud variable para optimizar la eficiencia de almacenamiento.
   - **Generación de Salida:** El compresor genera la salida comprimida, que consiste en una secuencia de índices que representan las frases en el texto de entrada.

2. **Descompresión:**
   - **Reconstrucción del Diccionario:** Durante la descompresión, el compresor reconstruye el diccionario utilizando los índices proporcionados en el archivo comprimido.
   - **Decodificación de Índices:** El descompresor lee la secuencia de índices del archivo comprimido y los decodifica utilizando decodificación de longitud variable para recuperar las frases originales.
   - **Reconstrucción de la Salida:** A medida que se decodifican los índices, el descompresor reconstruye el texto original reemplazando cada índice con su correspondiente frase del diccionario.

El Compresor de Longitud Variable LZ78 utiliza este proceso para lograr una compresión y descompresión eficientes de archivos de texto mientras mantiene la integridad de los datos.

## Ejemplo

Observemos el proceso de decodificación con este ejemplo.

Dado un diccionario y las tuplas de un mensaje, es posible decodificarlo de manera ordenada para obtener el mensaje. Por ejemplo, la primera entrada en el diccionario es A, por lo que su decodificación será A en sí misma. Lo mismo aplica a la segunda y tercera entradas en el diccionario, siendo letras individuales.

Para la cuarta entrada en el diccionario, se decodifica como AC, y así sucesivamente para todas las entradas. El mensaje final en este caso es el resultado de concatenar todas las entradas en el diccionario, para este ejemplo es 'ABRACADABRA'.

Como podemos ver, la presencia de entradas en el diccionario facilita enormemente la decodificación, haciéndola casi trivial. Podría suceder que no estemos al tanto de las entradas en nuestro diccionario y solo conozcamos la relación entre cada tupla y su índice en el diccionario. En este caso, la forma más fácil sería obtener la entrada de cada posición del diccionario de manera similar a cómo se hizo en el ejemplo anterior.

<div align="center">

| Decodificación | Tupla | Índice del Diccionario | Entrada del Diccionario |
|---------------|-------|------------------------|-------------------------|
| A             | (0,a) | 1                      | A                       |
| B             | (0,b) | 2                      | B                       |
| R             | (0,r) | 3                      | R                       |
| AC            | (1,c) | 4                      | AC                      |
| AD            | (1,d) | 5                      | AD                      |
| AB            | (1,b) | 6                      | AB                      |
| RA            | (3,a) | 7                      | RA                      |

</div >

## Evaluación del Rendimiento del Compresor Basado en Diccionario:

Para evaluar el rendimiento de nuestro compresor basado en diccionario, realizamos pruebas de compresión en varios libros del Proyecto Gutenberg, incluyendo Philosophiae Naturalis Principia Mathematica, Guerra y Paz, así como el archivo del libro El ingenioso hidalgo don Quijote de la Mancha proporcionado en el campus virtual de la asignatura.

Hemos creado una tabla comparativa para ilustrar las pruebas realizadas con el programa, analizando el tamaño sin comprimir, el tamaño comprimido y el factor de compresión de cada archivo. El factor de compresión se define como la relación entre el tamaño comprimido de un archivo y su tamaño sin comprimir, lo que nos permite entender el porcentaje del tamaño original ocupado por el archivo comprimido.

<div align="center">

| Archivo                  | Tamaño sin Comprimir | Tamaño Comprimido | Factor de Compresión |
|--------------------------|-----------------------|-------------------|----------------------|
| quijote.txt              | 2100 KB               | 978 KB            | 0.466                |
| philosophiae_mathematica.txt | 852 KB            | 420 KB            | 0.493                |
| war_and_peace.txt        | 3400 KB               | 1500 KB           | 0.441                |
| a_reptidas.txt           | 1000 KB               | 3 KB              | 0.003                |
| checkmates_data.txt      | 18800 KB              | 3700 KB           | 0.197                |

</div>

Al analizar estos datos, observamos que el compresor basado en diccionario muestra una eficiencia significativa en la mayoría de los casos, con factores de compresión que van desde 0.003 hasta 0.493. Esto sugiere que la existencia de patrones en la cadena de caracteres del texto contribuye significativamente a la capacidad de compresión. Sin embargo, también observamos que el factor de compresión varía ampliamente dependiendo del contenido del archivo, como lo evidencia el archivo "a_reptidas.txt", que contiene caracteres repetidos, lo que resulta en una compresión extremadamente eficiente. En conclusión, estos resultados respaldan la efectividad del compresor basado en diccionario y subrayan la importancia de considerar la naturaleza del contenido al evaluar las técnicas de compresión de datos.

## Desarrollo Futuro

Aquí hay algunas áreas potenciales para el desarrollo futuro del Compresor de Longitud Variable LZ78:

1. **Algoritmos de Compresión Mejorados:** Explorar e implementar algoritmos de compresión avanzados para mejorar la relación de compresión y eficiencia del compresor.

2. **Interfaz Gráfica de Usuario (GUI):** Desarrollar una aplicación de GUI fácil de usar para el Compresor de Longitud Variable LZ78, que permita a los usuarios comprimir y descomprimir archivos con facilidad.

3. **Técnicas de Optimización:** Investigar técnicas de optimización para mejorar el rendimiento del compresor, haciéndolo más rápido y eficiente.

4. **Soporte para Formatos de Archivo Adicionales:** Ampliar el compresor para admitir la compresión y descompresión de varios formatos de archivo, más allá de solo archivos de texto.

5. **Manejo de Errores y Recuperación:** Implementar mecanismos de manejo de errores robustos y estrategias de recuperación para manejar errores de manera elegante durante los procesos de compresión y descompresión.

## Agradecimientos

Extiendo mi sincero agradecimiento a las siguientes personas y entidades por su invaluable apoyo y contribuciones al desarrollo del Compresor de Longitud Variable LZ78:

- **Profesor de Procesamiento Automático de la Información:** Agradezco la ayuda a nuestro profesor de Procesamiento Automático de la Información por su orientación, tutoría y apoyo a lo largo del desarrollo de este proyecto.

- **Fundación del Software Python:** Por desarrollar y mantener el lenguaje de programación Python, que sirve como base para este proyecto.

- **Spyder IDE:** Por proporcionar un entorno de desarrollo integrado intuitivo y potente para la programación en Python, facilitando el proceso de desarrollo del Compresor de Longitud Variable LZ78.

## Referencias:
Angel, P. (2022, April 28). Un Poco de Historia: Algoritmos LZ77, LZ78 y lzw - INCUBAWEB - software y web 2.0. Incubaweb. [https://www.incubaweb.com/un-poco-de-historia-algoritmos-lz77-lz78-y-lzw/](https://www.incubaweb.com/un-poco-de-historia-algoritmos-lz77-lz78-y-lzw/)

Hmong.wiki. (n.d.). LZ77 y lz78 Contenido y eficiencia Teórica [https://hmong.es/wiki/LZ77_and_LZ78](https://hmong.es/wiki/LZ77_and_LZ78)

Ignacio, F. M. J. (2020). Computación Matemática Con Python: Introducción Al Lenguaje python para Científicos e Ingenieros. Ediciones Universidad de Valladolid.
