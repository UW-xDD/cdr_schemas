from uuid import UUID

from pydantic import BaseModel, Field


class Document(BaseModel):
    """JSON model for user-facing document metadata"""

    id: UUID | None = Field(None, description="The internal ID of the xtraction")
    document_id: UUID = Field(None, description="The internal ID of the source document")
    extraction_type: str = Field(
        ..., description="The type of model that produced the extraction"
    )
    extraction_label: str = Field(
        ..., description="The classification of the extraction within its model"
    )
    score: float | None = Field(None, description="The confidence of the extraction")
    bbox: tuple[float, float, float, float] | None = Field(
        None, description="The bounding box of the extraction"
    )
    page_num: int | None = Field(None, description="The page number of the extraction")
    external_link: str | None = Field(None, description="A link to the extraction")
    data: dict | None = Field(
        None, description="Extra information about the extraction"
    )
