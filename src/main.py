from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controller import pautaController, feedbackController
import sys
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pautaController.pauta, prefix="/api")
app.include_router(feedbackController.feedback, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "UnB-TV!"}

if __name__ == '__main__':
    port = 8080
    if len(sys.argv) == 2:
        port = sys.argv[1]
    uvicorn.run('main:app', reload=True, port=int(port), host="0.0.0.0")
