from langchain_openai import ChatOpenAI
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
import os
import dotenv

dotenv.load_dotenv()
llmclient = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))

memory = ConversationBufferMemory(memory_key="messagememory", return_messages=True)

from langchain_core.prompts import MessagesPlaceholder

prompt = ChatPromptTemplate(
    input_variables=["humaninput", "messagememory"],
    messages=[
        MessagesPlaceholder(variable_name="messagememory"),  # Placeholder for conversation history
        HumanMessagePromptTemplate.from_template("{humaninput}")  # Template for new user input
    ]
)

chain = (
    RunnablePassthrough.assign(messages=lambda x: memory.load_memory_variables({})["messages"])  # Load and assign memory
    | prompt  # Apply the prompt template
    | chat  # Send to the chat model
    | StrOutputParser()  # Ensure output is a string
)
while True:
    humaninput = input(">> ")
    result = chain.invoke({"humaninput": humaninput})   
    print(result)

    