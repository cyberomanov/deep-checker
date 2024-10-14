from typing import List, Optional

from pydantic import BaseModel


class Result(BaseModel):
    data: List
    nextCursor: Optional[str]
    hasNextPage: bool


class ExplorerResponse(BaseModel):
    jsonrpc: str
    result: Result
    id: int
