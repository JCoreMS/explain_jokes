import streamlit as st
import openai
import os
from openai import OpenAI

# Set your OpenAI API key
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

st.title("Joke Explainer")

# Input field for the joke
joke_input = st.text_area("Enter a joke:", height=150)

# Submit button
if st.button("Submit"):
    if joke_input.strip() == "":
        st.warning("Please enter a joke.")
    else:
        with st.spinner("Explaining the joke..."):
            try:
                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user", 
                            "content": f"Can you explain this joke: {joke_input}",
                         }
                    ],
                    model=model,
                )
                explanation = response.choices[0].message.content
                st.subheader("Explanation")
                st.write(explanation)
            except Exception as e:
                st.error(f"Error communicating with OpenAI API: {e}")
            else:
                st.warning("Please enter a joke before submitting.")