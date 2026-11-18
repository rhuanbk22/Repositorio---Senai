def area_retangulo(base, altura):

 area = base * altura
    return area

base = float(input("Digite a base do retângulo:"))
altura = float(input("Digite a altura do retângulo:"))

resultado = area_retangulo(base, altura)

print(f"A área do retângulo é: {resultado:.2f}")
