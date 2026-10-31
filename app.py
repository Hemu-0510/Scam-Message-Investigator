
import streamlit as st
import requests

st.set_page_config(
    page_title="Scam Message Investigator",
    page_icon="🔍"
)

st.title("🔍 Scam Message Investigator")
st.write("Analyze suspicious messages using AI.")

message = st.text_area(
    "Enter the message you want to investigate:",
    placeholder="Paste your suspicious SMS, email or WhatsApp message here..."
)

if st.button("Investigate Message"):
    if message.strip():

        with st.spinner("Investigating message..."):

            prompt = f"""
            Analyze the following message for possible scams.

            Message: {message}

            Provide:
            1. Risk Level (High, Medium or Low)
            2. Warning Signs
            3. Explanation
            4. Safety Recommendations

            Be clear and simple.
            """

            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "gemma3:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=180
                )

                response.raise_for_status()
                result = response.json()["response"]

                st.subheader("Investigation Report")
                st.write(result)

            except requests.exceptions.RequestException:
                st.error("Unable to connect to Ollama. Please check whether it is running.")

    else:
        st.warning("Please enter a message first.")
