
from pydantic import BaseModel, Field


class Repository(BaseModel):
    owner: str = Field(pattern=r"^[a-zA-Z0-9-]+$")
    repo: str

class ContributorInfo(BaseModel):
    owner: str = Field(pattern=r"^[a-zA-Z0-9-]+$")
    repo: str
    username: str
    type: str