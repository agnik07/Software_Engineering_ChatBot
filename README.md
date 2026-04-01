# 💻 Software Engineering AI Agent

[![Streamlit](https://img.shields.io/badge/Streamlit-Powered-blue?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

A **senior software engineer AI mentor** that provides structured, production-ready Python solutions for your coding questions. Trained on 12k+ synthetic software engineering prompts.

## 🚀 Features

- **Smart Scope Filtering**: ML classifier detects if your question is software engineering related
- **Structured Responses**: Every answer follows exact format:
  ```
  Problem Explanation:
  Approach:
  Step-by-Step Logic:
  Python Implementation:
  Example Input/Output:
  Time & Space Complexity:
  ```
- **Production Models**: 
  - Custom sklearn classifier (trained on domain dataset)
  - Salesforce/codegen-350M-mono (350M params, code-focused LLM)
- **Streamlit Web UI**: Chat interface, conversation history

## 🏗️ Architecture

```
User Question → Vectorizer → Scope Classifier → [If in-scope] CodeGen LLM → Structured Answer
                          ↓
                     "Not in scope"
```

**ML Pipeline** (trained in `model.ipynb`):
1. **Dataset**: 12k synthetic prompts (`dataset.json`) + out-of-scope (`non_related.json`)
2. **Features**: TF-IDF vectorization
3. **Classifier**: Scikit-learn model (`scope_model.pkl`)
4. **LLM**: Salesforce/codegen-350M-mono via HuggingFace transformers

## 🎯 Demo

Ask: \"implement kruskal algorithm\" → Gets complete structured solution!

## 📦 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Setup & Run

```bash
# Clone repo
git clone https://github.com/agnik07/Software_Engineering_ChatBot.git
cd Software_Engineering_ChatBot

# Install dependencies
pip install -r requirements.txt

# Download models (automatic on first run)

# Run Streamlit app
streamlit run app.py
```

**Local URL**: http://localhost:8501

## 📊 Dataset

- **12,002 synthetic prompts** across 20+ skills:
  | Skill | Examples |
  |-------|----------|
  | algorithms | binary search, quicksort |
  | data_structures | linked list, stack |
  | backend | REST API, JWT auth |
  | system_design | chat backend, URL shortener |
  | devops | Docker, CI/CD |
  | ML/Database/SQL/etc. | |

- **3 difficulties**: easy/medium/hard
- **Training split**: Used for scope classification

## 🔧 Files Structure

```
├── app.py              # Streamlit UI
├── agent.py            # Core logic + ML inference
├── model.ipynb         # Model training notebook
├── dataset.json        # 12k+ training prompts
├── scope_model.pkl     # Trained classifier
├── vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt    # Dependencies
└── README.md           # You're reading it!
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| UI | Streamlit |
| Scope ML | scikit-learn + TF-IDF |
| Code LLM | Salesforce/codegen-350M-mono |
| Models | HuggingFace Transformers |
| Compute | CPU (device=-1) |

## 🤝 Contributing

1. Fork & clone
2. Create feature branch `git checkout -b feature/amazing-feature`
3. Commit changes `git commit -m 'Add amazing feature'`
4. Push & PR 🎉

## 📈 Future Work

- Fine-tune CodeGen on dataset
- Add RAG with verified solutions
- Multi-language support
- Authentication & sharing
- Docker deployment

## 📄 License

MIT - See [LICENSE](LICENSE) (create if needed)

---

**⭐ Star this repo if helpful!** Questions? Open an issue.

