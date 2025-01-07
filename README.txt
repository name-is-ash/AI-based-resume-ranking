Title : AI bases resume ranking System

This project provides an automated solution for analyzing and ranking resumes based on a job description. It leverages Pinecone, LangChain, and Azure OpenAI for efficient resume parsing, vector similarity, and summarization.

Features

📂 Upload multiple resumes (PDF format).
📝 Analyze resumes based on a provided job description.
📊 Rank resumes by relevance using Pinecone vector search.
🧾 Summarize key details of resumes for quick review.

Prerequisites
🐍 Python 3.8 or higher
🔑 Azure OpenAI API key
🔑 Pinecone API key and environment
📦 Required Python libraries (listed in requirements.txt)

Setup:
⚙️ Install the dependencies:
pip install -r requirements.txt

🔧 Configure the .env file with your API keys and endpoints:
pinecone_api_key='your_pinecone_api_key'
OPENAI_API_KEY='your_openai_api_key'
AZURE_OPENAI_ENDPOINT='https://your-azure-endpoint.openai.azure.com/'
AZURE_OPENAI_API_KEY='your_azure_openai_api_key'

How to Run
▶️ Start the Streamlit app:
streamlit run app.py

💻 Use the web interface to:
✏️ Paste the job description.
📤 Upload resumes.
📋 Retrieve and review ranked resumes with summaries.

File Structure
📄 .env: Stores API keys and configuration.
📄 app.py: The main Streamlit app for user interaction.
📄 utils.py: Utility functions for resume parsing, embedding creation, Pinecone operations, and summarization.

Technologies Used
🤖 LangChain: For embeddings and summarization.
🗂️ Pinecone: For vector storage and similarity search.
🌐 Azure OpenAI: For AI-powered resume analysis.
🖥️ Streamlit: For an interactive user interface.

Video_demo:
https://drive.google.com/file/d/1GFhFHDP8qaB5D1sD45hBBnMmcpNtoUs6/view?usp=drive_link

