import pickle
import streamlit as st
from transformers import pipeline

# Load classifier
model = pickle.load(open("scope_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


@st.cache_resource
def load_llm():
    return pipeline(
        "text-generation",
        model="Salesforce/codegen-350M-mono"
    )


llm = load_llm()


def software_agent(user_input):

    # classify query
    vec = vectorizer.transform([user_input])
    scope = model.predict(vec)[0]

    if scope == "not_scope":
        return "❌ Not in scope. Ask a software engineering question."

    prompt = f"""
You are a senior software engineer.

Provide a detailed answer.

Structure your response like this:

Problem Explanation:
Approach:
Step-by-step Logic:
Python Implementation:
Example Input/Output:
Time Complexity:
Space Complexity:

User Question:
{user_input}

Answer:
"""

    result = llm(prompt, max_new_tokens=300)

    output = result[0]["generated_text"]

    return output.replace(prompt, "")
