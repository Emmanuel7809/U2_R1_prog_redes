#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
def display_siete_segmentos(numero):
    digitos = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]

    digitos_str = [[digitos[int(digito)][i] for i in range(5)] for digito in str(numero)]

    for i in range(5):
        print(" ".join(digit[i] for digit in digitos_str))

entrada_usuario = input("Por favor, ingresa un numero no negativo: ")
try:
    numero = int(entrada_usuario)
    display_siete_segmentos(numero)
except ValueError:
    print("Por favor, puede ingresar un numero valido.")

