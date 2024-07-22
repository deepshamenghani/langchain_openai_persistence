from langchain_openai import ChatOpenAI
from langchain_core.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()

chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = (
    RunnablePassthrough.assign(messages=lambda x: memory.load_memory_variables({})["messages"])
    | prompt
    | chat
    | StrOutputParser()
)

while True:
    content = input(">> ")
    result = chain.invoke({"content": content})
    print(result)
    memory.save_context({"content": content}, {"output": result})