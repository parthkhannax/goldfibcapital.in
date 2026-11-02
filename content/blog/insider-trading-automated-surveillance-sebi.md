---
slug: insider-trading-automated-surveillance-sebi
title: 'Automating SEBI Insider Trading Surveillance: PIT Rules, Connected Persons,
  and Trading Windows'
seo_title: Automating SEBI PIT Insider Trading Surveillance
short: Automating SEBI PIT Compliance
description: "How Indian asset managers and listed firms automate SEBI PIT compliance: Structured Digital Databases (SDD), grey lists, and personal trading tracking."
cluster: automation
level: intermediate
order: 24
date: '2026-11-02'
keywords:
- sebi insider trading surveillance automation
- prohibition of insider trading pit compliance
- structured digital database sdd software
- connected persons tracking sebi
- trading window closure automation
- personal account trading pat pre-clearance
- upsi Unpublished Price Sensitive Information
answer: Asset managers automate SEBI Prohibition of Insider Trading (PIT) compliance
  by deploying algorithmic surveillance engines that maintain immutable Structured
  Digital Databases (SDD), track Unpublished Price Sensitive Information (UPSI) access
  logs, enforce automated trading window closures, and cross-reference employee Personal
  Account Trading (PAT) against grey lists and broker contract notes.
takeaways:
- SEBI mandates non-tamperable Structured Digital Databases (SDD) with immutable audit
  trails for every individual possessing UPSI.
- Manual tracking of 'Connected Persons' and immediate relatives using spreadsheets
  is the primary cause of regulatory audit failures.
- Automated Personal Account Trading (PAT) engines require digital pre-clearance and
  programmatically cross-reference broker contract notes.
- Surveillance systems cross-reference internal research meetings with market volume
  spikes to detect front-running and confidential leaks.
faq:
- q: What is a Structured Digital Database (SDD) under SEBI PIT Regulations?
  a: Under Regulation 3(5) of SEBI (Prohibition of Insider Trading) Regulations, 2015,
    every entity handling UPSI must maintain an internal digital database containing
    names, PANs, and timestamps of everyone who shared or received price-sensitive
    information. The database must include non-tamperable audit logs with digital
    signatures and cannot be maintained on simple Excel sheets.
- q: Who qualifies as a 'Connected Person' under SEBI rules?
  a: A Connected Person includes any individual associated with the company in any
    capacity (directors, key managerial personnel, employees, legal advisors, auditors,
    or consultants) who has had access to UPSI during the preceding six months, as
    well as immediate relatives (spouse, parents, siblings, children financially dependent
    on the person).
- q: How does automated trading window closure work?
  a: Trading windows are automatically closed from the end of each financial quarter
    until 48 hours after financial results are published on the stock exchanges. An
    automated compliance engine locks broker execution terminals and denies all Personal
    Account Trading pre-clearance requests during this window.
cta:
  heading: Automating your SEBI PIT compliance or SDD database?
  body: Goldfib Capital builds customized Structured Digital Databases (SDD), automated
    PAT pre-clearance workflows, and insider surveillance engines for Indian financial
    intermediaries.
  subject: SEBI PIT automation enquiry
---

The Securities and Exchange Board of India (SEBI) has elevated insider trading surveillance to the top of its enforcement agenda. Armed with sophisticated data algorithms, artificial intelligence pattern-matching systems, and direct data feeds from depositories (NSDL/CDSL) and telecom providers, SEBI actively investigates front-running, selective information leaks, and unlawful trading patterns across asset management desks and listed corporates.

For compliance officers, managing **SEBI (Prohibition of Insider Trading) Regulations, 2015** using manual spreadsheets and email acknowledgments is an extreme regulatory risk. If a single employee or immediate relative trades a listed security while in possession of Unpublished Price Sensitive Information (UPSI), the entire firm faces regulatory penalties, public reputational censure, and executive disqualification.

Institutional fund managers and listed companies are mitigating regulatory liability by deploying **Automated PIT Surveillance and Structured Digital Database (SDD) Engines**.

```viz
type: tree
title: "The automated SEBI PIT compliance architecture"
root:
  label: "PIT Surveillance Engine"
  children:
    - label: "UPSI Lifecycle Management"
      children:
        - label: "Structured Digital Database (SDD)"
        - label: "Non-Tamperable Timestamps"
        - label: "PAN & Aadhaar Identity Mapping"
    - label: "Access & Trading Controls"
      children:
        - label: "Automated Trading Window Lockouts"
        - label: "Restricted / Grey List Firewalls"
        - label: "Personal Account Trading (PAT) Engine"
    - label: "Surveillance & Audit"
      children:
        - label: "Broker Contract Note Reconciliation"
        - label: "Unusual Volume & P&L Alerts"
        - label: "One-Click Regulatory Audit Export"
caption: "Integrated compliance architecture enforcing pre-trade lockouts, immutable digital logs, and automated depository reconciliations."
```

## The Mandatory Structured Digital Database (SDD)

Under Regulation 3(5) and 3(6) of the SEBI PIT Regulations, maintaining a **Structured Digital Database (SDD)** is a non-negotiable statutory requirement:
- **No Excel Spreadsheets**: SEBI circulars explicitly prohibit maintaining SDD on manual Excel workbooks or shared spreadsheets, as cell timestamps can be edited retrospectively.
- **Immutable Audit Trails**: The database must preserve chronological logs of every entry, modification, and deletion. Once an entry is made (recording that Analyst X received preliminary Q3 earnings data), the record cannot be altered.
- **Identity Information**: The system must log the Permanent Account Number (PAN) or government-recognized identity of the sender, the recipient, the precise nature of UPSI, and the exact business purpose for sharing.

```viz
type: columns
title: "Quarterly audit time spent on PIT compliance (hours)"
unit: " hrs"
data:
  - ["Manual Spreadsheet Logging & Email Chasing", 75]
  - ["Automated SDD Audit Trail Logging", 4]
  - ["Manual Personal Account Trading Reviews", 45]
  - ["Automated Contract Note OCR & Reconciliation", 3]
  - ["Manual Trading Window Notification Dispatch", 18]
  - ["Automated Exchange API Trading Window Locks", 0.5]
caption: "Automation reduces recurring PIT compliance and audit preparation time from 138 hours to under 8 hours per quarter."
```

## Automating Personal Account Trading (PAT) Pre-Clearance

Employees working at fund management desks, investment banks, and research desks have personal investment accounts. To prevent conflicts of interest and front-running:

```viz
type: flow
title: "Automated Personal Account Trading (PAT) workflow"
steps:
  - title: "Digital Pre-Clearance Request"
    sub: "Employee submits order details (ticker, quantity, proposed broker, account) via compliance portal."
    tag: "Submission"
  - title: "Algorithmic Grey List & Window Scan"
    sub: "System verifies security against restricted list, active research coverage, and trading window status."
    tag: "Rule Engine"
  - title: "Automated Approval / Rejection"
    sub: "Instant approval granted with a 7-day execution window, or immediate rejection with compliance code."
    tag: "Decision"
  - title: "Broker Contract Note Reconciliation"
    sub: "Employee uploads broker contract note (or automated API ingest); system verifies price, date, and size."
    tag: "Reconciliation"
caption: "Programmatic four-stage personal trading workflow eliminating unauthorized employee dealing."
```

1. **Automated Grey List Screening**: If an analyst is currently writing an initiation report on a mid-cap manufacturing stock, that stock is automatically placed on the firm's confidential **Grey List**. Any personal buy or sell request in that security is instantly blocked by the system.
2. **Execution Window Validation**: If pre-clearance is approved, the employee has a mandatory statutory window (typically 7 trading days) to execute. If unexecuted, the approval lapses automatically.
3. **Depository Account Auditing**: Modern compliance engines connect directly to broker APIs or require automated uploading of broker contract notes, cross-referencing executed fills against the pre-cleared quantity.

<p>CTA</p>

## Managing 'Connected Persons' and Immediate Relatives

A frequent source of SEBI enforcement action is trading conducted by spouses, dependent parents, or siblings.

The compliance engine maintains an automated registry of **Connected Persons and Immediate Relatives**:
- Captures PAN and demat account numbers for all financially dependent family members.
- Automatically extends trading window closures and grey-list restrictions to relative demat accounts.
- Generates annual confirmation workflows where employees digitally re-verify their list of dependent relatives.

By upgrading from manual compliance record-keeping to an automated PIT surveillance engine, asset managers insulate their firm from regulatory penalties and build an unassailable institutional compliance record.

To learn more about fund operations, read our guide on [SEBI Compliance and Risk Monitoring Automation](/blog/sebi-compliance-risk-monitoring-automation/) and [PMS & AIF Operations Tech Stack Automation](/blog/pms-aif-operations-automation-tech-stack/).
