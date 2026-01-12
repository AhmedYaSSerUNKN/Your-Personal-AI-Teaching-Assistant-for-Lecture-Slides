# ============================================================================
# RAG LECTURE Q&A SYSTEM - CLEAN VERSION (NO WARNINGS)
# Save this as: app.py
# Run with: streamlit run app.py
# ============================================================================
# ============================================================================
# ROBUST AUTO-LAUNCHER (Fixed Infinite Loop)
# ============================================================================
# This block uses an environment variable to ensure we only launch Streamlit ONCE.
import sys
import os
import subprocess

if __name__ == "__main__":
    # Check if we are already running via the launcher
    if os.environ.get("STREAMLIT_LAUNCHED") != "true":
        file_path = os.path.abspath(__file__)
        print(f"🚀 Launching Streamlit app: {file_path}")
        
        # Set flag to prevent infinite loop
        env = os.environ.copy()
        env["STREAMLIT_LAUNCHED"] = "true"
        
        # Run "streamlit run" in a separate process
        cmd = [sys.executable, "-m", "streamlit", "run", file_path]
        
        try:
            subprocess.run(cmd, env=env)
        except KeyboardInterrupt:
            pass
        
        # Exit this process so it doesn't run the app logic in the wrong context
        sys.exit(0)

"""
Install all required packages for RAG system with Streamlit GUI.
"""

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


print("✅ All dependencies installed!")

import streamlit as st
import fitz  # PyMuPDF
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer
from huggingface_hub import InferenceClient
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="📚 Lecture Q&A System",
    page_icon="📚",
    layout="wide"
)

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

@st.cache_resource
def load_embedding_model(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """Load and cache the sentence transformer model."""
    return SentenceTransformer(model_name)


def get_embeddings(model, texts: List[str]) -> np.ndarray:
    """Convert a list of texts to embeddings."""
    return model.encode(texts, show_progress_bar=False)


def get_query_embedding(model, query: str) -> np.ndarray:
    """Convert a single query to embedding."""
    return model.encode([query])[0]


def extract_text_from_pdf(pdf_file) -> List[Dict]:
    """Extract text from uploaded PDF file."""
    documents = []
    
    # Save to temp file
    temp_filename = f"temp_{pdf_file.name}"
    with open(temp_filename, "wb") as f:
        f.write(pdf_file.read())
    
    try:
        doc = fitz.open(temp_filename)
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text().strip()
            if text:
                documents.append({
                    "text": text,
                    "lecture": pdf_file.name.replace(".pdf", ""),
                    "file": pdf_file.name,
                    "page": page_num,
                    "id": f"{pdf_file.name}_page_{page_num}"
                })
        doc.close()
    finally:
        # Cleanup temp file
        if os.path.exists(temp_filename):
            try:
                os.remove(temp_filename)
            except:
                pass
    
    return documents


def find_relevant_documents(
    query: str,
    documents: List[Dict],
    doc_embeddings: np.ndarray,
    model,
    top_k: int = 3
) -> List[Dict]:
    """Retrieve top-k most relevant documents ."""
    
    if not documents:
        return []
    
    # Check for specific slide number request
    slide_match = re.search(r'\b(?:slide|page)\s*(\d+)\b', query.lower())
    if slide_match:
        slide_num = int(slide_match.group(1))
        for doc in documents:
            if doc['page'] == slide_num:
                return [{
                    'text': doc['text'],
                    'metadata': {
                        'file': doc['file'],
                        'page': doc['page'],
                        'lecture': doc['lecture']
                    },
                    'score': 1.0
                }]
    
    # Semantic search
    query_embedding = get_query_embedding(model, query)
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    
    # Get top-k results - returns all top-k regardless of score
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    retrieved_docs = []
    for idx in top_indices:
        doc = documents[idx]
        retrieved_docs.append({
            'text': doc['text'],
            'metadata': {
                'file': doc['file'],
                'page': doc['page'],
                'lecture': doc['lecture']
            },
            'score': float(similarities[idx])
        })
    
    return retrieved_docs


def generate_llm_response(
    api_token: str,
    prompt: str,
    model_name: str = "meta-llama/Llama-3.2-3B-Instruct"
) -> str:
    """Generate text using Hugging Face LLM."""
    
    client = InferenceClient(token=api_token)
    
    try:
        response = client.chat_completion(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = str(e)
        if "rate limit" in error_msg.lower() or "429" in error_msg:
            return "⚠️ Rate limit reached. Please wait and try again."
        elif "authorization" in error_msg.lower() or "401" in error_msg:
            return "❌ Invalid API token. Please check your token."
        return f"❌ Error: {error_msg}"


def build_prompt(query: str, context_docs: List[Dict]) -> Optional[str]:
    """Construct the prompt for the LLM."""
    
    if not context_docs:
        return None
    
    context_parts = []
    for doc in context_docs:
        meta = doc['metadata']
        text = doc['text'][:500]
        context_parts.append(f"[{meta['file']}, Slide {meta['page']}]:\n{text}")
    
    context = "\n\n".join(context_parts)
    
    prompt = f"""You are a helpful teaching assistant. Answer based ONLY on the lecture content below.

LECTURE CONTENT:
{context}

QUESTION: {query}

Provide a clear, educational answer based only on the content above.

ANSWER:"""
    
    return prompt


def run_rag_pipeline(
    question: str,
    documents: List[Dict],
    doc_embeddings: np.ndarray,
    model,
    api_token: str
) -> Dict:
    """Orchestrate the complete RAG pipeline."""
    
    # Step 1: Retrieve relevant documents
    retrieved_docs = find_relevant_documents(
        query=question,
        documents=documents,
        doc_embeddings=doc_embeddings,
        model=model,
        top_k=3
    )
    
    if not retrieved_docs:
        return {
            'answer': "❌ No relevant information found in the lectures.",
            'sources': [],
            'retrieved_docs': []
        }
    
    # Step 2: Build prompt with context
    prompt = build_prompt(question, retrieved_docs)
    
    if not prompt:
        return {
            'answer': "❌ Could not build prompt from retrieved documents.",
            'sources': [],
            'retrieved_docs': []
        }
    
    # Step 3: Generate answer
    answer = generate_llm_response(api_token, prompt)
    
    # Step 4: Format with sources
    sources = [f"{doc['metadata']['file']} (Slide {doc['metadata']['page']})"
               for doc in retrieved_docs]
    formatted_answer = f"{answer}\n\n📚 **Sources:** {', '.join(sources)}"
    
    return {
        'answer': formatted_answer,
        'sources': [doc['metadata'] for doc in retrieved_docs],
        'retrieved_docs': retrieved_docs
    }


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'documents' not in st.session_state:
    st.session_state.documents = []

if 'doc_embeddings' not in st.session_state:
    st.session_state.doc_embeddings = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'system_ready' not in st.session_state:
    st.session_state.system_ready = False


# ============================================================================
# SIDEBAR - CONFIGURATION
# ============================================================================

with st.sidebar:
    st.title("⚙️ Configuration")
    
    # API Token Section
    st.subheader("🔑 API Settings")
    api_token = st.text_input(
        "Hugging Face API Token",
        type="password",
        help="Get your token at https://huggingface.co/settings/tokens"
    )
    
    if api_token:
        st.success("✅ API token configured")
    else:
        st.warning("⚠️ Please enter your API token")
    
    st.divider()
    
    # File Upload Section
    st.subheader("📁 Upload Lectures")
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload one or more lecture PDF files"
    )
    
    # Initialize System Button
    if st.button("🚀 Initialize System", disabled=not api_token):
        if not uploaded_files:
            st.error("❌ Please upload at least one PDF file")
        else:
            with st.spinner("Initializing system..."):
                try:
                    # Step 1: Load embedding model
                    st.write("🧠 Loading embedding model...")
                    model = load_embedding_model()
                    
                    # Step 2: Extract text from PDFs
                    all_documents = []
                    progress_bar = st.progress(0)
                    
                    for i, file in enumerate(uploaded_files):
                        st.write(f"📄 Processing {file.name}...")
                        docs = extract_text_from_pdf(file)
                        all_documents.extend(docs)
                        progress_bar.progress((i + 1) / len(uploaded_files))
                    
                    st.session_state.documents = all_documents
                    st.write(f"✅ Extracted {len(all_documents)} pages")
                    
                    # Step 3: Compute embeddings
                    st.write("🔢 Computing embeddings...")
                    texts = [doc["text"] for doc in all_documents]
                    embeddings = get_embeddings(model, texts)
                    st.session_state.doc_embeddings = embeddings
                    
                    # Step 4: Mark system as ready
                    st.session_state.system_ready = True
                    
                    st.success(f"✅ System ready! Indexed {len(all_documents)} pages from {len(uploaded_files)} files")
                    
                except Exception as e:
                    st.error(f"❌ Error during initialization: {str(e)}")
    
    st.divider()
    
    # System Status Section
    st.subheader("📊 System Status")
    if st.session_state.system_ready:
        st.success("✅ System Ready")
        st.metric("Documents Indexed", len(st.session_state.documents))
        st.metric("Questions Asked", len(st.session_state.chat_history))
    else:
        st.warning("⚠️ System Not Initialized")
        st.info("Upload PDFs and click Initialize to get started")
    
    st.divider()
    
    # Clear Chat Button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")
        st.rerun()


# ============================================================================
# MAIN INTERFACE
# ============================================================================

st.title("📚 Lecture Q&A System")

if not st.session_state.system_ready:
    # Welcome Screen
    st.info("👋 Welcome to the Lecture Q&A System!")
    
    st.markdown("""
    ### 🚀 Getting Started
    
    1. **Enter your Hugging Face API token** in the sidebar
       - Get it from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
       - It's completely free!
    
    2. **Upload your lecture PDF files** in the sidebar
       - You can upload multiple files at once
       - Supported format: PDF
    
    3. **Click "Initialize System"** in the sidebar
       - This will extract text and create embeddings
       - Takes about 30 seconds
    
    4. **Start asking questions!**
       - Ask about specific slides or general concepts
       - Get AI-powered answers with source citations
    """)
    
    st.divider()
    
    st.subheader("💡 Example Questions")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - What is explained in slide 5?
        - Summarize lecture 1
        - What is gradient descent?
        """)
    
    with col2:
        st.markdown("""
        - Explain the main concepts
        - How does backpropagation work?
        - What are neural networks?
        """)

else:
    # Display Chat History
    if st.session_state.chat_history:
        st.subheader("💬 Chat History")
        
        for i, chat in enumerate(st.session_state.chat_history):
            # Question
            st.markdown(f"**❓ Question {i + 1}:** {chat['question']}")
            
            # Answer
            st.info(chat['answer'])
            
            # Sources (expandable)
            if chat.get('retrieved_docs'):
                with st.expander(f"📄 View {len(chat['retrieved_docs'])} Source(s)"):
                    for j, doc in enumerate(chat['retrieved_docs'], 1):
                        meta = doc['metadata']
                        score = doc['score']
                        st.markdown(f"**{j}. {meta['file']} - Slide {meta['page']}** (Relevance: {score:.1%})")
                        with st.container():
                            st.text(doc['text'][:300] + "...")
                        if j < len(chat['retrieved_docs']):
                            st.markdown("---")
            
            st.divider()
    
    # Question Input Area
    st.subheader("❓ Ask a Question")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        question = st.text_input(
            "Your question:",
            placeholder="e.g., What is gradient descent? or Explain slide 5",
            label_visibility="collapsed",
            key="question_input"
        )
    
    with col2:
        ask_button = st.button("🔍 Ask", use_container_width=True)
    
    # Process Question
    if ask_button:
        if question:
            with st.spinner("🤔 Searching lectures and generating answer..."):
                try:
                    # Load model from cache
                    model = load_embedding_model()
                    
                    # Run RAG pipeline
                    result = run_rag_pipeline(
                        question=question,
                        documents=st.session_state.documents,
                        doc_embeddings=st.session_state.doc_embeddings,
                        model=model,
                        api_token=api_token
                    )
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        'question': question,
                        'answer': result['answer'],
                        'sources': result['sources'],
                        'retrieved_docs': result['retrieved_docs']
                    })
                    
                    # Rerun to display new message
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error processing question: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question")
    
    # Example Questions
    with st.expander("💡 Need ideas? Click for example questions"):
        st.markdown("""
        **Specific Slide Questions:**
        - What is slide 9 about?
        - Explain the content on page 5
        - Show me slide 12
        
        **Concept Questions:**
        - What is gradient descent?
        - Explain backpropagation
        - How do neural networks work?
        
        **Summary Questions:**
        - Summarize the main concepts
        - What are the key takeaways from lecture 1?
        - Give me an overview of the course material
        """)


# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    Supervised By DR. Manar El Shazly ❤️
</div>
""", unsafe_allow_html=True)