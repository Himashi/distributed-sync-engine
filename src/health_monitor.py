import time
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class NodeHealthMonitor:
    def __init__(self, failure_threshold_seconds: float = 5.0):
        self.failure_threshold = failure_threshold_seconds
        self.node_registry: Dict[str, float] = {}

    def heartbeat(self, node_id: str):
        self.node_registry[node_id] = time.time()
        logging.info("Heartbeat received from node: '%s'", node_id)

    def check_cluster_health(self) -> Dict[str, str]:
        current_time = time.time()
        health_status = {}
        
        for node_id, last_seen in self.node_registry.items():
            age = current_time - last_seen
            if age > self.failure_threshold:
                health_status[node_id] = "DEAD"
                logging.warning("Node [%s] marked DEAD (silent for %.2f seconds)", node_id, age)
            else:
                health_status[node_id] = "HEALTHY"
                logging.info("Node [%s] status: HEALTHY", node_id)
                
        return health_status

if __name__ == "__main__":
    monitor = NodeHealthMonitor(failure_threshold_seconds=2.0)
    monitor.heartbeat("replica-node-01")
    monitor.check_cluster_health()