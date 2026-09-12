# 🔬 ResearchForge AI — Multi-Agent Research System

ResearchForge AI is an AI-powered multi-agent research system that automates the research process by searching the web, extracting information from relevant sources, generating a structured research report, and critically reviewing the final output.

The system uses specialized AI agents and LangChain Runnable pipelines to divide the research workflow into independent stages.

---

## 🚀 Features

- 🔎 **Search Agent**
  - Searches the web for recent, relevant, and reliable information.
  - Uses Tavily for web search.

- 📖 **Reader Agent**
  - Analyzes search results and selects relevant sources.
  - Scrapes webpages to retrieve detailed information.
  - Uses BeautifulSoup for webpage extraction.

- ✍️ **Writer**
  - Combines search results and scraped content.
  - Generates a structured research report.
  - Implemented using LangChain LCEL / Runnables.

- 🧐 **Critic**
  - Reviews the generated research report.
  - Identifies potential issues, missing information, and weaknesses.
  - Implemented using LangChain LCEL / Runnables.

- 🧠 **Multi-Agent Workflow**
  - Each component has a specialized responsibility.
  - The complete workflow is orchestrated through a central research pipeline.

- 🖥️ **Interactive UI**
  - Built with Streamlit.
  - Allows users to enter research topics and view the generated results.

---

## 🏗️ System Architecture

```text
                         ┌───────────────────┐
                         │       USER        │
                         │   Research Topic  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   SEARCH AGENT    │
                         │                   │
                         │   Groq + Tavily   │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Search Results  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   READER AGENT    │
                         │                   │
                         │ Groq + BeautifulSoup
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Scraped Content  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │      WRITER       │
                         │                   │
                         │   LCEL / Runnable │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Research Report  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │      CRITIC       │
                         │                   │
                         │   LCEL / Runnable │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Final Research  │
                         │      Output      │
                         └───────────────────┘


![alt text](image.png)

🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
LangChain	Agent and LLM orchestration
LangGraph	Agent runtime
Groq	LLM inference
GPT-OSS 20B	Language model used by the agents
Tavily	Web search
BeautifulSoup	Web scraping
Requests	HTTP requests
Streamlit	Interactive web interface
LCEL / Runnables	Writer and Critic pipelines
python-dotenv	Environment variable management


🔄 How It Works
1. User Input

The user enters a research topic through the Streamlit interface.

Example:

Latest advances in AI agents
2. Search Agent

The Search Agent receives the research topic and uses Tavily to search the web for relevant information.

Research Topic
      ↓
Search Agent
      ↓
Tavily Web Search
      ↓
Search Results
3. Reader Agent

The Reader Agent receives the search results, identifies a relevant source, and scrapes the webpage to obtain deeper information.

Search Results
      ↓
Reader Agent
      ↓
Relevant URL
      ↓
BeautifulSoup
      ↓
Detailed Web Content
4. Writer

The Writer combines the search results and scraped content to generate a structured research report.

Search Results
       +
Scraped Content
       ↓
     Writer
       ↓
Research Report

The Writer is implemented using LangChain LCEL / Runnables.

5. Critic

The Critic reviews the generated report and provides feedback about its quality and potential weaknesses.

Research Report
       ↓
     Critic
       ↓
 Critic Feedback


📂 Project Structure
multi-agent-research-system/
│
├── agents.py
│   └── Search Agent and Reader Agent
│
├── tools.py
│   └── Web search and web scraping tools
│
├── pipeline.py
│   └── Main research workflow
│
├── app.py
│   └── Streamlit user interface
│
├── requirements.txt
│   └── Project dependencies
│
├── .env.example
│   └── Environment variable template
│
├── .gitignore
│   └── Git ignored files
│
└── README.md
    └── Project documentation


⚙️ Installation
1. Clone the repository
git clone https://github.com/Yashdarekar1/multi-agent-research-system.git
2. Navigate to the project
cd multi-agent-research-system
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

On Windows:

.venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

You can use .env.example as a template.

Never commit your actual .env file or API keys to GitHub.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

💻 Run the Research Pipeline From Terminal

The research pipeline can also be executed directly:

python pipeline.py

Enter a research topic when prompted.

🧩 Core Components
Search Agent

Responsible for discovering relevant information from the web.

Tools:

Tavily Search
Groq LLM
Reader Agent

Responsible for extracting deeper information from selected webpages.

Tools:

BeautifulSoup
Requests
Groq LLM
Writer

Responsible for generating the final research report.

Technology:

LangChain LCEL
Runnables
Groq LLM
Critic

Responsible for reviewing the generated report.

Technology:

LangChain LCEL
Runnables
Groq LLM
Pipeline

Responsible for orchestrating the complete workflow:

Search
  ↓
Read
  ↓
Write
  ↓
Critique

⚠️ Limitations
Some websites may block automated scraping requests.
Webpages can have different HTML structures, which can affect content extraction.
Search quality depends on the search provider and research query.
LLM-generated content may contain inaccuracies and should be verified against original sources.
Free API tiers may have rate limits.


🔮 Future Improvements
 Multi-source parallel research
 Better source validation
 Automatic source citations
 Fact-checking agent
 Parallel agent execution
 RAG integration
 Vector database integration
 Persistent research history
 Agent memory
 Human-in-the-loop review
 PDF report export
 Markdown report export
 Improved source ranking
 Production deployment
🎯 Project Objective

The goal of ResearchForge AI is to demonstrate how multiple specialized AI agents can collaborate to perform a complete research workflow.

Instead of relying on a single LLM call, the system separates the research process into specialized stages:

🔎 Search
   ↓
📖 Read
   ↓
✍️ Write
   ↓
🧐 Critique

This modular architecture makes the system easier to extend, debug, and improve.

👨‍💻 Author
Yash Darekar

Computer Engineering Graduate | AI/ML Engineer

GitHub:
https://github.com/Yashdarekar1

⭐ Project

If you find this project interesting, feel free to explore the implementation and experiment with different research topics.


### Then run:

```bash
git add README.md
git commit -m "Add professional project README"
git push