from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from app.services.tagger import tagger_service
from app.core.config import settings
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

class TagRequest(BaseModel):
    text: str

class TagResponse(BaseModel):
    tokens: List[str]
    pos_tags: List[str]
    tagged_sentence: str

@router.post("/tag", response_model=TagResponse)
@limiter.limit(settings.RATE_LIMIT)
async def tag_text(request: Request, body: TagRequest):
    tokens, pos_tags = tagger_service.predict(body.text)
    
    if tokens is None:
        raise HTTPException(status_code=500, detail="POS Tagger model is not available.")
    
    tagged_sentence = "".join([f"{token}: {tag}\n" for token, tag in zip(tokens, pos_tags)])
    
    return TagResponse(
        tokens=tokens,
        pos_tags=pos_tags,
        tagged_sentence=tagged_sentence
    )
