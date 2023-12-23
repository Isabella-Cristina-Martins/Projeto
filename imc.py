peso = float(input("Digite seu peso em kg: "))
altura = float(input('Digite sua altura em metros(ex: 1.80): '))

def imc(peso, altura):

    imc = peso / altura**2

    if imc <= 18.5:
        print('Abaixo do peso')
    elif imc >= 18.5 and imc <= 24.9:
        print('Peso normal')
    elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30 and imc <= 34.9:
        print('Obesidade grau 1')
    elif imc >= 35 and imc <= 39.9:
        print('Obesidade grau 2')
    elif imc >= 40:
        print('Obesidade Morbida')
    else:
        print('Inválido')

imc(peso, altura)