# 🚀 Resume Reviewer AI

An AI-powered Resume Reviewer built using **FastAPI, OpenAI, PDF Parsing, Pydantic Structured Output, Docker, and DevOps best practices**.

Upload a resume PDF and receive:

* 📊 Overall Resume Score
* 🤖 ATS Score
* ✅ Strengths
* ⚠️ Weaknesses
* 💡 Improvement Suggestions
* 📝 Resume Summary

---

# 📌 Features

* Resume PDF Upload
* PDF Text Extraction
* AI-Powered Resume Analysis
* Resume Score (0–100)
* ATS Score (0–100)
* Strengths & Weaknesses Detection
* Actionable Suggestions
* Structured AI Output using Pydantic
* FastAPI REST API
* Docker Support
* Error Handling & Validation

---

# 🏗 Architecture

```text
User
 │
 │ Upload Resume PDF
 ▼
FastAPI API
 │
 ▼
PDF Parser (pypdf)
 │
 ▼
Resume Text
 │
 ▼
OpenAI GPT
 │
 ▼
Structured Output
 │
 ▼
Pydantic Validation
 │
 ▼
JSON Response
```

---

# 🛠 Tech Stack

| Category              | Technology    |
| --------------------- | ------------- |
| Backend               | FastAPI       |
| AI                    | OpenAI API    |
| PDF Parsing           | pypdf         |
| Validation            | Pydantic      |
| Environment Variables | python-dotenv |
| API Server            | Uvicorn       |
| Containerization      | Docker        |
| Language              | Python 3.13   |

---

# 📁 Project Structure

```text
resume-reviewer-ai/
│
├── app/
│   ├── main.py
│   ├── parser.py
│   ├── ai_reviewer.py
│   └── models.py
│
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 📄 Module Explanation

## main.py

Handles:

* FastAPI app
* API routes
* File upload
* Validation
* Error handling

```text
Client
  ↓
FastAPI
  ↓
Parser
  ↓
AI
  ↓
Response
```

---

## parser.py

Responsible for:

```text
PDF
 ↓
Text Extraction
```

Uses:

```python
pypdf
```

---

## ai_reviewer.py

Responsible for:

```text
Resume Text
 ↓
Prompt
 ↓
OpenAI
 ↓
Structured Review
```

---

## models.py

Contains Pydantic models:

```python
ResumeReview
UploadResponse
```

Used for:

* Validation
* Structured Output
* Type Safety

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-reviewer-ai.git

cd resume-reviewer-ai
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create:

```text
.env
```

Add:

```text
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

# ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

## Home

```http
GET /
```

Response:

```json
{
  "message": "Welcome to Resume Reviewer AI"
}
```

---

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "service": "resume-reviewer-ai"
}
```

---

## Upload Resume

```http
POST /upload
```

Upload:

```text
resume.pdf
```

---

# 📊 Example Response

```json
{
  "filename": "resume.pdf",
  "review": {
    "score": 84,
    "ats_score": 78,
    "summary": "Strong DevOps profile with AWS and Kubernetes experience.",
    "strengths": [
      "AWS knowledge",
      "Kubernetes skills",
      "CI/CD implementation"
    ],
    "weaknesses": [
      "Few quantified achievements"
    ],
    "suggestions": [
      "Add deployment metrics",
      "Include monitoring tools"
    ]
  }
}
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t resume-reviewer-ai .
```

---

## Run Container

```bash
docker run -p 8000:8000 --env-file .env resume-reviewer-ai
```

Open:

```text
http://localhost:8000/docs
```

---

# 🚨 Error Handling

Supported validations:

* Invalid file type
* Empty PDF
* Large file
* Corrupted PDF
* No extractable text
* Missing API Key
* AI API Failure

---

# 🧠 AI Prompt Flow

```text
Resume PDF
      ↓
Extract Text
      ↓
Prompt Engineering
      ↓
OpenAI GPT
      ↓
Structured Output
      ↓
Pydantic Validation
      ↓
JSON Response
```

---

# 🔒 Security

* API key stored in `.env`
* `.env` excluded from Git
* Docker secrets support
* Input validation
* File type validation

---

# 📈 Future Improvements

* OCR for scanned resumes
* Frontend UI (React/Streamlit)
* Authentication
* Resume history
* Database integration
* AWS Deployment
* Kubernetes Deployment
* CI/CD Pipeline
* GitHub Actions
* Monitoring with Prometheus & Grafana

---

# ☁️ Future DevOps Architecture

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
Docker Hub / ECR
   ↓
AWS EKS
   ↓
Kubernetes
```

---

# 👨‍💻 Author

Ajinkya Waghe

DevOps Engineer | AWS | Kubernetes | Docker | Terraform | GenAI | FastAPI
