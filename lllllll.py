# app.py

import streamlit as st
import os
from openai import OpenAI

# 💡 Set your OpenAI API key in environment variable before running:
# For Windows CMD: set OPENAI_API_KEY=your-key
# For PowerShell:   $env:OPENAI_API_KEY="your-key"
# For macOS/Linux:  export OPENAI_API_KEY=your-key

# Get the API key from the environment
api_key = os.getenv("sk-proj-vdczPi_7KsfTWCPffbafmg_lOxqoExgq8neWzPv71kUT44Mllf4ccU9RQ3k0ONmUP29xuDfrAMT3BlbkFJDxUEdkhvE5Btf6V-ixSOIg2Dsre_XvG9o9GpkL6v8evdcx2HbYCkm8NP2UdV3tmW9pmjUw_dAAs")
# Stop the app if the key is not set
if not api_key:
    st.error("⚠️ OPENAI_API_KEY environment variable is not set.")
    st.stop()

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("💊 Medicine Similarity Finder")
st.write("Enter a medicine name, and I'll suggest similar medicines (generic or brand alternatives).")

# Input field
medicine_name = st.text_input("Enter a medicine name:")

# Button to trigger the LLM call
if st.button("Find Similar Medicines"):
    if not medicine_name.strip():
        st.warning("Please enter a valid medicine name.")
    else:
        with st.spinner("💬 Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful medical assistant who suggests similar medicines (brand and generic)."
                        },
                        {
                            "role": "user",
                            "content": f"List medicines similar to '{medicine_name}'. Include generic alternatives, brand names, and similar compounds."
                        }
                    ],
                    temperature=0.7,
                    max_tokens=300
                )

                # Extract and display result
                result = response.choices[0].message.content
                st.markdown("### 💊 Similar Medicines")
                st.write(result)

            except Exception as e:
                st.error(f"❌ Error from OpenAI API: {e}")
