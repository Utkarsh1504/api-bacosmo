from fastapi import FastAPI
from routes.route import router
app = FastAPI(
    title="Backend Intern Hiring Task: Solution - Utkarsh Mishra",
    description="Implemented all these APIs in FastAPI and MongoDB tech stack as mentioned on the problem statement document.",
    version="1.0.0",
    openapi_url="/openapi.json", 
)

app.include_router(router)
