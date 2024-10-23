from pydantic import BaseModel

class GenerateImageRequest(BaseModel):
    prompt: str
    model_version: str

class GenerateImageResponse(BaseModel):
    image_url: str

class FineTuneRequest(BaseModel):
    model_version: str
    dataset_url: str

class FineTuneResponse(BaseModel):
    status: str
    message: str

