from pydantic import BaseModel, Field
from typing import List

class DocumentInsight(BaseModel):
    """Structured insights from document analysis"""
    document_type: str = Field(description="Type of document (contract, report, email, etc.)")
    main_topic: str = Field(description="Primary subject/topic of the document")
    key_points: List[str] = Field(description="3-5 most important points from the document")
    sentiment: str = Field(description="Overall sentiment: positive, negative, or neutral")
    urgency_level: int = Field(description="Urgency level from 1-10", ge=1, le=10)
    action_items: List[str] = Field(description="Actionable items or next steps identified")
    summary: str = Field(description="Concise 2-3 sentence summary")
    potential_risks: List[str] = Field(description="Any risks or concerns identified")
