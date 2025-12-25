from fastapi import FastAPI
from app.api.v1.endpoints import pos
from app.core.config import settings
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title=settings.APP_NAME)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(pos.router, prefix="/api/v1", tags=["POS Tagging"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Amharic POS Tagger API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
