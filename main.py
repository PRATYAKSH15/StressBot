# app-1
# import streamlit as st
# from therapy_chain import load_therapy_chain

# def render_chat_ui():
#     st.set_page_config(page_title="Stress Relief Chatbot", page_icon="🧘‍♀️")
#     st.title("Welcome to StressBOT! 👋")

#     st.markdown("""
# ### 🧠 Stress Management & Motivation Chatbot
# I'm your personal stress management companion — here to help you navigate stress, boost emotional well-being, and stay motivated.
# Whether you're feeling overwhelmed, anxious, or just need a mental reset, I'm here to support you.  
                
# Feel free to share what's on your mind, you're not alone. 💬
# """)


#     st.markdown("---")

#     conversation = load_therapy_chain()

#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     user_input = st.chat_input("How are you feeling today?")

#     if user_input:
#         response = conversation.predict(input=user_input)
#         st.session_state.chat_history.append((user_input, response))

#     for user_msg, bot_msg in st.session_state.chat_history:
#         st.chat_message("user").write(user_msg)
#         st.chat_message("assistant").write(bot_msg)
   
# render_chat_ui()

# app-2
# import streamlit as st
# from therapy_chain import load_therapy_chain
# import uuid

# # ────────────────────────────────
# # Session Initialization
# # ────────────────────────────────
# if "chat_sessions" not in st.session_state:
#     st.session_state.chat_sessions = {}  # {chat_id: [(user_msg, bot_msg), ...]}
# if "active_chat_id" not in st.session_state:
#     st.session_state.active_chat_id = None

# # ────────────────────────────────
# # Sidebar UI
# # ────────────────────────────────
# def render_sidebar():
#     st.sidebar.title("💬 Chat Sessions")

#     # New Chat Button
#     if st.sidebar.button("➕ New Chat"):
#         new_id = str(uuid.uuid4())[:8]
#         st.session_state.chat_sessions[new_id] = []
#         st.session_state.active_chat_id = new_id

#     # Search functionality
#     search_query = st.sidebar.text_input("🔍 Search chats")

#     filtered_chats = {
#         cid: history for cid, history in st.session_state.chat_sessions.items()
#         if any(search_query.lower() in msg[0].lower() or search_query.lower() in msg[1].lower()
#                for msg in history)
#     } if search_query else st.session_state.chat_sessions

#     if filtered_chats:
#         selected_chat = st.sidebar.selectbox(
#             "📂 Select chat",
#             options=list(filtered_chats.keys()),
#             format_func=lambda cid: f"Chat {cid}"
#         )
#         st.session_state.active_chat_id = selected_chat
#     else:
#         st.sidebar.info("No chats yet or no matches.")

# # ────────────────────────────────
# # Main Chat UI
# # ────────────────────────────────
# def render_chat_ui():
#     st.set_page_config(page_title="Stress Relief Chatbot", page_icon="🧘‍♀️")
#     st.title("Welcome to StressBOT! 👋")

#     st.markdown("""
# ### 🧠 Stress Management & Motivation Chatbot
# I'm your personal stress management companion — here to help you navigate stress, boost emotional well-being, and stay motivated.
# Whether you're feeling overwhelmed, anxious, or just need a mental reset, I'm here to support you.  
                
# Feel free to share what's on your mind, you're not alone. 💬
# """)

#     st.markdown("---")

#     render_sidebar()

#     if st.session_state.active_chat_id is None:
#         st.info("Start a new chat from the sidebar ➕")
#         return

#     conversation = load_therapy_chain()
#     chat_id = st.session_state.active_chat_id
#     chat_history = st.session_state.chat_sessions[chat_id]

#     # Show previous messages
#     for user_msg, bot_msg in chat_history:
#         st.chat_message("user").write(user_msg)
#         st.chat_message("assistant").write(bot_msg)

#     # Input and response
#     user_input = st.chat_input("How are you feeling today?")

#     if user_input:
#         response = conversation.predict(input=user_input)
#         chat_history.append((user_input, response))
#         st.chat_message("user").write(user_input)
#         st.chat_message("assistant").write(response)

# render_chat_ui()

# app-3
# import streamlit as st
# from therapy_chain import load_therapy_chain
# import uuid

# # ────────────────────────────────
# # Session Initialization
# # ────────────────────────────────
# if "chat_sessions" not in st.session_state:
#     st.session_state.chat_sessions = {}  # {chat_id: [(user_msg, bot_msg), ...]}
# if "chat_titles" not in st.session_state:
#     st.session_state.chat_titles = {}    # {chat_id: "Custom Title"}
# if "active_chat_id" not in st.session_state:
#     st.session_state.active_chat_id = None

# # ────────────────────────────────
# # Sidebar UI
# # ────────────────────────────────
# def render_sidebar():
#     st.sidebar.title("💬 Chat Sessions")

#     # ➕ New Chat
#     if st.sidebar.button("➕ New Chat"):
#         new_id = str(uuid.uuid4())[:8]
#         st.session_state.chat_sessions[new_id] = []
#         st.session_state.chat_titles[new_id] = f"Chat {new_id}"
#         st.session_state.active_chat_id = new_id

#     # 🔍 Search
#     search_query = st.sidebar.text_input("🔍 Search chats")

#     filtered = {
#         cid: msgs for cid, msgs in st.session_state.chat_sessions.items()
#         if any(search_query.lower() in msg[0].lower() or search_query.lower() in msg[1].lower()
#                for msg in msgs)
#     } if search_query else st.session_state.chat_sessions

#     if filtered:
#         selected_chat = st.sidebar.selectbox(
#             "📂 Select chat",
#             options=list(filtered.keys()),
#             format_func=lambda cid: st.session_state.chat_titles.get(cid, f"Chat {cid}")
#         )
#         st.session_state.active_chat_id = selected_chat

#         # ✏️ Rename selected chat
#         current_title = st.session_state.chat_titles.get(selected_chat, f"Chat {selected_chat}")
#         new_title = st.sidebar.text_input("✏️ Rename chat", value=current_title, key=f"rename_{selected_chat}")
#         if new_title.strip():
#             st.session_state.chat_titles[selected_chat] = new_title.strip()
#     else:
#         st.sidebar.info("No chats yet or no matches found.")

# # ────────────────────────────────
# # Main Chat UI
# # ────────────────────────────────
# def render_chat_ui():
#     st.set_page_config(page_title="Stress Relief Chatbot", page_icon="🧘‍♀️")
#     st.title("Welcome to StressBOT! 👋")

#     st.markdown("""
# ### 🧠 Stress Management & Motivation Chatbot
# I'm your personal stress management companion — here to help you navigate stress, boost emotional well-being, and stay motivated.
# Whether you're feeling overwhelmed, anxious, or just need a mental reset, I'm here to support you.  
                
# Feel free to share what's on your mind, you're not alone. 💬
# """)

#     st.markdown("---")

#     render_sidebar()

#     if st.session_state.active_chat_id is None:
#         st.info("Start a new chat from the sidebar ➕")
#         return

#     conversation = load_therapy_chain()
#     chat_id = st.session_state.active_chat_id
#     chat_history = st.session_state.chat_sessions[chat_id]

#     # Show previous messages
#     for user_msg, bot_msg in chat_history:
#         st.chat_message("user").write(user_msg)
#         st.chat_message("assistant").write(bot_msg)

#     # Input and response
#     user_input = st.chat_input("How are you feeling today?")
#     if user_input:
#         response = conversation.predict(input=user_input)
#         chat_history.append((user_input, response))
#         st.chat_message("user").write(user_input)
#         st.chat_message("assistant").write(response)

# render_chat_ui()


import streamlit as st
from therapy_chain import load_therapy_chain
import uuid

# ──────────────── Session Initialization ────────────────
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}
if "chat_titles" not in st.session_state:
    st.session_state.chat_titles = {}
if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = None

# ──────────────── Sidebar with Rename ────────────────
def render_sidebar():
    st.sidebar.title("💬 My Chats")

    if st.sidebar.button("➕ New Chat"):
        new_id = str(uuid.uuid4())[:8]
        st.session_state.chat_sessions[new_id] = []
        st.session_state.chat_titles[new_id] = f"Chat {new_id}"
        st.session_state.active_chat_id = new_id

    st.sidebar.markdown("---")

    for cid, msgs in st.session_state.chat_sessions.items():
        title = st.session_state.chat_titles.get(cid, f"Chat {cid}")

        with st.sidebar.expander(f"💬 {title}", expanded=False):
            # Select this chat
            if st.button(f"🔁 Switch to this", key=f"switch_{cid}"):
                st.session_state.active_chat_id = cid

            # Rename field
            new_title = st.text_input("✏️ Rename", value=title, key=f"rename_{cid}")
            if new_title.strip():
                st.session_state.chat_titles[cid] = new_title.strip()

# ──────────────── Main Chat UI ────────────────
def render_chat_ui():
    st.set_page_config(page_title="Stress Relief Chatbot", page_icon="🧘‍♀️")
    st.title("Welcome to StressBOT! 👋")

    st.markdown("""
### Stress Management & Motivation Chatbot 🧠 
I'm your personal stress management companion — here to help you navigate stress, boost emotional well-being, and stay motivated.
Whether you're feeling overwhelmed, anxious, or just need a mental reset, I'm here to support you.  
Feel free to share what's on your mind. 💬
""")

    st.markdown("---")
    render_sidebar()

    if not st.session_state.active_chat_id:
        st.info("Start a chat from the sidebar ➕")
        return

    conversation = load_therapy_chain()
    cid = st.session_state.active_chat_id
    chat_history = st.session_state.chat_sessions[cid]

    for user_msg, bot_msg in chat_history:
        st.chat_message("user").write(user_msg)
        st.chat_message("assistant").write(bot_msg)

    user_input = st.chat_input("How are you feeling today?")
    if user_input:
        response = conversation.predict(input=user_input)
        chat_history.append((user_input, response))
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(response)

render_chat_ui()
