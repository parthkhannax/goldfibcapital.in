---
slug: ais-form-26as-capital-gains-india
title: "AIS, Form 26AS and Capital Gains Statements: India's Answer to the K-1 Tax Document"
seo_title: "AIS vs Form 26AS: Capital Gains Tax Documents in India"
short: "AIS, 26AS & capital gains statements"
description: "What AIS, TIS, Form 26AS and broker capital gains statements show, how they differ, and how investors reconcile them before filing ITR in India."
cluster: investor-tax
level: beginner
order: 2
date: 2026-10-10
keywords: [AIS income tax, Form 26AS, AIS vs 26AS, capital gains statement India, tax documents for investors India, TIS income tax, K1 tax document India]
answer: "Indian investors have no single K-1 style document. Instead, three sources must agree: Form 26AS (tax deducted and paid against your PAN), the Annual Information Statement or AIS (everything reported about you, including share sales, dividends and interest), and your broker or mutual fund capital gains statement (cost, holding period and gain per lot). Reconcile them, fix mismatches through AIS feedback, then file your ITR."
takeaways:
  - "Form 26AS is about tax already paid. AIS is about income reported. You need both."
  - "AIS shows sale value but often not your cost. The broker statement fills that gap."
  - "Mismatches between AIS and your ITR are the most common trigger for tax notices."
  - "Disagree with an AIS entry? Submit feedback on the portal before you file."
faq:
  - q: "What is the difference between AIS and Form 26AS?"
    a: "Form 26AS mainly shows tax deducted or collected at source and advance or self-assessment tax paid against your PAN. AIS is broader. It lists income and transactions reported by banks, brokers, registrars and companies, such as share sales, dividends, interest and mutual fund redemptions. TIS is a summary of AIS by income category."
  - q: "Is there a K-1 tax document in India?"
    a: "No. The US K-1 reports a partner's share of partnership income. In India, unitholders of AIFs and REITs/InvITs get a statement of income from the fund (often Form 64C/64D for pass-through AIFs), and stock and mutual fund investors rely on AIS plus broker capital gains statements."
  - q: "Where do I get my capital gains statement?"
    a: "Your broker provides a tax P&L or capital gains report in its back-office console. For mutual funds, CAMS and KFintech issue consolidated capital gains statements across fund houses. Use these for cost and holding period, since AIS usually shows only sale value."
  - q: "What if AIS shows wrong information?"
    a: "Log in to the income tax portal, open AIS, and submit feedback on the specific entry, for example that it is duplicated or belongs to someone else. The reporting entity may be asked to confirm. File your return based on correct figures and keep evidence."
cta:
  heading: "Running a family portfolio with five brokers and three PANs?"
  body: "Goldfib builds automated reconciliations that pull broker, registrar and AIS data into one verified ledger, so tax season is a review rather than a scramble."
  subject: "Portfolio reconciliation enquiry"
---

US investors wait for a K-1 each spring. Indian investors do not get one neat document. They get three overlapping ones, and the tax department already holds a copy of most of them.

That changes the job. **You are not reporting your gains to the department. You are confirming numbers it already has.** Any gap between your return and its data becomes a notice.

## The three documents

```viz
type: tree
title: "The Indian investor's tax paperwork"
node_width: 200
root:
  label: "Your ITR"
  children:
    - label: "Form 26AS"
      children:
        - label: "TDS on salary, dividends, interest"
        - label: "Advance & self-assessment tax"
        - label: "TCS, refunds"
    - label: "AIS / TIS"
      children:
        - label: "Share & MF sale values"
        - label: "Dividends and interest"
        - label: "Foreign remittances, high-value deals"
    - label: "Broker / RTA statements"
      children:
        - label: "Cost of acquisition per lot"
        - label: "Holding period, LTCG vs STCG"
        - label: "Grandfathered cost (pre-2018)"
caption: "Each source answers a different question. Only together do they give a complete capital gains schedule."
```

## What each one actually contains

| Document | Source | Best for | Weak on |
|---|---|---|---|
| Form 26AS | TRACES | Tax credits you can claim | Income without TDS |
| AIS | Income tax portal | What the department knows | Cost and holding period |
| TIS | Derived from AIS | Category totals | Lot-level detail |
| Broker tax P&L | Your broker | Gain per trade, LTCG/STCG | Other brokers |
| CAMS/KFintech CG statement | Mutual fund registrars | MF gains across AMCs | Direct stocks |
| AIF/REIT income statement | The fund | Pass-through income | Timing (often late) |

AIS shows sale value but rarely cost. If you copy AIS straight into the return, you would be taxed on the full sale value. The broker statement supplies the cost.

## Where mismatches come from

```viz
type: donut
title: "Illustrative: causes of AIS–ITR mismatches"
center: "100"
center_sub: "mismatches"
data:
  - ["Missing broker / AMC", 30]
  - ["Duplicate AIS entries", 20]
  - ["Dividend not reported", 18]
  - ["Wrong cost / grandfathering", 17]
  - ["Off-market transfers", 15]
caption: "Illustrative mix based on common reconciliation issues, not official statistics. Most come from incomplete source data rather than from the department's errors."
```

## A five-step reconciliation

```viz
type: flow
title: "Reconcile before you file"
steps:
  - title: "Download"
    sub: "26AS, AIS (JSON or PDF), and capital gains reports from every broker and both MF registrars."
    tag: "Collect"
  - title: "Match sales"
    sub: "Each AIS sale value should map to a broker or RTA line. Unmatched lines mean a missing account."
    tag: "Check"
  - title: "Add cost"
    sub: "Use broker cost, with 31 January 2018 grandfathering for older equity."
    tag: "Compute"
  - title: "Check credits"
    sub: "TDS in 26AS should equal the credit you claim, including dividend TDS."
    tag: "Check"
  - title: "Feedback & file"
    sub: "Flag wrong AIS entries on the portal, then file with figures you can document."
    tag: "File"
caption: "Thirty minutes for a single broker account. Several days for a family with many PANs and accounts, which is why it is worth automating."
```

::: example One family, many statements
A family with four PANs, three brokers each and two registrars handles about 20 source documents a year. Each lists hundreds of lines. A script that maps ISIN and trade date across them turns a week of work into a review. This is the same extraction problem behind our [filings data pipeline](/blog/nse-bse-filings-research-data-pipeline/).
:::

## Rates to apply

For listed equity and equity funds, LTCG above ₹1.25 lakh is taxed at 12.5% and STCG at 20% for transfers from 23 July 2024. ESOP shares follow the same rates but use the exercise-date FMV as cost. See our [ESOP taxation guide](/blog/esop-taxation-india/). For in-kind and off-market transfers, which often produce confusing AIS entries, read [transferring shares between demat accounts](/blog/demat-account-transfer-india/).


## Form 26AS in detail

Form 26AS is drawn from TRACES, the TDS system. Its main parts show:

- **TDS on salary, interest, dividends and rent,** deducted by employers, banks and companies under your PAN.
- **TCS** collected on items such as foreign remittances under the Liberalised Remittance Scheme above the threshold.
- **Advance tax and self-assessment tax** you paid with challan details.
- **Refunds** issued.
- **High-value transactions** reported by banks, registrars and others (now largely moved into AIS).

Every TDS credit you claim in your return must match 26AS. If a deductor has not filed its TDS return, or filed it under a wrong PAN, the credit will not appear and the return will be processed without it. Fix that by asking the deductor to file a correction, not by editing your return.

## AIS in detail

The Annual Information Statement, introduced in November 2021, is far broader. It includes:

- interest from every bank and post office account,
- dividends from every company,
- sale of listed shares and mutual fund units reported by depositories and registrars,
- off-market transfers,
- purchase of property and high-value cash deposits,
- foreign remittances and GST turnover.

Each entry shows the **reported value** and lets you submit **feedback**: correct, incorrect, duplicate, belongs to another PAN, or income not taxable. Feedback does not change the return, but it updates the department's records and reduces the chance of a mismatch notice. The **Taxpayer Information Summary (TIS)** aggregates AIS into categories and shows a "derived value" that is used to pre-fill the return.

## Filling Schedule CG from these documents

The capital gains schedule in ITR-2 and ITR-3 needs, for each asset class:

| Field | Where to get it |
|---|---|
| Sale value | Broker tax P&L; check against AIS |
| Cost of acquisition | Broker P&L, contract notes, CAS |
| Grandfathered cost (pre-1 Feb 2018 equity) | Higher of cost and 31 Jan 2018 FMV, capped at sale value |
| Transfer expenses | Brokerage, STT is not deductible, exchange charges |
| Holding period | Purchase and sale dates from contract notes |

Listed equity bought before 1 February 2018 gets grandfathering: the cost is the higher of actual cost and the 31 January 2018 closing price, but not more than the sale value. Reporting is done scrip-wise by ISIN for grandfathered shares in Schedule 112A.

## Worked example of a mismatch

::: example AIS says ₹18 lakh, broker says ₹15 lakh
Anil's AIS shows ₹18 lakh of share sales. His main broker's tax P&L shows ₹15 lakh. The gap turns out to be ₹3 lakh of mutual fund redemptions reported by CAMS, which are not in the broker statement. He adds the CAMS capital gains statement, and total sales reconcile to ₹18 lakh. His actual gain is ₹2.4 lakh. Had he ignored the gap, the department's system could have flagged ₹3 lakh of unreported sales.
:::

## If you receive a notice

Mismatch notices usually come under Section 143(1)(a) as a proposed adjustment, or as an e-verification query under the compliance portal. Respond on the portal within the deadline, attach the reconciliation, and use AIS feedback for the wrong entries. Most mismatches caused by reporting duplicates or missing cost data close without additional tax once the documents are submitted.

## Timeline for a smooth filing

1. **April–May:** download broker and registrar statements once March trades have settled.
2. **Mid-June:** 26AS and AIS are usually complete after deductors file Q4 TDS returns by 31 May.
3. **June–July:** reconcile, submit AIS feedback, and file.
4. **Due date:** 31 July for non-audit individuals unless extended; later dates apply to audit cases.


## Special cases that trip up reconciliation

**Bonus shares and splits.** Bonus shares have a cost of zero and a holding period starting on allotment. On a split, the original cost is divided across the new shares and the holding period carries over. Many brokers get bonus lots wrong when shares were bought elsewhere.

**Mutual fund switches.** A switch between schemes, even within the same fund house, is a sale and a fresh purchase. It appears in AIS as a redemption. Switching between growth and IDCW options of the same scheme is also a sale.

**Debt fund units bought after 1 April 2023.** Gains are taxed at slab rates regardless of holding period, because these units are treated as specified mutual funds. Do not apply the equity rates to them.

**Intraday and F&O trades.** These are business income, not capital gains, and require ITR-3. AIS may show the turnover, but the tax treatment is completely different.

**Foreign shares.** Sales of US-listed stocks often do not appear in AIS at all, but they must still be reported in Schedule CG and Schedule FA. The absence from AIS does not make them non-taxable.

## Tools that help

Most large brokers publish a downloadable tax P&L that maps directly onto Schedule CG and Schedule 112A. CAMS and KFintech offer a consolidated capital gains statement across fund houses. The depositories issue a monthly Consolidated Account Statement (CAS) that shows all holdings in one place. For families with many accounts, combining these into a single ledger keyed on PAN, ISIN and trade date is the most reliable approach.

::: note Not tax advice
Forms and portal features change each year. Confirm treatment with a chartered accountant.
:::
