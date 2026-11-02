---
slug: automated-broker-contract-note-parser
title: 'Automated PDF Contract Note Parsing: OCR, Multi-Broker Extraction, and STP
  Integration'
seo_title: Automated Broker Contract Note Parser for Indian Equities
short: Contract Note OCR & STP Parsing
description: 'How investment desks automate broker contract note processing: OCR,
  multi-broker PDF parsing, statutory levy reconciliation, and Straight-Through Processing.'
cluster: automation
level: intermediate
order: 29
date: '2026-11-02'
keywords:
- automated broker contract note parser
- pdf contract note ocr python
- stt sebi turnover levy reconciliation
- zerodha icici direct contract note extraction
- straight through processing stp fund operations
- automated trade reconciliation india
- trade allocation contract note parsing
answer: Investment desks automate trade reconciliation by deploying automated PDF
  parsers and OCR pipelines that ingest broker contract notes across multiple institutional
  brokers. These engines extract executed order timestamps, net prices, ISINs, and
  statutory levies (STT, GST, Stamp Duty), reconciling trade fills against internal
  Order Management Systems (OMS) in seconds.
takeaways:
- Manual contract note entry is slow, prone to human error, and delays T+1 custodian
  trade matching.
- Indian brokers issue contract notes in fragmented, proprietary PDF layouts with
  password encryption.
- Automated parsers extract trade tables, recalculate statutory levies to ₹0.01 precision,
  and flag overcharges.
- Straight-Through Processing (STP) converts unstructured PDF text into structured
  JSON/CSV feeds for fund accounting systems.
faq:
- q: Why are Indian broker contract notes difficult to parse automatically?
  a: Brokers (Kotak Securities, ICICI Securities, Motilal Oswal, Zerodha) format contract
    notes in vastly different table layouts, font encodings, and password-protected
    PDF structures. Furthermore, transactions span multiple pages with separate sections
    for equity delivery, F&O derivatives, and statutory tax annexures.
- q: How do automated parsers verify statutory levies?
  a: The parser programmatically recalculates Securities Transaction Tax (0.1%), SEBI
    turnover charges (₹10/crore), Exchange turnover fees, Stamp Duty (0.015%), and
    CGST/SGST/IGST (18% on brokerage) based on gross traded value, alerting operations
    if the broker has overcharged the account.
- q: Can the parser handle password-protected institutional PDFs?
  a: Yes. Institutional parsing engines integrate automated credential vaults that
    programmatically decrypt files using pre-registered entity PANs or custom client
    passwords upon secure SFTP ingestion.
cta:
  heading: Automating contract note ingestion across multiple brokers?
  body: Goldfib Capital builds multi-broker PDF parsers, automated tax recalculation
    engines, and STP middle-office pipelines for Indian wealth desks and family offices.
  subject: Contract note parser automation enquiry
---

Every evening after market close on the NSE and BSE, Indian investment desks receive dozens of digital **Broker Contract Notes**. These legal documents—issued as password-protected PDF files—detail every executed trade, execution timestamp, exchange trade ID, settlement price, and statutory tax levy.

For a family office or PMS desk routing orders through three to five institutional brokers (e.g., Kotak, ICICI Securities, Axis Capital, Zerodha), processing these PDFs manually is an operational bottleneck. Junior operations personnel spend two to three hours every evening opening PDFs, manually copying execution prices and tax numbers into accounting workbooks, and checking for errors.

A single transposed digit in an executed price or an unrecorded stamp duty charge creates a **Trade Break** during T+1 custodian settlement.

Institutional desks replace human data entry with an **Automated PDF Contract Note Parsing Pipeline**.

```viz
type: flow
title: "The automated contract note parsing pipeline"
steps:
  - title: "Automated SFTP / Email Ingestion"
    sub: "Monitors dedicated compliance inboxes; automatically ingests and decrypts password-protected PDF notes."
    tag: "16:30 IST"
  - title: "Layout Detection & Table Extraction"
    sub: "Computer vision and coordinate-based text extractors parse broker-specific table structures and ISIN rows."
    tag: "Parsing"
  - title: "Statutory Levy Recalculation"
    sub: "Programmatically verifies STT, SEBI turnover fees, Stamp Duty, and GST against statutory exchange rules."
    tag: "Tax Engine"
  - title: "Three-Way OMS Matching"
    sub: "Matches fills against internal Order Management System logs; flags price or quantity breaks instantly."
    tag: "Reconciliation"
  - title: "Accounting System Dispatch"
    sub: "Transmits structured JSON trade records directly into fund accounting ledgers without human intervention."
    tag: "STP Output"
caption: "Automated Straight-Through Processing (STP) pipeline converting raw PDF contract notes into reconciled accounting entries."
```

## The Structural Challenge: Multi-Broker Layout Fragmentation

Unlike mature Western markets where trades are exchanged via standardized electronic FIX drops, Indian brokers generate diverse PDF document layouts:

```viz
type: columns
title: "Processing velocity: Manual vs Automated parsing"
unit: " mins"
data:
  - ["Manual Entry (5 Broker PDFs / 60 Trades)", 110]
  - ["Automated Multi-Broker Extraction Pipeline", 0.5]
caption: "Automation cuts contract note data ingestion from nearly two hours to under 30 seconds with 100% mathematical accuracy."
```

- **Password Protection**: Every file is encrypted using combinations of the client's PAN and date of birth.
- **Embedded Fonts and Scanned Artifacts**: Many legacy institutional brokers generate PDFs with non-standard font encodings that produce garbled text when parsed using simple open-source text extractors.
- **Tax Annexure Separation**: Taxes and charges are often broken into separate summary tables at the end of the document, requiring reconciliation between line-item brokerage and aggregate exchange turnover levies.

## Programmatic Tax and Levy Verification

Broker billing errors are surprisingly common. An automated engine verifies every statutory fee down to ₹0.01:

```viz
type: waterfall
title: "Statutory levies breakdown on ₹10 Lakh equity delivery trade"
prefix: "₹"
unit: ""
steps:
  - ["Gross Traded Value", 1000000]
  - ["Securities Transaction Tax (0.1%)", -1000]
  - ["Exchange Turnover Fee (0.003%)", -30]
  - ["SEBI Turnover Charge (₹10/Cr)", -1]
  - ["Stamp Duty (0.015%)", -150]
  - ["Brokerage Commission (5 bps)", -500]
  - ["GST (18% on Brokerage & Exchange)", -95.5]
  - ["=Net Settlement Debit", 1001776.5]
caption: "Programmatic recalculation ensures brokers do not inflate brokerage commissions or miscalculate state stamp duties."
```

If the broker's invoice reflects a 0.15% STT charge or misapplies interstate IGST instead of local CGST/SGST, the system flags the invoice with a `TAX_VARIANCE_ERROR` before payment is released.

<p>CTA</p>

## Achieving True Straight-Through Processing (STP)

By transforming unstructured PDF documents into clean, standardized JSON data objects, fund managers achieve **Straight-Through Processing**:
- Executed fills flow directly from broker emails into the fund accounting system.
- Trade breaks are identified within minutes of market close, leaving ample time to resolve discrepancies with the broker before overnight clearing cutoffs.
- Operations teams are freed from manual data entry, enabling the desk to scale AUM without adding back-office headcount.

To explore how trade reconciliation integrates with custodial reporting, read our guide on [PMS & AIF Operations Tech Stack Automation](/blog/pms-aif-operations-automation-tech-stack/) and [SEBI Compliance and Risk Monitoring Automation](/blog/sebi-compliance-risk-monitoring-automation/).
