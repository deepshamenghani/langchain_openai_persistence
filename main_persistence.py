from langchain_openai import ChatOpenAI
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_message_histories import FileChatMessageHistory
import os
import dotenv

dotenv.load_dotenv()
llmclient = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))

memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messagememory.json"),
    memory_key="messagememory",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["humaninput"],
    messages=[
        MessagesPlaceholder(variable_name="messagememory"),  
        HumanMessagePromptTemplate.from_template("{humaninput}")  
    ]
)

chain = (
    RunnablePassthrough.assign(
        messagememory=lambda x: memory.load_memory_variables({})["messagememory"]
    ) 
    | prompt  
    | llmclient 
    | StrOutputParser()  
)

while True:
    humaninput = input(">> ")
    result = chain.invoke({"humaninput": humaninput})   
    print(result)
    memory.save_context({"humaninput": humaninput}, {"output": result})    