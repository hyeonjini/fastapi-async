from fastapi import FastAPI

import uvicorn
from app.core.config import settings
from app.api.api_v2.api import api_router


if __name__ == "__main__":
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_STR}/openapi.json",
    )
    app.include_router(api_router, prefix=settings.API_STR)

    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
