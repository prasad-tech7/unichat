import streamlit as st
from dotenv import load_dotenv
import os
from src.provider_manager import ProviderManager, PROVIDERS
from src.session_manager import SessionManager

load_dotenv()

st.set_page_config(
    page_title="UniChat — One Chat, All AI Models",
    page_icon="🤖",
    layout="wide"
)

# ─── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Root Variables ── */
:root {
    --accent: #7C6FF7;
    --accent-light: #EEE9FF;
    --accent-glow: rgba(124, 111, 247, 0.18);
    --surface: #FFFFFF;
    --surface-alt: #F7F6FF;
    --border: rgba(124, 111, 247, 0.15);
    --text-primary: #1A1535;
    --text-muted: #8A84A3;
    --success: #10B981;
    --warning: #F59E0B;
    --radius: 16px;
    --shadow: 0 4px 24px rgba(124,111,247,0.10);
}

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #F3F1FF !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 900px !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #1A1535 0%, #2D2260 100%) !important;
    border-right: none !important;
}
[data-testid="stSidebar"] * {
    color: #E8E4FF !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSubheader {
    color: #A89EEF !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 22px !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    letter-spacing: -0.02em !important;
    margin-bottom: 2px !important;
}
[data-testid="stSidebar"] [data-testid="stCaption"] {
    color: #7C6FF7 !important;
    font-size: 12px !important;
}
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.08) !important;
    margin: 12px 0 !important;
}

/* ── Sidebar selectbox ── */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: #FFFFFF !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div:hover {
    border-color: rgba(124,111,247,0.6) !important;
    background: rgba(124,111,247,0.15) !important;
}

/* ── Sidebar info box ── */
[data-testid="stSidebar"] [data-testid="stInfo"] {
    background: rgba(124,111,247,0.15) !important;
    border: 1px solid rgba(124,111,247,0.3) !important;
    border-radius: 12px !important;
    color: #E8E4FF !important;
}
[data-testid="stSidebar"] [data-testid="stSuccess"] {
    background: rgba(16,185,129,0.12) !important;
    border: 1px solid rgba(16,185,129,0.25) !important;
    border-radius: 10px !important;
    color: #6EE7B7 !important;
}

/* ── Sidebar metrics ── */
[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 24px !important;
    color: #FFFFFF !important;
}
[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
    color: #A89EEF !important;
    font-size: 12px !important;
}

/* ── Sidebar button ── */
[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #C4BCFF !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(220,60,60,0.15) !important;
    border-color: rgba(220,60,60,0.4) !important;
    color: #FF9999 !important;
}

/* ── Main title ── */
.main .stMarkdown h1,
.main h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 32px !important;
    font-weight: 800 !important;
    color: #1A1535 !important;
    letter-spacing: -0.03em !important;
    margin-bottom: 0 !important;
}
[data-testid="stCaption"] {
    color: var(--text-muted) !important;
    font-size: 14px !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 16px 20px !important;
    box-shadow: 0 2px 12px rgba(124,111,247,0.06) !important;
    margin-bottom: 12px !important;
}
[data-testid="stChatMessage"][data-testid*="user"] {
    background: linear-gradient(135deg, #1A1535 0%, #2D2260 100%) !important;
    border-color: transparent !important;
}
[data-testid="stChatMessage"][data-testid*="user"] p,
[data-testid="stChatMessage"][data-testid*="user"] .stMarkdown {
    color: #FFFFFF !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
    background: var(--surface) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 20px !important;
    box-shadow: 0 4px 24px rgba(124,111,247,0.12) !important;
    padding: 4px 8px !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 4px 32px rgba(124,111,247,0.22) !important;
}
[data-testid="stChatInput"] textarea {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    color: var(--text-primary) !important;
}
[data-testid="stChatInput"] button {
    background: var(--accent) !important;
    border-radius: 12px !important;
    color: white !important;
}

/* ── Alert / info / warning / error ── */
[data-testid="stAlert"] {
    border-radius: 14px !important;
    border: none !important;
    font-size: 14px !important;
}
[data-testid="stInfo"] {
    background: #EEE9FF !important;
    border-left: 4px solid var(--accent) !important;
    color: var(--text-primary) !important;
}
[data-testid="stSuccess"] {
    background: #ECFDF5 !important;
    border-left: 4px solid var(--success) !important;
    color: #065F46 !important;
}
[data-testid="stWarning"] {
    background: #FFFBEB !important;
    border-left: 4px solid var(--warning) !important;
    color: #92400E !important;
}
[data-testid="stError"] {
    background: #FFF1F2 !important;
    border-left: 4px solid #F43F5E !important;
    color: #9F1239 !important;
}

/* ── Toast ── */
[data-testid="stToast"] {
    background: #1A1535 !important;
    color: white !important;
    border-radius: 14px !important;
    box-shadow: 0 8px 32px rgba(26,21,53,0.35) !important;
    border: 1px solid rgba(124,111,247,0.3) !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] > div {
    border-top-color: var(--accent) !important;
}

/* ── Welcome card ── */
.welcome-card {
    background: linear-gradient(135deg, #1A1535 0%, #2D2260 60%, #3D2080 100%);
    border-radius: 20px;
    padding: 36px 40px;
    color: white;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.welcome-card::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(124,111,247,0.35) 0%, transparent 70%);
    border-radius: 50%;
}
.welcome-card::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 40px;
    width: 140px; height: 140px;
    background: radial-gradient(circle, rgba(168,158,239,0.2) 0%, transparent 70%);
    border-radius: 50%;
}
.welcome-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
    position: relative;
    z-index: 1;
}
.welcome-card p {
    font-size: 15px;
    color: rgba(255,255,255,0.75);
    line-height: 1.6;
    position: relative;
    z-index: 1;
    margin-bottom: 20px;
}
.provider-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 50px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 500;
    margin: 4px 4px 4px 0;
    backdrop-filter: blur(4px);
}
.tip-badge {
    display: inline-block;
    background: rgba(124,111,247,0.3);
    border: 1px solid rgba(124,111,247,0.5);
    color: #D4CFFF;
    border-radius: 50px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ─── Initialize session state ─────────────────────────────────
if "session" not in st.session_state:
    st.session_state.session = SessionManager()

if "manager" not in st.session_state:
    manager = ProviderManager()
    provider_keys = {
        "Groq (LLaMA)": os.getenv("GROQ_API_KEY"),
        "Google Gemini": os.getenv("GEMINI_API_KEY"),
        "Mistral": os.getenv("MISTRAL_API_KEY"),
        "Cohere": os.getenv("COHERE_API_KEY"),
    }
    for provider_name, api_key in provider_keys.items():
        if api_key:
            manager.initialize_provider(provider_name, api_key)
    st.session_state.manager = manager

if "current_provider" not in st.session_state:
    st.session_state.current_provider = None

# ─── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.title("✦ UniChat")
    st.caption("One chat · All AI models")
    st.divider()

    st.subheader("Select Model")
    initialized = st.session_state.manager.get_initialized_providers()

    if not initialized:
        st.error("No providers configured. Contact admin.")
    else:
        selected = st.selectbox(
            "Active AI provider",
            options=initialized,
            format_func=lambda x: f"{PROVIDERS[x]['icon']}  {x}",
            key="provider_select",
            label_visibility="collapsed"
        )

        if selected != st.session_state.current_provider:
            old_provider = st.session_state.current_provider
            st.session_state.manager.switch_provider(selected)
            if old_provider and old_provider != selected:
                st.session_state.session.record_switch(old_provider, selected)
                st.toast(f"Switched to {selected} ✦", icon="🔄")
            st.session_state.current_provider = selected

        if st.session_state.current_provider:
            info = PROVIDERS[st.session_state.current_provider]
            st.info(
                f"{info['icon']} **{st.session_state.current_provider}**\n\n"
                f"{info['description']}"
            )

    st.divider()
    st.subheader("Available Models")
    for provider_name in initialized:
        info = PROVIDERS[provider_name]
        st.success(f"{info['icon']}  {provider_name}")

    st.divider()
    st.subheader("Session Stats")
    session = st.session_state.session
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len(session.messages))
    with col2:
        st.metric("Switches", len(session.provider_switches))

    if session.provider_switches:
        st.markdown("**Recent switches**")
        for switch in session.provider_switches[-3:]:
            st.caption(f"↪ {switch['from']} → {switch['to']}")

    st.divider()
    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.session.clear()
        st.rerun()

# ─── Main Chat Area ───────────────────────────────────────────
st.title("✦ UniChat")
st.caption("Switch AI providers anytime — your conversation never stops")

session = st.session_state.session

# ── Provider switch banner ──
if session.provider_switches:
    last_switch = session.provider_switches[-1]
    if last_switch["message_index"] >= len(session.messages) - 2:
        st.success(
            f"🔄 Switched from **{last_switch['from']}** to **{last_switch['to']}** — history preserved ✅"
        )

# ── Welcome screen ──
if session.is_empty():
    providers_html = "".join([
        f'<span class="provider-pill">{PROVIDERS[p]["icon"]} {p}</span>'
        for p in initialized
    ])
    st.markdown(f"""
<div class="welcome-card">
    <span class="tip-badge">✦ Welcome</span>
    <h3>Never lose your conversation again.</h3>
    <p>UniChat lets you switch between AI providers mid-conversation.<br>
    Hit a rate limit? Just switch — your full history comes along.</p>
    <div style="margin-bottom: 12px;">{providers_html}</div>
    <p style="font-size:13px; color: rgba(255,255,255,0.5); margin:0;">
        💡 Tip: Select a provider in the sidebar, then start chatting below.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Display messages ──
for msg in session.get_display_messages():
    role = msg["role"]
    content = msg["content"]
    provider = msg.get("provider")
    timestamp = msg.get("timestamp", "")

    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
            st.caption(f"🕐 {timestamp}")
    elif role == "assistant":
        with st.chat_message("assistant"):
            st.markdown(content)
            if provider:
                info = PROVIDERS.get(provider, {})
                icon = info.get("icon", "🤖")
                st.caption(f"{icon} **{provider}** · {timestamp}")

# ── Chat input ──
user_input = st.chat_input("Ask anything...")

if user_input:
    if not st.session_state.manager.is_ready():
        st.error("Please select a provider from the sidebar.")
        st.stop()

    session.add_user_message(user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        provider_info = PROVIDERS[st.session_state.current_provider]
        with st.spinner(
            f"{provider_info['icon']} {st.session_state.current_provider} is thinking..."
        ):
            try:
                response = st.session_state.manager.chat(
                    session.get_messages_for_api()
                )
                st.markdown(response)

                provider = st.session_state.current_provider
                info = PROVIDERS.get(provider, {})
                icon = info.get("icon", "🤖")
                st.caption(f"{icon} **{provider}**")

                session.add_assistant_message(response, st.session_state.current_provider)

            except Exception as e:
                error = str(e)
                if "LIMIT_EXCEEDED" in error:
                    current = st.session_state.current_provider
                    others = [p for p in initialized if p != current]
                    st.warning(
                        f"⚠️ **{current} free limit reached!**\n\n"
                        f"Switch to another model in the sidebar:\n"
                        + "\n".join([f"- {PROVIDERS[p]['icon']} **{p}**" for p in others])
                        + "\n\n✅ Your chat history will be preserved!"
                    )
                else:
                    st.error(f"❌ {error}")

    st.rerun()