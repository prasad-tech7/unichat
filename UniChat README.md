# 🤖 UniChat — One Chat, All AI Models

> **A multi-provider AI chat application that lets you switch between AI providers mid-conversation without losing your chat history.**

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-HuggingFace-yellow?style=for-the-badge)](https://huggingface.co/spaces/komaraprasad/unichat)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/Deployed-Hugging%20Face-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/)

---

## 🌐 Live Demo

🚀 **Try UniChat Live:**

**https://huggingface.co/spaces/komaraprasad/unichat**

Switch between AI providers and continue the same conversation without losing context.

---

# 🎯 Problem

Modern AI platforms often provide free access with usage limits.

Users frequently encounter errors such as:

- ❌ "You've exceeded your free limit"
- ❌ "Quota exceeded for today"
- ❌ "Too many requests"
- ❌ Losing conversation context when changing providers

Switching to another AI provider usually means starting a **new conversation from scratch**.

### 💡 UniChat solves this problem.

With UniChat, users can:

- Chat with multiple AI providers from one interface
- Switch providers at any time
- Preserve the complete conversation history
- Continue the conversation seamlessly
- Track provider switches and session statistics

---

# ✨ Features

| Feature | Description |
|---|---|
| 💬 **Conversational AI** | ChatGPT-style interface for natural conversations |
| 🔄 **Provider Switching** | Switch between multiple AI providers during a conversation |
| 💾 **History Preserved** | Complete conversation history is maintained |
| ⚡ **Multiple Free Models** | Groq, Gemini, Mistral and Cohere |
| 📊 **Session Statistics** | Track messages and provider switches |
| 🎨 **Premium UI** | Custom dark sidebar with purple design system |
| 🔒 **Secure API Keys** | API keys stored as Hugging Face Secrets |
| 🌐 **Cloud Deployment** | Deployed on Hugging Face Spaces |

---

# 🤖 Supported AI Providers

UniChat currently supports four AI providers:

| Provider | Model | Speed | Free Tier |
|---|---|---|---|
| ⚡ Groq | LLaMA 3.3 70B | Fastest | ~14,400 requests/day |
| 🌟 Google Gemini | Gemini 2.5 Flash | Fast | ~1,500 requests/day |
| 🌊 Mistral | Mistral Small | Fast | ~1,000 requests/month |
| 🤝 Cohere | Command R Plus | Medium | ~1,000 requests/month |

> **Note:** Free-tier limits can change depending on the provider and account type. Check the provider's current pricing/usage documentation before relying on specific limits.

---

# 🧠 How UniChat Works

The core idea is simple:

```text
                    ┌─────────────────────┐
                    │       User          │
                    │   Streamlit Chat    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SessionManager   │
                    │                     │
                    │ Chat History        │
                    │ Message Metadata    │
                    │ Switch Tracking     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ProviderManager  │
                    │                     │
                    │ Provider Selection  │
                    │ Provider Routing    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
        ┌─────────┐       ┌─────────┐       ┌─────────┐
        │  Groq   │       │ Gemini  │       │ Mistral │
        └─────────┘       └─────────┘       └─────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                         ┌───────────┐
                         │  Cohere   │
                         └───────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AI Response      │
                    │                     │
                    │ Provider + Message  │
                    │ Metadata stored     │
                    └─────────────────────┘
```

---

# 🔄 Provider Switching

One of UniChat's main features is **seamless provider switching**.

### Step 1 — Normal Chat

```text
User
 ↓
UniChat
 ↓
Groq
 ↓
AI Response
```

The conversation is stored in the session history.

---

### Step 2 — Rate Limit

Suppose Groq reaches its rate limit:

```text
Groq
 ↓
LIMIT_EXCEEDED
 ↓
UniChat detects the error
```

The user can then select another provider.

---

### Step 3 — Switch Provider

```text
Groq
  ↓
Provider Switch
  ↓
Gemini
```

UniChat does **not** delete the existing conversation.

The complete conversation history is passed to the new provider.

---

### Step 4 — Continue Conversation

```text
Previous Conversation
        +
New User Message
        ↓
     Gemini
        ↓
New Response
```

The conversation continues naturally.

### ✅ No lost history  
### ✅ No new conversation required  
### ✅ Switch providers whenever needed

---

# 🏗️ Architecture

UniChat follows a modular provider architecture.

```text
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SessionManager    │
                    │                     │
                    │ • Messages          │
                    │ • History           │
                    │ • Switch tracking   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ProviderManager   │
                    │                     │
                    │ • Provider registry │
                    │ • Routing           │
                    │ • Switching         │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐     ┌──────────┐     ┌──────────┐
        │   Groq   │     │  Gemini  │     │ Mistral  │
        └──────────┘     └──────────┘     └──────────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                         ┌──────────┐
                         │  Cohere  │
                         └──────────┘
```

---

# 🛠️ Tech Stack

### Frontend

- **Streamlit**
- Custom CSS
- Responsive chat interface

### AI Providers

- **Groq SDK**
- **Google GenAI SDK**
- **Mistral AI SDK**
- **Cohere SDK**

### Language

- **Python**

### Deployment

- **Hugging Face Spaces**

### Security

- Hugging Face Secrets
- Environment variables
- No hardcoded API keys

---

# 📁 Project Structure

```text
UNICHAT/
│
├── app.py
│   └── Streamlit UI + Custom CSS
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
├── .gitignore
│   └── Ignored files and secrets
│
└── src/
    │
    ├── __init__.py
    │
    ├── provider_manager.py
    │   └── Provider registry + switching logic
    │
    ├── session_manager.py
    │   └── Chat history + switch tracking
    │
    └── providers/
        │
        ├── __init__.py
        │
        ├── base_provider.py
        │   └── Abstract provider interface
        │
        ├── groq_provider.py
        │   └── Groq + LLaMA integration
        │
        ├── gemini_provider.py
        │   └── Google Gemini integration
        │
        ├── mistral_provider.py
        │   └── Mistral AI integration
        │
        └── cohere_provider.py
            └── Cohere Command R integration
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/unichat.git

cd unichat
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Keys

UniChat requires API keys for the providers you want to use.

| Environment Variable | Provider |
|---|---|
| `GROQ_API_KEY` | Groq |
| `GEMINI_API_KEY` | Google Gemini |
| `MISTRAL_API_KEY` | Mistral AI |
| `COHERE_API_KEY` | Cohere |

---

# 🔐 Environment Configuration

Create a `.env` file locally:

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
MISTRAL_API_KEY=your_mistral_api_key
COHERE_API_KEY=your_cohere_api_key
```

> ⚠️ **Never commit your `.env` file to GitHub.**

Make sure `.gitignore` contains:

```gitignore
.env
__pycache__/
*.pyc
venv/
```

---

# 🚀 Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🔒 Security

API keys are **never hardcoded** into the application.

For local development:

```text
.env
 ↓
Environment Variables
 ↓
Provider Classes
```

For Hugging Face deployment:

```text
Hugging Face Secrets
 ↓
Environment Variables
 ↓
Provider Classes
```

This keeps sensitive credentials outside the source code.

### ⚠️ Important

Never do this:

```python
GROQ_API_KEY = "gsk_xxxxxxxxx"
```

Instead:

```python
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

---

# 🎨 UI Design

UniChat uses a custom premium dark interface.

### Design System

```text
Primary Accent:
#7C6FF7

Sidebar:
#1A1535

Typography:
Syne       → Headings
DM Sans    → Body
```

### UI Components

- 🌑 Dark sidebar
- 💜 Purple accent system
- 💬 ChatGPT-style conversation
- 🪟 Frosted-glass elements
- ✨ Gradient cards
- 🏷️ Provider badges
- ⏱️ Message timestamps
- 📊 Session statistics
- 🔄 Provider switch controls

---

# 📊 Session Management

UniChat tracks important conversation information.

Example:

```text
Session
│
├── Messages
│   ├── User message
│   ├── Assistant response
│   ├── User message
│   └── Assistant response
│
├── Active Provider
│
└── Provider Switch Count
```

Each assistant response can contain provider metadata such as:

```text
Provider: Groq
Timestamp: 15:42
Response: ...
```

This makes it easy to understand which AI model generated each response.

---

# ⚡ Performance

| Metric | Target |
|---|---|
| Active Providers | 4 |
| Provider Switching | Near-instant |
| History | Session-based |
| Response Time | ~1–5 seconds |
| Deployment | Hugging Face Spaces |
| Infrastructure Cost | $0 on free tiers |

> Actual response times and free-tier limits depend on provider availability, network conditions, and account limits.

---

# 🌐 Deployment

UniChat is deployed using:

**Hugging Face Spaces + Streamlit**

Deployment flow:

```text
GitHub / Local Project
        ↓
Hugging Face Space
        ↓
Streamlit Application
        ↓
Environment Secrets
        ↓
Live Application
```

### Live Application

🚀 **https://huggingface.co/spaces/komaraprasad/unichat**

---

# 🧪 Example Workflow

Imagine the user starts with Groq:

```text
User:
Explain transformers in simple terms.

Groq:
A transformer is...
```

The user continues:

```text
User:
Give me a Python example.
```

Then Groq reaches its limit.

UniChat shows:

```text
⚠️ Provider limit reached.

Available providers:
• Gemini
• Mistral
• Cohere
```

The user selects Gemini.

The existing conversation remains:

```text
User:
Explain transformers...

Groq:
A transformer is...

User:
Give me a Python example.

Gemini:
Sure! Here's a Python example...
```

### 🔥 The conversation never resets.

---

# 🧩 Design Principles

UniChat is built around a few core principles:

### 1. Provider Independence

The application should not depend on a single AI provider.

### 2. Conversation Continuity

Changing the underlying model should not destroy the user's context.

### 3. Modular Architecture

Each provider is implemented independently.

### 4. Secure Configuration

Credentials should always remain outside the source code.

### 5. Simple User Experience

Users should focus on the conversation rather than managing APIs.

---

# 🔮 Future Improvements

The project roadmap includes:

- ⏳ OpenAI integration
- 🤖 Automatic provider switching when rate limits occur
- 📄 Export conversations as PDF
- ⚙️ Custom system prompts
- 🔬 Response comparison mode
- 📈 Usage analytics dashboard
- 📱 Mobile-optimized interface
- 💾 Persistent conversation storage
- 🧠 Model-specific configuration
- 🔌 Additional AI providers

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

```bash
git fork
```

### 2. Create a feature branch

```bash
git checkout -b feature/new-provider
```

### 3. Make your changes

### 4. Commit

```bash
git commit -m "Add new AI provider"
```

### 5. Push

```bash
git push origin feature/new-provider
```

### 6. Open a Pull Request

---

# 📜 License

This project is available for educational and personal use.

Add a formal license such as **MIT** if you want others to freely reuse and modify the project.

---

# 👨‍💻 Author

## Komara Prasad

**AI Engineer | LLM Systems | Multi-Provider AI | Streamlit Applications**

Interested in:

- 🤖 Generative AI
- 🧠 Large Language Models
- 🔗 LLM Applications
- ⚡ AI APIs
- 🏗️ AI System Architecture
- 🚀 AI Deployment

---

# 🔗 Connect

- 💼 LinkedIn
- 🤗 Hugging Face
- 🐙 GitHub

---

# ⭐ Support

If you found UniChat useful:

⭐ **Star the repository**

🐛 **Report issues**

💡 **Suggest new providers**

🤝 **Contribute improvements**

---

## 🚀 UniChat

### **One Chat. Multiple AI Models. Zero Lost Context.**

> **Switch providers. Keep your conversation. Keep building. 🤖💜**