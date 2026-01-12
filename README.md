# Your Personal AI Teaching Assistant for Lecture Slides

A comprehensive Streamlit-based Retrieval-Augmented Generation (RAG) system designed to enhance learning experiences by providing intelligent Q&A capabilities for lecture materials.

## 🎯 Overview

This application leverages advanced AI technologies to create an interactive learning platform that allows students to:
- Upload and process lecture slide PDFs
- Ask questions about lecture content
- Receive accurate, contextual answers powered by RAG and large language models
- Maintain conversation history for better learning continuity
- Access citations and references for verified answers

## ✨ Key Features

### 📚 Document Management
- **PDF Upload & Processing**: Upload multiple lecture slide PDFs for comprehensive coverage
- **Automatic Indexing**: Documents are automatically processed and indexed for fast retrieval
- **Multiple File Support**: Handle various lecture formats and sources simultaneously

### 🤖 Intelligent Q&A System
- **RAG Technology**: Combines document retrieval with generative AI for contextually relevant answers
- **Smart Context Window**: Retrieves the most relevant document sections for each query
- **Citation Support**: Provides references to source material for answer verification
- **Conversation Memory**: Maintains chat history for contextual follow-up questions

### 🎨 User Interface
- **Clean, Intuitive Design**: Built with Streamlit for a smooth user experience
- **Real-time Processing**: Instant feedback and response generation
- **Chat Interface**: Natural conversation flow with message history
- **Document Visualization**: Preview and manage uploaded documents

### 🔐 Safety & Reliability
- **Error Handling**: Robust error management for graceful failure recovery
- **Rate Limiting**: Prevents system overload and ensures fair resource usage
- **Input Validation**: Sanitizes all user inputs for security
- **Caching**: Optimized performance through intelligent caching mechanisms

## 🛠️ Technology Stack

### Backend & Core Libraries
- **Streamlit**: Modern web application framework for rapid development
- **LangChain**: Orchestration framework for LLM applications
- **PyPDF2/pdfplumber**: PDF parsing and text extraction
- **FAISS/Chroma**: Vector database for efficient document retrieval
- **OpenAI API**: LLM backbone for answer generation (configurable)

### Data Processing
- **NumPy**: Numerical operations and vector manipulation
- **Pandas**: Data manipulation and analysis
- **Python-dotenv**: Environment configuration management

### Additional Tools
- **Streamlit Session State**: For managing application state
- **Python Logging**: Comprehensive logging for debugging
- **JSON**: Configuration and data interchange

## 📋 Requirements

```
python >= 3.8
streamlit >= 1.28.0
langchain >= 0.1.0
openai >= 1.0.0
faiss-cpu >= 1.7.4
pdfplumber >= 0.10.0
python-dotenv >= 1.0.0
numpy >= 1.24.0
pandas >= 1.5.0
requests >= 2.31.0
```

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides.git
cd Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
```

### 5. Run the Application
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 💡 Usage Guide

### Getting Started
1. **Launch the Application**: Run the Streamlit server
2. **Upload Documents**: Use the sidebar to upload your lecture PDF files
3. **Wait for Processing**: The system will process and index your documents
4. **Start Asking**: Enter your questions in the chat interface

### Best Practices
- **Clear Questions**: Ask specific, well-formulated questions for better results
- **Context Matters**: Provide context if asking follow-up questions
- **Verify Answers**: Check citations provided with answers
- **Iterative Learning**: Use follow-up questions to deepen understanding
- **Session Management**: Clear chat history when switching between different lecture topics

### Example Interactions
```
User: "What is the main topic covered in slide 5?"
Assistant: [Retrieves relevant content and provides comprehensive answer with citations]

User: "Can you explain this concept in simpler terms?"
Assistant: [Provides simplified explanation using conversation context]

User: "What are the key takeaways from today's lecture?"
Assistant: [Summarizes main points from uploaded documents]
```

## 📁 Project Structure

```
Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Example environment configuration
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── config/
│   └── settings.py           # Configuration settings
├── src/
│   ├── __init__.py
│   ├── document_processor.py  # PDF processing and indexing
│   ├── rag_engine.py          # RAG implementation
│   ├── llm_interface.py       # LLM integration
│   └── utils.py               # Utility functions
├── data/
│   ├── uploads/               # Uploaded lecture files
│   ├── vectors/               # Vector database storage
│   └── cache/                 # Cached data
└── logs/
    └── app.log               # Application logs
```

## 🔧 Configuration

### Main Settings (config/settings.py)
```python
# LLM Configuration
LLM_MODEL = "gpt-3.5-turbo"  # or "gpt-4" for better results
TEMPERATURE = 0.7
MAX_TOKENS = 1024
TOP_K_DOCUMENTS = 5  # Number of relevant documents to retrieve

# Document Processing
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MAX_FILE_SIZE = 50  # MB

# UI Settings
MAX_CONVERSATION_HISTORY = 20
SIDEBAR_WIDTH = 300
```

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `STREAMLIT_SERVER_PORT`: Server port (default: 8501)
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## 📊 How RAG Works

1. **Document Ingestion**: PDFs are uploaded and parsed into text chunks
2. **Embedding Creation**: Text chunks are converted to vector embeddings
3. **Vector Storage**: Embeddings are stored in FAISS/Chroma vector database
4. **Query Processing**: User questions are converted to embeddings
5. **Similarity Search**: Most similar document chunks are retrieved
6. **Context Augmentation**: Retrieved chunks augment the LLM prompt
7. **Answer Generation**: LLM generates answers based on context
8. **Response Delivery**: Answer with citations is returned to user

## 🧪 Testing

### Running Tests
```bash
pytest tests/ -v
```

### Test Coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

## 🐛 Troubleshooting

### Common Issues

**Issue: "API Key not found"**
- Solution: Ensure `.env` file exists with `OPENAI_API_KEY` set correctly

**Issue: "PDF processing fails"**
- Solution: Verify PDF is not corrupted; check file size doesn't exceed limits

**Issue: "Slow response time"**
- Solution: Reduce chunk size in settings; consider using GPT-4 or optimizing embeddings

**Issue: "Out of memory"**
- Solution: Reduce number of documents loaded; use `faiss-cpu` with index optimization

### Debugging
Enable debug logging by setting in `.env`:
```env
LOG_LEVEL=DEBUG
```

Check logs in `logs/app.log` for detailed error information.

## 📈 Performance Optimization

### Vector Database Optimization
- Use FAISS for large document collections
- Implement index quantization for memory efficiency
- Regular index rebuilding for consistency

### LLM Optimization
- Implement prompt caching for repeated queries
- Use batch processing for multiple questions
- Adjust temperature based on query complexity

### UI Optimization
- Enable Streamlit caching with `@st.cache_data`
- Implement lazy loading for large document lists
- Use session state management efficiently

## 🔒 Security Considerations

- **API Key Management**: Never commit API keys; use `.env` files
- **File Upload Security**: Implement file type validation and size limits
- **Input Sanitization**: Sanitize all user inputs to prevent injection attacks
- **Error Messages**: Avoid exposing sensitive system information in errors
- **Access Control**: Implement authentication for production deployments

## 📝 Contributing

We welcome contributions to enhance this teaching assistant! Here's how:

1. **Fork the Repository**: Create your own copy
2. **Create a Feature Branch**: `git checkout -b feature/YourFeature`
3. **Make Changes**: Implement your improvements
4. **Commit Changes**: `git commit -m 'Add YourFeature'`
5. **Push to Branch**: `git push origin feature/YourFeature`
6. **Open Pull Request**: Submit your changes for review

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation accordingly
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💼 Author

**Ahmed Yasser**
- GitHub: [@AhmedYaSSerUNKN](https://github.com/AhmedYaSSerUNKN)
- Contact: Open an issue for support or questions

## 🙏 Acknowledgments

- OpenAI for GPT models and API
- LangChain community for RAG framework
- Streamlit team for the amazing framework
- All contributors and users who help improve this project

## 📚 Additional Resources

### Documentation
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)

### Related Articles
- [RAG (Retrieval-Augmented Generation) Explained](https://docs.langchain.com/docs/modules/chains/index_related_chains/retrieval_qa)
- [Vector Databases and Embeddings](https://towardsdatascience.com/vector-databases-for-llm-models-7ff3b92277f8)

## 🚦 Roadmap

### Upcoming Features
- [ ] Multi-language support
- [ ] Advanced search filters
- [ ] Answer quality metrics
- [ ] Export conversation history
- [ ] Dark mode UI
- [ ] User authentication system
- [ ] Cloud deployment templates
- [ ] Mobile application
- [ ] Voice Q&A capability
- [ ] Integration with learning management systems (LMS)

### Future Enhancements
- Support for additional document formats (DOCX, PPTX, images)
- Real-time collaborative learning sessions
- Personalized learning analytics
- Advanced caching mechanisms
- Support for multiple LLM providers
- Fine-tuned models for domain-specific content

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review troubleshooting section above

---

**Last Updated**: 2026-01-12

**Status**: Active Development ✅
