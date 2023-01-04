import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una interfaz de usuario con streamlit
st.title("Generador de ensayo largo")

# Agrega una caja de texto para que el usuario ingrese el tema del ensayo
topic = st.text_input("Ingrese el tema del ensayo:")

# Genera los títulos de los cinco subensayos
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Por favor, genera cinco títulos de subensayos para un ensayo sobre " + topic + ".",
    max_tokens=1024
)
subtopic_titles = response["choices"][0]["text"].split("\n")

# Muestra los títulos al usuario y permite que elija los subtítulos que desee utilizar
selected_subtopics = st.multiselect("Seleccione los subtítulos para incluir en el ensayo:", subtopic_titles)

# Genera un subensayo para cada subtítulo seleccionado
subessays = {}
for subtopic in selected_subtopics:
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="Por favor, genera un subensayo sobre " + subtopic + ".",
      max_tokens=1024
  )
  subessay = response["choices"][0]["text"]
  subessays[subtopic] = subessay

# Muestra el contenido de subessays
print(subessays)

# Muestra el ensayo completo al usuario
st.write("Ensayo completo:")
full_essay = ""
for subtopic, subessay in subessays.items():
  full_essay += "**" + subtopic + "**\n" + subessay + "\n\n"
st.markdown(full_essay)
