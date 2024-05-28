from langchain_groq import ChatGroq
import streamlit as st



user_prompt = st.text_input("Input here", placeholder = "Ask me!")

system_prompt = f"Share your response based on {user_prompt} as a python code. Share only python code, nothing else."
def groqfunction(query):
    GROQ_API_KEY = "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"
    
    #new_prompt= str(system_prompt)+ str("\n\n\n user query:")+ str(user_prompt)

 # Groq model set up with llama2-70b model
    llm = ChatGroq(groq_api_key = GROQ_API_KEY,
               model_name = "llama3-70b-8192")
    response = llm.invoke(query).content
  
    return response
if user_prompt:
    response=groqfunction(system_prompt)
    st.write(response)
