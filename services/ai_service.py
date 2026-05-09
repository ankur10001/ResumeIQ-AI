import os
import json
from groq import Groq
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Configuration
DEFAULT_MODEL = "llama-3.3-70b-versatile"

class AIService:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key) if self.api_key else None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True
    )
    def analyze_resume(self, prompt: str) -> str:
        """
        Calls Groq API to analyze the resume.
        Includes retry logic for rate limits and server errors.
        """
        if not self.client:
            raise ValueError("Groq API Key is missing. Please provide it in the sidebar or .env file.")

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career consultant and ATS optimization engine. Output ONLY valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=DEFAULT_MODEL,
                response_format={"type": "json_object"},
                temperature=0.2,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            # Handle common Groq errors (Rate limits, etc)
            if "rate_limit" in str(e).lower() or "429" in str(e):
                raise e # Tenacity will retry
            raise Exception(f"Groq API Error: {str(e)}")

    def get_mock_data(self) -> dict:
        """
        Returns high-quality mock data for Demo Mode.
        """
        return {
            "ats_data": {
                "ats_score": 82,
                "skills_match_score": 85,
                "keyword_score": 78,
                "experience_score": 88,
                "formatting_score": 90,
                "hiring_probability": 75,
                "resume_grade": "A",
                "salary_range": "$95k - $125k",
                "years_of_experience_detected": 4,
                "seniority_level": "Mid-Level",
                "summary": "Strong candidate with relevant cloud experience. The resume is well-structured but could benefit from more quantitative achievements in the lead role."
            },
            "skills_data": {
                "missing_technical_skills": ["Kubernetes", "Terraform", "GraphQL"],
                "missing_technologies": ["Prometheus", "Grafana"],
                "missing_keywords": ["CI/CD pipelines", "Microservices architecture"],
                "suggested_certifications": ["AWS Certified Solutions Architect", "CKA"],
                "improvement_suggestions": ["Quantify impact with metrics (e.g., 'reduced latency by 20%')", "Add a professional summary at the top"],
                "resume_strengths": ["Clear hierarchy", "Relevant tech stack", "No spelling errors"],
                "quick_wins": ["Update LinkedIn URL", "Standardize date formats"]
            },
            "interview_data": {
                "hr_questions": [{"question": "Tell us about a time you solved a complex technical problem.", "tip": "Focus on the Situation-Action-Result format."}],
                "technical_questions": [{"question": "Explain the difference between vertical and horizontal scaling.", "tip": "Mention state management and load balancing."}],
                "project_questions": [{"question": "What was the most challenging part of your latest project?", "tip": "Discuss trade-offs and decision making."}],
                "behavioral_questions": [{"question": "How do you handle conflict in a technical team?", "tip": "Showcase empathy and collaborative problem solving."}]
            },
            "roadmap_data": {
                "week_1_2": ["Learn Kubernetes basics", "Set up a local cluster"],
                "week_3_4": ["Deploy a microservices app", "Implement monitoring"],
                "month_2": ["Master Terraform for IaC", "Automate infrastructure"],
                "month_3": ["Optimize performance", "Prepare for certification"],
                "top_resources": ["Official Documentation", "Udemy: Master Kubernetes", "Cloud Academy"]
            }
        }
