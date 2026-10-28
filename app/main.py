from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello OpenShift"}

@app.get("/health")
def health():
    return {"status": "ok"}