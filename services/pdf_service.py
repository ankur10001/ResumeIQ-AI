from PyPDF2 import PdfReader
import streamlit as st

class PDFService:
    @staticmethod
    def extract_text(uploaded_file) -> str:
        """
        Extracts raw text from a PDF file.
        """
        try:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            return text.strip()
        except Exception as e:
            st.error(f"❌ Failed to extract text from PDF: {e}")
            return ""

    @staticmethod
    def validate_text(text: str) -> bool:
        """
        Validates extracted text quality.
        """
        if not text or len(text.strip()) < 100:
            return False
        return True

    @staticmethod
    def check_for_scanned_pdf(text: str) -> bool:
        """
        Heuristic to detect if a PDF is likely a scanned image (low text-to-page ratio).
        """
        # Very basic check: if length is very small but it has pages, it might be scanned.
        return len(text.strip()) < 50
