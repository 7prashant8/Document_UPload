from fastapi import FastAPI
from app.routes import pdf, qa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(pdf.router, prefix="/pdf", tags=["PDF"])
app.include_router(qa.router, prefix="/qa", tags=["QA"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF QA Application"}
