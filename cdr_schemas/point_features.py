from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

from cdr_schemas.common import GeoJsonType, GeomType


class Point(BaseModel):
    """
    coordinates in line are (column from left, row from bottom).
    """

    coordinates: List[Union[float, int]]
    type: str = Field(default=GeomType.Point)


class PointProperties(BaseModel):
    """
    Properties of the Point.
    """

    id: str = Field(description="your internal id")
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )
    bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the point item.
        Column value from left, row value from bottom."""
    )
    dip: Optional[int]
    dip_direction: Optional[int]


class PointFeature(BaseModel):
    """
    Point feature.
    """

    type: Literal[GeoJsonType.Feature] = GeoJsonType.Feature
    geometry: Point
    properties: PointProperties


class PointFeatureCollection(BaseModel):
    """
    All point features for legend item.
    """

    type: Literal[GeoJsonType.FeatureCollection] = GeoJsonType.FeatureCollection
    features: List[PointFeature]


class PointLegendAndFeaturesResult(BaseModel):
    """
    Point legend item metadata along with associated point features found.
    """

    id: str = Field(description="your internal id")
    name: Optional[str] = Field(description="name of legend item")
    description: Optional[str]
    legend_bbox: Optional[List[Union[float, int]]] = Field(
        description="""
        The extacted bounding box of the legend item.
        Column value from left, row value from bottom.
        """
    )
    point_features: Optional[List[PointFeatureCollection]]
