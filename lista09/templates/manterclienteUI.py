import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    tab1, tab2, tab3 = st.tabs(["Listar", "Atualizar", "Excluir"])
    with tab1: ManterClienteUI.listar()
    with tab2: ManterClienteUI.atualizar()
    with tab3: ManterClienteUI.excluir()

  def listar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      lista = []
      for cliente in clientes:
        nome = cliente.get_nome()
        email = cliente.get_email()
        fone = cliente.get_fone()
        lista.append([nome, email, fone])
      df = pd.DataFrame(lista, columns=["Nome", "E-mail", "Fone"])
      st.dataframe(df)


  def atualizar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        id = op.get_id()
        if View.cliente_inserir(nome, email, fone, senha):
            st.success("Cliente atualizado com sucesso")
        else:
            st.error("email ja utilizado")
        time.sleep(2)
        st.rerun()

  def excluir():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Exclusão de Clientes", clientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Cliente excluído com sucesso")
        time.sleep(2)
        st.rerun()
