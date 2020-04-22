'''
CALCULADORA V5
'''
 # ---------------------------------------------FUNCIONES PARA LAS CONVERSIONES-----------------------------------------------

#funciones binario*****************************************
def binario_decimal(numero_de_entrada):
    '''Función 1 única para pasar binario a decimal'''
    contador = 0
    sumando = 2**(len(numero_de_entrada)-1)
    for a in numero_de_entrada:
        contador += sumando * int(a)
        sumando //=2
    result_bin_dec = contador
    return result_bin_dec


def binario_octal(result_bin_dec):
    '''Función 2 llamo a la variable anterior para pasar a octal desde desde
    el resiltado en binario.'''
    numero_bin_oct = result_bin_dec
    lista = []
    while numero_bin_oct >=1:
        lista.insert(0,numero_bin_oct%8)
        numero_bin_oct //=8
    result_bin_oct = "".join(str(i) for i in lista)
    return result_bin_oct 


def binario_hexadecimal(result_bin_dec):
    '''Función 3 llamo a la variable anterior para pasar a hexa desde desde
    el resultado en decimal.'''
    numero_bin_hex = result_bin_dec
    lista = []
    while numero_bin_hex >= 1:
        lista.insert(0,numero_bin_hex%16)
        numero_bin_hex //=16
    result_bin_hex = formateo_hexadecimal(lista)
    return result_bin_hex 


 # desde_octal***************************************************
def octal_decimal(numero_de_entrada):
    '''Función 4. única para pasar de octal a decimal'''
    contador = 0
    sumando = 8**(len(numero_de_entrada)-1)
    for i in numero_de_entrada:
        contador += sumando *int(i)
        sumando //=8
    result_oct_dec = contador
    return result_oct_dec 


def octal_binario(result_oct_dec):
    '''Función 5. LLama a la función anterior para pasa desde el 
    resultado decimal anterior a binario paraasí 
    hacer la conversión octal a binario'''
    num_oct_bin = result_oct_dec
    lista = []
    while num_oct_bin >=1:
        lista.insert(0,num_oct_bin%2)
        num_oct_bin //=2
    result_oct_bin = "".join(str(i)for i in lista)
    return result_oct_bin


def octal_hexadecimal(result_bin_dec):
    '''Función 6. Llama a resultado decimal anterior a hexadecimal para
    así hacer la conversión octal a hexadecimal'''
    num_oct_hex = result_bin_dec
    lista = []
    while num_oct_hex >=1:
        lista.insert(0,num_oct_hex%16)
        num_oct_hex //=16
    result_oct_hex = formateo_hexadecimal(lista)
    return result_oct_hex 


#desde_hexadecimal*************************************************
def hexadecimal_decimal(numero_de_entrada):
    '''Función 7. Única conversión hexadecimal a decimal'''
    result_hex_dec = int(numero_de_entrada, 16)
    return result_hex_dec 


def hexadecimal_binario(result_hex_dec):
    '''Función 8. pasa desde el resultado decimal anterior a hexadecimal para
    así hacer la conversión octal a hexadecimal'''
    num_hex_bin = result_hex_dec
    lista = []
    while num_hex_bin >=1:
        lista.insert(0,num_hex_bin%2)
        num_hex_bin //=2
    result_hex_dec = "".join(str(i) for i in lista)
    return result_hex_dec


def hexadecimal_octal(result_hex_dec):
    '''Función 9. Pasa desde el resultado decimal anterior a hexadecimal para
    así hacer la conversión octal a hexadecimal'''
    num_hex_octal = result_hex_dec
    lista = []
    while num_hex_octal >=1:
        lista.insert(0,num_hex_octal%8)
        num_hex_octal //=8
    result_hex_dec = "".join(str(i) for i in lista)
    return result_hex_dec


def formateo_hexadecimal(numero):
    '''Función 10. formatea los numeos en letras para las conversiones en las que participe hexadecimal'''
    resultado = ""
    for i in numero:
        if i == 10:
            resultado += 'A'
        elif i == 11:
            resultado += 'B'
        elif i == 12:
            resultado += 'C'
        elif i == 13:
            resultado += 'D'
        elif i == 14:
            resultado += 'E'
        elif i == 15:
            resultado += 'F'
        else:
            resultado += str(i)
    return resultado


#funciones decimal***************************###
def decimal_binario(numero_de_entrada):
    '''Función 11. Única para convertit decimal a binario
    También se utiliza para hacer el complemento a2 de los numeros añadiendole
    0 en la funciónde abajo'''
    numero_decimal = int(numero_de_entrada)
    lista = []
    while numero_decimal >=1:
        lista.insert(0,numero_decimal%2)
        numero_decimal //=2
    result_dec_bin = "".join(str(i) for i in lista)
    return result_dec_bin


def decimal_octal(numero_de_entrada):
    '''Función 12. Única para convertir de decimal a octal'''
    numero_decimal = int(numero_de_entrada)
    lista = []
    while numero_decimal >=1:
        lista.insert(0,numero_decimal%8)
        numero_decimal //= 8
    result_dec_oct = "".join(str(i) for i in lista)
    return result_dec_oct 


def decimal_hexadecimal(numero_de_entrada):
    '''Función 13. Única para converir de decimal a hexadecimal'''
    numero_decimal = int(numero_de_entrada)
    lista = []
    while numero_decimal >= 1:
        lista.insert(0,numero_decimal%16)
        numero_decimal //= 16
    result_dec_hex = formateo_hexadecimal(lista)
    return result_dec_hex

 #-----------------------------------------------------FUNCIONES PARA LOS COMPLEMENTOS--------------------------------------------------------------------

def comprueba_negativo(decimal):
    '''Función 14. Comprueba si el numero decimal que se está introduciendo es negativo'''
    if numero_de_entrada[0] == '-':
        return True # Es negativo
    return False # Si no devuelve Falso


def invertir(n):
    '''Función 15. Invierte los valores binarios (similar al operador and)'''
    if n == '0':
        return '1'
    return '0'


def ca1(numero):
    '''Función 16. Complemento a1 de un numero'''
    resultado = ""
    for i in numero:
        resultado += invertir(i)
    return resultado

def ca2_num_neg(numero_de_entrada):
    '''Función 17. Hace el ca2 de un numero'''
    # Primero entra en un bucle para recorrer el contenido de la lista en sentido inverso apuntando
    # los valores en una nueva cadena; cuando llega a 1 entra y se para
    # Mediante un contador cuento las posiciones que recorre esta dentro de la cadena
    # gracias a las posiciones contadas en el bucle anterior y mediante len cogo la rebanada que
    # ha sido tratada por el bucle y le hago el ca1(cambiar valores 1 por 0 y viceversa)
    # esto se lo sumo al resultado cadena con el final y lo retorno de la función 
    c = 0
    resultado = ""
    for i in reversed(numero_de_entrada):
        c += 1
        if valores_posibles_binario(i) == False:
            return 'Los valores son erroneos'
        elif i == '0':
            resultado = i + "" + resultado
        elif i == '1':
            resultado = i + "" + resultado
            break
    return "1" + ca1(numero_de_entrada[0:len(numero_de_entrada)-c]) + resultado


#------------------------------------------------FUNCIONES PARA CONTROLAR LAS ENTRADAS -----------------------------


def valores_posibles_binario(n):
    '''Función 18 Comprueba si se han introducido correctamente los números binarios en los complementos'''
    v = ('0','1')
    if n not in v:
        return False # no es un valor binario
    return True # es un valor binari0

def binario(n):
    '''Funcion 19. Para para comprobar las entradas de de binario en conversiones'''
    v = ('0','1')
    for i in n:
        if i not in v:
            return False
    return True

def valores_posibles_decimal(n):
    '''Función 20. Para comoprobar las entradas en decimal'''
    v = ('0','1','2','3','4','5','6','7','8','9')
    for i in numero_de_entrada:
        if i not in v:
            return False # no es un valor decimal
    return True # es un valor decimal

def valores_posibles_octal(n):
    '''Función 21. Para controlar las entradas en octal'''
    v = ('0','1','2','3','4','5','6','7')
    for i in numero_de_entrada:
        if i not in v:
            return False # no es un octal
    return True  # es un octal

def valores_posibles_hexadecimal(n):
    '''Función 22. Para controlar las entradas en hexadecimal'''
    v = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f')
    for i in numero_de_entrada:
        if i not in v:
            return False # no es hexadecimal
    return True # es hexadecimal
    

#--------------------------------------------------MENÚ Y LLAMADA A FUNCIONES---------------------------------------------------
print('-'*60+'\n'+'\t'*2+'   CALCULADORA BINARIA\n'+'-'*60)
while True:
    try: #escepciones
        numero_de_entrada = input("\nIntroduzca un número por teclado un número en el formato que quieras:\n>>> ")
        eleccion = str(input("Indique que función va ha realizar\n\n"+"-"*60+"\n\"binario_decimal\"\t\"binario_octal\"\n\"binario_hexadecimal\"\t\"octal_decimal\"\n\"octal_binario\"\t\t\"octal_hexadecimal\"\n\"hexadecimal_decimal\"\t\"hexadecimal_octal\"\n\"binario_binario\"\t\"decimal_binario\"\n\"decimal_octal\"\t\t\"decimal_hexadecimal\"\n\"ca1_desde_binario\"\t\"ca2_desde_binario\n\t   \"ca2_desde_decimal\"\n\n\tPARA SALIR INTRODUCE \"FIN\"\n"+"-"*60+"\n\n>>> "))
 # resultados(llamada_a_dunciones)
        

         # resultados binario
        if eleccion.lower() == "binario_decimal" or eleccion.lower() == "binario_octal" or eleccion.lower() == "binario_hexadecimal":
           
            if binario(numero_de_entrada) == True:
           
                if eleccion.lower() == "binario_decimal":
                    print(f"{numero_de_entrada} convertido a decimal es igual a {binario_decimal(numero_de_entrada)}")
                
                elif eleccion.lower() == "binario_octal":
                    print(f"{numero_de_entrada} convertido a octal es igual a {binario_octal(binario_decimal(numero_de_entrada))}")
                
                elif eleccion.lower() == "binario_hexadecimal":
                    print(f"{numero_de_entrada} convertido a hexadecimal es iguál a {binario_hexadecimal(binario_decimal(numero_de_entrada))}")
            else:
                print("Los valores introducidos no son binarios")
        
        
         # resultados octal
        elif eleccion.lower() == 'octal_decimal' or eleccion.lower() == 'octal_binario' or eleccion.lower() == 'octal_hexadecimal':    
            if valores_posibles_octal(numero_de_entrada):
                if eleccion.lower() == "octal_binario":
                    print(f"{numero_de_entrada} convertido a binario es igual a {octal_binario(octal_decimal(numero_de_entrada))}")
                    
                elif eleccion.lower() == "octal_decimal":
                    print(f"{numero_de_entrada} convertido a decimal es igual a {octal_decimal(numero_de_entrada)}")
                    
                elif eleccion.lower() == "octal_hexadecimal":
                    print(f"{numero_de_entrada} convertido a hexadecimal es igual a {octal_hexadecimal(octal_decimal(numero_de_entrada))}")
            else:
                print("los valores introducidos no son en octal")        
        
        
         # resultados hexadecimal
        elif eleccion.lower() == "hexadecimal_decimal" or eleccion.lower() == "hexadecimal_binario" or eleccion.lower() == "hexadecimal_octal": 
            if valores_posibles_hexadecimal(numero_de_entrada) == True:
                if eleccion.lower() == "hexadecimal_decimal":
                    print(f"{numero_de_entrada} convertido a decimal es igual a {hexadecimal_decimal(numero_de_entrada)}")
                
                elif eleccion.lower() == "hexadecimal_binario":
                    print(f"{numero_de_entrada} convertido a binario es igual a {hexadecimal_binario(hexadecimal_decimal(numero_de_entrada))}")
                
                elif eleccion.lower() == "hexadecimal_octal":
                    print(f"{numero_de_entrada} convertido a octal es igual a {hexadecimal_octal(hexadecimal_decimal(numero_de_entrada))}")
            else:
                print("Los valores introducidos no son en hexadecimal")    
        

         # resultados decimal
        elif eleccion.lower() == "decimal_binario" or eleccion.lower() == "decimal_octal" or eleccion.lower() == "decimal_hexadecimal":
            
            if valores_posibles_decimal(numero_de_entrada) == True:
                
                if eleccion.lower() == "decimal_binario":
                    print(f"{numero_de_entrada} covertido a binario es igual a {decimal_binario(numero_de_entrada)}")
            
                elif eleccion.lower() == "decimal_octal":
                    print(f"{numero_de_entrada} convertido a octal es igual a {decimal_octal(numero_de_entrada)}")
            
                elif eleccion.lower() == "decimal_hexadecimal":
                    print(f"{numero_de_entrada} convertido a hexadecimal es igual a {decimal_hexadecimal(numero_de_entrada)}")
            else:
                print("El numero decimal que has introducido no es decimal")
         

         # complementos
        elif eleccion.lower() == "ca2_desde_binario": # la comprobación se hace en la función
            print(ca2_num_neg(numero_de_entrada))

        elif eleccion.lower() == "ca1_desde_binario":
            if binario(numero_de_entrada): # si es binario
                print(ca1(numero_de_entrada))
            else:
                print("El numero que has introducido no es binario")

        elif eleccion.lower() == "ca2_desde_decimal":
            if comprueba_negativo(numero_de_entrada): # si es negativo
                numero_de_entrada = numero_de_entrada[1:]
                print(ca2_num_neg(decimal_binario(numero_de_entrada)))
            else:
                print(decimal_binario(numero_de_entrada)) # si no hace el decimal_biario

        
        elif eleccion.lower() == "fin":
            print("hasta luego amigo")
            break
        
        else:
            print("La acción que ha introducido no es reconocida por el software\n"+"-"*60)
    
    except ValueError:
        print("Valor introducido no válido\n"+"-"*60)
    except EOFError:
        print("Valor introducido no válido\n"+"-"*60)