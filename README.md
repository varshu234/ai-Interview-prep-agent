# 🚀 Interview Preparation Agent

An AI-powered interview preparation and mock interview application that generates **role- and company-specific interview questions**, evaluates candidate answers, and provides **AI-powered scoring and improvement feedback**.

## ✨ Features

* 🎯 Generate interview questions based on the target **job role and company**
* 🧪 Conduct an interactive **mock interview**
* 🤖 AI-powered answer evaluation
* 📊 Score answers out of 10
* 💡 Receive personalized improvement tips
* 🔄 Track interview progress using session state
* ⚡ Powered by Groq's high-speed LLM inference
* 🖥️ Simple and interactive Streamlit interface

## 🧠 How It Works

```text
User enters Job Role + Company
            ↓
    AI generates questions
            ↓
       Mock Interview
            ↓
      User submits answer
            ↓
     AI evaluates answer
            ↓
    Score + Improvement Tips
            ↓
       Next Question
```

## 🔧 Tech Stack

* **Python**
* **Streamlit** – Web application interface
* **LangChain** – LLM integration
* **Groq API** – LLM inference
* **GPT-OSS-20B** – Language model
* **Streamlit Session State** – Interview state management

## 📸 Project Screenshot

![Project UI](images/screenshot.png)

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/varshu234/ai-Interview-prep-agent.git
cd ai-Interview-prep-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

**Never upload your API key or `.env` file to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Example Workflow

1. Enter a job role, such as **Python Developer**
2. Enter a company name
3. Click **Start Preparation**
4. Answer the generated interview questions
5. Submit each answer
6. Receive an AI-generated score and improvement tips
7. Continue until the mock interview is completed

## 📁 Project Structure

```text
ai-Interview-prep-agent/
│
├── app.py
├── requirements.txt
├── images/
│   └── screenshot.png
├── .gitignore
└── README.md
```

## 🔐 Security

API credentials are stored using environment variables and are **not included in the source code**.

## 🎯 Future Enhancements

* 🔎 Company research using web-search tools
* 🧠 Long-term candidate memory
* 📚 Resume-based interview preparation
* 🎤 Voice-based mock interviews
* 📈 Interview performance analytics
* 📝 Difficulty-based question generation
* 🔗 Integration with job descriptions

## 👩‍💻 Author

**Varsha S**

Computer Science Engineering Student

🔗 GitHub: [varshu234](https://github.com/varshu234)

---

⭐ If you find this project useful, consider giving it a star!
