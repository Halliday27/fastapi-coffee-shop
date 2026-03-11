from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    date: date
    category_id: int


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    date: Optional[date] = None
    category_id: Optional[int] = None


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    description: Optional[str]
    date: date
    category_id: int
    user_id: int

    class Config:
        from_attributes = True
