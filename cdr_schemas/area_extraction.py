from typing import List, Union, Optional
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict
from cdr_schemas.common import GeomType


class AreaType(str, Enum):
    Map_Area = "map_area"
    Legend_Area = "legend_area"
    CrossSection = "cross_section"
    OCR = "ocr"
    Polygon_Legend_Area = "polygon_legend_area"
    Line_Point_Legend_Area = "line_point_legend_area"


class Area_Extraction(BaseModel):
    """
    Area extraction of a cog.
    """

    type: GeomType = GeomType.Polygon
    coordinates: List[List[List[Union[float, int]]]]
    bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the area. 
        Column value from left, row value from bottom."""
    )
    category: AreaType = Field(
        ...,
        description="""
            The type of area extraction.
        """,
    )
    text: Optional[str] = Field(
        ...,
        description="""
            The text within the extraction area.
        """,
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )
    model_config = ConfigDict(protected_namespaces=())
