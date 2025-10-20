# Distributed Sync Engine

**Core event-driven routing framework and asynchronous state synchronization engine** engineered for high-concurrency distributed systems.

## Architectural Overview
* **Async Event Broker:** Non-blocking publish-subscribe routing engine built on Python's `asyncio` loop.
* **State Synchronizer:** Distributed replica state manager handling conflict resolution and concurrent node synchronization.
* **Resilient Dispatcher:** Guaranteed message delivery pipeline with fault-tolerant error boundaries.

## Getting Started & Local Execution

Follow these instructions to set up the repository locally and verify the distributed modules.

### Prerequisites
* Python 3.11 or higher installed on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/Himashi/distributed-sync-engine.git](https://github.com/Himashi/distributed-sync-engine.git)
cd distributed-sync-engine
```

2. Run Module Tests Locally

You can execute each core component independently using Python's module runner:

Test the Asynchronous Event Broker:

```Bash
python -m src.event_broker
```
Test the State Synchronizer:

```Bash
python -m src.state_synchronizer
```
Test the Node Health Monitor:

```Bash
python -m src.health_monitor
```