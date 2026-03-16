import pickle
from transformers import pipeline
import streamlit as st
from transformers import pipeline

# load classifier
model = pickle.load(open("scope_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# load lightweight coding model
llm = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono",
    device=-1
)

def software_agent(user_input):

    vec = vectorizer.transform([user_input])
    scope = model.predict(vec)[0]

    if scope == "not_scope":
        return "❌ Not in scope. Ask a software engineering question."

    prompt = f"""
You are a senior software engineer and technical mentor.

Provide a detailed and precise answer for the following programming question.

Follow this structure exactly:

Problem Explanation:
Explain clearly what the problem means.

Approach:
Describe the algorithm or logic used to solve the problem.

Step-by-Step Logic:
Explain the solution step by step.

Python Implementation:
Provide clean, well-formatted Python code.

Example Input and Output:
Give a small example showing how the code works.

Time Complexity:
Explain the Big-O time complexity.

Space Complexity:
Explain memory usage.

User Question:
{user_input}

Answer:
"""

@st.cache_resource
def load_llm():
    return pipeline(
        "text-generation",
        model="Salesforce/codegen-350M-mono"
    )

llm = load_llm()

    output = result[0]["generated_text"]

    return output.replace(prompt,"")
