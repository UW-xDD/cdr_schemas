from pydantic import BaseModel


class MapEventPayload(BaseModel):
    map_id: str
    cog_url: str
