from fastapi import FastAPI

app = FastAPI()


@app.get("/")
# 异步定义
async def root():
    return {"message": "Hello World"}
