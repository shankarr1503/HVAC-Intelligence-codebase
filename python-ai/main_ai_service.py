# main_ai_service.py
"""Entry point for the AI microservice."""

from services import ai_service_api

# The FastAPI app is in ai_service_api.app
# Execution is handled if invoked directly

if __name__ == "__main__":
    import uvicorn
    from utils.config import settings

    uvicorn.run("services.ai_service_api:app", host="0.0.0.0", port=settings.ai_service_port, reload=True)
