from pydantic import BaseModel

class GenerateImageRequest(BaseModel):
    model_version: str

    model_config = {
        'protected_namespaces': ()
    }

class GenerateImageResponse(BaseModel):
    image_url: str

class FineTuneRequest(BaseModel):
    model_version: str

    model_config = {
        'protected_namespaces': ()
    }

class FineTuneResponse(BaseModel):
    status: str
    message: str

