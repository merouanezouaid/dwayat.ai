# Dwayat AI: Your Personal Health Assistant Bot

Dwayat AI is a RAG based medical chatbot designed to assist users with health-related queries, medication information, and prescription analysis. 
It combines advanced natural language processing techniques + the power of LLMs, with a comprehensive medical database to provide accurate and helpful responses.

## 🚀 Features

- 💬 Interactive chat interface for health-related questions
- 💊 Detailed information on medications, including side effects, contraindications, and pricing
- 📄 PDF prescription analysis
- 🌐 Multilingual support (English and Darija)
  
## 🛠️ Technologies Used

- Frontend: React.js
- Backend: Flask (Python)
- NLP: Sentence Transformers, FAISS, Hugging Face Transformers
- Database: Pandas (CSV)
- API: Hugging Face Inference API

## 🏗️ Architecture

Dwayat AI uses a Retrieval Augmented Generation (RAG) architecture:

1. A structured knowledge base of medications
2. Embedding-based search system using FAISS
3. Large Language Model (Mixtral-8x7B-Instruct-v0.1) for response generation
4. Text translation (Atlasia/Terjman-Large) model for English/Darija

## 🚀 Getting Started

### Prerequisites

- Node.js
- Python 3.7+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dwayat-ai.git
   cd dwayat-ai
   ```

2. Install frontend dependencies:
   ```
   npm install
   ```

3. Install backend dependencies:
   ```
   pip install -r server/requirements.txt
   ```

### Running the Application

1. Start the backend server:
   ```
   cd server
   python app.py
   ```

2. In a new terminal, start the frontend:
   ```
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/merouanezouaid/dwayat-ai/issues).

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 👥 Authors

- [Merouane Zouaid](https://github.com/merouanezouaid)
- [Aissa Lamin](https://www.linkedin.com/in/aissa-lamin-86a428250/)

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing powerful NLP models
- [Atlasia](https://huggingface.co/atlasia) for building decent Moroccan AI datasets and models (ily)
---

Made with ❤️ and </>
