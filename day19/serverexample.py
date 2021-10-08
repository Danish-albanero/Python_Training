import websockets
import asyncio


PORT = 7890

print("server listening on port " + str(PORT))

connected = set()

async def echo(websocket, path):
        print("a client just connected")
        connected.add(websocket)
        try:
            async for message in websocket:
                print("Received message from client: " + message)
                for conn in connected:
                        if conn != websocket:
                                await conn.send("someone said:" + message)
                
        except websockets.exceptions.ConnectionClosed as e:
                print("a client just disconnected")
                print(e)
        finally:
                connected.remove(websocket)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
      
