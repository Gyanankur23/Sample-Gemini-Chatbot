# 🤖 Gemini Chatbot (Streamlit Edition)

[![Live App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?logo=streamlit&logoColor=white)](https://sample-gemini-chatbot-8vue39zezr6hiea6jjb9t6.streamlit.app/)
[![Source Code](https://img.shields.io/badge/Vercel-Source%20Code-000000?logo=vercel&logoColor=white)](https://github.com/Gyanankur23/Sample-Gemini-Chatbot)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/API-Gemini-4285F4?logo=google&logoColor=white)
![Deployment](https://img.shields.io/badge/Hosted%20On-Streamlit%20Cloud-FF4B4B?logo=streamlit&logoColor=white)



## Overview
This project demonstrates how to build, optimize, and deploy a dynamic, API-integrated web application using the free Gemini API. The chatbot is designed for university students, providing concise, clear, and helpful explanations in a conversational interface. It showcases stateful chat sessions, secure API handling, and a responsive Streamlit UI.

## Live Deployment
- 🌐 [Live App on Streamlit](https://sample-gemini-chatbot-8vue39zezr6hiea6jjb9t6.streamlit.app/)
- 💻 [Source Code on GitHub](https://github.com/Gyanankur23/Sample-Gemini-Chatbot)

## Features
- Secure API key input (no hardcoding).
- Stateful chat session that remembers conversation history.
- Clear conversation button to reset state.
- Responsive Streamlit interface with mobile compatibility.
- Error handling for invalid keys or failed API calls.

## Installation and Usage
Clone the repository:
```bash
git clone https://github.com/Gyanankur23/Sample-Gemini-Chatbot.git
cd Sample-Gemini-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```
Run the app locally

```bash
streamlit run app.py
```
When prompted, enter your Gemini API key securely in the input field.

### Code Example
Below is a snippet showing secure API key handling and Gemini API integration:

```bash
import streamlit as st
import google.generativeai as genai

def setup_chat(api_key: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="You are a helpful assistant."
    )
    return model.start_chat(history=[])

api_key = st.text_input("Enter your Gemini API Key:", type="password")
if api_key:
    chat_session = setup_chat(api_key)
    response = chat_session.send_message("Hello Gemini!")
    st.write(response.text)
```

## Debugging and Optimization
- Verified API integration with `gemini-2.5-flash` model.
- Replaced deprecated `experimental_rerun()` with `st.rerun()`.
- Ensured responsiveness across devices and screen sizes.
- Added user feedback messages for connection success, errors, and resets.

## Cross-Device Testing
The chatbot was tested on:
- Desktop browsers (Chrome, Edge).
- Mobile browsers (Android Chrome).
- Tablet display sizes.
All tests confirmed usability and responsiveness.

## Documentation
The repository includes:
- Project purpose and features.
- API usage and configuration.
- Deployment link.
- Instructions for local setup and usage.
- Screenshots and optional walkthrough video.

## Reflection
This module taught me how to:
- Deploy a frontend web application to a hosting platform.
- Debug deployment issues such as API misconfigurations.
- Optimize for performance, accessibility, and usability across devices.
- Document and present a project professionally for portfolio showcase.
- Reflect on challenges faced and how the chatbot solves a real-world problem.

## Conclusion
Deliverable 6, *Deploying and Showcasing Your Web Application*, demonstrates readiness to build and ship real-world web applications. The Gemini Chatbot is now portfolio-ready, publicly accessible, and fully documented.

```
