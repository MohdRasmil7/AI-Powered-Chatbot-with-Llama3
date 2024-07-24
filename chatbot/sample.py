import streamlit as st
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes()


# Title of the app
st.title("Chat with LLama3 or Gemma 3")

# Create radio buttons for selecting the model
model_option = st.radio("Choose a model to chat with:", ("LLama3", "Gemma 3"))

# Display a text box with a heading based on the selected model
if model_option == "LLama3":
    st.subheader("Chat with LLama3")
    user_input = st.text_input("Type your message:")
    if user_input:
        st.write(f"You: {user_input}")
        # Here, you would add the code to send the user_input to the LLama3 model and display the response
elif model_option == "Gemma 3":
    st.subheader("Chat with Gemma 3")
    user_input = st.text_input("Type your message:")
    if user_input:
        st.write(f"You: {user_input}")
        # Here, you would add the code to send the user_input to the Gemma 3 model and display the response
