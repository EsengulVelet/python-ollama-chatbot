Qwen AI ChatBot (PyQt6 Desktop App)
A modern desktop AI chatbot application built with PyQt6 and powered by a local Large Language Model (LLM) using Ollama API.
This project provides an interactive chat interface and an advanced code analysis tool integrated into a desktop GUI.
✨ Features
💬 AI Chat Interface
🧑‍💻 Code Analysis Mode
🎨 Styled Chat UI (HTML formatted messages)
📦 Local LLM Integration (Ollama)
🔒 Privacy-friendly (runs locally)
🧩 Code block auto-formatting
📜 Scrollable chat history
🛠️ Technologies Used
Python 3
PyQt6
Requests
Ollama API
Qwen2:1.5B Model
HTML Styling inside QTextEdit
🏗️ Application Architecture
User Input
     ↓
PyQt6 GUI
     ↓
API Request (Ollama)
     ↓
Qwen LLM Response
     ↓
Code Formatting Engine
     ↓
Chat Interface Output
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/qwen-chatbot.git
cd qwen-chatbot
2️⃣ Install Dependencies
pip install PyQt6 requests
3️⃣ Install Ollama
Download Ollama:
https://ollama.ai
Pull the model:
ollama pull qwen2:1.5b
4️⃣ Run Ollama Server
ollama serve
▶️ Run Application
python main.py
🧑‍💻 Usage
Chat Mode
Type a message
Click Gönder
Receive AI response
Code Analysis Mode
Paste your code
Click Analiz Et
Get detailed analysis including:
Purpose
Functions & classes
Strengths & weaknesses
Improvement suggestions
📸 Screenshots
(Add screenshots here)
🚀 Future Improvements
Streaming responses
Conversation memory
Dark mode
Multi-model selection
Syntax highlighting
Export chat history
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.
📄 License
MIT License
👩‍💻 Author
Computer Engineering Student interested in AI, LLM systems and software development.
