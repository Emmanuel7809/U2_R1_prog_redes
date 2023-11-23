#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
def contar_letras(contenido):
    try:
        contenido = contenido.lower()
        
        recuentos_letras = {}

        for caracter in contenido:
            if caracter.isalpha() and caracter.isascii():
                recuentos_letras[caracter] = recuentos_letras.get(caracter, 0) + 1

        for letra in sorted(recuentos_letras):
            print(f"{letra} -> {recuentos_letras[letra]}")

    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    contenido_archivo = input("Ingrese el contenido del archivo: ")
    contar_letras(contenido_archivo)
