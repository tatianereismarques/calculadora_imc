import streamlit as st

def calculadora_imc():

    st.title("Calculadora de IMC")
    st.subheader("Descubra como está o seu Índice de Massa Corporal")
    st.write("")
    st.write("")

    peso_str = st.text_input("Insira o seu peso em kg: ")
    altura_str = st.text_input("Agora insira a sua altura: Exemplo 1.70 ")

    if st.button("Calcular IMC"):

        peso = float(peso_str)
        altura = float(altura_str)
        imc = peso / (altura * altura)
        resultado = str(imc)
        st.write(f"O seu IMC é de: {resultado[:2] + '.' + resultado[3:5]}")

        if imc < 18.5:
            st.subheader("Você está abaixo do peso. O seu IMC indica Magreza.")
        elif imc >= 18.5 and imc <= 24.9:
            st.subheader("Você está dentro do peso. O seu IMC indica Eutrófico.")
        elif imc >= 25 and imc <= 29.9:
            st.subheader("Você está em sobrepeso. O seu IMC indica Pré-obesidade.")
        elif imc >= 30 and imc <= 34.9:
            st.subheader("Você está em obesidade. O seu IMC indica Obesidade grau I.")
        elif imc >= 35 and imc <= 39.9:
            st.subheader("Você está em obesidade. O seu IMC indica Obesidade grau II.")
        elif imc >= 40:
            st.subheader("Você está em obesidade. O seu IMC indica Obesidade grau III, Mórbida.")
        else:
            st.subheader("Ops, algo deu errado! Reinicie novamente a calculadora. Tchau!")