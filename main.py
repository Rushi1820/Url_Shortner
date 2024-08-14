from fastapi import FastAPI
from database import engine, Base
import routing

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the router
app.include_router(routing.router,tags=["URL_shortner"])


if __name__ == "__main__":
    logger.debug("Starting uvicron FastAPI app")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug")