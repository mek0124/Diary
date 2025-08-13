from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime


class EntryCreate(BaseModel):
    entry_id: int
    title: str
    details: str
    created_at: str


class Entry(BaseModel):
    entry_id: int
    title: str
    details: str
    created_at: str