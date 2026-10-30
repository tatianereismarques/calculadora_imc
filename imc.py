#%%
def calculadoraimc():
    peso = float(input("Bem-vindo a Calculadora de IMC! Para começar, insira o seu pedo em kg: "))
    altura = float(input("Agora insira a sua altura: "))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Você está abaixo do peso. O seu IMC indica Magreza.")
    elif imc >= 18.5 and imc <= 24.9:
        print("Você está dentro do peso. O seu IMC indica Eutrófico.")
    elif imc >= 25 and imc <= 29.9:
        print("Você está em sobrepeso. O seu IMC indica Pré-obesidade.")
    elif imc >= 30 and imc <= 34.9:
        print("Você está em obesidade. O seu IMC indica Obesidade grau I.")
    elif imc >= 35 and imc <= 39.9:
        print("Você está em obesidade. O seu IMC indica Obesidade grau II.")
    elif imc >= 40:
        print("Você está em obesidade. O seu IMC indica Obesidade grau III, Mórbida.")
    else:
        print("Ops, algo deu errado! Reinicie novamente a calculadora. Tchau!")

# %%

# %%
calculadoraimc()
