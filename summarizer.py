from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

# Get a free key from https://console.groq.com/
llm = ChatGroq(
    temperature=0, 
    groq_api_key="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", 
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a legal expert analyzer."),
    ("human", "Summarize this contract: {text}")
])


summary_chain = summary_prompt | llm

def summarize_contract(text):
    # This gets the full object from Groq
    response = summary_chain.invoke({"text": text})
    
    # Extract ONLY the text content
    if hasattr(response, 'content'):
        return response.content
    return str(response)