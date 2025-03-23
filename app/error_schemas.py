from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str

class SuccesfulResponse(BaseModel):
    detail: str