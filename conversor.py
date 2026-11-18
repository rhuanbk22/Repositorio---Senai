
# Função para converter Celsius em Fahrenheit
def celsius_para_fahrenheit(celsius):
    """
    Recebe uma temperatura em Celsius
    e converte para Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Função para converter quilômetros em milhas
def km_para_milhas(km):
    """
    Recebe uma distância em quilômetros
    e converte para milhas.
    """
    milhas = km * 0.621371
    return milhas


# Função para converter quilogramas em libras
def kg_para_libras(kg):
    """
    Recebe um peso em quilogramas
    e converte para libras.
    """
    libras = kg * 2.20462
    return libras


# Menu principal
while True:
    print("\n===== CONVERSOR DE UNIDADES =====")
    print("1 - Celsius para Fahrenheit")
    print("2 - Quilômetros para Milhas")
    print("3 - Quilogramas para Libras")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        celsius = float(input("digite a temperatura em celsius:"))

        resultado = celsius_para_fahrenheit(celsius)

        print(f"Temperatura em fahrenheit: {resultado:.2f}")

    elif opcao == '2':
        km = float(input("digite a distancia em quilômetros:"))

        resultado = km_para_milhas(km)

        print(f"distancia em milhas: {resultado:.2f}")

    elif opcao == '3':
        kg = float(input("digite o peso em quilogramas:"))

        resultado = kg_para_libras(kg)

        print(f"peso em libras: {resultado:.2f}")

    elif opcao == '0':
        print("programa encerrado,até mais!")
        break

    else:
        print("opção inválida, tente novamente.")
