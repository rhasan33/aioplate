import asyncio
import aio_pika

from configs import RABBITMQ_URL


async def main(loop):
    connection = await aio_pika.connect_robust(
        RABBITMQ_URL, loop=loop
    )

    async with connection:
        routing_key = "rabbit_queue"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body="Hello {}".format(routing_key).encode()),
            routing_key=routing_key,
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
