from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.auth import router as auth_router
from app.upload import router as upload_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(upload_router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>Piano Industriale MVP - Funziona!</h1><p><a href=\"/login\">Login demo</a></p>"

@app.get("/health")
def health():
    return {"status":"ok"}

