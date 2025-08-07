# Utilitario para cargar variables de entorno
import os
from dotenv import load_dotenv

# Carga el archivo .env (debe estar en la misma carpeta del script)
load_dotenv()

# Importa la clase ChatOpenAI
from langchain_openai import ChatOpenAI

# Lee la clave desde la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Conexión a un modelo usando la clave desde .env
llm = ChatOpenAI(
    model="gpt-4.1",
    openai_api_key=api_key,
    temperature=0.2,
)

# (El resto del código se mantiene igual)
# ...

# "Personalidad" (contexto general) del modelo
contextoGeneral = """
  Eres un asistente llamado "BDA" que atenderá consultas de alumnos en una academia llamada "Big Data Academy", de
  formación de cursos de Big Data, Cloud Computing e Inteligencia Artificial. Al contestar debes
  seguir las siguientes reglas:

  1. Debes contestar en un lenguaje formal pero amigable
  2. Debes de usar emojis al responder
  3. No debes responder cosas no relacionadas con Big Data, Cloud Computing o Inteligencia Artificial
"""

from langchain.memory import ConversationBufferMemory

memoria = ConversationBufferMemory()
memoria.chat_memory.add_ai_message(contextoGeneral)

from langchain.chains import ConversationChain

chat = ConversationChain(
    llm=llm,
    memory=memoria,
    verbose=False
)

respuesta = chat.predict(input="""
Muy buenos días, estoy interesado en llevar cursos con ustedes.
¿Qué cursos tienen?, qué tipo de cursos tienen???
""")

print(respuesta)

respuesta = chat.predict(input="""
Dame un dato interesante del fútbol
""")

print(respuesta)

respuesta = chat.predict(input="""
Dame un resumen de la conversación
""")

print(respuesta)

