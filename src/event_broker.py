import asyncio
import logging
from typing import Callable, Dict, List, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AsyncEventBroker:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_topic: str, callback: Callable):
        if event_topic not in self.subscribers:
            self.subscribers[event_topic] = []
        self.subscribers[event_topic].append(callback)
        logging.info("Subscribed listener to topic: '%s'", event_topic)

    async def publish(self, event_topic: str, payload: Dict[str, Any]):
        if event_topic not in self.subscribers:
            logging.warning("No active subscribers found for topic: '%s'", event_topic)
            return

        logging.info("Dispatching event on topic '%s' to %d subscribers", event_topic, len(self.subscribers[event_topic]))
        await asyncio.gather(*(cb(payload) for cb in self.subscribers[event_topic]))

async def sample_listener(payload: Dict[str, Any]):
    await asyncio.sleep(0.1)
    logging.info("Received event payload: %s", payload)

if __name__ == "__main__":
    async def main():
        broker = AsyncEventBroker()
        broker.subscribe("node.heartbeat", sample_listener)
        await broker.publish("node.heartbeat", {"node_id": "us-east-cluster-01", "status": "HEALTHY"})

    asyncio.run(main())