import uvicorn

if __name__ == "__main__":
    uvicorn.run("source.main:app", host="0.0.0.0", reload=True)
