from pydantic import BaseModel
from typing import List, Optional

class ProductImageSchema(BaseModel):
    imageUrl: str
    class Config:
        from_attributes = True

class ProductSchema(BaseModel):
    images: List[ProductImageSchema] = []
    class Config:
        from_attributes = True

class ArtTermSchema(BaseModel):
    id: int
    title_en: str
    description_en: str
    product: Optional[ProductSchema] = None
    class Config:
        from_attributes = True

class AIAnalysisResult(BaseModel):
    original_description: str
    ai_generated_description: str
    tags: List[str]
