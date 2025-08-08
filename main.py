from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
import database, models, schemas

# Створюємо таблиці в базі при першому запуску, якщо їх немає
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Art-Culture AI Microservice")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/art-terms", response_model=List[schemas.ArtTermSchema])
def list_art_terms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    art_terms = db.query(models.ArtTerm).options(
        joinedload(models.ArtTerm.product).joinedload(models.Product.images)
    ).offset(skip).limit(limit).all()
    return art_terms

@app.get("/ai/analyze-artwork/{artwork_id}", response_model=schemas.AIAnalysisResult)
def analyze_artwork(artwork_id: int, db: Session = Depends(get_db)):
    db_artwork = db.query(models.ArtTerm).filter(models.ArtTerm.id == artwork_id).first()
    if db_artwork is None:
        raise HTTPException(status_code=404, detail="Artwork not found")
    original_description = db_artwork.description_en
    ai_generated_description = f"Це новий, згенерований AI опис для терміну '{db_artwork.title_en}'."
    tags = ["abstract", "modern", db_artwork.title_en.lower().replace(" ", "-")]
    return {
        "original_description": original_description,
        "ai_generated_description": ai_generated_description,
        "tags": tags
    }
