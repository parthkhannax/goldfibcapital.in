---
slug: market-data-pipeline-websocket-nse-tick
title: 'High-Throughput Market Data Ingestion: Building Tick-Level WebSocket Pipelines
  on NSE'
seo_title: Building High-Throughput WebSocket Data Pipelines on NSE
short: NSE WebSocket Tick Data Pipeline
description: 'How quantitative desks build low-latency market data pipelines on NSE:
  WebSocket streaming, tick-level order book reconstruction, and Redis time-series
  storage.'
cluster: automation
level: advanced
order: 30
date: '2026-11-02'
keywords:
- nse websocket market data pipeline python
- tick level order book reconstruction india
- low latency market data ingestion nse
- redis time series tick storage python
- zerodha kite dhan websocket streamer
- quantitative trading infrastructure india
- market depth l2 l3 data nse
answer: Quantitative trading desks build low-latency market data infrastructure on
  the National Stock Exchange (NSE) by implementing asynchronous Python WebSocket
  pipelines. These engines ingest binary tick packets, reconstruct real-time Level
  2 (5-depth) order books, buffer high-frequency data in memory using Redis time-series,
  and stream normalized bars into algorithmic strategy engines.
takeaways:
- REST polling APIs fail during high-volatility market opens; asynchronous WebSockets
  are mandatory for live trading execution.
- NSE tick data is streamed as compact binary packets, requiring efficient struct
  unpacking and bitwise decoding in Python.
- Level 2 market depth streams provide real-time bid-ask queues, allowing execution
  algorithms to calculate dynamic order book imbalance.
- High-throughput time-series databases (TimescaleDB, Redis, QuestDB) persist tick-level
  data for post-trade slippage analysis.
faq:
- q: What is the difference between Level 1, Level 2, and Level 3 market data on the
    NSE?
  a: Level 1 data provides the best bid and ask price with traded volume. Level 2
    (L2) data provides the top 5 bids and asks with corresponding quantities (standard
    market depth). Level 3 (L3 / tick-by-tick) provides individual order additions,
    modifications, and cancellations across the entire order book, typically accessible
    only via direct exchange co-location.
- q: Why is asynchronous programming (asyncio) essential for Indian market data pipelines?
  a: During market openings, the NSE generates tens of thousands of tick updates per
    second across cash and derivative contracts. Synchronous blocking code causes
    buffer overflows and network packet drops. Asynchronous event loops (`asyncio`
    / `aiohttp`) ingest network streams without blocking strategy computation.
- q: How should tick data be stored efficiently without consuming terabytes of disk
    space?
  a: Desks use specialized columnar time-series databases (such as QuestDB, ClickHouse,
    or TimescaleDB) that utilize delta-of-delta timestamp compression and Gorillas
    floating-point compression, reducing raw tick storage footprints by over 80%.
cta:
  heading: Building low-latency market data pipelines for NSE trading?
  body: Goldfib Capital engineers asynchronous WebSocket ingestors, order-book reconstruction
    engines, and high-frequency time-series storage for Indian quant desks.
  subject: Market data pipeline enquiry
---

In systematic quantitative trading, data latency and integrity are paramount. If an execution algorithm receives market prices delayed by even 500 milliseconds, or if a sudden volatility spike drops network packets, algorithmic fills suffer severe slippage.

Many retail quants and emerging funds rely on standard REST polling APIs (e.g., polling an exchange or broker endpoint every second). 

During market opens or major RBI monetary policy announcements, REST servers choke under traffic, returning rate-limit errors (HTTP 429) or stale cached quotes.

Institutional quantitative desks build **High-Throughput Asynchronous WebSocket Streaming Pipelines** to ingest, decode, and store live tick data across thousands of NSE equity and derivative instruments.

```viz
type: flow
title: "The low-latency tick data processing pipeline"
steps:
  - title: "Binary WebSocket Stream Ingest"
    sub: "Asynchronous event loop maintains persistent TCP connection with broker/exchange market data gateways."
    tag: "Network Layer"
  - title: "Binary Struct Unpacking"
    sub: "C-based Python decoders unpack raw binary bytes into structured price, volume, and depth tuples in < 50 μs."
    tag: "Decoding"
  - title: "In-Memory Order Book Reconstruction"
    sub: "Rebuilds real-time Level 2 (5-depth) bid/ask queues, computing instant order-book imbalance ratios."
    tag: "Order Book"
  - title: "ZeroMQ Pub/Sub Broadcast"
    sub: "Distributes normalized tick streams to independent strategy execution engines via local IPC sockets."
    tag: "IPC Routing"
  - title: "Columnar Time-Series Archival"
    sub: "Batches ticks into ClickHouse / QuestDB for end-of-day execution slippage and transaction cost analysis."
    tag: "Persistence"
caption: "Sub-millisecond data pipeline converting high-frequency exchange streams into actionable strategy signals."
```

## Decoding Binary Tick Packets: Struct vs JSON

High-throughput brokers (such as Zerodha Kite, Dhan, or institutional FIX gateways) do not transmit tick data in human-readable JSON. JSON is too bandwidth-intensive and introduces massive string parsing overhead.

Instead, ticks are transmitted as **compact binary byte arrays**:
- A single market packet consists of a 44-byte or 184-byte binary payload containing instrument token, last traded price (multiplied by 100 as an integer), traded quantity, and 5 levels of market depth.
- Using Python's native `struct` module, the decoder unpacks binary data into memory in microseconds:
```python
import struct
# Unpack token, ltp, last_quantity, volume
token, ltp, qty, vol = struct.unpack(">IIII", packet[0:16])
real_price = ltp / 100.0
```

```viz
type: columns
title: "Decoding latency: Binary struct vs JSON parsing (microseconds)"
unit: " μs"
data:
  - ["Raw Binary Struct Unpacking", 1.8]
  - ["Fast C-JSON (orjson/ujson)", 45.0]
  - ["Standard Python json.loads()", 185.0]
caption: "Binary struct unpacking processes market updates 100x faster than JSON, preventing buffer bloat during market panics."
```

## Level 2 Market Depth and Order Book Imbalance

Beyond the last traded price (LTP), the most valuable short-term predictive signal in cash equities is **Order Book Imbalance (OBI)**:

```viz
type: quadrant
title: "Market depth signal utility vs latency sensitivity"
x_label: "Computational Latency Requirement"
y_label: "Predictive Short-Term Alpha Signal"
quadrants:
  - "Low Latency / High Alpha (OBI Signals)"
  - "Sub-Millisecond Alpha Sweet Spot"
  - "Low Signal / Slow Execution"
  - "Fast / Low Signal"
points:
  - x: 0.85
    y: 0.90
    label: "Level 2 Order Book Imbalance"
    hl: true
  - x: 0.40
    y: 0.45
    label: "LTP / Moving Average Crossover"
  - x: 0.92
    y: 0.70
    label: "Tick-by-Tick Microstructure"
  - x: 0.20
    y: 0.20
    label: "End-of-Day EOD Bar"
caption: "Level 2 Order Book Imbalance provides potent short-term execution alpha when processed with low latency."
```

The pipeline continuously reconstructs the top 5 bids and asks:
$$\text{OBI} = \frac{\sum_{i=1}^{5} Q_{\text{bid}, i} - \sum_{i=1}^{5} Q_{\text{ask}, i}}{\sum_{i=1}^{5} Q_{\text{bid}, i} + \sum_{i=1}^{5} Q_{\text{ask}, i}}$$
When OBI surges above +0.65, buy pressure heavily outweighs sell liquidity, signaling favorable execution conditions for accumulation algorithms.

<p>CTA</p>

## Columnar Time-Series Storage: ClickHouse and QuestDB

Storing millions of daily ticks for the entire NSE universe requires high-performance columnar time-series storage:
- Traditional relational databases (PostgreSQL, MySQL) collapse under the write load of 50,000 writes/second.
- Columnar engines (**ClickHouse**, **QuestDB**) compress time-series data using gorilla and double-delta compression, allowing instantaneous historical queries across billions of ticks for backtesting execution slippage.

By engineering low-latency WebSocket pipelines and columnar storage, quantitative desks build institutional trading infrastructure capable of capturing persistent alpha in fast-moving Indian markets.

To explore how data feeds integrate with factor models, read our guide on [Building an Institutional Python Backtesting Engine](/blog/custom-backtesting-engine-python-nse/) and [Quantitative Factor Models in Indian Equities](/blog/quantitative-factor-models-indian-equities/).
