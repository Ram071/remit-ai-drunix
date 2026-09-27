from fastapi import FastAPI

app = FastAPI(title="RemitAI API Shell")

@app.get("/")
def read_root():
    return {"status": "active", "project": "RemitAI", "message": "API shell initialized"}

@app.get("/health")
def health_check():
    return {"health": "ok"}from fastapi import FastAPI

app = FastAPI(title="RemitAI API Shell")

@app.get("/")
def read_root():
    return {"status": "active", "project": "RemitAI", "message": "API shell initialized"}

@app.get("/health")
def health_check():
    return {"health": "ok"}
