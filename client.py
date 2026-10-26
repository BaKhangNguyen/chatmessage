import asyncio
from websockets.asyncio.client import connect


URL = "wss://ubiquitous-fishstick-p7gr4px6q55f7r74-10000.app.github.dev/"


async def receive(chat):
    async for message in chat:
        print("\n" + message)


async def main():
    name = input("Your name: ")


    try:
        async with connect(URL, open_timeout=30) as chat:
            print("Connected! Type /quit to leave.")
            listener = asyncio.create_task(receive(chat))




            while True:
                message = await asyncio.to_thread(input, "You: ")




                if message == "/quit":
                    break




                if message:
                    await chat.send(name + ": " + message)




            listener.cancel()


    except Exception as error:
        print("Connection error:", type(error).__name__, repr(error))


asyncio.run(main())
