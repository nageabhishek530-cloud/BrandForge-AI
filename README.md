# 🎨 BrandForge AI

**Your AI-Powered Branding Studio**

BrandForge AI is a locally running AI chatbot that helps users develop ideas for their brands. It uses **Ollama** with the **Llama 3.2 3B** model to generate branding suggestions through a conversational interface.

The application is built with Python and Streamlit. It also saves chat conversations locally so users can revisit or delete previous chats.

## ✨ Features

- **AI branding assistant:** Chat with an AI assistant about your branding ideas.
- **Brand name suggestions:** Get creative brand-name ideas.
- **Tagline creation:** Generate taglines for your brand.
- **Brand identity guidance:** Get help developing a brand identity.
- **Colour palette suggestions:** Explore colour ideas for your brand.
- **Social media content:** Get ideas for social media posts and content.
- **Launch strategy suggestions:** Get practical marketing and launch suggestions.
- **Chat history:** Conversations are saved locally and can be reopened.
- **Delete conversations:** Remove saved conversations from the sidebar.
- **Dark interface:** Custom dark theme with purple accents.

## 🛠️ Technologies Used

- **Python** – Application programming language
- **Streamlit** – Chatbot web interface
- **Ollama** – Runs the AI model locally
- **Llama 3.2 3B** – Language model used to generate responses
- **JSON** – Local conversation storage
- **CSS** – Interface styling

## 📁 Project Structure

```text
BrandForgeAI/
│
├── app.py                 # Main Streamlit application
├── chat_storage.py        # Saves, loads and deletes conversations
├── style.css              # Additional stylesheet
├── requirements.txt       # Python package dependencies
├── README.md              # Project documentation
└── chat_history.json      # Created automatically when chats are saved
```

`chat_history.json` is created in the project directory when the application saves a conversation. It does not need to be created manually.

## ⚙️ Prerequisites

Before running BrandForge AI, install:

1. **Python** – Python 3.10 or later recommended.
2. **Ollama** – Download and install it from [https://ollama.com/](https://ollama.com/).
3. **Llama 3.2 3B model** – The application expects the Ollama model name `llama3.2:3b`.

The AI model runs locally through Ollama. An internet connection is needed to download Ollama and the model initially. After they are downloaded, the application can generate responses locally.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/BrandForgeAI.git
cd BrandForgeAI
```

Replace `YOUR-USERNAME` with your GitHub username and adjust the repository name if you choose a different one.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, you can use this command for your current Windows user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try the activation command again.

### 4. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Download the Ollama model

Make sure Ollama is installed and running, then open a terminal and run:

```bash
ollama pull llama3.2:3b
```

The model download is required before using the chatbot for the first time.

### 6. Run the application

From the project directory, with the virtual environment activated, run:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL, usually:

```text
http://localhost:8501
```

Open that address in your web browser to use BrandForge AI.

## 💬 How to Use

1. Start BrandForge AI using the command above.
2. Enter your brand idea in the chat input.
3. Send your message and wait for the AI response.
4. Continue the conversation to explore branding ideas and suggestions.
5. Use **New Conversation** to start a separate chat.
6. Select a conversation in the sidebar to reopen it.
7. Use the delete button beside a conversation to remove it.

## 💾 Chat Storage

Conversation history is stored in a local JSON file named `chat_history.json` in the project directory.

- The file is created automatically when a conversation is saved.
- Conversations remain available between application sessions as long as this file is kept.
- Deleting the file removes the locally saved conversation history.
- The file is local to the machine running the application; it is not a cloud-synchronised database.

## 🔒 Privacy and Local Usage

BrandForge AI sends prompts to the locally running Ollama service on your computer. It does not require a Gemini API key or another cloud AI API in the code provided for this project.

Avoid entering sensitive personal information into any AI application.

## 🧩 Troubleshooting

**Ollama connection error**
- Confirm that Ollama is installed and running.
- Check that the model is available by running `ollama list`.
- If the model is missing, run `ollama pull llama3.2:3b`.

**Model not found**
- The model name in the application is `llama3.2:3b`.
- Download that exact model using the command above.

**Python package import error**
- Activate the project's virtual environment.
- Run `python -m pip install -r requirements.txt` again.

**Port already in use**
- If port 8501 is occupied, Streamlit may offer another local URL in the terminal.

## 🔮 Future Improvements

- More structured branding workflows and guided questions.
- Exportable brand identity reports.
- More customisation options for generated branding outputs.
- Additional local language models.

## 👥 Project

**BrandForge AI – From Idea to Identity.**

Developed as a college project to demonstrate the use of prompt-based AI assistance in branding.

---

*Note: The current application code includes its main CSS styling directly in `app.py`. The separate `style.css` file is included in the project, but the supplied `app.py` does not currently load it.*
