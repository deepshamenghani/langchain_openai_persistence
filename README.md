# LangChain OpenAI Persistence: Building a Chatbot with Long-Term Memory

This repository demonstrates the process of building a persistent conversational chatbot using LangChain and OpenAI. It showcases the evolution from a simple Q&A bot to a sophisticated chatbot with memory that persists across sessions.

## Project Structure

- `main_base.py`: Basic Q&A bot implementation
- `main_conversation.py`: Chatbot with in-memory conversation history
- `main_persistence.py`: Chatbot with persistent memory across sessions
- `main.py`: Final implementation combining all features

## Features

- Simple Q&A functionality
- Conversation memory within a single session
- Persistent conversation memory across multiple sessions
- Integration with OpenAI's language models
- Utilization of LangChain for building conversational AI

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone this repository
2. Install required packages: pip install langchain langchain-openai python-dotenv
3. Set up your OpenAI API key in a `.env` file: OPENAI_API=your_api_key_here

## Usage

Run the different versions of the chatbot:

1. Basic Q&A: python main_base.py
2. Conversation with in-memory history: python main_conversation.py
3. Persistent conversation across sessions: python main_persistence.py

## How It Works

This project demonstrates the step-by-step process of building an increasingly sophisticated chatbot:

1. **Basic Q&A System (main_base.py)**
- Sets up a simple interaction with OpenAI's language model
- Processes each query independently without retaining context

2. **In-Memory Conversation (main_conversation.py)**
- Implements conversation memory using LangChain's ConversationBufferMemory
- Maintains context within a single session
- Enhances the chatbot's ability to engage in contextual conversations

3. **Persistent Memory (main_persistence.py)**
- Introduces FileChatMessageHistory for persistent storage
- Allows conversations to continue across multiple sessions
- Stores chat history in a local JSON file

4. **Final Implementation (main.py)**
- Combines all features for a fully-functional, persistent chatbot

Each step builds upon the previous, showcasing the incremental development of the chatbot's capabilities.

## Key Components

- **ChatOpenAI**: Interface to OpenAI's chat models
- **ConversationBufferMemory**: Stores conversation history in memory
- **FileChatMessageHistory**: Enables persistent storage of conversation history
- **ChatPromptTemplate**: Structures prompts for the language model
- **RunnablePassthrough**: Facilitates the flow of data through the conversation chain

## Customization

Feel free to modify the code to experiment with different:
- Language models
- Prompt templates
- Memory management strategies
- Conversation flow structures

---

This project is part of a tutorial series on building advanced chatbots. For a detailed explanation of each step, please refer to the associated blog post: [https://medium.com/@menghani.deepsha](https://medium.com/@menghani.deepsha)
