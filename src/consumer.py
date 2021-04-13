import aio_pika
import asyncio

from configs import RABBITMQ_URL


async def rabbit():
    connection = await aio_pika.connect_robust(url=RABBITMQ_URL)
    queue_name = 'rabbit_queue'

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, auto_delete=True)
        async with queue.iterator() as queue_itr:
            async for message in queue_itr:
                async with message.process():
                    print(message.body)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(rabbit())
    loop.close()
