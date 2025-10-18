import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class StateSynchronizer:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.state_store: Dict[str, Any] = {}
        self.version_clock: int = 0

    def update_state(self, key: str, value: Any) -> int:
        self.version_clock += 1
        self.state_store[key] = {
            "value": value,
            "version": self.version_clock,
            "origin_node": self.node_id
        }
        logging.info("Node [%s] synchronized state key '%s' at version %d", self.node_id, key, self.version_clock)
        return self.version_clock

    def get_state(self, key: str) -> Dict[str, Any]:
        return self.state_store.get(key, {})

if __name__ == "__main__":
    sync_engine = StateSynchronizer("nexus-node-alpha")
    sync_engine.update_state("cluster_mode", "ACTIVE_REPLICA")