from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return "Hello, world!"


@app.websocket("/actions")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            data = "%.2f" % (int(data) / 63.44)
            await websocket.send_text(data)
        except ValueError:
            data = "Error"
            await websocket.send_text(data)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, debug=True)
