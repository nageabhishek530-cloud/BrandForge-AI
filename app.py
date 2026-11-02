
import streamlit as st
import ollama
import uuid
from chat_storage import load_all_chats, save_chat, load_chat, delete_chat

st.set_page_config(
    page_title="BrandForge AI",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
<style>

/* Main application background */
.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #15112b 50%, #1b1538 100%);
    color: #f5f3ff;
}

/* Main content area */
.main .block-container {
    padding-top: 2.5rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* Headings */
h1 {
    color: #ffffff !important;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Subtitle and normal text */
.stApp p {
    color: #c4bce0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111027 0%, #191431 100%);
    border-right: 1px solid #30264f;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] p {
    color: #bcb3d9 !important;
}

/* Sidebar divider */
section[data-testid="stSidebar"] hr {
    border-color: #393052;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: linear-gradient(135deg, #1c1b32, #25203e);
    border: 1px solid #38305c;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.18);
}

/* Chat message text */
[data-testid="stChatMessage"] p {
    color: #eeeaff !important;
    line-height: 1.7;
}

/* Chat input */
[data-testid="stChatInput"] {
    border: 1px solid #8055ff;
    border-radius: 16px;
    background: #1c1930;
    box-shadow: 0 0 15px rgba(128, 85, 255, 0.12);
}

/* Chat input focus */
[data-testid="stChatInput"]:focus-within {
    border-color: #a78bfa;
    box-shadow: 0 0 18px rgba(167, 139, 250, 0.25);
}

/* Input text */
[data-testid="stChatInput"] textarea {
    color: #ffffff !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #7048e8, #9b5de5);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1rem;
    font-weight: 600;
    transition: all 0.25s ease;
}

/* Button hover */
.stButton > button:hover {
    background: linear-gradient(135deg, #8055ff, #b06cff);
    color: #ffffff;
    border: none;
    box-shadow: 0 5px 18px rgba(128, 85, 255, 0.35);
    transform: translateY(-2px);
}

/* Spinner */
.stSpinner > div {
    border-top-color: #a78bfa !important;
}

/* Links */
.stApp a {
    color: #b69cff;
}

/* Selection color */
::selection {
    background: #8055ff;
    color: #ffffff;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #111027;
}

::-webkit-scrollbar-thumb {
    background: #514078;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #8055ff;
}

/* Footer */
footer {
    visibility: hidden;
}

/* Streamlit header */
header[data-testid="stHeader"] {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)


st.title("🎨 BrandForge AI")
st.subheader("Your AI-powered branding studio")
st.write("Build your brand identity, one idea at a time.")


# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = None


# Load all saved conversations
saved_chats = load_all_chats()


# Sidebar
with st.sidebar:

    st.markdown("## 🎨 BrandForge AI")
    st.caption("Your Personal AI Branding Studio")

    st.divider()

    st.markdown("### Create")

    # New conversation button
    if st.button("＋ New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.active_chat_id = None
        st.rerun()

    st.divider()

    # Chat History
    st.markdown("### 💬 Chat History")

    if saved_chats:

        # Show newest conversations first
        sorted_chats = sorted(
            saved_chats.items(),
            key=lambda item: item[1].get("updated_at", ""),
            reverse=True
        )

        for chat_id, chat_data in sorted_chats:

            chat_title = chat_data.get("title", "New Conversation")

            # Keep sidebar titles short
            display_title = (
                chat_title[:30] + "..."
                if len(chat_title) > 30
                else chat_title
            )

            col1, col2 = st.columns([0.80, 0.20])

            # Open conversation
            with col1:

                if st.button(
                    display_title,
                    key=f"open_{chat_id}",
                    use_container_width=True
                ):
                    selected_chat = load_chat(chat_id)

                    if selected_chat:
                        st.session_state.messages = selected_chat.get(
                            "messages", []
                        )
                        st.session_state.active_chat_id = chat_id

                    st.rerun()

            # Delete conversation
            with col2:

                if st.button(
                    "🗑️",
                    key=f"delete_{chat_id}",
                    help="Delete this conversation",
                    use_container_width=True
                ):

                    delete_chat(chat_id)

                    # Clear active conversation if it was deleted
                    if st.session_state.active_chat_id == chat_id:
                        st.session_state.messages = []
                        st.session_state.active_chat_id = None

                    st.rerun()

    else:
        st.caption("No saved conversations yet.")

    st.divider()

    st.markdown("### Branding Tools")

    st.markdown("""
    ✨ Brand Name Generator

    🏷️ Tagline Creator

    🎨 Colour Palette

    📱 Social Media Content

    🚀 Launch Strategy
    """)

    st.divider()

    st.caption("Powered by Llama 3.2 · Ollama")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Accept user input
if prompt := st.chat_input("Describe your brand idea..."):

    # Create a new chat ID if this is a new conversation
    if st.session_state.active_chat_id is None:
        st.session_state.active_chat_id = str(uuid.uuid4())

    chat_id = st.session_state.active_chat_id

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("BrandForge AI is thinking..."):

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are BrandForge AI, a professional branding assistant. Help users create brand names, taglines, brand identities, colour palettes, social media content, and marketing strategies. Give creative, practical, and well-organized answers."
                    },
                    *st.session_state.messages
                ]
            )

            answer = response["message"]["content"]

            st.write(answer)

    # Add assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Generate conversation title from first user message
    chat_title = next(
        (
            message["content"]
            for message in st.session_state.messages
            if message["role"] == "user"
        ),
        "New Conversation"
    )

    # Save conversation
    save_chat(
        chat_id,
        chat_title,
        st.session_state.messages
    )

    st.rerun()
