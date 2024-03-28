from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Document(BaseModel):
    """JSON model for user-facing document metadata"""

    id: UUID = Field(..., description="The internal ID of the document")
    title: str = Field(..., description="Title of the document")
    is_public: bool = Field(
        ...,
        description="Whether the full content of the PDF can be downloaded without authorization",
    )

    xdd_id: Optional[str] = Field(
        None, description="The XDD Canonical ID of the document, if present"
    )
    doi: Optional[str] = Field(
        None, description="The digital object identifier of the document, if present"
    )
    pages: Optional[int] = Field(None, description="Document page count")
    page_width: Optional[int] = Field(
        None, description="Width of a page in the document"
    )
    page_height: Optional[int] = Field(
        None, description="Height of a page in the document"
    )
    ingest_date: Optional[Any] = Field(None, description="Article ingest date")
    ingest_batch: Optional[Any] = Field(None, description="Article ingest batch")

    xdd_link: Optional[str] = Field(None, description="xdd api link to the article")
    doi_link: Optional[str] = Field(None, description="doi.org link to the article")
