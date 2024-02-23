import openai
import streamlit as st

st.title("majik_Ruiz")

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

messages = [
    {"role": "system", "content": "Sarcastic yet efficient AI assistant."},
]

while True:
    user_message = st.text_input("User:")
    if user_message: 
        messages.append(
            {"role": "user", "content": user_message},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-4-1106-preview", messages = messages
        )

        reply = chat.choices[0].message.content

        st.text_area("ChatGPT:", value=reply, height=200)
        messages.append({"role": "assistant", "content": reply})
