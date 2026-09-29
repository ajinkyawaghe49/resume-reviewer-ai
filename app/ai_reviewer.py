import os

from dotenv import load_dotenv
from openai import OpenAI

from app.models import ResumeReview


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def review_resume(resume_text):

    response = client.responses.parse(
        model="gpt-5",
        input=[
            {
                "role": "system",
                "content": """
You are an expert technical recruiter specializing
in DevOps Engineer resumes.

Analyze the resume specifically for a DevOps Engineer role.

Evaluate:

- AWS
- Docker
- Kubernetes
- CI/CD
- Terraform
- Linux
- Monitoring
- Cloud technologies
- DevOps project experience
- Resume clarity
- Quantified achievements

Provide:

1. An overall resume score from 0 to 100.
2. An ATS score from 0 to 100.
3. A concise summary.
4. Key strengths.
5. Key weaknesses.
6. Specific and actionable suggestions.

For the ATS score, consider:
- Relevant DevOps keywords
- Job-title alignment
- Technical skills
- Clear section structure
- Readability
- Quantifiable achievements
- Whether the resume is likely to be parsed correctly by an ATS.

Return the result using the required structured format.
"""
            },
            {
                "role": "user",
                "content": resume_text
            }
        ],
        text_format=ResumeReview
    )

    return response.output_parsed