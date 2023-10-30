import streamlit as st
import pandas as pd
from views import View
import time

class Cadastrar_cliente:
    def main():
        st.header("Cadastro de Clientes")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            if View.cliente_inserir(nome, email, fone, senha):
                st.success("Cliente inserido com sucesso")
            else:
                st.error("email ja utilizado")
            time.sleep(2)
            st.rerun()
