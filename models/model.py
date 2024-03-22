
from pydantic import BaseModel


class Repository(BaseModel):
    owner: str
    repo: str

class ContributorInfo(BaseModel):
    owner: str
    repo: str
    username: str
    type: str
