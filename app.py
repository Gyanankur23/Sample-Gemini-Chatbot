# =============================================================================
# PROJECT 1: Streamlit Chatbot
# Workshop: Building with the Free Gemini API
# =============================================================================
# WHAT THIS PROJECT TEACHES:
#   1. How to connect to the Gemini API using an API key
#   2. How to start a ChatSession that remembers conversation history
#   3. How statefulness works — the model "remembers" earlier messages
#   4. How to build a simple Streamlit chatbot interface
#
# HOW TO RUN:
#   1. pip install -r requirements.txt
#   2. streamlit run chatbot_streamlit.py
# =============================================================================

import streamlit as st
import google.generativeai as genai

# =============================================================================
# SECTION 1: CONFIGURATION
# =============================================================================

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_PROMPT = """
You are a friendly and helpful assistant for university students.
You explain concepts clearly, in simple language, with examples where possible.
Keep your responses concise — no longer than a short paragraph unless asked.
If you don't know something, say so honestly.
"""

# =============================================================================
# SECTION 2: SETUP FUNCTION
# =============================================================================

def setup_chat(api_key: str):
    """Configures the Gemini API and returns a ready-to-use ChatSession."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=SYSTEM_PROMPT,
    )
    chat_session = model.start_chat(history=[])
    return chat_session

# =============================================================================
# SECTION 3: STREAMLIT APP
# =============================================================================

def main():
    st.title("🤖 Gemini Chatbot (Streamlit Edition)")
    st.write("Welcome! Chat with Gemini below. Your conversation history is saved during the session.")

    # --- API Key Input ---
    api_key = st.text_input("🔑 Enter your Gemini API Key:", type="password")

    if not api_key:
        st.warning("Please enter your API key to start chatting.")
        return

    # --- Initialize Chat Session ---
    if "chat_session" not in st.session_state:
        try:
            st.session_state.chat_session = setup_chat(api_key)
            st.success("✅ Connected to Gemini!")
        except Exception as e:
            st.error(f"❌ Failed to connect: {e}")
            return

    chat_session = st.session_state.chat_session

    # --- Display Conversation ---
    for i, message in enumerate(chat_session.history):
        role = "🧑 You" if message.role == "user" else "🤖 Bot"
        content = " ".join(part.text for part in message.parts)
        st.markdown(f"**{role}:** {content}")

    # --- User Input ---
    user_input = st.chat_input("Type your message here...")

    if user_input:
        try:
            response = chat_session.send_message(user_input)
            st.experimental_rerun()  # Refresh to show updated history
        except Exception as e:
            st.error(f"❌ Error: {e}")

    # --- Clear Conversation ---
    if st.button("🔄 Clear Conversation"):
        st.session_state.chat_session = setup_chat(api_key)
        st.info("Conversation cleared. Start fresh!")

# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
