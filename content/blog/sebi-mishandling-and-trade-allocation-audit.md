---
slug: sebi-mishandling-and-trade-allocation-audit
title: 'Automating Trade Allocation Compliance: SEBI STP Routing and Client Fair-Treatment
  Audits'
seo_title: Automating SEBI Trade Allocation & Fair-Treatment Audits
short: Automating SEBI Trade Allocation
description: 'How Indian asset managers automate trade allocation compliance: block
  trade execution, pro-rata client fills, SEBI fair-treatment audits, and time-stamping.'
cluster: automation
level: intermediate
order: 35
date: '2026-11-02'
keywords:
- sebi trade allocation compliance automation
- pro rata trade allocation pms aif
- block trade execution fair treatment sebi
- cherry picking prevention algorithms india
- time stamped order allocation audit trail
- sebi inspection trade allocation circular
- automated broker stp allocation
answer: Indian PMS and AIF managers automate trade allocation compliance by implementing
  programmatic block-execution engines that aggregate orders, enforce pro-rata fill
  distribution across client accounts at weighted-average prices, and generate immutable,
  time-stamped audit trails to satisfy SEBI fair-treatment mandates and eliminate
  cherry-picking penalties.
takeaways:
- SEBI strictly prohibits 'cherry-picking,' where favorable trade fills are selectively
  allocated to larger or preferred client accounts.
- Block orders executed across multiple client demats must be allocated on a strict
  mathematical pro-rata basis at the volume-weighted average price (VWAP).
- Pre-trade allocation instructions must be recorded digitally before orders are routed
  to broker terminals.
- Automated compliance engines generate immutable, time-stamped audit trails that
  prove fair treatment during annual SEBI regulatory inspections.
faq:
- q: What is 'cherry-picking' in Indian asset management and why does SEBI penalize
    it?
  a: Cherry-picking occurs when an unethical fund manager places aggregate trades
    and waits until market close to see which trades were profitable. Profitable trades
    are allocated to personal accounts, proprietary funds, or high-value clients,
    while losing trades are dumped into retail or discretionary client accounts. SEBI
    considers this serious fraud and imposes severe bans.
- q: How does statutory pro-rata trade allocation work?
  a: 'If a portfolio manager places an order to buy 10,000 shares across three client
    accounts (Client A: 50%, Client B: 30%, Client C: 20%), but the market only fills
    6,000 shares, the execution engine must allocate exactly 3,000 shares to A, 1,800
    to B, and 1,200 to C, with all three receiving the identical weighted-average
    executed price.'
- q: What documentation does SEBI inspect during a trade allocation audit?
  a: SEBI inspects pre-trade allocation sheets, Order Management System (OMS) time-stamped
    logs, broker contract notes, depository participant transaction statements, and
    allocation distribution files to verify that order sizing was committed before
    execution.
cta:
  heading: Automating your trade allocation or SEBI fair-treatment compliance?
  body: Goldfib Capital builds automated pro-rata trade allocation engines, pre-trade
    commitment logs, and SEBI compliance audit trail systems for Indian fund managers.
  subject: Trade allocation compliance enquiry
---

In multi-account portfolio management, the fair treatment of clients is a non-negotiable regulatory mandate. When a portfolio manager managing 200 individual PMS accounts or multiple AIF schemes executes trades, every client—regardless of whether they have invested ₹50 lakh or ₹50 crore—is entitled to fair, equitable execution.

Historically, unscrupulous market operators engaged in **Cherry-Picking**: placing large speculative orders, observing intraday market movements, and selectively allocating winning trades to preferred accounts while dumping loss-making fills into secondary clients.

To eradicate this malpractice, the Securities and Exchange Board of India (SEBI) notified stringent **Trade Allocation and Fair-Treatment Circulars**. Under current rules, managers must demonstrate pre-trade allocation commitments, mathematical pro-rata distributions, and immutable time-stamped audit logs.

Institutional investment desks satisfy regulatory standards by deploying **Automated Trade Allocation Engines**.

```viz
type: flow
title: "The compliant trade allocation execution lifecycle"
steps:
  - title: "Pre-Trade Allocation Commitment"
    sub: "OMS calculates required quantities per account; generates digital time-stamped allocation matrix before routing."
    tag: "Pre-Trade"
  - title: "Parent Block Order Execution"
    sub: "Aggregated parent order is routed to institutional broker terminal via FIX protocol; executed across market day."
    tag: "Execution"
  - title: "Weighted-Average Price Ingestion"
    sub: "Ingests broker fill reports; calculates exact Volume-Weighted Average Price (VWAP) across all executed lots."
    tag: "VWAP Pricing"
  - title: "Automated Pro-Rata Distribution"
    sub: "Distributes partial or full fills proportionally across client demat accounts down to single-share precision."
    tag: "Allocation"
  - title: "Immutable Audit Trail Archival"
    sub: "Saves digital hash of pre-trade commitment against post-trade fills for one-click SEBI audit export."
    tag: "Compliance"
caption: "Programmatic five-stage pipeline ensuring fair client treatment and zero manual cherry-picking interference."
```

## The Mathematical Principle: Pro-Rata Allocation at VWAP

Under SEBI regulations, manual discretion after execution is prohibited.

If a fund manager places a block order to buy 50,000 shares of an infrastructure company across four client portfolios, and the market provides only a partial fill of 32,000 shares across varying intraday prices:

```viz
type: columns
title: "Compliant partial fill allocation across client accounts (Shares)"
unit: " shs"
data:
  - ["Client 1 (Target: 25k shs)", 16000]
  - ["Client 2 (Target: 15k shs)", 9600]
  - ["Client 3 (Target: 6k shs)", 3840]
  - ["Client 4 (Target: 4k shs)", 2560]
caption: "Strict pro-rata allocation: Every client receives exactly 64% of their target order at the identical weighted-average execution price."
```

The algorithm allocates shares based on the exact pre-trade commitment ratio:
$$\text{Allocated Shares}_i = \text{Total Executed Shares} \times \left( \frac{\text{Target Order}_i}{\sum_{j=1}^{N} \text{Target Order}_j} \right)$$

Every account receives the **identical Volume-Weighted Average Price (VWAP)**:
$$\text{Execution Price} = \frac{\sum (P_k \times Q_k)}{\sum Q_k}$$
No client receives an advantageous price due to early execution.

<p>CTA</p>

## Eliminating Audit Friction During SEBI Inspections

During periodic regulatory inspections, SEBI enforcement officers request trade allocation logs for random trading days. 

Firms that manage allocations manually on Excel spreadsheets take weeks to reconstruct historical trade rationale, frequently facing audit qualifications for timestamp discrepancies.

An automated allocation engine generates a **Certified SEBI Audit Dossier** in one click:
- Proves pre-trade allocation intent was locked prior to market order dispatch.
- Demonstrates mathematical pro-rata distribution across all fills.
- Reconciles final depository demat transfers against broker contract notes.

By automating trade allocation, fund managers protect their firm from regulatory penalties, build operational integrity, and deliver institutional transparency to investors.

To explore fund middle-office infrastructure, read our guide on [PMS & AIF Operations Tech Stack Automation](/blog/pms-aif-operations-automation-tech-stack/) and [SEBI Compliance and Risk Monitoring Automation](/blog/sebi-compliance-risk-monitoring-automation/).
