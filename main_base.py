from langchain_openai import ChatOpenAI
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import dotenv

dotenv.load_dotenv()
llmclient = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))

prompt = ChatPromptTemplate(
    input_variables=["humaninput"],  
    messages=[
        HumanMessagePromptTemplate.from_template("{humaninput}")  
    ]
)

chain = prompt | llmclient | StrOutputParser()

while True:
    humaninput = input(">> ")
    result = chain.invoke({"humaninput": humaninput})   
    print(result)