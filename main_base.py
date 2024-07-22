# Import necessary classes for creating chat prompts
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# Import the ChatOpenAI class to interact with OpenAI's chat models
from langchain_openai import ChatOpenAI

# Import StrOutputParser to ensure the output is in string format
from langchain_core.output_parsers import StrOutputParser

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Import os to access environment variables
import os

# Load environment variables from .env file
load_dotenv()

# Initialize ChatOpenAI with the API key from environment variables
chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))

# Create a ChatPromptTemplate with a single HumanMessagePromptTemplate
prompt = ChatPromptTemplate(
    input_variables=["content"],  # Define the input variable for the prompt
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")  # Create a template for human messages
    ]
)

# Create a chain: prompt -> chat model -> string output
chain = prompt | chat | StrOutputParser()

# Start an infinite loop for continuous interaction
while True:
    # Get user input and store it in 'content'
    content = input(">> ")

    # Invoke the chain with the user input
    result = chain.invoke({"content": content})
    
    # Print the result (AI's response)
    print(result)