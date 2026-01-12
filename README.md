# 🎓 LectureAI - Your Personal AI Teaching Assistant for Lecture Slides

<div align="center">

![LectureAI Logo](https://img.shields.io/badge/LectureAI-AI%20Teaching%20Assistant-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow?style=flat-square)

**Transform your lecture slides into an interactive learning experience with AI-powered assistance**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

LectureAI is an intelligent AI-powered teaching assistant designed to enhance your learning experience with lecture slides. It analyzes presentation content, generates comprehensive study materials, answers questions, and provides personalized learning insights.

Whether you're a student looking to master complex topics or an educator seeking to create more engaging learning materials, LectureAI bridges the gap between passive slide viewing and active learning.

---

## ✨ Features

### 🤖 AI-Powered Analysis
- **Intelligent Slide Parsing**: Automatically extracts key concepts, definitions, and important points from lecture slides
- **Content Understanding**: Uses advanced NLP to comprehend and contextualize lecture material
- **Concept Mapping**: Identifies relationships between different topics and concepts

### 📚 Learning Materials Generation
- **Study Guides**: Automatically generates comprehensive study guides from slide content
- **Quiz Generation**: Creates practice questions with multiple choice, short answer, and essay formats
- **Summary Notes**: Produces concise summaries of each lecture section
- **Key Terms & Definitions**: Extracts and organizes important terminology

### 💬 Interactive Q&A
- **Question Answering**: Ask questions about lecture content and receive detailed, contextual answers
- **Clarification Support**: Get explanations for complex concepts in simple terms
- **Deep Dives**: Request in-depth exploration of specific topics from your slides
- **Real-time Assistance**: Get instant answers during study sessions

### 📊 Learning Analytics
- **Progress Tracking**: Monitor your learning progress across different topics
- **Weak Area Identification**: Get insights on concepts that need more attention
- **Personalized Recommendations**: Receive tailored learning paths based on your needs
- **Performance Reports**: Visual dashboards showing your mastery of different topics

### 🎯 Personalization
- **Learning Style Adaptation**: Adjusts explanations based on your learning preferences
- **Difficulty Levels**: Content can be adjusted from beginner to advanced
- **Custom Focus Areas**: Concentrate on specific topics relevant to your needs
- **Progress-Based Feedback**: Adaptive feedback that evolves with your learning

### 📁 Multi-Format Support
- **PowerPoint Presentations** (.pptx, .ppt)
- **PDF Slides** (.pdf)
- **Google Slides** (via integration)
- **Image-based Slides** (.png, .jpg, .jpeg)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key (for AI features)

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides.git
cd Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Keys**
```bash
# Create a .env file in the project root
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

5. **Run the Application**
```bash
python main.py
```

---

## 📖 Usage

### Basic Usage

#### 1. Load Your Lecture Slides
```python
from lectureai import LectureAI

# Initialize the AI assistant
assistant = LectureAI(api_key="your_openai_api_key")

# Load presentation
presentation = assistant.load_slides("path/to/your/lecture.pptx")
```

#### 2. Generate Study Materials
```python
# Generate study guide
study_guide = presentation.generate_study_guide()
print(study_guide)

# Generate quiz
quiz = presentation.generate_quiz(num_questions=10)
print(quiz)

# Get summary
summary = presentation.get_summary()
print(summary)
```

#### 3. Ask Questions
```python
# Ask a question about the lecture
question = "What is the main concept discussed in slide 3?"
answer = presentation.ask_question(question)
print(answer)

# Get clarification
clarification = presentation.clarify_concept("Newton's Laws of Motion")
print(clarification)
```

#### 4. Track Progress
```python
# Get learning analytics
analytics = presentation.get_analytics()
print(f"Topics Covered: {analytics['topics']}")
print(f"Estimated Study Time: {analytics['study_time']}")
print(f"Difficulty Level: {analytics['difficulty']}")
```

### Advanced Usage

#### Custom Configuration
```python
config = {
    'model': 'gpt-4',
    'language': 'en',
    'difficulty_level': 'advanced',
    'learning_style': 'visual'
}

assistant = LectureAI(
    api_key="your_openai_api_key",
    config=config
)
```

#### Batch Processing
```python
# Process multiple presentations
presentations = [
    "lecture1.pptx",
    "lecture2.pptx",
    "lecture3.pptx"
]

for lecture_file in presentations:
    presentation = assistant.load_slides(lecture_file)
    study_guide = presentation.generate_study_guide()
    quiz = presentation.generate_quiz()
    # Process results...
```

#### Export Materials
```python
# Export to different formats
presentation.export_study_guide("output/study_guide.pdf")
presentation.export_quiz("output/quiz.docx")
presentation.export_notes("output/notes.md")
```

---

## 📚 Documentation

### API Reference

#### LectureAI Class
```
LectureAI(api_key, config=None)
  ├── load_slides(file_path)
  ├── get_status()
  └── set_config(config_dict)
```

#### Presentation Object
```
Presentation
  ├── generate_study_guide()
  ├── generate_quiz(num_questions, question_types)
  ├── get_summary()
  ├── ask_question(question)
  ├── clarify_concept(concept_name)
  ├── get_analytics()
  ├── export_study_guide(output_path)
  ├── export_quiz(output_path)
  └── export_notes(output_path)
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `model` | string | gpt-3.5-turbo | AI model to use (gpt-3.5-turbo, gpt-4) |
| `language` | string | en | Language for content generation |
| `difficulty_level` | string | intermediate | Content difficulty (beginner, intermediate, advanced) |
| `learning_style` | string | balanced | Learning style preference (visual, textual, auditory, kinesthetic) |
| `max_tokens` | integer | 2000 | Maximum tokens for responses |
| `temperature` | float | 0.7 | Creativity level of responses (0.0-1.0) |

### Supported Question Types
- Multiple Choice
- Short Answer
- Essay
- True/False
- Fill in the Blank
- Matching

---

## 🛠️ Project Structure

```
Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── main.py                  # Entry point
│
├── lectureai/               # Main package
│   ├── __init__.py
│   ├── core.py             # Core LectureAI class
│   ├── presentation.py     # Presentation handling
│   ├── analyzer.py         # Content analysis
│   ├── generator.py        # Material generation
│   └── utils.py            # Utility functions
│
├── tests/                  # Unit tests
│   ├── test_core.py
│   ├── test_analyzer.py
│   └── test_generator.py
│
├── examples/               # Example scripts
│   ├── basic_usage.py
│   ├── advanced_usage.py
│   └── batch_processing.py
│
└── docs/                   # Additional documentation
    ├── API.md
    ├── TUTORIAL.md
    └── TROUBLESHOOTING.md
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_api_key_here
OPENAI_API_ENDPOINT=https://api.openai.com/v1

# Application Settings
APP_LOG_LEVEL=INFO
MAX_FILE_SIZE=100MB
TEMP_DIR=./temp

# Feature Flags
ENABLE_CACHING=true
ENABLE_ANALYTICS=true
ENABLE_EXPORT=true
```

---

## 💡 Examples

### Example 1: Create Study Materials from Lecture
```python
from lectureai import LectureAI

assistant = LectureAI(api_key="sk-...")
presentation = assistant.load_slides("biology_lecture.pptx")

# Generate comprehensive study materials
study_guide = presentation.generate_study_guide()
quiz = presentation.generate_quiz(num_questions=15)
summary = presentation.get_summary()

print("Study Guide Generated!")
print("Quiz Created with 15 Questions!")
print("Summary Ready for Review!")
```

### Example 2: Interactive Learning Session
```python
presentation = assistant.load_slides("chemistry_lecture.pptx")

questions = [
    "What are the main types of chemical reactions?",
    "Can you explain the law of conservation of mass?",
    "What is the difference between exothermic and endothermic reactions?"
]

for question in questions:
    answer = presentation.ask_question(question)
    print(f"Q: {question}")
    print(f"A: {answer}\n")
```

### Example 3: Progress Monitoring
```python
presentation = assistant.load_slides("physics_lecture.pptx")

analytics = presentation.get_analytics()
print(f"Topics Covered: {', '.join(analytics['topics'])}")
print(f"Difficulty Level: {analytics['difficulty']}")
print(f"Estimated Study Time: {analytics['study_time']} minutes")
print(f"Key Concepts: {len(analytics['key_concepts'])} identified")
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lectureai

# Run specific test file
pytest tests/test_core.py -v
```

---

## 📋 Requirements

```
openai>=0.27.0
python-pptx>=0.6.21
pdf2image>=1.16.0
PyPDF2>=3.0.0
python-dotenv>=0.19.0
requests>=2.28.0
numpy>=1.21.0
pandas>=1.3.0
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
```bash
git clone https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides.git
```

2. **Create a Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Make Your Changes**
- Write clean, documented code
- Add tests for new features
- Update documentation as needed

4. **Commit Your Changes**
```bash
git commit -m "Add description of your changes"
```

5. **Push to Your Fork**
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request**
- Provide clear description of changes
- Reference any related issues

### Contribution Guidelines
- Follow PEP 8 style guide
- Add docstrings to all functions
- Write tests for new features
- Keep commits atomic and meaningful
- Update CHANGELOG.md

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🐛 Troubleshooting

### Common Issues

**Issue: API Key Not Found**
```bash
# Solution: Ensure .env file exists with OPENAI_API_KEY set
echo "OPENAI_API_KEY=your_key_here" > .env
```

**Issue: PDF Processing Error**
```bash
# Solution: Install required system dependencies
# Ubuntu/Debian:
sudo apt-get install libpoppler-cpp-dev

# macOS:
brew install poppler
```

**Issue: Slow Response Times**
```python
# Solution: Use caching and optimize configuration
config = {
    'enable_caching': True,
    'cache_ttl': 3600,
    'batch_size': 5
}
```

For more troubleshooting tips, see [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 🚀 Roadmap

### Current Version (v1.0)
- ✅ Basic slide parsing
- ✅ Study guide generation
- ✅ Q&A functionality
- ✅ Quiz creation

### Upcoming (v1.1)
- 🔄 Google Slides integration
- 🔄 Audio/Video lecture support
- 🔄 Collaborative learning features
- 🔄 Mobile app

### Future (v2.0)
- 📋 Real-time collaboration
- 📋 Custom AI model training
- 📋 Advanced analytics dashboard
- 📋 Integration with LMS platforms

---

## 📞 Support & Contact

- **Issues & Bugs**: [GitHub Issues](https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides/discussions)
- **Email**: [contact information]
- **Documentation**: [See docs/ folder](docs/)

---

## 📊 Project Statistics

![Stars](https://img.shields.io/github/stars/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides?style=social)
![Forks](https://img.shields.io/github/forks/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides?style=social)
![Issues](https://img.shields.io/github/issues/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides)
![Last Updated](https://img.shields.io/github/last-commit/AhmedYaSSerUNKN/Your-Personal-AI-Teaching-Assistant-for-Lecture-Slides)

---

## 🎉 Acknowledgments

Special thanks to:
- The OpenAI team for providing powerful AI models
- All contributors who have helped improve this project
- The open-source community for amazing libraries and tools

---

<div align="center">

**Made with ❤️ by [AhmedYaSSerUNKN](https://github.com/AhmedYaSSerUNKN)**

[⬆ back to top](#-lectureai---your-personal-ai-teaching-assistant-for-lecture-slides)

</div>
