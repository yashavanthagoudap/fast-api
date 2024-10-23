from fastapi import FastAPI, HTTPException
from app.schemas import GenerateImageRequest, GenerateImageResponse, FineTuneRequest, FineTuneResponse
from app.services import generate_image, fine_tune_model

app = FastAPI(
    title="Replicate Image Generation API",
    description="An API for generating images and fine-tuning models using the Replicate service.",
    version="1.0.0",
    contact={
        "name": "Yashavanthagouda S Patil",
        "email": "yashavanthagoudap@gmail.com"
    }
)

@app.post("/generate-image", response_model=GenerateImageResponse, tags=["Image Generation"])
async def create_image(request: GenerateImageRequest):
    try:
        image_url = generate_image(request.prompt, request.model_version)
        return GenerateImageResponse(image_url=image_url)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/fine-tune", response_model=FineTuneResponse, tags=["Model Fine-Tuning"])
async def fine_tune(request: FineTuneRequest):
    try:
        result = fine_tune_model(request.model_version, request.dataset_url)
        return FineTuneResponse(status="success", message="Fine-tuning started successfully.")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

