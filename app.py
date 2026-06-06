import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from rag import get_context

# Load environment variables
load_dotenv()

# OpenRouter API Key
api_key = os.getenv("OPENROUTER_API_KEY")

# Page Configuration
st.set_page_config(
    page_title="Ganesh AI Representative",
    page_icon="🤖",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stChatMessage {
    border-radius: 12px;
}

.block-container {
    max-width: 1100px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("👨‍💻 Ganesh Navre")

    st.link_button(
        "📅 Schedule Interview",
        "https://cal.com/ganesh-navre-1earaq/30min"
    )

    st.markdown("---")

    st.markdown("""
### Contact

📧 ganeshnavre1@gmail.com

📞 +91 9579225968

### About

AI Engineer focused on:
- Generative AI
- LLM Applications
- RAG Systems
- Machine Learning
- Data Analytics
""")

# Main Header
st.title("🤖 Ganesh AI Representative")

st.markdown("""
Welcome!

I can answer questions about Ganesh's:

- Education
- Technical Skills
- AI & Machine Learning Projects
- Experience
- Career Background
- AI Engineer Role Fit

You can also schedule an interview directly through the booking link.
""")

# Validate API Key
if not api_key:
    st.error("OPENROUTER_API_KEY not found.")
    st.stop()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# User Input
question = st.chat_input("Ask a question about Ganesh")

if question:

    with st.chat_message("user"):
        st.write(question)

    # Interview Scheduling Keywords
    booking_keywords = [
        "interview",
        "schedule",
        "book",
        "availability",
        "meeting"
    ]

    # Handle Scheduling Requests
    if any(keyword in question.lower() for keyword in booking_keywords):

        with st.chat_message("assistant"):
            st.markdown("""
### 📅 Interview Scheduling

You can schedule an interview with Ganesh using the booking link below:

**Booking Link:**  
https://cal.com/ganesh-navre-1earaq/30min

Please choose an available slot and complete the booking process.

Once booked, the meeting will automatically be added to Ganesh's calendar.
""")

    else:

        try:
            # Retrieve Relevant Context
            context = get_context(question)

            prompt = f"""
You are Ganesh Navre's AI representative.

Instructions:
- Answer only using the provided context.
- Do not invent information.
- If information is unavailable, respond:
  "I don't have enough information to answer that."
- Keep responses professional and concise.

Context:
{context}

Question:
{question}
"""

            # OpenRouter Request
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
                max_tokens=500
            )

            answer = response.choices[0].message.content

            with st.chat_message("assistant"):
                st.write(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")