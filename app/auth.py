from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

router = APIRouter()

DEMO_USER = {"username": "admin", "password": "password"}

@router.get("/login", response_class=HTMLResponse)
def login_form():
    return """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Login demo</title>
</head>
<body>
  <h2>Login demo</h2>
  <form id="loginForm" method="post" action="/login" enctype="application/x-www-form-urlencoded">
    <label>Username <input name="username" placeholder="username" required/></label><br/>
    <label>Password <input name="password" type="password" placeholder="password" required/></label><br/>
    <button type="submit">Login</button>
  </form>

  <script>
    document.getElementById('loginForm').addEventListener('submit', function(){ console.log('Submitting form (debug)'); });
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(function(regs){ regs.forEach(r => r.unregister()); }).catch(()=>{});
    }
  </script>
</body>
</html>
"""

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):


    if username.strip() == DEMO_USER["username"] and password.strip() == DEMO_USER["password"]:
        resp = RedirectResponse(url="/upload", status_code=HTTP_303_SEE_OTHER)
        resp.set_cookie(
            key="session",
            value="demo-session-token",
            httponly=True,
            path="/",
            samesite="lax",
            secure=False
        )
        return resp

    return HTMLResponse("<h3>Credenziali errate</h3>", status_code=401)

@router.get("/logout")
def logout():
    resp = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    resp.delete_cookie("session", path="/")
    return resp

from fastapi import Cookie
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

@router.get('/logout')
async def logout(session: str | None = Cookie(None)):
    resp = RedirectResponse(url='/', status_code=HTTP_303_SEE_OTHER)
    resp.delete_cookie('session', path='/')
    return resp


from fastapi import Cookie
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

@router.get('/logout')
async def logout(session: str | None = Cookie(None)):
    resp = RedirectResponse(url='/', status_code=HTTP_303_SEE_OTHER)
    resp.delete_cookie('session', path='/')
    return resp

