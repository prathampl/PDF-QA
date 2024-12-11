from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, qa
from app.routes.qa import router as qa_router
from app.routes.upload import router as upload_router

app = FastAPI(title="PDF-QA Backend", version="1.0.0")

# Middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; can be restricted for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
# Include the routers
app.include_router(qa_router, prefix="/qa", tags=["Q&A"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])

@app.get("/")
def read_root():
    return {"message": "Welcome to PDF-QA Backend"}
