---
slug: sebi-compliance-risk-monitoring-automation
title: "Automating SEBI Portfolio Limits and Risk Checks for PMS and AIF Desks"
seo_title: "SEBI Compliance & Risk Monitoring Automation"
short: "SEBI Compliance Risk Automation"
description: "How investment desks automate SEBI regulatory limits: 10% single-stock caps, 25% sector limits, unlisted asset ceilings, and PIT insider trading checks."
cluster: automation
level: intermediate
order: 5
date: 2026-11-02
keywords:
  - "sebi compliance automation pms aif"
  - "sebi 10 percent single stock limit check"
  - "portfolio risk management software india"
  - "sebi pit compliance automated monitoring"
  - "aif cat 2 investment restriction checks"
  - "automated pre trade post trade compliance sebi"
  - "fund compliance monitoring tool"
answer: "Investment managers automate SEBI regulatory compliance by running algorithmic pre-trade and post-trade rule engines that continuously validate order sizing against statutory thresholds. These systems enforce 10% single-stock limits, 25% sector caps, unlisted equity ceilings, and SEBI Prohibition of Insider Trading (PIT) restricted list checks before orders reach broker execution desks."
takeaways:
  - "Passive breaches caused by organic stock price appreciation require algorithmic rebalancing workflows to restore compliance within statutory grace periods."
  - "Automated pre-trade checks prevent active limit violations by computing hypothetical post-trade portfolio weights before orders are routed to exchange terminals."
  - "SEBI Prohibition of Insider Trading (PIT) regulations mandate automated grey list cross-referencing and personal account trading (PAT) pre-clearances for investment personnel."
  - "Automated compliance monitoring builds immutable audit trails, reducing quarterly SEBI audit preparation time from weeks to hours."
faq:
  - q: "What is the difference between an active and a passive limit breach under SEBI rules?"
    a: "An active breach occurs when a fund manager executes a new trade that pushes an asset or sector concentration above statutory limits (e.g., buying shares that push a position to 10.5%). A passive breach occurs organically without trading, such as when a 9.5% holding rallies sharply while the rest of the portfolio declines, pushing its weight above 10%."
  - q: "What is the SEBI single-issuer limit for Portfolio Management Services (PMS)?"
    a: "Under SEBI (Portfolio Managers) Regulations, 2020, a portfolio manager cannot invest more than 10% of a client's portfolio value in listed securities of a single issuer, unless a specific discretionary mandate or accredited investor waiver is explicitly documented."
  - q: "How do automated compliance systems handle Structured Digital Databases (SDD) under PIT regulations?"
    a: "Automated SDD systems log every instance of Unpublished Price Sensitive Information (UPSI) sharing with exact timestamps, PAN numbers of all recipients, nature of information, and purpose of sharing, creating non-tamperable audit logs mandated by SEBI."
  - q: "Can compliance automation handle Category 1 and Category 2 AIF unlisted asset caps?"
    a: "Yes. The rules engine models specific investment restrictions under SEBI AIF Regulations, 2012, including the 25% corpus limit in a single investee company for Cat 1/2 AIFs (10% for Cat 3 AIFs) and unlisted exposure thresholds."
cta:
  heading: "Need automated SEBI compliance and limit monitoring?"
  body: "Goldfib Capital builds customized pre-trade compliance firewalls, automated regulatory reporting engines, and risk monitors for Indian PMS and AIF funds."
  subject: "SEBI compliance automation enquiry"
---

Regulatory compliance in Indian asset management has entered an era of zero tolerance. The Securities and Exchange Board of India (SEBI) has intensified supervisory audits, deploying automated surveillance systems to detect insider trading, front-running, and portfolio limit breaches across Portfolio Management Services (PMS) and Alternative Investment Funds (AIFs).

For compliance officers and Chief Risk Officers (CROs), monitoring regulations manually using end-of-day Excel exports is an unsustainable gamble. In fast-moving markets, a single rogue order or an unanticipated corporate action can cause an active regulatory breach within seconds.

Institutional asset managers are mitigating regulatory liability by implementing **Automated Pre-Trade and Post-Trade Compliance Engines**. These systems sit between portfolio managers and broker execution rails, intercepting orders to enforce SEBI statutory caps and internal risk mandates programmatically.

```viz
type: tree
title: "Automated compliance and risk monitoring engine"
root:
  label: "Compliance & Risk Gateway"
  children:
    - label: "Pre-Trade Prevention"
      children:
        - label: "Single-Stock Limit (10% Cap)"
        - label: "Sector Exposure (25% Cap)"
        - label: "Restricted Grey List Check"
        - label: "Liquidity / ADTV Capacity Check"
    - label: "Post-Trade Surveillance"
      children:
        - label: "Passive Breach Monitoring"
        - label: "EOD Custodian Re-Verification"
        - label: "Personal Trading (PAT) Recs"
    - label: "Regulatory Reporting"
      children:
        - label: "SEBI Monthly Annexure XML"
        - label: "Structured Digital Database (SDD)"
        - label: "Immutable Audit Trail Export"
caption: "Comprehensive risk architecture intercepting orders before market routing and generating statutory SEBI audit trails automatically."
```

## The regulatory limits every Indian fund must enforce

SEBI mandates strict investment limits across investment vehicles. Violations trigger regulatory inspection notices, public disclosure penalties, and reputational damage.

```viz
type: columns
title: "Statutory concentration ceilings across Indian fund structures"
unit: "%"
data:
  - ["PMS Single-Stock Cap", 10.0]
  - ["PMS Sector Exposure Limit", 25.0]
  - ["Cat 3 AIF Single-Investee Cap", 10.0]
  - ["Cat 1 & 2 AIF Single-Investee Cap", 25.0]
  - ["Associate Group Entity Cap (AIF)", 25.0]
caption: "SEBI statutory concentration caps: Cat 3 AIFs and PMS are bound by a 10% single-issuer ceiling, while Cat 1 and 2 AIFs have a 25% single-company limit."
```

### 1. The 10% Single-Stock Limit
Under SEBI (Portfolio Managers) Regulations, 2020, a PMS cannot allocate more than 10% of a client's portfolio corpus to a single listed stock. Similarly, Category 3 AIFs cannot invest more than 10% of their net assets in a single investee company.
- **The Active Breach Hazard**: A portfolio manager places a buy order for ₹2 crore of Infosys when the portfolio already holds ₹9.2 crore against a total AUM of ₹100 crore. If executed, the position reaches 11.2%, committing an active regulatory violation.
- **The Passive Breach Trap**: A stock purchased at 8.5% portfolio weight surges 35% in three weeks due to an earnings blowout, while other holdings stagnate, pushing its portfolio weight to 11.1%. SEBI grants a statutory grace period (typically 30 days) to rebalance back below 10%, but manual spreadsheets frequently miss the ticking clock.

### 2. The 25% Sector Concentration Ceiling
SEBI restricts fund exposure to any single economic sector (e.g., Financial Services, Information Technology, Healthcare) to 25% of AUM. Determining sectoral classification requires mapping National Industrial Classification (NIC) codes or AMFI sector definitions to eliminate ambiguous company categorizations.

### 3. Associate and Related-Party Entity Limits
Under SEBI AIF Regulations, 2012, funds cannot deploy more than 25% of their investable funds into associate companies or group entities of the sponsor or investment manager without supermajority unitholder approval.

## Pre-Trade Compliance: Halting breaches before execution

Post-trade alerts are fundamentally reactive—by the time a compliance officer identifies a breach in an end-of-day report, the trade has already settled on the exchange, and the violation has legally occurred.

Modern compliance architectures implement **Algorithmic Pre-Trade Interception**:

```viz
type: flow
title: "The pre-trade compliance verification pipeline"
steps:
  - title: "Order Entry & Intent Capture"
    sub: "Portfolio manager inputs target ticker, quantity, limit price, and execution account in OMS."
    tag: "01. OMS Entry"
  - title: "Hypothetical Portfolio Simulation"
    sub: "Engine calculates simulated post-trade portfolio weights, factoring in active intraday market values."
    tag: "02. Simulation"
  - title: "Statutory & Mandate Check"
    sub: "Tests single-stock, sector, associate caps, cash drag, and minimum ticket sizes against SEBI and client IM."
    tag: "03. Rules Engine"
  - title: "SEBI PIT Grey List Screening"
    sub: "Automated scan of restricted trading lists to prevent insider trading violations across firm personnel."
    tag: "04. PIT Check"
  - title: "Execution Decision"
    sub: "Pass: Routes order via FIX protocol to broker terminal. Fail: Hard block with compliance escalation code."
    tag: "05. Routing"
caption: "Orders must pass five programmatic tests in under 20 milliseconds before reaching exchange broker rails."
```

If an order pushes a position above 9.7%, the system triggers a **Soft Warning**, requiring the portfolio manager to re-verify sizing. If an order attempts to breach 10.0%, the system executes a **Hard Block**, preventing the order from reaching the broker terminal.

## SEBI PIT Regulations and Structured Digital Databases (SDD)

Insider trading compliance under the SEBI (Prohibition of Insider Trading) Regulations, 2015 is a top enforcement priority. SEBI mandates that every intermediary handling Unpublished Price Sensitive Information (UPSI) must maintain an automated **Structured Digital Database (SDD)**.

Key compliance requirements enforced programmatically include:
- **Restricted / Grey List Automation**: When an analyst conducts research or enters confidential discussions with a listed issuer, the stock is automatically tagged on the firm's internal Grey List. Any order in that security—whether for fund portfolios or employee Personal Account Trading (PAT)—is automatically locked.
- **Non-Tamperable Audit Logs**: SEBI regulations mandate that SDD records must preserve entry timestamps, the PAN of the person sharing and receiving UPSI, and the precise nature of the confidential data. The database must include internal controls ensuring that timestamps and entries cannot be altered or deleted retrospectively.

```viz
type: bars
title: "Audit preparation & investigation time (days per quarter)"
unit: " days"
data:
  - ["Manual Spreadsheet Audit Compilation", 18]
  - ["Automated Regulatory Engine Audit Export", 1]
  - ["Manual Personal Account Trading (PAT) Recs", 12]
  - ["Automated Broker Contract Note PAT Match", 1]
  - ["Manual SEBI Monthly Annexure Filing", 8]
  - ["Automated One-Click SEBI XML Generation", 0.5]
caption: "Automation reduces quarterly regulatory audit preparation and compliance filing time from 38 days to under 3 days per quarter."
```

<p>CTA</p>

## Managing passive breaches and dynamic rebalancing

A common failure in fund compliance is neglecting **passive limit breaches**. 

Consider a fund with ₹100 crore AUM holding ₹9.5 crore of a mid-cap manufacturing stock. If the stock rallies 20% while broad markets fall 5%, the stock value rises to ₹11.4 crore against a total fund value of ₹98 crore—a portfolio weight of **11.63%**.

An automated compliance system manages passive breaches through three automated workflows:
1. **Automated Ticking Clock**: The moment an asset crosses 10.0% due to price appreciation, the engine logs a passive breach timestamp and initiates a 30-day countdown in accordance with SEBI guidelines.
2. **Rebalancing Order Generator**: The system calculates the exact number of shares required to sell to restore portfolio concentration back to an optimal target (e.g., 9.0%, creating a protective buffer).
3. **Escalation Notifications**: Automated alerts notify the portfolio manager at 15 days, 7 days, and 48 hours prior to statutory grace period expiry.

By moving from manual oversight to automated risk infrastructure, Indian fund managers transform compliance from an operational friction into an institutional competitive advantage that builds lasting LP trust.

For further insights into fund structuring and operational scaling, read our analysis on [PMS vs AIF vs Direct Equity in India](/blog/pms-vs-aif-vs-direct-equity-india/) and [Promoter Pledging & Shareholding Signals](/blog/promoter-pledging-shareholding-signals/).
