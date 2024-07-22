# Import ChatOpenAI for interacting with OpenAI's chat models
from langchain_openai import ChatOpenAI
# Import components for creating chat prompts
from langchain_core.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
# Import StrOutputParser to ensure the output is in string format
from langchain_core.output_parsers import StrOutputParser
# Import RunnablePassthrough for creating the chain
from langchain_core.runnables import RunnablePassthrough
# Import ConversationBufferMemory for maintaining conversation history
from langchain.memory import ConversationBufferMemory
# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv
# Import os to access environment variables
import os

# Load environment variables from .env file
load_dotenv()

# Initialize ChatOpenAI with the API key from environment variables
chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API"))

# Initialize ConversationBufferMemory to store conversation history
memory = ConversationBufferMemory(memory_key="messages", return_messages=True)

# Create a ChatPromptTemplate with placeholders for messages and content
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),  # Placeholder for conversation history
        HumanMessagePromptTemplate.from_template("{content}")  # Template for new user input
    ]
)

# Create the chain: load memory -> apply prompt -> chat model -> string output
chain = (
    RunnablePassthrough.assign(messages=lambda x: memory.load_memory_variables({})["messages"])  # Load and assign memory
    | prompt  # Apply the prompt template
    | chat  # Send to the chat model
    | StrOutputParser()  # Ensure output is a string
)

# Start an infinite loop for continuous interaction
while True:
    # Get user input
    content = input(">> ")
    # Invoke the chain with the user input
    result = chain.invoke({"content": content})
    # Print the result (AI's response)
    print(result)
    # Save the interaction to memory
    memory.save_context({"content": content}, {"output": result})