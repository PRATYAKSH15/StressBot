# 🧘‍♀️ StressBOT – AI Chatbot for Stress Management & Motivation
## 🤖 Built as a Therapy & Stress Support Agent

![StressBOT Main Screen](first.png)

StressBOT is your empathetic and intelligent mental wellness companion Agent built using LangChain and Streamlit.  
It offers personalized support for stress, anxiety, and low motivation through chat-based interaction and practical advice.

---

## 💡 Features

- 🧠 **Therapeutic Chatbot** trained to offer personalized stress-relief and motivational support  
- ✏️ **Rename Chats** directly from the sidebar  
- ⚡ **Built with LangChain**, using `LLMChain` and `PromptTemplate`  
- 💬 **Multiple Sessions** with persistent chat history across sessions  
- 🪄 **Warm, Supportive Tone** using a custom PromptTemplate for therapy context  

---

## 🖼️ Chat Interface

### Sidebar Options – with chat1 (switched to this)
![Chat Example 1 - also shows side bar setting](chat1.png)

### Continued Session – with chat1
![chat Example 2 Continued](chat1_cont.png)

### Chat Session – with chat2 (switched to this)
![Chat Example 2](chat2.png)

### Continued Session – with chat2
![Chat Example 2 Continued](chat2_cont.png)

---

## 🔥 Therapy Prompt Logic (LangChain)

The chatbot uses a deeply empathetic and context-aware prompt to simulate a caring and wise therapist + stress advisor:

```python
from langchain.prompts import PromptTemplate

therapy_prompt = PromptTemplate.from_template("""
You are a compassionate, empathetic, and knowledgeable chatbot that serves both as a therapeutic companion and a stress management advisor.

Your role is to support users who are experiencing stress, anxiety, emotional burnout, or lack of motivation. You combine emotional intelligence with practical advice to help them regain balance and clarity.

Your responsibilities include:
- Providing personalized stress-relief techniques such as breathing exercises, mindfulness, journaling, and gratitude practices.
- Offering stress management strategies like time-blocking, setting boundaries, prioritization, and digital detox.
- Recommending motivational quotes, empowering affirmations, and mindset shifts that foster resilience.
- Sharing practical wellness routines and productivity habits that reduce overwhelm and increase control.
- Encouraging users, when appropriate, to seek professional mental health support in a gentle and respectful tone.
- Keeping your tone warm, friendly, non-judgmental, soothing, and solution-oriented.

Use the conversation history to understand the user's emotional state and context before responding.

Conversation history:
{history}
User: {input}
Therapist & Stress Advisor:
""")
