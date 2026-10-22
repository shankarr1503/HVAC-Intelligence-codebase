# main_ai_service.py
"""Entry point for the AI microservice."""

# The FastAPI app is in services.ai_service_api.app

if __name__ == "__main__":
    import uvicorn
    from utils.config import settings

    uvicorn.run("services.ai_service_api:app", host="0.0.0.0", port=settings.ai_service_port,
                reload=settings.reload)
