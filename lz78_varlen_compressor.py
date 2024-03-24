"""
Compressor using Variable Length LZ78 Encoding (12 bits).

This program implements LZ78 compression with a variable-length encoder capable of handling up to 12 bits.

Start Date:            27/10/2021
Completion Date:       30/12/2021
"""


# IMPORTS:
#   Importación de librerías y funciones necesarias para la ejecución del programa.
import os
import sys
from bitarray import bitarray

# Declaración de constantes.
MINBITS = 2
MAXBITS = 12
LIMBITS = MAXBITS + 1
TAMBYTE = 8

def rellenar_bitarray_ceros(b, bits): 
    """
    rellenar_bitarray_ceros(b, bits)
    
    Objetivo de la función:
    -----------------------
        Este método tiene la función de añadir una serie del carácter '0'
        al bitarray hasta que tenga un tamaño adecuado de bits, descrito
        por el programador en la llamada a esta función.
    
    Parámetros y tipos de entrada:
    ------------------------------
        b : bitarray
            Representa el array de bits empleado para realizar la codificación.
        bits : número entero
            Representa el tamaño de la cadena de carácteres denominada texto.
            
    Parámetros y tipos de salida:
    -----------------------------
        b : bitarray
            Representa el array de bits empleado para realizar la codificación.

    """
    while(len(b) < bits):
        
        b.insert(0, False) #Añadimos ceros mediante esta función.
        
    return b
# ------------------------------------------------------------------
    
def agregar(bits, arraybits, c):
    """
    agregar(bits, arraybits, c)
    
    Objetivo de la función:
    -----------------------
        Este método tiene la labor de añadir, un carácter (número o letra)
        cualquiera al bitarray que hayamos seleecionado previamente en la 
        llamada de la función.        

    Parámetros y tipos de entrada:
    ------------------------------
        bits : número entero
            Este parámetro describe el número de bits 
        arraybits : bitarray
            Describe el array de bits al cual añadiremos el nuevo fragmento
            de bits.
        c : número entero
            Este parámetro describe la posición del número o la letra en 
            el diccionario.

    Parámetros y tipos de salida:
    -----------------------------
        No dispone de ellos.
        
    """
    ba = bitarray()
    
    aux = format(c, 'b') # Formateamos la posición del carácter a binario.
    
    ba.extend(aux)
    
    ba = rellenar_bitarray_ceros(ba, bits)
    
    arraybits.extend(ba) # Añadimos el bitarray auxiliar al principal.
# ------------------------------------------------------------------   

#-------------------------------------------------------------------------->
def sumar_bits(i, bits_exp):
    """
    sumar_bits(i, bits_exp)

    Objetivo de la función:
    -----------------------
        Este método tiene que sumar un bit en al escribir los carácteres
        si es necesario, según la posición que tienen en el diccionario.
    
    Parámetros y tipos de entrada:
    ------------------------------
        i : número entero
            Representa la última posición del diccionario coincidente en
            cada entrada de nuevos carácteres.
        bits_exp : número entero
            Representa el número de bits empleado en la compresión y descompresión.
            
    Parámetros y tipos de salida:
    -----------------------------
        bits_exp : número entero
            Representa el número de bits empleado en la compresión y descompresión.

    """
    max_b = (2 ** bits_exp) - 1
    
    if(i == max_b):
        bits_exp += 1
    
    return bits_exp
# ------------------------------------------------------------------  
    
def vaciar_diccionario(bits_exp, diccionario):
    """
    vaciar_diccionario(bits_exp, diccionario)
    
    Objetivo de la función:
    -----------------------
        Este método tiene como objetivo el reinicio del diccionario cuando
        el número de bits supera el umbral establecido (LIMBITS).
        
    Parámetros y tipos de entrada:
    ------------------------------
        bits_exp : número entero
            Representa el número de bits empleado en la compresión y descompresión.
        diccionario : dictionary
            Describe el diccionario mediante el cual se creará y vaciará 
            cuando se lleve a cabo la compresión y descompresión de datos.

            
    Parámetros y tipos de salida:
    -----------------------------
        diccionario : dictionary
            Describe el diccionario mediante el cual se creará y vaciará 
            cuando se lleve a cabo la compresión y descompresión de datos.

    """
    if(bits_exp == LIMBITS): 
        
        diccionario.clear()
# ------------------------------------------------------------------  

def comprimir(texto):
    """
    comprimir(texto)
    
    Objetivo de la función:
    -----------------------
        Este método es de los más importantes de este programa. Dicho método
        aporta la funcionalidad de la compresión real de una cadena de 
        carácteres (texto) en una variable (a) que contendrá la codificación
        binaria. Para ello, se hace uso de los diferentes métodos satélite
        presentes en este programa.

        El desarrollo de este método sigue el algoritmo de compresión sin
        pérdidas LZ78. Este se explicará con más detalle en la pertinente
        documentación facilitada (memoria).
        
    Parámetros y tipos de entrada:
    ------------------------------
        texto : cadena de carácteres
            Representa el texto que queremos comprimir.
            
    Parámetros y tipos de salida:
    -----------------------------
        a : bitarray
            Representa la cadena de bits que contiene la codificación del texto
            mencionado anteriormente.

    """
    
    # Cada acceso al diccionario se realiza de la siguiente forma:
    # diccionario[...] = {índice, carácter}
    #   el índice es un contador previo a la entrada del diccionario, y el carácter
    #   en concreto se une con la cadena representada por dictionary[indice]
    diccionario = dict()
    
    # Crear array de bits
    a = bitarray()

    len_texto = len(texto)

    last_matching_index = 0 # última posición leída del bitarray
    next_available_index = 1 # siguiente entrada al diccionario, posición  
    
    bits_exp = MINBITS

    # Establecemos los datos necesarios para realizar la compresión (CABEZERA):
    #   Número inicial de lectura de bits y el máximo de bits que se pueden emplear.
    agregar(TAMBYTE, a, MINBITS)
    agregar(TAMBYTE, a, MAXBITS)
    
    # Se recorre todo el texto del fichero correspondiente.
    while(last_matching_index < len_texto): 
    
        c = texto[last_matching_index]

        if(c in diccionario):
            
            band = True
            
            while(c in diccionario and band):
                
                nodo = diccionario[c] # Es la posición del índice del diccionario.
                
                last_matching_index += 1 
                
                if(last_matching_index < len_texto):
                    
                    c += texto[last_matching_index] # añadimos caracteres
                    
                else:
                    
                    last_matching_index -= 1
                    
                    band = False
            
            diccionario[c] = next_available_index 
         
            # Formateamos el carácter introducido        
            agregar(bits_exp, a, nodo) 
            
        else:
            
            diccionario[c] = next_available_index
            
            # Añadimos el carácter introducido (Numérico)
            agregar(bits_exp, a, 0)
            
            
        # Añadimos el carácter introducido (Letra)
        agregar(TAMBYTE, a, ord(texto[last_matching_index]))
        
        next_available_index += 1

        bits_exp = sumar_bits(next_available_index, bits_exp) 
                
        vaciar_diccionario(bits_exp, diccionario) 
                
        last_matching_index += 1  # avanzamos posición en la lectura del texto

    return a
# ------------------------------------------------------------------

def extraer_simbolo(c, bits_exp, k, cad, len_cod, cod):
    """
    extraer_simbolo(c, bits_exp, k, cad, len_cod, cod)
    
    Objetivo de la función:
    -----------------------
        Este método únicamente se emplea en el método #descomprimir(codificacion).
        El objetivo de este es el de extraer una cadena de carácteres, ya sea 
        una letra o un número, para incluirlo en el diccionario de la 
        descodificación y finalmente en la cadena de carácteres que queremos
        descomprimir (texto).

    Parámetros y tipos de entrada:
    ------------------------------
        c : número entero
            Representa un contador empleado en el método.
        bits_exp : número entero
            Representa el número de bits empleado en la descompresión.
        k : número entero
            Representa la posición del bitarray en el método principal (descompresión).
        cad : cadena de carácteres
            Representa una cadena de carácteres auxiliar .
        len_cod : número entero
            Representa el número de carácteres (0s y 1s) presentes en el bitarray
            codificado.
        cod : bitarray
            Representa la cadena de bits que contiene la codificación del texto
            comprimido mediante el algoritmo pertinente.

    Parámetros y tipos de salida:
    -----------------------------
        cad : bitarray
            Idem.
        c : número entero
            Idem.
        k : número entero
            Idem.

    """
    
    for c in range(bits_exp):
        
        if(k < len_cod):
            cad += str(int(cod[k]))
            k += 1
        
    return cad, c, k
# ------------------------------------------------------------------  
    
def descomprimir(codificacion):
    """
    descomprimir(codificacion)
    
    Objetivo de la función:
    -----------------------
        Este método es de los más importantes de este programa. Dicho método
        aporta la funcionalidad de la descompresión real de una cadena de 
        bits (codificación) en una variable (texto) que contendrá la cadena
        de carácteres descomprimida orignalmente.
        Para ello, se hace uso de los diferentes métodos satélite
        presentes en este programa.

        El desarrollo de este método sigue el algoritmo de compresión sin
        pérdidas LZ78. Este se explicará con más detalle en la pertinente
        documentación facilitada (memoria).
        
    Parámetros y tipos de entrada:
    ------------------------------
        codificacion : bitarray
            Representa la cadena de bits que contiene la codificación del texto
            comprimido mediante el algoritmo pertinente.
            
    Parámetros y tipos de salida:
    -----------------------------
        texto : cadena de carácteres
            Representa el texto que queremos descomprimir.

    """
    diccionario = dict()
    
    bits_exp = MINBITS
    
    texto = ''
    
    i = 1
    j = 1
    k = 16
    
    len_cod = len(codificacion)
 
    while(k < len_cod):
        
        cad = ''
        
        c = 0
         
        cad, c, k = extraer_simbolo(c, bits_exp, k, cad, len_cod, codificacion) # Extraemos un número
        
        cad_int = int(cad, base = 2)
                
        i += 1
        
        c = 0
        
        cad = '' 

        bits_exp = sumar_bits(i, bits_exp)
        
        cad, c, k = extraer_simbolo(c, TAMBYTE, k, cad, len_cod, codificacion) # Extraemos una letra
        
        # Comprobamos que los números tengan o no letras asociadas a los mismos
        if(k < len_cod): 
        
            letra = chr(int(cad, base = 2))

            if(cad_int != 0):                   
                diccionario[j] = diccionario[cad_int] + letra    
            else:
                diccionario[j] = letra
                
            texto += diccionario[j]
            
            j += 1
        
        vaciar_diccionario(bits_exp, diccionario)

    return texto
# ------------------------------------------------------------------

def compresion(archivo_texto, archivo_lz78):
    """
    compresion(archivo_texto, archivo_lz78)
    
    Objetivo de la función:
    -----------------------
        Este método tiene la tarea de comprobar que los ficheros introducidos
        por parte del usuario en el método #menu_compresion() tienen un formato
        válido. Por otro lado, se realiza la compresión del archivo de texto
        extrayendo sus datos en bruto, se comprimen estos datos creando un
        fichero binario (con extensión .lz78 por defecto) comprimido.
    
    Parámetros y tipos de entrada:
    ------------------------------
        archivo_texto : cadena de carácteres
            Representa el nombre o ruta del archivo de texto que queremos comprimir.
        archivo_lz78 : cadena de carácteres
            Representa el nombre del archivo binario comprimido que queremos crear.
            
    Parámetros y tipos de salida:
    -----------------------------
        archivo_lz78 : cadena de carácteres
            Representa el nombre del archivo binario comprimido que queremos crear.
            Se ha considerado que es un parámetro de salida pues puede que la 
            extensión del archivo cambie si el usuario la introduce incorrectamente.

    """
    print("\n\tComprimiendo fichero...")
    
    texto = ''
    
    try: 
        # Sacamos la extensión del fichero solicitado
        ext_txt = os.path.splitext(archivo_texto)[1]
        
        if ext_txt != '.txt':
            print('\nEl fichero de texto no tiene extensión .txt')
            sys.exit(1)
            
    except IOError:
        print("\nNo se ha podido abrir el fichero de texto.")
        sys.exit(1)
    
    # Abrimos el fichero y cargamos los datos en una variable
    with open(archivo_texto, 'r', encoding='utf-8') as fo:        
        texto = fo.read()
        
    payload = comprimir(texto)
    
    ext_lz = os.path.splitext(archivo_lz78)[1]
    
    if ext_lz != ".lz78":
        archivo_lz78 = os.path.splitext(archivo_lz78)[0]+ ".lz78"
          
    with open(archivo_lz78, 'wb') as f1:
        payload.tofile(f1)
        
    print("\n\t¡Compresión completada!")
    input("\tPulse <Intro> para continuar")
# ------------------------------------------------------------------

def descompresion(archivo_lz78, archivo_texto):
    """
    descompresion(archivo_texto, archivo_lz78)
    
    Objetivo de la función:
    -----------------------
        Este método tiene la tarea de comprobar que los ficheros introducidos
        por parte del usuario en el método #menu_descompresion() tienen un formato
        válido. Por otro lado, se realiza la descompresión del archivo binario
        extrayendo sus datos en bruto, se descomprimen dichos datos creando un
        fichero de texto (con extensión .txt por defecto) con la información
        original.
    
    Parámetros y tipos de entrada:
    ------------------------------
        archivo_lz78 : cadena de carácteres
            Representa el nombre o ruta del archivo binario que queremos descomprimir.
        archivo_texto : cadena de carácteres
            Representa el nombre del archivo de texto que queremos recuperar.
            
    Parámetros y tipos de salida:
    -----------------------------
        archivo_lz78 : cadena de carácteres
            Representa el nombre del archivo binario comprimido que queremos crear.
            Se ha considerado que es un parámetro de salida pues puede que la 
            extensión del archivo cambie si el usuario la introduce incorrectamente.
    """
    print("\n\tDesomprimiendo fichero...")
    
    codificacion = bitarray()
    
    try:
        ext_lz = os.path.splitext(archivo_lz78)[1]
        
        if ext_lz != '.lz78':
            print('\nEl fichero comprimido carece de la extensión .lz78')
            sys.exit(1)
            
    except IOError: 
        print("\nNo se ha podido abrir el fichero comprimido.")
        sys.exit(1)
    
    
    with open(archivo_lz78,'rb') as fo:
        codificacion.fromfile(fo)
        
    payload = descomprimir(codificacion)
    
    ext_txt = os.path.splitext(archivo_texto)[1]
    
    if ext_txt != ".lz78":
        archivo_texto = os.path.splitext(archivo_texto)[0] + ".txt"
        
    with open(archivo_texto, 'w') as ft:
        ft.write(payload)
        
    print("\n\t¡Descompresión completada!")
    input("\tPulse <Intro> para continuar")
# ------------------------------------------------------------------
        
def menu():
    """
    menu()
    
    Objetivo de la función:
    -----------------------
        Este método se encarga de mostrar en pantalla una lista con las
        diferentes opciones que se pueden elegir en el menú principal de
        la aplicación. Asimismo, solicita por pantalla la opción elegida por
        el usuario.
        
    Parámetros y tipos de entrada:
    ------------------------------
        No dispone de ellos.

    Parámetros y tipos de salida:
    -----------------------------
        op : cadena de carácteres
            Retorna la opción elegida por parte del usuario, como cadena de carácteres.

    """
    print("_________________________________________________________________________\n")
    print("\n\tMENÚ COMPRESOR LZ78")
    print("\t───────────────────\n")
    print("\t\t1.- Comprimir archivo de texto.")
    print("\t\t2.- Descomprimir archivo .lz78.")
    print("\t\t0.- Salir.")
    op = input("\tIntroduzca una opción:  ")
    print("\n_________________________________________________________________________\n")

    return op
# ------------------------------------------------------------------

def menu_compresion():
    """
    menu_compresion()
    
    Objetivo de la función:
    -----------------------
        Este método se encarga de pedir por pantalla al usuario el nombre o ruta 
        del fichero de texto que desea comprimir, así como el nombre del 
        fichero binario comprimido. Este método devolverá el método 
        #compresion(input_file, output_file), donde ser realizará la compresión
        del fichero correspondiente.

    Parámetros y tipos de entrada:
    ------------------------------
        No dispone de ellos.
    
    Parámetros y tipos de salida:
    -----------------------------
        compresion(input_file, output_file):
            Este método retorna otra función, la cual realiza la compresión
            del fichero de texto introducido al fichero binario solicitado.
        
    """
    print("\n\tCOMPRESIÓN")
    print("\t──────────")
    
    input_file = input("\tEscriba por teclado el nombre o la ruta del fichero de texto a comprimir: ")
    
    output_file = input("\tEscriba por teclado el nombre del archivo donde se guardará la compresión (por defecto tendrá extensión .lz78): ")
    
    return compresion(input_file, output_file)
# ------------------------------------------------------------------

def menu_descompresion():
    """
    menu_descompresion()
    
    Objetivo de la función
    ----------------------
        Este método se encarga de pedir por pantalla al usuario el nombre o ruta 
        del fichero binario (con extensión .lz78) que desea comprimir, así como
        el nombre del fichero de texto descomprimido. Este método devolverá el método 
        #descompresion(input_file, output_file), donde ser realizará la descompresión
        del fichero correspondiente.

    Parámetros y tipos de entrada
    -----------------------------
        No dispone de ellos.
    
    Parámetros y tipos de salida
    ----------------------------
        Este método retorna otra función, la cual realiza la descompresión
        del fichero binario introducido al fichero de texto solicitado.
            
    """
    print("\n\tDESCOMPRESIÓN")
    print("\t─────────────")
    
    input_file = input("\tEscriba por teclado la ruta del fichero .lz78 a descomprimir: ")
    
    output_file = input("\tEscriba por teclado el nombre del fichero de texto donde se guardará la descompresión (por defecto tendrá extensión .txt): ")
    
    return descompresion(input_file, output_file)
# ------------------------------------------------------------------

def despedida():
    """
    despedida()
    
    Objetivo de la función
    ----------------------
        Este método se encarga de mostrar por pantalla un mensaje de despedida al 
        usuario, comunicando a este último la finalización de la ejecución del 
        programa.

    Parámetros y tipos de entrada
    -----------------------------
        No dispone de ellos.
    
    Parámetros y tipos de salida
    ----------------------------
        No retorna ningún parámetro (None).
        
    """
    print("\n\tFIN DE PROGRAMA")
    print("\n_________________________________________________________________________\n")
# ------------------------------------------------------------------

def fallo_introducir():
    """
    fallo_introducir()
    
    Objetivo de la función
    ----------------------
        Este método muestra en pantalla un mensaje de error, comunicando al usuario
        que ha introducido un valor erróneo por teclado en cualquier parte del
        programa, excepto en los casos en los que se desea emitir un mensaje acorde
        con una situación concreta.

    Parámetros y tipos de entrada
    -----------------------------
        No dispone de ellos.
    
    Parámetros y tipos de salida
    ----------------------------
        No retorna ningún parámetro (None).
        
    """
    print("\n\t¡ENTRADA ERRÓNEA! Volviendo al Menú Principal ...\n")
# ------------------------------------------------------------------

def main():
    """
    main()
    
    Objetivo de la función
    ----------------------
        Este método será lo primero que se ejecute en nuestro programa.
        A partir del mismo, se invocarán al resto de elementos del programa.
        Esencialmente, este subprograma nos da la posibilidad de comprimir o 
        descomprimir un archivo de texto o binario, respectivamente.
    
    Parámetros y tipos de entrada
    -----------------------------
        No dispone de ellos.
    
    Parámetros y tipos de salida
    ----------------------------
        No dispone de ellos.
        
    """
    op = ''

    while(op != '0'):

        op = menu()

        if(op == '1'):
            menu_compresion()      
        elif(op == '2'):         
            menu_descompresion()         
        elif(op == '0'):      
            despedida()
        else:  
            fallo_introducir()
# ------------------------------------------------------------------

# Inicializamos el programa siguiendo la recomendación del profesor
if __name__ == '__main__':
    main()
    
# ------------------------- FIN DE PROGRAMA