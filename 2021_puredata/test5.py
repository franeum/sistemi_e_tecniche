#!/usr/bin/env python3

import aioserial
import asyncio
import asyncio_dgram

async def udp_echo_server():
    stream = await asyncio_dgram.bind(("127.0.0.1", 7000))

    print(f"Serving on {stream.sockname}")

    while True:
        data, remote_addr = await stream.recv()
        print(f"Echoing {data.decode()!r}")
    #await stream.send(data, remote_addr)

    #await asyncio.sleep(0.5)
    #print(f"Shutting down server")

async def udp_echo_client(v):
    stream = await asyncio_dgram.connect(("127.0.0.1", 8000))

    await stream.send(str.encode(v))
    #data, remote_addr = await stream.recv()
    #print(f"Client received: {data.decode()!r}")

    stream.close()

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        #print((await aioserial_instance.read_async()).decode(errors='ignore'), end='', flush=True)
        value = aioserial_instance.read_async()
        val = (await value).decode(errors='ignore')
        await udp_echo_client(val)

ser = aioserial.AioSerial(port='/dev/ttyUSB0', baudrate=115200)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(read_and_print(ser), udp_echo_server()))


if __name__ == "__main__":
    main()
