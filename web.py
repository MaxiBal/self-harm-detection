import asyncio
import websockets
import detect

model = detect.train_model()


async def echo(websocket):
    async for message in websocket:
        vectorized_message = detect.vectorize_string(message)
        at_risk = model.predict(vectorized_message)
        await websocket.send(at_risk)


async def main():
    async with websockets.serve(echo, 'localhost', 8080):
        await asyncio.Future()


asyncio.run(main())