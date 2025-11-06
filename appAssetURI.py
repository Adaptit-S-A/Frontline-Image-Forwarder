from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data import *
import uvicorn

# Create the FastAPI app
app = FastAPI()

# Define the request body schema
class ImageRequest(BaseModel):
    image: str

# Define the POST endpoint
@app.post("/upload-image")
async def upload_image(request: ImageRequest):
    if not request.image:
        raise HTTPException(status_code=400, detail="Image string cannot be empty")
    
    uri = request.image
    #print(uri)
    
    # User authentication
    token = authenticate()

    # Download Image from URI
    response_code = downloadImage(uri, token)

    return {"Status Code": response_code}


if __name__ == "__main__":
    uvicorn.run(
        "appAssetURI:app",
        host=HOSTNAME,
        port=PORT,
        ssl_keyfile=SSL_KEY_PATH,
        ssl_certfile=SSL_CERT_PATH,
    )