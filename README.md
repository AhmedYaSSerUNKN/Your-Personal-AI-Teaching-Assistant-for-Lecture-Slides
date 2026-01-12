# Your Personal AI Teaching Assistant for Lecture Slides

An intelligent AI-powered teaching assistant designed to help students understand lecture slides through interactive conversations, real-time explanations, and personalized learning experiences.

## Features

- 🤖 **AI-Powered Explanations**: Get instant, detailed explanations for complex lecture concepts
- 📊 **Slide Analysis**: Automatic extraction and analysis of content from lecture slides
- 💬 **Interactive Chat**: Have natural conversations with the AI assistant about your course material
- 🎯 **Personalized Learning**: Adaptive responses based on your learning style and pace
- 📚 **Multi-Format Support**: Works with PDF, image, and document formats
- 🔍 **Context-Aware Responses**: Leverages RAG (Retrieval-Augmented Generation) for accurate information

## Screenshots

### Main Chat Interface
This screenshot shows the primary user interface featuring:
- A clean chat window for student-AI interactions
- Real-time message display with timestamp information
- Input field for typing questions about lecture content
- System status and connection indicators
- Responsive design optimized for both desktop and tablet viewing

### Document Processing Dashboard
This interface demonstrates the document management capabilities:
- Drag-and-drop area for uploading lecture slide PDFs
- Progress indicators for document processing and indexing
- Visual feedback for successful uploads and processing status
- Quick access to recently uploaded lecture materials
- Preview thumbnails of processed documents

## RAG Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     User Query Input                             │
│              (Student Question about Slides)                     │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│               Query Embedding Generation                         │
│        (Convert text to vector representation)                  │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│           Vector Database Search / Retrieval                     │
│    (Find most relevant slide content & lecture context)         │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│          Retrieved Context Aggregation                           │
│   (Combine multiple relevant document chunks)                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│         LLM Prompt Construction                                  │
│  (Build prompt with context + user question)                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│        AI Model Generation                                       │
│  (Generate contextual, accurate response)                       │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              Response Formatting                                 │
│   (Structure output with citations & references)                │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              Deliver to User                                     │
│       (Display answer with source references)                   │
└─────────────────────────────────────────────────────────────────┘
```

### RAG Workflow Components

1. **Query Embedding**: User questions are converted into numerical vector representations using advanced NLP models
2. **Retrieval**: The system searches through embedded lecture slide content to find the most relevant information
3. **Augmentation**: Retrieved context is combined with the original query to provide grounded information
4. **Generation**: The LLM uses the augmented context to generate accurate, reference-backed responses
5. **Response Delivery**: Answers include citations to source slide sections for verification

## Installation

```bash
# Clone the repository
git clone https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides.git

# Navigate to project directory
cd Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Usage

1. **Upload Lecture Slides**: Use the interface to upload PDF or image files of your lecture slides
2. **Ask Questions**: Type your questions in the chat interface about the lecture content
3. **Receive Explanations**: Get detailed, context-aware responses backed by the actual slide content
4. **Review Sources**: Check the referenced slide sections for additional learning

## Tech Stack

- **Frontend**: React/Vue.js (responsive UI)
- **Backend**: Python with FastAPI
- **AI/ML**: 
  - LangChain for RAG implementation
  - OpenAI/Hugging Face models
  - Vector database (Pinecone/Weaviate)
- **Document Processing**: PyPDF2, pdf2image
- **Embeddings**: Sentence-Transformers, OpenAI Embeddings

## License

This project is licensed under the MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated**: 2026-01-12 | **Version**: 1.1.0
