import streamlit as st
import openai
import os

# Use OpenAI's actual API key
openai.api_key = os.environ["OPENAI_API_KEY"]
model = "openai/gpt-4.1-mini"

st.title("Joke Explainer")
joke_input = st.text_area("Enter a joke:", height=150)

if st.button("Submit"):
    if joke_input.strip() == "":
        st.warning("Please enter a joke.")
    else:
        with st.spinner("Explaining the joke..."):
            try:
                response = openai.responses.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": f"Can you explain this joke: {joke_input}"}
                    ]
                )
                explanation = response.choices[0].message.content
                st.subheader("Explanation")
                st.write(explanation)
            except Exception as e:
                st.error(f"Error communicating with OpenAI API: {e}")
