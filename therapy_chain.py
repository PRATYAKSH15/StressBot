from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from config_settings import GOOGLE_API_KEY
from therapy_prompt import therapy_prompt
import os

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def load_therapy_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0.7,
        convert_system_message_to_human=True
    )

    memory = ConversationBufferMemory(return_messages=True)

    return ConversationChain(
        llm=llm,
        memory=memory,
        prompt=therapy_prompt,
        verbose=False
    )
