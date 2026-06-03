# 🤖 UniChat — One Chat, All AI Models
A production-grade multi-provider AI chat application that lets users switch between AI providers mid-conversation without losing chat history — deployed live on Hugging Face Spaces.

🔗 **Live Demo:** https://huggingface.co/spaces/komaraprasad/unichat

---

## 🎯 Problem It Solves
Free AI models have rate limits. Users constantly face:

- "You've exceeded your free limit" — Groq
- "Quota exceeded for today" — Gemini
- "Too many requests" — Mistral
- Losing entire conversation history on every switch

**UniChat solves this** — switch providers anytime, your full conversation is always preserved.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 💬 Conversational AI | ChatGPT-like chat interface for natural conversations |
| 🔄 Provider Switching | Switch between 4 AI providers mid-conversation |
| 💾 History Preserved | Full chat history carries over on every switch |
| ⚡ Multiple Free Models | Groq, Gemini, Mistral, Cohere — all free tier |
| 📊 Session Stats | Track messages sent and provider switches |
| 🎨 Premium UI | Custom dark sidebar, purple accent design system |
| 🔒 Secure | API keys stored as HF Secrets — never hardcoded |
| 🌐 24/7 Availability | Deployed on Hugging Face Spaces — always online |

---

## 🏗️ Architecture

```
User sends message (Streamlit Chat UI)
              ↓
SessionManager stores message with metadata
              ↓
ProviderManager routes to active provider
              ↓
Active Provider (Groq / Gemini / Mistral / Cohere)
              ↓
Full conversation history sent as context
              ↓
Response generated + stored with provider tag
              ↓
Displayed in chat with provider badge + timestamp

On Provider Switch:
              ↓
Old provider → New provider
Full message history passed to new provider ✅
Conversation continues seamlessly ✅
```

---

## 🛠️ Tech Stack

```
Streamlit          — Chat UI frontend
Groq SDK           — LLaMA 3.3 70B inference (fastest free)
Google GenAI SDK   — Gemini 2.5 Flash
MistralAI SDK      — Mistral Small Latest
Cohere SDK         — Command R Plus
Python             — Core language
HuggingFace Spaces — Free cloud deployment
```

---

## 📁 Project Structure

```
UNICHAT/
│
├── app.py                    — Streamlit UI + custom CSS
├── requirements.txt          — Python dependencies
├── README.md                 — Project overview
├── .gitignore                — Git ignore rules (.env)
│
└── src/
    ├── __init__.py
    ├── provider_manager.py   — Provider registry + switching logic
    ├── session_manager.py    — Chat history + switch tracking
    └── providers/
        ├── __init__.py
        ├── base_provider.py      — Abstract base class
        ├── groq_provider.py      — Groq LLaMA integration
        ├── gemini_provider.py    — Google Gemini integration
        ├── mistral_provider.py   — Mistral AI integration
        └── cohere_provider.py    — Cohere Command R integration
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/unichat.git
cd unichat
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get free API keys

| Key | Provider | Get it here | Cost |
|---|---|---|---|
| `GROQ_API_KEY` | Groq LLaMA | console.groq.com | Free |
| `GEMINI_API_KEY` | Google Gemini | aistudio.google.com | Free |
| `MISTRAL_API_KEY` | Mistral AI | console.mistral.ai | Free |
| `COHERE_API_KEY` | Cohere | dashboard.cohere.com | Free |

### 4. Add keys to `.env`
```
GROQ_API_KEY=your_key
GEMINI_API_KEY=your_key
MISTRAL_API_KEY=your_key
COHERE_API_KEY=your_key
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🔑 API Keys Required

| Key | Purpose | Free Limit |
|---|---|---|
| `GROQ_API_KEY` | LLaMA 3.3 70B inference | 14,400 req/day |
| `GEMINI_API_KEY` | Gemini 2.5 Flash | 1,500 req/day |
| `MISTRAL_API_KEY` | Mistral Small | ~1,000 req/month |
| `COHERE_API_KEY` | Command R Plus | 1,000 req/month |

---

## 💡 How Provider Switching Works

```
Step 1 — Normal Chat:
User message → Groq responds ✅

Step 2 — Rate Limit Hit:
Groq → LIMIT_EXCEEDED error
User sees warning + list of available providers

Step 3 — User Switches:
Sidebar → Select Gemini
SessionManager passes full history to Gemini

Step 4 — Conversation Continues:
Gemini has full context of previous conversation
User continues exactly where they left off ✅
```

---

## 🤖 Supported Providers

| Provider | Model | Speed | Free Limit |
|---|---|---|---|
| ⚡ Groq | LLaMA 3.3 70B | Fastest | 14,400/day |
| 🌟 Google Gemini | Gemini 2.5 Flash | Fast | 1,500/day |
| 🌊 Mistral | Mistral Small | Fast | ~1,000/month |
| 🤝 Cohere | Command R Plus 08-2024 | Medium | 1,000/month |

---

## 🎨 UI Design

```
Color System  : Purple accent (#7C6FF7) + Dark sidebar (#1A1535)
Typography    : Syne (headings) + DM Sans (body)
Chat Messages : White cards with purple borders (assistant)
                Dark gradient cards (user messages)
Sidebar       : Deep purple gradient with frosted glass elements
Welcome Card  : Full-bleed dark gradient with radial glow effects
```

---

## 📊 Performance

```
Providers      : 4 active (Groq, Gemini, Mistral, Cohere)
Switch Time    : < 100ms (instant)
History        : Unlimited messages preserved
Response Time  : 1-5 seconds depending on provider
Availability   : 24/7 (Hugging Face Spaces)
Cost           : $0 (completely free)
```

---

## 🌐 Deployment

```
Platform  : Hugging Face Spaces (free tier)
Framework : Streamlit
URL       : https://huggingface.co/spaces/komaraprasad/unichat
Status    : Live 24/7
Secrets   : API keys stored securely in HF Secrets
```

---

## 🔮 Future Improvements

- ⏳ Add OpenAI GPT-4o when free tier available
- ⏳ Auto-switch on rate limit (no manual switching needed)
- ⏳ Export conversation as PDF
- ⏳ System prompt customization per provider
- ⏳ Response comparison mode (same question, all providers)
- ⏳ Usage analytics dashboard
- ⏳ Mobile-optimized UI

---

## 🙋 Author

**Komara Prasad**
AI Engineer | LLM Systems | Multi-Provider AI | Streamlit Apps

[LinkedIn](https://www.linkedin.com/in/prasadkpk) • [HuggingFace](https://huggingface.co/komaraprasad)
