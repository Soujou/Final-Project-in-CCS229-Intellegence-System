#Angelica Villar BSCS3A
#Final Project in CCS 229 - Intelligent Systems


#App.py
import streamlit as st
import openai

#OpenAI API key
openai.api_key = "FINALPROJECTCCS229"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    st.title("GPT-4 Streamlit App")
    user_input = st.text_input("Enter a prompt:")
    if user_input:
        response = generate_response(user_input)
        st.write("Generated Response:")
        st.write(response)

if __name__ == "__main__":
    main()
