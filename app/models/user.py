from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# --------------------- User Registration Schema --------------------- #
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=12, le=100)
    gender: Optional[str] = Field(default=None, regex="^(Male|Female|Other)$")

# --------------------- User Login Schema --------------------- #
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# --------------------- User Profile Schema --------------------- #
class UserProfile(BaseModel):
    user_id: str
    username: str
    full_name: Optional[str] = None
    email: EmailStr
    age: Optional[int] = None
    gender: Optional[str] = None
