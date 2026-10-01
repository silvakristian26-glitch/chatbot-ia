# titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    #mostrar a mensagem na tela
    # mandar a mensagem para IA responder
    #mostrar a resposta da IA na tela

# pip installstreamlit e openai
# google ia studio

import streamlit as st
from openai import OpenAI


modelo_ia = OpenAI(api_key=st.secrets["API_KEY"],
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

st.write("## Chatbot de IA")

# criar uma lista para armazenar as mensagens do chat
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"] 
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)


if mensagem_usuario:
    # exibir a mensagem na tela
    # user-> usuario
    # assistant -> IA
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role": "user", "content": mensagem_usuario}

    st.session_state["lista_mensagens"].append(mensagem1)
    

    # pegar a resposta da IA 
    resposta_modelo = modelo_ia.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=st.session_state["lista_mensagens"]
    )

    print(resposta_modelo)

    resposta_ia = resposta_modelo.choices[0].message.content

    # enviar a mensagem da IA no chat 
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}

    st.session_state["lista_mensagens"].append(mensagem2)


# manter o historico (criar uma memoria) 
# tornar as respostas da IA mais inteligentes
# codigo para colocar audio em pergunta na barra de mensagem 
