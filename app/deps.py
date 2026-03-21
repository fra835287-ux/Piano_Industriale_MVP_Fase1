from fastapi import Cookie, HTTPException, status

def get_current_session(session: str | None = Cookie(None)):
    if not session or session != "demo-session-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return session
