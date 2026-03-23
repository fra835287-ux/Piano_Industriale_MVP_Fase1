from fastapi import FastAPI
app = FastAPI(title="AI Logistics Platform")

@app.get("/health")
async def health():
    return {"status": "ok"}

import importlib
candidates = ["app", "app_main", "app.main", "app-main"]
for name in candidates:
    try:
        mod = importlib.import_module(name)
        existing_app = getattr(mod, "app", None)
        if existing_app:
            app.mount("/legacy", existing_app)
            break
    except Exception:
        continue
