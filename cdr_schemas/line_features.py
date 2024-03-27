from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.common import GeoJsonType, GeomType


class DashType(str, Enum):
    Point = "solid"
    LineString = "dash"
    Polygon = "dotted"


class Line(BaseModel):
    """
    coordinates in line are  (column from left, row from bottom).
    """

    coordinates: List[List[Union[float, int]]]
    type: str = Field(default=GeomType.LineString)


class LineProperty(BaseModel):
    """
    Properties of the line.
    """

    id: str = Field(description="your internal id")
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )

    model_config = ConfigDict(protected_namespaces=())


class LineFeature(BaseModel):
    """
    Line Feature.
    """

    type: str = GeoJsonType.Feature
    geometry: Line
    properties: LineProperty


class LineFeatureCollection(BaseModel):
    """
    All line features for legend item.
    """

    type: Literal[GeoJsonType.FeatureCollection] = GeoJsonType.FeatureCollection
    features: Optional[List[LineFeature]]


class LineLegendAndFeaturesResult(BaseModel):
    """
    Line legend item with metadata and associated line features found.
    """

    id: str = Field(description="your internal id")
    name: Optional[str]
    dash_pattern: Optional[DashType] = Field(
        default=None, description="values = {solid, dash, dotted}"
    )
    description: Optional[str]
    symbol: Optional[str]
    legend_bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the legend item.
        Column value from left, row value from bottom."""
    )
    line_features: Optional[LineFeatureCollection]
