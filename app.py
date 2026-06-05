import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

from rag import get_context

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="Ganesh AI Representative")

st.title("Ganesh AI Representative")
st.write("Ask questions about Ganesh's skills, projects and experience.")

if not api_key:
    st.error("OPENROUTER_API_KEY not found in .env file")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

question = st.chat_input("Ask a question about Ganesh")

if question:

    with st.chat_message("user"):
        st.write(question)

    # Interview booking check
    booking_keywords = [
        "interview",
        "schedule",
        "book",
        "availability",
        "meeting"
    ]

    if any(keyword in question.lower() for keyword in booking_keywords):

        with st.chat_message("assistant"):
            st.write("""
You can schedule an interview with Ganesh using the booking link below:

https://cal.com/ganesh-navre-1earaq/30min

Please select an available time slot and complete the booking process.

Once booked, the meeting will automatically be added to Ganesh's calendar.
""")

    else:

        try:
            context = get_context(question)

            prompt = f"""
You are Ganesh Navre's AI representative.

Rules:
- Answer only from the provided context.
- Do not make up information.
- If information is not available, say:
  "I don't have enough information to answer that."
- Be professional and concise.

Context:
{context}

Question:
{question}
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b:free",
                messages=[
                    {
                        "role": "system",
                        "content": "You are Ganesh Navre's AI representative."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=400
            )

            answer = response.choices[0].message.content

            with st.chat_message("assistant"):
                st.write(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("API Key Loaded:", bool(api_key))