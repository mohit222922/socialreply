from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()

class PostRequest(BaseModel):
    platform: str
    post_text: str

@app.post("/reply")
def generate_reply(request: PostRequest):
    try:
        prompt = f"Reply on {request.platform}: {request.post_text}\nReply:"
        outputs = generator(prompt, max_length=600, num_return_sequences=1)
        reply = outputs[0]['generated_text'].split('Reply:')[1].strip()
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
