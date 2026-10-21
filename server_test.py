import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

people = set()

async def relay(user):
    people.add(user)
    try:
        async for message in user:
            for other in people.copy():
                if other != user:
                    try:
                        await other.send(message)
                    except ConnectionClosed:
                        people.discard(other)
    finally:
        people.discard(user)

async def main():
    server = await serve(relay, "0.0.0.0", 10000)
    print("Server ready on port 10000")
    await server.serve_forever()

asyncio.run(main())
