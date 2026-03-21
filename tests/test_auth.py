import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_login_and_upload():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/login", data={"username":"admin","password":"password"}, follow_redirects=False)
        assert r.status_code == 303
        sid = r.cookies.get("session")
        assert sid is not None

        r2 = await ac.get("/upload", cookies={"session": sid})
        assert r2.status_code == 200
        assert "Upload page" in r2.text

@pytest.mark.asyncio
async def test_invalid_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/login", data={"username":"bad","password":"bad"})
        assert r.status_code == 401
