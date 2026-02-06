from sqlalchemy import Column, Integer, String, JSON
from database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String)
    industry = Column(String)
    metrics = Column(JSON)
    risks = Column(JSON)
    credit_score = Column(Integer)
    ai_report = Column(String)
