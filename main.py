from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
import pickle
import os
from langchain_utils import search_doc

load_dotenv()

def load_docsearch(pth):
    with open(pth, "rb") as f:
        return pickle.load(f)

meta_hype = load_docsearch(os.path.join("data", "META_hype.pkl"))


app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI! Changed!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{query}")
async def query(query: str):
    answer = search_doc(query, meta_hype, return_only_outputs=True)["output_text"]
    return {"response": f"{answer}"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)