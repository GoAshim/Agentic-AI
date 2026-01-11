# Import necessary libraries
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load the API keys of the LLMs stored as environment variables in .env file
load_dotenv(override=True)

# OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

# Create a list to store the messages
messages = []

# Add the system message to the list
messages.append(SystemMessage(content="""
    You are a travel expert, who knows all about places around the world. 
    If the user asks about a place, you should provide brief information about the place.
    If the user asks about anything else, you should say that you can only answer travel related questions.
    """))

# Build the user prompt
while True:
    user_prompt = input("User: ")
    if user_prompt.lower() == "exit":
        break
    
    # Add the user message to the list
    messages.append(HumanMessage(content=user_prompt))
    # Call the model
    response = model.invoke(messages)
    # Add the AI message to the list
    messages.append(AIMessage(content=response.content))
    # Print the AI message
    print(f"AI: {response.content}")
