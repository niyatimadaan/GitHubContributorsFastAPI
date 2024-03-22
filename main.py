from fastapi import FastAPI, HTTPException, Request, status
# from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import httpx
from motor.motor_asyncio import AsyncIOMotorClient
from models.model import ContributorInfo, Repository


app = FastAPI()

# MongoDB setup
MONGODB_URL = "mongodb://localhost:27017"
MONGODB_DB = "github_contributors"
client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGODB_DB]

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.post("/ingest-contributors")
async def ingest_contributors(repository: Repository):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/repos/{repository.owner}/{repository.repo}/contributors")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch contributors")
        contributors = response.json()
        collection = db[f"{repository.owner}_{repository.repo}.contributors"]
        await collection.insert_many(contributors)
        return {"message": f"Successfully ingested {len(contributors)} contributors into {repository.owner}_{repository.repo}.contributors"}


@app.post("/contributors")
async def get_contributor_info(info: ContributorInfo):
    collection = db[f"{info.owner}_{info.repo}.contributors"]
    contributor = await collection.find_one({"login": info.username})
    if not contributor:
        raise HTTPException(status_code=404, detail="Contributor not found")
    return {
        "username": contributor["login"],
        "avatar_url": contributor["avatar_url"],
        "site_admin": contributor["site_admin"],
        "contributions": contributor["contributions"]
    }
