from fastapi import APIRouter, File, UploadFile, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import os

router = APIRouter()

def check_session(request: Request):
    if request.cookies.get("session") != "demo-session-token":
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.get("/upload", response_class=HTMLResponse)
def upload_form(request: Request):
    # semplice controllo sessione: se non loggato, mostra link al login
    if request.cookies.get("session") != "demo-session-token":
        return HTMLResponse('<p>Non autenticato. Vai a <a href="/login">login</a></p>', status_code=401)
    return """
    <form action="/upload" enctype="multipart/form-data" method="post">
      <input name="file" type="file" accept=".csv"/>
      <button type="submit">Upload CSV</button>
    </form>
    """

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...), request: Request = None, _=Depends(check_session)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Solo file CSV")
    os.makedirs("sample_data", exist_ok=True)
    safe_name = os.path.basename(file.filename)
    path = os.path.join("sample_data", safe_name)
    with open(path, "wb") as f:
        f.write(await file.read())
    df = pd.read_csv(path)
    preview_html = df.head(10).to_html(index=False)
    return HTMLResponse(f"<h3>File salvato: {safe_name}</h3>{preview_html}")

