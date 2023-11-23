#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
def contar_letras(entrada):
    try:
        contenido = entrada.lower()
        recuentos_letras = {}
        for caracter in contenido:
            if caracter.isalpha() and caracter.isascii():
                recuentos_letras[caracter] = recuentos_letras.get(caracter, 0) + 1
        recuentos_ordenados = sorted(recuentos_letras.items(), key=lambda x: x[1], reverse=True)
        for letra, frecuencia in recuentos_ordenados:
            print(f"{letra} -> {frecuencia}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
if __name__ == "__main__":
    cadena_entrada = input("Ingrese la cadena de entrada: ")
    contar_letras(cadena_entrada)
