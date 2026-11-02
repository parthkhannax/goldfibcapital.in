---
slug: how-to-read-drhp-sebi-prospectus-checklist
title: "How to Read a SEBI DRHP Like a Buy-Side Analyst: A 10-Step Institutional Checklist"
seo_title: "How to Read a SEBI DRHP: 10-Step Buy-Side Checklist"
short: "How to read a SEBI DRHP"
description: "A page-by-page institutional guide to dissecting an Indian DRHP: restated financials, litigation reserves, related party transactions, and dilution math."
cluster: ipo
level: advanced
order: 15
date: 2026-10-26
pillar: true
keywords: [how to read DRHP, SEBI DRHP checklist, draft red herring prospectus analysis, forensic DRHP diligence, buy-side IPO analysis, Indian IPO red flags]
answer: "A SEBI Draft Red Herring Prospectus (DRHP) spans 400 to 800 pages, but 80% of critical forensic signals hide in five specific sections: restated financial statements, related party transactions, outstanding litigation, promoter share acquisition costs, and the Objects of the Issue. Analysts never read sequentially; they read forensically."
takeaways:
  - "Never read front-to-back: the executive summary and industry overview are curated marketing; start with restated auditor notes."
  - "Check the promoter's average cost of acquisition: compare it against the upper IPO price band to quantify insider markups."
  - "Scrutinize restated financial adjustments: identify which past operational expenses were capitalized or reclassified to inflate pre-IPO EBITDA."
  - "Audit litigation and contingent liabilities: tax disputes and customer lawsuits often exceed total annual net profit."
faq:
  - q: "What is the difference between a DRHP and an RHP?"
    a: "The Draft Red Herring Prospectus (DRHP) is filed with SEBI and stock exchanges for regulatory review and public comment, containing company details but omitting the final share price and issue dates. Once SEBI issues observation letters and the issue is approved, the Red Herring Prospectus (RHP) is filed with the Registrar of Companies (RoC), containing the exact price band, bidding dates, and updated anchor allocations."
  - q: "Where do merchant bankers hide the biggest red flags in a DRHP?"
    a: "In Section IX ('Outstanding Litigation and Material Developments') and Note 36/38 of the Restated Financial Statements ('Related Party Transactions'). These sections reveal whether company funds were loaned to promoter-owned private shell companies or if disputed tax demands could wipe out net worth upon adverse judicial rulings."
  - q: "Why do pre-IPO financial statements in a DRHP look so much better than earlier ROC filings?"
    a: "Because Indian regulations require 'Restated Financial Information' under Ind AS for the last three fiscal years. Promoters frequently use this restatement window to reclassify prior non-operating expenses, capitalize previously expensed software/R&D costs, or write back tax provisions to present an accelerating profit curve prior to public valuation."
cta:
  heading: "Need a rapid 48-hour forensic memo on an active DRHP?"
  body: "Goldfib extracts related-party flows, audits restated Ind AS financials, and models dilution metrics for family offices evaluating upcoming listings."
  subject: "DRHP forensic teardown enquiry"
---

When an Indian company files a Draft Red Herring Prospectus (DRHP) with SEBI, it submits a dense, legalistic document frequently exceeding 600 pages. 

Retail investors and media outlets typically read page one: the headline issue size, the names of the marquee investment bankers (Kotak, Morgan Stanley, Axis Capital), and the flattering 'Industry Overview' written by paid consultancy firms like CRISIL, Frost & Sullivan, or Technopak.

Institutional buy-side analysts at top family offices and long-only funds take the opposite approach. They know that a DRHP is a legal liability defense document: every catastrophic risk the promoters and underwriters fear being sued for later is explicitly buried in the small print.

To extract real investment signal from a prospectus, you must follow a disciplined, non-linear reading order. Here is the 10-step institutional checklist our research desk uses to dissect Indian DRHPs.

## The 10-Step Buy-Side Reading Order

Do not read a DRHP from cover to cover. Follow this forensic sequence:

```viz
type: flow
title: "The 10-step institutional DRHP reading sequence"
steps:
  - title: "1. Objects of the Issue"
    sub: "Distinguish Fresh Issue growth capital from sponsor Offer for Sale (OFS) exits."
    tag: "Capital Use"
  - title: "2. Promoter Acquisition Cost"
    sub: "Compare founder/PE entry prices with the public issue price band."
    tag: "Valuation Gap"
  - title: "3. Restated Auditor Report"
    sub: "Inspect restatement adjustments, qualifications, and accounting policy shifts."
    tag: "Accounting Quality"
  - title: "4. Related Party Transactions"
    sub: "Track loans, rent payments, and sales to promoter-controlled private entities."
    tag: "Governance"
  - title: "5. Contingent Liabilities & Tax"
    sub: "Quantify disputed GST, excise, and income tax demands relative to net worth."
    tag: "Balance Sheet Risk"
  - title: "6. Customer & Supplier Concentration"
    sub: "Check revenue dependency on top 5 customers and key vendor agreements."
    tag: "Operational Moat"
  - title: "7. Cash Flow vs Reported PAT"
    sub: "Verify whether reported accounting profits convert into real Operating Cash Flow."
    tag: "Earnings Quality"
  - title: "8. Management Remuneration & ESOPs"
    sub: "Evaluate promoter compensation spikes and upcoming employee stock option dilution."
    tag: "Alignment"
  - title: "9. Section IX: Outstanding Litigation"
    sub: "Review criminal proceedings, SEBI debarments, and intellectual property disputes."
    tag: "Legal Defense"
  - title: "10. Industry & Competitive Benchmarking"
    sub: "Re-calculate peer valuation multiples using normalized trailing earnings."
    tag: "Pricing Power"
caption: "Always start where promoters are legally forced to disclose risks, and read the marketing summary last."
```

## Step 1: Objects of the Issue (Where Does the Cash Go?)

Turn immediately to the section titled **'Objects of the Issue'**.

Calculate the exact split between:
- **Fresh Issue**: New shares issued by the company. The net proceeds land on the corporate balance sheet to build factories, pay down bank debt, or fund technology capex.
- **Offer for Sale (OFS)**: Existing shares sold by promoters, private equity funds, or angel investors. Zero money enters the company; the entire cash proceeds flow into the selling shareholders' personal bank accounts.

As demonstrated in our analysis of [Hyundai Motor India's 100% OFS IPO](/blog/hyundai-motor-india-ipo-valuation-analysis/), a heavy OFS means public shareholders are providing exit liquidity at peak private market valuations rather than financing domestic business expansion.

## Step 2: Promoter Cost of Acquisition vs IPO Price Band

Search the document for the table titled **'Weighted Average Cost of Acquisition'**. Under SEBI regulations, companies must disclose what promoters, directors, and selling shareholders paid for their shares over the preceding 12 to 36 months.

```viz
type: bars
title: "Illustrative: Insider acquisition cost vs IPO issue price (₹ per share)"
data:
  - ["Promoter Initial Allotment (Par)", 10]
  - ["PE Series B Round (24 Mo ago)", 85]
  - ["Pre-IPO Placement (6 Mo ago)", 210]
  - ["Proposed IPO Price Band (Upper)", 650]
highlight: ["Proposed IPO Price Band (Upper)", "Promoter Initial Allotment (Par)"]
prefix: "₹"
label_width: 250
caption: "Illustrative tech IPO cap-table walk. Promoters enjoy a 65x markup over initial equity cost, while pre-IPO investors capture a 3x multiple."
```

If private equity funds entered at ₹85 per share two years ago and are now dumping 100% of their holding at ₹650 per share through an OFS, ask: what fundamental transformation occurred in the operating business to justify an 8x multiple in 24 months?

## Step 3: Restated Financial Adjustments

Companies do not publish their raw statutory annual reports in a DRHP. Instead, an independent chartered accountant compiles **'Restated Consolidated Financial Information'** under Ind AS.

Compare the restated profits in the DRHP with the company's historical MCA filings on the Ministry of Corporate Affairs portal:
- Did the restatement capitalize operating expenses (such as server hosting or marketing costs) as intangible assets, artificially inflating reported EBITDA?
- Were old provisions for bad debts or inventory obsolescence reversed into income just ahead of the IPO year?

For an institutional methodology on auditing corporate accounting notes, review our guide on [how to read an Indian annual report](/blog/reading-indian-annual-report-checklist/).

## Step 4: Related Party Transactions (The Drainage Pipe)

Navigate to the **'Related Party Transactions' (RPT)** disclosure note. This is where corporate governance fractures emerge.

Look for four specific red flags:
1. **Promoter Property Leases**: Does the operating company pay exorbitant monthly rent to a private partnership firm owned by the promoter's spouse for corporate headquarters or warehouses?
2. **Interest-Free Advances**: Did the listed entity extend unsecured loans or business advances to loss-making promoter subsidiaries that have not been repaid?
3. **Key Management Remuneration Spikes**: Did promoter salaries jump from ₹2 crore to ₹18 crore in the fiscal year preceding the IPO filing?
4. **Supply Chain Intermediaries**: Does the company purchase raw materials through an offshore trading entity controlled by promoter family members?

::: warn Promoter Pledging Disclosures
Check whether promoter shares are encumbered. If existing shares are pledged to NBFCs to secure private borrowings, a post-listing share price decline can trigger forced margin selling, as documented in our study on [promoter pledging signals](/blog/promoter-pledging-shareholding-signals/).
:::

## Step 5: Contingent Liabilities and Tax Claims

In Section IX, locate the summary of **'Outstanding Litigation and Material Developments'**.

Sum the total value of disputed tax claims:
- Disputed GST and service tax demands under litigation at appellate tribunals.
- Income tax notices under Section 148 for reassessment of unaccounted income.
- Custom duty disputes regarding tariff classifications.

Compare the total contingent tax liability against the company's net worth. If disputed claims represent more than 30% of total equity, an adverse High Court or Supreme Court ruling post-listing could instantly erase two years of corporate net profit.

## Step 6: Customer Concentration and Contract Duration

Locate the operational business summary to identify revenue concentration:

```viz
type: donut
title: "Illustrative customer concentration risk profile"
center: "Top 5"
center_sub: "64% of Revenue"
data:
  - ["Top Customer Account", 32]
  - ["Customer 2 & 3", 21]
  - ["Customer 4 & 5", 11]
  - ["All Other Customers", 36]
prefix: ""
unit: "%"
caption: "High customer concentration leaves operating cash flow vulnerable to single-client contract renegotiations or project completion cliffs."
```

If one or two customers generate more than 40% of corporate turnover, check the underlying master service agreements (MSAs):
- Are contracts long-term (3 to 5 years) or project-by-project purchase orders?
- Does the client possess unilateral termination-for-convenience clauses without financial penalty?

As seen in our [Tata Technologies post-IPO analysis](/blog/tata-technologies-ipo-post-listing-reality-check/), client concentration in EV engineering created multi-quarter revenue drag when single customer capex slowed.

## Step 7: Cash Flow from Operations vs Reported Net Profit

In the financial statements, place the **Profit After Tax (PAT)** from the Profit and Loss statement directly side-by-side with **Cash Flow from Operating Activities (CFO)** from the Cash Flow Statement for the last three years.

```viz
type: columns
title: "Forensic check: Reported PAT vs Operating Cash Flow (CFO) (₹ crore)"
data:
  - ["FY22 Reported PAT", 110]
  - ["FY22 Real Cash CFO", 102]
  - ["FY23 Reported PAT", 185]
  - ["FY23 Real Cash CFO", 140]
  - ["FY24 Pre-IPO PAT", 290]
  - ["FY24 Real Cash CFO", 85]
highlight: ["FY24 Pre-IPO PAT", "FY24 Real Cash CFO"]
caption: "Forensic divergence: Reported PAT nearly doubled in FY24, but real Operating Cash Flow collapsed due to aggressive trade receivable booking."
```

A healthy business converts at least 70% to 90% of its cumulative net profits into cash flow from operations. 

If reported PAT surges from ₹100 crore to ₹290 crore ahead of an IPO while CFO stagnates or turns negative, the company is likely stuffing distribution channels with inventory or booking unbilled revenue to create an artificial pre-IPO profit spike.

## Step 8: Management Remuneration and Employee ESOP Dilution

Examine the share-based compensation disclosures and ESOP grant pools.

Many venture-backed startups grant extensive tranches of deep-discounted ESOPs to founders and senior executives right before filing a DRHP. Because employee stock compensation is amortized over vesting periods, these grants create heavy non-cash accounting charges that suppress post-listing GAAP earnings for several years.

Furthermore, check the exercise price of outstanding options: if millions of employee options are exercisable at ₹10 while the IPO is priced at ₹500, calculate the total percentage dilution of post-issue public equity.

## Step 9: Section IX — Criminal and Regulatory Proceedings

Do not skip **Section IX ('Legal and Other Information')**.

Under SEBI regulations, the company must disclose:
- All criminal cases pending against promoters or whole-time directors.
- Actions taken by statutory authorities (SEBI, RBI, Enforcement Directorate, SFIO, CCI).
- Disciplinary actions by stock exchanges against group entities.

Promoters involved in past regulatory consent orders or willful-defaulter proceedings represent structural corporate governance discounts.

## Step 10: Industry Benchmarking and Valuation Modeling

Only after completing the forensic accounting checks should you open the **'Industry Overview'** and **'Basis for Issue Price'** sections.

Calculate normalized valuation metrics:
- Strip out pre-IPO one-time tax write-backs, government subsidies, and asset sales.
- Model steady-state EBITDA margins assuming normalized raw material costs.
- Benchmark normalized trailing P/E, EV/EBITDA, and Price-to-Sales against listed peers.

If the IPO is priced at a 40% premium to established market leaders like Larsen & Toubro, Maruti Suzuki, or Titan without demonstrating superior Return on Capital Employed (ROCE), public market allocators should decline the primary offering and wait for secondary market price discovery.

To understand how to value unlisted opportunities before DRHP filing, review our guide on [pre-IPO unlisted share diligence](/blog/pre-ipo-unlisted-shares-due-diligence-india/).

## Institutional Takeaway: Build a Forensic Filter

A DRHP is an adversarial document: investment bankers are paid tens of crores to present the company in its most seductive light, while compliance lawyers work to shield the firm from investor lawsuits.

By following this 10-step institutional reading sequence, family offices and investment managers can strip away promotional marketing decks, identify balance-sheet vulnerabilities, and ensure capital is allocated only to businesses with genuine competitive moats and transparent corporate governance.
