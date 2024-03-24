"""
Compresor utilizando Codificación LZ78 de Longitud Variable (12 bits).

Este programa implementa compresión LZ78 con un codificador de longitud variable capaz de manejar hasta 12 bits.

Autores:               Juan Francisco Montero (Aka: monp4r)
                       Luis Alfonso Martínez

Fecha de inicio:       27/10/2021
Fecha de finalización: 30/12/2021
"""

# IMPORTS:
import os   # Librería para interactuar con el sistema operativo.
import sys  # Librería para la manipulación de variables y funciones específicas del intérprete de Python.
from bitarray import bitarray  # Librería para trabajar con secuencias de bits eficientemente.

# Declaración de constantes.
MINBITS = 2   # Número mínimo de bits para representar una entrada en el diccionario.
MAXBITS = 12  # Número máximo de bits para representar una entrada en el diccionario.
LIMBITS = MAXBITS + 1  # Límite superior de bits permitidos en el diccionario.
TAMBYTE = 8   # Tamaño de un byte en bits.

def rellenar_bitarray_ceros(b, bits): 
    """
    Rellena un bitarray con ceros hasta alcanzar una longitud específica.

    Args:
    - b: Bitarray a rellenar.
    - bits: Longitud deseada del bitarray.

    Returns:
    - El bitarray modificado con ceros añadidos al principio si es necesario.
    """
    while(len(b) < bits):
        # Añadimos ceros mediante esta función.
        b.insert(0, False)
        
    return b
# ------------------------------------------------------------------
def agregar(bits, arraybits, c):
    """
    Agrega un carácter codificado en binario a un bitarray, rellenando con ceros si es necesario.

    Args:
    - bits: Longitud deseada del bitarray.
    - arraybits: Bitarray principal al que se añadirá el carácter codificado.
    - c: Carácter a codificar en binario y añadir al bitarray principal.

    Returns:
    - None
    """
    ba = bitarray()  # Inicializamos un nuevo bitarray
    aux = format(c, 'b')  # Formateamos la posición del carácter a binario
    ba.extend(aux)  # Extendemos el bitarray con la representación binaria del carácter
    ba = rellenar_bitarray_ceros(ba, bits)  # Rellenamos con ceros si es necesario
    arraybits.extend(ba)  # Añadimos el bitarray auxiliar al principal
# ------------------------------------------------------------------
def sumar_bits(i, bits_exp):
    """
    Incrementa la cantidad de bits necesarios para representar un número en binario si es necesario.

    Args:
    - i: Número entero a comparar.
    - bits_exp: Cantidad actual de bits necesarios para representar i en binario.

    Returns:
    - La cantidad de bits necesarios actualizada si i es igual al máximo valor representable con los bits actuales, de lo contrario, la cantidad de bits no se modifica.
    """
    max_b = (2 ** bits_exp) - 1  # Calculamos el máximo valor representable con la cantidad actual de bits
    
    if i == max_b:
        bits_exp += 1  # Incrementamos la cantidad de bits si i alcanza el máximo valor representable
    
    return bits_exp
# ------------------------------------------------------------------      
def vaciar_diccionario(bits_exp, diccionario):
    """
    Vacía un diccionario si la cantidad de bits alcanza un límite especificado.

    Args:
    - bits_exp: Cantidad de bits actual.
    - diccionario: Diccionario que se desea vaciar.

    Returns:
    - None
    """
    if bits_exp == LIMBITS:  # Verifica si la cantidad de bits es igual al límite definido
        diccionario.clear()  # Vacía el diccionario si se cumple la condición
# ------------------------------------------------------------------  
def comprimir(texto):
    """
    Realiza la compresión de un texto utilizando el algoritmo LZ78 sin pérdidas.

    Args:
    - texto: Cadena de caracteres que se desea comprimir.

    Returns:
    - a: Objeto bitarray que contiene la codificación binaria del texto comprimido.
    """

    # Inicialización del diccionario
    diccionario = dict()
    
    # Creación del objeto bitarray
    a = bitarray()

    len_texto = len(texto)

    last_matching_index = 0 # última posición leída del texto
    next_available_index = 1 # siguiente entrada al diccionario
    
    bits_exp = MINBITS

    # Configuración de los datos iniciales de la compresión
    agregar(TAMBYTE, a, MINBITS)  # Número inicial de bits de lectura
    agregar(TAMBYTE, a, MAXBITS)  # Máximo de bits permitidos

    # Proceso de compresión
    while last_matching_index < len_texto: 
    
        c = texto[last_matching_index]

        if c in diccionario:
            
            band = True
            
            while c in diccionario and band:
                
                nodo = diccionario[c]
                
                last_matching_index += 1 
                
                if last_matching_index < len_texto:
                    
                    c += texto[last_matching_index]  # Añadimos caracteres
                    
                else:
                    
                    last_matching_index -= 1
                    
                    band = False
            
            diccionario[c] = next_available_index 
         
            # Codificamos el carácter introducido
            agregar(bits_exp, a, nodo) 
            
        else:
            
            diccionario[c] = next_available_index
            
            # Codificamos el carácter introducido como 0 (Numérico)
            agregar(bits_exp, a, 0)
            
        # Codificamos el carácter introducido (Letra)
        agregar(TAMBYTE, a, ord(texto[last_matching_index]))
        
        next_available_index += 1

        bits_exp = sumar_bits(next_available_index, bits_exp) 
                
        vaciar_diccionario(bits_exp, diccionario) 
                
        last_matching_index += 1  # Avanzamos a la siguiente posición en el texto

    return a
# ------------------------------------------------------------------
def extraer_simbolo(c, bits_exp, k, cad, len_cod, cod):
    """
    Extrae un símbolo de un bitarray durante el proceso de descompresión.

    Args:
    - c: Número entero, contador empleado en el método.
    - bits_exp: Número entero, cantidad de bits empleados en la descompresión.
    - k: Número entero, posición del bitarray en el método principal (descompresión).
    - cad: Cadena de caracteres auxiliar.
    - len_cod: Número entero, cantidad de caracteres (0s y 1s) presentes en el bitarray codificado.
    - cod: Bitarray, cadena de bits que contiene la codificación del texto comprimido.

    Returns:
    - cad: Bitarray, cadena de bits actualizada.
    - c: Número entero, contador actualizado.
    - k: Número entero, posición del bitarray actualizada.
    """
    
    for _ in range(bits_exp):
        
        if k < len_cod:
            cad += str(int(cod[k]))
            k += 1
        
    return cad, c, k
# ------------------------------------------------------------------
def descomprimir(codificacion):
    """
    Realiza la descompresión de una cadena de bits utilizando el algoritmo LZ78.

    Args:
    - codificacion: Bitarray que contiene la codificación del texto comprimido.

    Returns:
    - texto: Cadena de caracteres descomprimida.
    """
    diccionario = dict()
    
    bits_exp = MINBITS
    
    texto = ''
    
    i = 1
    j = 1
    k = 16
    
    len_cod = len(codificacion)
 
    while k < len_cod:
        
        cad = ''
        
        c = 0
         
        cad, c, k = extraer_simbolo(c, bits_exp, k, cad, len_cod, codificacion) # Extraemos un número
        
        cad_int = int(cad, base=2)
                
        i += 1
        
        c = 0
        
        cad = '' 

        bits_exp = sumar_bits(i, bits_exp)
        
        cad, c, k = extraer_simbolo(c, TAMBYTE, k, cad, len_cod, codificacion) # Extraemos una letra
        
        # Comprobamos si los números tienen o no letras asociadas
        if k < len_cod: 
        
            letra = chr(int(cad, base=2))

            if cad_int != 0:                   
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
    Comprime un archivo de texto utilizando el algoritmo LZ78.

    Args:
    - archivo_texto: Cadena de caracteres, nombre o ruta del archivo de texto que se desea comprimir.
    - archivo_lz78: Cadena de caracteres, nombre del archivo binario comprimido que se desea crear.

    Returns:
    - archivo_lz78: Cadena de caracteres, nombre del archivo binario comprimido creado.
    """
    print("\n\tComprimiendo fichero...")
    
    texto = ''
    
    try: 
        # Verificamos la extensión del archivo de texto
        ext_txt = os.path.splitext(archivo_texto)[1]
        
        if ext_txt != '.txt':
            print('\nEl fichero de texto no tiene extensión .txt')
            sys.exit(1)
            
    except IOError:
        print("\nNo se ha podido abrir el fichero de texto.")
        sys.exit(1)
    
    # Abrimos el archivo de texto y cargamos los datos en una variable
    with open(archivo_texto, 'r', encoding='utf-8') as fo:        
        texto = fo.read()
        
    payload = comprimir(texto)
    
    # Verificamos la extensión del archivo de salida
    ext_lz = os.path.splitext(archivo_lz78)[1]
    
    if ext_lz != ".lz78":
        archivo_lz78 = os.path.splitext(archivo_lz78)[0] + ".lz78"
          
    with open(archivo_lz78, 'wb') as f1:
        payload.tofile(f1)
        
    print("\n\t¡Compresión completada!")
    input("\tPulse <Intro> para continuar")
    return archivo_lz78
# ------------------------------------------------------------------
def descompresion(archivo_lz78, archivo_texto):
    """
    Descomprime un archivo binario utilizando el algoritmo LZ78.

    Args:
    - archivo_lz78: Cadena de caracteres, nombre o ruta del archivo binario que se desea descomprimir.
    - archivo_texto: Cadena de caracteres, nombre del archivo de texto que se desea recuperar.

    Returns:
    - archivo_lz78: Cadena de caracteres, nombre del archivo binario comprimido que se ha descomprimido.
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
        
    texto_descomprimido = descomprimir(codificacion)
    
    ext_txt = os.path.splitext(archivo_texto)[1]
    
    if ext_txt != ".txt":
        archivo_texto = os.path.splitext(archivo_texto)[0] + ".txt"
        
    with open(archivo_texto, 'w') as ft:
        ft.write(texto_descomprimido)
        
    print("\n\t¡Descompresión completada!")
    input("\tPulse <Intro> para continuar")
# ------------------------------------------------------------------
def menu():
    """
    Muestra un menú con opciones para que el usuario elija y solicita la opción elegida.

    Returns:
    - op: Cadena de caracteres, opción elegida por el usuario.
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
    Solicita al usuario el nombre o ruta del archivo de texto que desea comprimir
    y el nombre del archivo binario comprimido. Luego, llama a la función de compresión.

    Returns:
    - compresion(input_file, output_file): Función que realiza la compresión del archivo de texto
                                            introducido al archivo binario solicitado.
    """
    print("\n\tCOMPRESIÓN")
    print("\t──────────")
    
    input_file = input("\tEscriba por teclado el nombre o la ruta del fichero de texto a comprimir: ")
    
    output_file = input("\tEscriba por teclado el nombre del archivo donde se guardará la compresión (por defecto tendrá extensión .lz78): ")
    
    return compresion(input_file, output_file)
# ------------------------------------------------------------------
def menu_descompresion():
    """
    Solicita al usuario el nombre o ruta del archivo binario (.lz78) que desea descomprimir
    y el nombre del archivo de texto descomprimido. Luego, llama a la función de descompresión.

    Returns:
    - descompresion(input_file, output_file): Función que realiza la descompresión del archivo binario
                                               introducido al archivo de texto solicitado.
    """
    print("\n\tDESCOMPRESIÓN")
    print("\t─────────────")
    
    input_file = input("\tEscriba por teclado la ruta del fichero .lz78 a descomprimir: ")
    
    output_file = input("\tEscriba por teclado el nombre del fichero de texto donde se guardará la descompresión (por defecto tendrá extensión .txt): ")
    
    return descompresion(input_file, output_file)
# ------------------------------------------------------------------
def despedida():
    """
    Muestra un mensaje de despedida al usuario, indicando la finalización del programa.

    Returns:
    - None
    """
    print("\n\tFIN DE PROGRAMA")
    print("\n_________________________________________________________________________\n")
# ------------------------------------------------------------------
def fallo_introducir():
    """
    Muestra un mensaje de error al usuario indicando que ha introducido un valor erróneo por teclado.

    Returns:
    - None
    """
    print("\n\t¡ENTRADA ERRÓNEA! Volviendo al Menú Principal ...\n")
# ------------------------------------------------------------------
def main():
    """
    Función principal que inicia el programa y gestiona las opciones del usuario.

    Returns:
    - None
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
# Inicializamos el programa llamando a la función principal.
if __name__ == '__main__':
    main()
# -------------------------------------------------- FIN DE PROGRAMA
