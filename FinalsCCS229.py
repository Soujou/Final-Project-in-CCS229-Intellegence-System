#Angelica Villar BSCS3A
#Final Project in CCS 229 - Intelligent Systems

import streamlit as st
from openai import OpenAI

from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        
#OpenAI API key
openai.api_key = "FINALPROJECTCCS229"

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")

def main():
    st.title("GPT-4 Streamlit App")
    user_input = st.text_input("Enter a prompt:")
    if user_input:
        response = generate_response(user_input)
        st.write("Generated Response:")
        st.write(response)

if __name__ == "__main__":
    main()