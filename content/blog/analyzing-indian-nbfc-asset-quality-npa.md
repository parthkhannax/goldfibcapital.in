---
slug: analyzing-indian-nbfc-asset-quality-npa
title: 'Auditing NBFC Balance Sheets: Stage 3 NPAs, Provision Coverage, and ALM Mismatches'
seo_title: 'Auditing Indian NBFC Balance Sheets: NPAs & ALM'
short: Auditing Indian NBFC Balance Sheets & ALM
description: 'How to audit Indian NBFC financials: Stage 1/2/3 ECL provisioning, Provision
  Coverage Ratios (PCR), Asset-Liability Management (ALM), and liquidity coverage.'
cluster: research
level: intermediate
order: 38
date: '2026-11-02'
keywords:
- auditing nbfc balance sheets india
- stage 3 gross npa provision coverage ratio
- asset liability management alm mismatch nbfc
- expected credit loss ecl model ind as 109
- liquidity coverage ratio lcr nbfc upper layer
- cost of funds net interest margin nim analysis
- financial sector equity research india
answer: Auditing Indian NBFC balance sheets requires evaluating credit quality under
  Ind AS 109 across Stage 1, 2, and 3 loans, verifying that Provision Coverage Ratios
  (PCR) exceed 60% on Stage 3 NPAs, inspecting structural Asset-Liability Management
  (ALM) buckets to prevent short-term refinancing traps, and monitoring Liquidity
  Coverage Ratios (LCR).
takeaways:
- In financial services, balance sheet quality is everything; a lender's equity can
  be wiped out by a 4% to 6% credit loss on total assets.
- Ind AS 109 categorizes assets into Stage 1 (Standard), Stage 2 (Overdue 30-89 days),
  and Stage 3 (NPA overdue 90+ days).
- Lending long-term loans (e.g. 15-year mortgages) using short-term borrowings (e.g.
  90-day commercial paper) creates fatal ALM refinancing risks.
- NBFCs in the RBI Upper Layer must maintain strict capital adequacy (CRAR > 15%)
  and formal Liquidity Coverage Ratios (LCR).
faq:
- q: What is the difference between Stage 1, Stage 2, and Stage 3 loans under Ind
    AS 109?
  a: 'Under Ind AS 109 Expected Credit Loss (ECL) guidelines: Stage 1 comprises standard
    performing loans with low credit risk, requiring a 12-month ECL provision; Stage
    2 comprises loans exhibiting significant increase in credit risk (typically 30
    to 89 days past due), requiring lifetime ECL provisioning; Stage 3 represents
    credit-impaired assets (90+ days overdue), requiring full lifetime loss provisioning.'
- q: Why is an Asset-Liability Management (ALM) mismatch dangerous for an NBFC?
  a: An ALM mismatch occurs when an NBFC funds long-tenor assets (such as 10-year
    loan against property or housing loans) with short-tenor liabilities (such as
    3- to 6-month commercial paper or short-term bank credit). If financial markets
    experience a liquidity shock or credit freeze, lenders refuse to roll over short-term
    paper, leaving the NBFC unable to honor maturing debt despite holding a performing
    loan book.
- q: What is a healthy Provision Coverage Ratio (PCR) for an Indian retail NBFC?
  a: For retail asset-backed lenders (vehicle finance, gold loans, affordable housing),
    a Provision Coverage Ratio between 55% and 70% of Gross Stage 3 assets is considered
    robust. For unsecured personal loan or microfinance portfolios, where collateral
    recovery upon default is zero, prudent institutional analysts expect PCR to exceed
    75% to 85%.
cta:
  heading: Automating NBFC credit and ALM analytics across your holdings?
  body: Goldfib Capital builds automated banking and NBFC screening tools that parse
    Ind AS ECL disclosures, track ALM duration buckets, and monitor capital adequacy
    ratios.
  subject: NBFC analytics enquiry
---

In non-financial companies, an analyst focuses on operating margins, working capital, and fixed asset turnover. In financial institutions—such as Non-Banking Financial Companies (NBFCs) and Housing Finance Companies (HFCs)—**the balance sheet is the business**.

Because NBFCs operate with financial leverage of 4x to 7x equity, a credit loss of just 4% across their loan portfolio can destroy 25% to 30% of their net worth.

The 2018 IL&FS crisis and subsequent liquidity squeeze across DHFL and Reliance Capital demonstrated that **headline Gross NPA numbers alone cannot protect investors**.

Institutional analysts must audit Expected Credit Loss (ECL) staging, Provision Coverage Ratios (PCR), structural Asset-Liability Management (ALM), and liquidity coverage buffers.

```viz
type: flow
title: "The Ind AS 109 loan asset classification framework"
steps:
  - title: "Stage 1: Performing Portfolio"
    sub: "0 to 29 days past due (DPD). No significant credit deterioration. Provision: 12-month Expected Credit Loss (ECL)."
    tag: "Standard Loans"
  - title: "Stage 2: Elevated Risk Portfolio"
    sub: "30 to 89 days past due. Significant increase in credit risk. Provision: Lifetime Expected Credit Loss."
    tag: "Watchlist / SMA-1/2"
  - title: "Stage 3: Credit-Impaired Assets (NPA)"
    sub: "90+ days past due or objectively impaired. Provision: Lifetime ECL. Target PCR: >60%."
    tag: "Gross NPA"
```

## Auditing Loan Asset Quality: Beyond Headline GNPA

When analyzing an NBFC's loan portfolio, looking only at Gross Stage 3 (GNPA) is dangerously insufficient. Analysts scrutinize:

### 1. Stage 2 Loans as a Leading Indicator
Stage 2 loans represent borrowers who are 30 to 89 days late on installments. If an NBFC reports an optically clean Gross Stage 3 ratio of 2.1%, but its Stage 2 book suddenly surges from 3.5% to 8.2% of total assets, a wave of loan defaults will inevitably hit Stage 3 in the following two quarters.

```viz
type: columns
title: "Loan asset classification breakdown: tier-1 vs stressed NBFC (%)"
unit: "%"
data:
  - ["Tier-1 NBFC: Stage 1 Performing", 94.8]
  - ["Tier-1 NBFC: Stage 2 Watchlist", 3.2]
  - ["Tier-1 NBFC: Stage 3 Impaired (GNPA)", 2.0]
  - ["Stressed NBFC: Stage 1 Performing", 84.5]
  - ["Stressed NBFC: Stage 2 Watchlist", 9.8]
  - ["Stressed NBFC: Stage 3 Impaired (GNPA)", 5.7]
caption: "Staging comparison: Stressed lenders carry nearly 10% of their loan book in Stage 2, signaling substantial hidden credit distress."
```

### 2. Provision Coverage Ratio (PCR)
The Provision Coverage Ratio measures how much cushion management has set aside against bad loans:

$$\text{PCR} = \frac{\text{Impairment Loss Allowance on Stage 3}}{\text{Gross Stage 3 Loans}}$$

If two housing finance companies report identical 3.0% Gross NPAs, but Firm A maintains a 75% PCR while Firm B maintains only a 30% PCR, Firm A has conservatively expensed its bad loans through the P&L, whereas Firm B's future earnings remain highly vulnerable to sudden write-offs.

```viz
type: bars
title: "Recommended Provision Coverage Ratios (PCR) by collateral type (%)"
unit: "%"
data:
  - ["Gold Loans (High Liquidity Collateral)", 45.0]
  - ["Affordable Housing Mortgages (LTV <65%)", 55.0]
  - ["Commercial Vehicle & Tractor Financing", 65.0]
  - ["Loan Against Property (LAP) MSME", 70.0]
  - ["Unsecured Personal Loans & Microfinance", 85.0]
caption: "Collateral-driven PCR requirements: Unsecured consumer lending mandates aggressive 85%+ coverage due to zero recovery upon borrower default."
```

## The Structural ALM Mismatch: The Silent Killer

Credit quality issues destroy an NBFC over several years, but **Asset-Liability Management (ALM) mismatches can destroy an NBFC in 72 hours**.

NBFCs borrow money from debt markets (commercial paper, non-convertible debentures, bank term loans) and lend it to customers.

```viz
type: quadrant
title: "NBFC Liquidity & Solvency Risk Matrix"
x: "ALM Structural Balance (Cumulative Inflows vs Outflows)"
y: "Provision Coverage Ratio (PCR)"
labels:
  top_right: "Institutional Tier-1 Lenders (Bajaj, Chola)"
  top_left: "High Provisioning / Short-Term Refinancing Drag"
  bottom_right: "Asset-Liability Matched / Inadequate Provisioning"
  bottom_left: "Acute Systemic Risk / Default Traps"
points:
  - {label: "Tier-1 Retail NBFC", x: 0.85, y: 0.78, hl: true}
  - {label: "Conservative HFC", x: 0.82, y: 0.65}
  - {label: "Aggressive FinTech MFI", x: 0.35, y: 0.72}
  - {label: "Wholesale Real Estate Lender", x: 0.22, y: 0.32}
  - {label: "Commercial Paper Reliant NBFC", x: 0.28, y: 0.40}
caption: "Strategic classification: Avoiding lenders in the lower-left quadrant prevents catastrophic financial defaults."
```

### The Maturity Mismatch Trap
- **Short-Term Borrowing**: Issuing 90-day Commercial Paper (CP) at 7.2% to keep interest costs low.
- **Long-Term Lending**: Lending that capital out as 10-year Loan Against Property (LAP) at 12.5%.
- **The Shock**: When a systemic liquidity event occurs, mutual funds refuse to roll over maturing CP. The NBFC must repay hundreds of crores of maturing debt immediately, but its assets are locked in multi-year borrower loan schedules.

Under RBI Master Directions, institutional analysts inspect the **Structural Liquidity Statement** in annual reports, verifying that cumulative inflows exceed cumulative outflows across all short-term buckets (1 day to 1 year).

## The Four-Step Institutional NBFC Audit Checklist

1. **Calculate Net NPA and Net Staged Assets**: Add Stage 2 loans to Net Stage 3 loans to calculate true 'Stressed Assets' as a percentage of tangible net worth.
2. **Review Borrowing Mix Diversification**: Ensure the NBFC is not over-reliant on commercial paper (<15% of total borrowings) and maintains diversified funding across bank term loans, long-term NCDs, and external commercial borrowings (ECBs).
3. **Verify Liquidity Coverage Ratio (LCR)**: Upper-layer NBFCs must maintain an LCR exceeding 100% in high-quality liquid assets (HQLA—primarily cash and sovereign G-Secs) to survive a 30-day liquidity stress scenario.
4. **Audit Off-Balance-Sheet Direct Assignments & PTCs**: When an NBFC sells loan pools to banks via securitization, check whether it carries significant credit enhancement or first-loss default guarantees (FLDG).

<p>Automating financial sector due diligence? <strong><a href="/contact/">Connect with Goldfib Capital</a></strong> to deploy automated NBFC screening models, ALM bucket analyzers, and credit provisioning audit tools.</p>

By enforcing rigorous balance sheet analysis and verifying ALM durability, institutional investors navigate Indian financial cycles with fortified downside protection.

For related frameworks, read our guide on [Analyzing Contingent Liabilities in Indian Annual Reports](/blog/analyzing-contingent-liabilities-notes-accounts/) and [Forensic Accounting Checklist for Indian Equities](/blog/forensic-accounting-checklist-indian-equities/).
