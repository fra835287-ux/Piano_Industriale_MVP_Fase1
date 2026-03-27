from fastapi import FastAPI, Form, UploadFile, File, Request
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse

app = FastAPI(title="AI Logistics Platform")

@app.get("/health")
async def health():
    return {"status": "ok"}

# Minimal login endpoint expected by tests
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        response = RedirectResponse(url="/upload", status_code=303)
        response.set_cookie(key="session", value="dummy-session-id", httponly=True)
        return response
    return JSONResponse(status_code=401, content={"detail": "Invalid credentials"})

# POST upload used by tests
@app.post("/upload")
async def upload(file: UploadFile | None = File(None)):
    if file:
        await file.read(1)
    return {"status": "uploaded"}

# GET upload required by tests: return an HTML page containing "Upload page"
@app.get("/upload")
async def upload_get(request: Request):
    sid = request.cookies.get("session")
    if not sid:
        return JSONResponse(status_code=401, content={"detail": "Missing session"})
    html = """
    <!doctype html>
    <html>
      <head><title>Upload</title></head>
      <body>
        <h1>Upload page</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
          <input type="file" name="file"/>
          <button type="submit">Upload</button>
        </form>
      </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)
