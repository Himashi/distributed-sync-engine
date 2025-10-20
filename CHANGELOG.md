# Changelog

## 1.1.0
- Distributed heartbeat and node health monitoring system (`src/health_monitor.py`) to detect cluster failures and automate replica node liveness checks.

## 1.0.0
- Initial release of asynchronous event broker publish-subscribe routing engine (`src/event_broker.py`) and CI workflows.
- Distributed state synchronization engine with version clock tracking (`src/state_synchronizer.py`) for multi-node replica coordination.