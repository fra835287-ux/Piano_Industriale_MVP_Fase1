from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from app.deps import get_current_session

router = APIRouter()

@router.get("/upload")
def upload_page(session = Depends(get_current_session)):
    return HTMLResponse("<h2>Upload page (autenticato)</h2>")
