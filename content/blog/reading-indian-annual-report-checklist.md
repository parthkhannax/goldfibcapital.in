---
slug: reading-indian-annual-report-checklist
title: "How to Read an Indian Annual Report Like a Buy-Side Analyst"
seo_title: "How to Read an Indian Annual Report: Buy-Side Checklist"
short: "Reading an annual report like the buy side"
description: "A page-by-page method for reading Indian annual reports: where the real signals hide, the red-flag heatmap, and a 90-minute reading order analysts use."
cluster: research
level: intermediate
order: 3
date: 2026-10-03
keywords: [how to read annual report India, annual report analysis, related party transactions, CARO report, contingent liabilities, red flags annual report]
answer: "Don't start at the chairman's letter. Start with the auditor's report and CARO annexure, then the notes on related-party transactions, contingent liabilities and borrowings, then the cash flow statement, and only then the management discussion. That order puts the hardest-to-fake evidence first and the marketing last. It takes about 90 minutes."
takeaways:
  - "Read in reverse order of how much management controls the text: auditor first, notes second, MD&A last."
  - "Five places hold most red flags: auditor's report, CARO, related-party note, contingent liabilities and the cash flow statement."
  - "Compare at least three years side by side. Single-year reading misses changes in accounting policy and segment definitions."
  - "Use the heatmap below to prioritise. A clean report can be read in 90 minutes."
faq:
  - q: "What is the most important section of an Indian annual report?"
    a: "For risk, the independent auditor's report, including the CARO annexure and any qualifications or emphasis-of-matter paragraphs. For understanding the business, the segment note and the cash flow statement. The chairman's letter and MD&A are useful context, but they are management's narrative and should be read last."
  - q: "What is CARO in an annual report?"
    a: "CARO is the Companies (Auditor's Report) Order, which requires auditors of most Indian companies to report on specific matters such as fixed asset records, inventory verification, loans to related parties, statutory dues, defaults on borrowings and fraud. Adverse remarks in the CARO annexure are a useful early warning."
  - q: "How do you spot red flags in an Indian annual report?"
    a: "Check for auditor qualifications or resignations, large or rising related-party transactions, contingent liabilities that are large relative to net worth, operating cash flow persistently below reported profit, rising receivable days, frequent changes in accounting policies or segments, and growing loans or guarantees to group companies."
  - q: "How long does it take to analyse an annual report?"
    a: "A focused first pass on a company you already understand takes about 90 minutes using a fixed reading order. A first-time deep read for an initiation, including three years of comparisons and notes, typically takes a full day."
cta:
  heading: "Want a red-flag review on a company you hold?"
  body: "Goldfib analysts run this reading order across three to five years of filings and deliver a two-page red-flag memo with every number sourced. Send us the name."
  subject: "Annual report red-flag review"
---

An Indian annual report for a mid-sized listed company can run to 250–400 pages. Most investors read the first thirty: the chairman's letter, the highlights and the management discussion. Most of the useful information sits in the other three hundred.

This guide gives a reading order, a red-flag heatmap and a checklist built for Indian disclosures under the Companies Act, 2013 and Ind AS.

## The principle: read in reverse order of management control

Every section of an annual report has a different author, and a different incentive.

```viz
type: bars
title: "How much management controls each section (and how much to trust it)"
data:
  - ["Chairman's letter / highlights", 95]
  - ["Management discussion & analysis", 85]
  - ["Directors' report", 70]
  - ["Corporate governance report", 60]
  - ["Financial statements", 45]
  - ["Notes to accounts", 35]
  - ["Independent auditor's report + CARO", 10]
highlight: ["Notes to accounts", "Independent auditor's report + CARO"]
unit: ""
max: 100
label_width: 240
caption: "Conceptual scale from 0 (independent) to 100 (fully management-authored). Read from the bottom up: the less control management has over a section, the earlier you read it."
```

So the reading order runs bottom-up: the auditor first, the notes second, the statements third, and the narrative last. By the time you reach the chairman's letter, you can test every claim in it against evidence you have already seen.

## The 90-minute reading order

```viz
type: timeline
title: "A 90-minute first pass"
events:
  - when: "0–15 min"
    title: "Independent auditor's report and CARO annexure"
    sub: "Qualifications, emphasis of matter, key audit matters, going-concern language, CARO remarks on loans, statutory dues and defaults."
    hl: true
  - when: "15–35 min"
    title: "Notes: related parties, contingent liabilities, borrowings"
    sub: "Size of RPTs versus revenue and net worth. Guarantees for group companies. Debt maturity, covenants and security."
    hl: true
  - when: "35–50 min"
    title: "Cash flow statement, three years side by side"
    sub: "Operating cash flow versus EBITDA and PAT. Working-capital swings. Capex versus depreciation. Where the cash actually went."
  - when: "50–65 min"
    title: "Segment note and revenue disclosures"
    sub: "Segment revenue and margin trends. Any redefinition of segments. Geographic split and concentration."
  - when: "65–80 min"
    title: "Governance report and directors' report"
    sub: "Board composition, independent director tenure and exits, remuneration versus profit, auditor changes."
  - when: "80–90 min"
    title: "MD&A and chairman's letter"
    sub: "Now test the story. Which claims are supported by what you just read, and which aren't?"
caption: "Reading order for a company you already broadly understand. A first-time initiation takes a day, but follows the same sequence."
```

## Where the red flags live

Not every section is equally likely to contain a problem. The heatmap below scores, on a 1–5 scale, how often each class of issue shows up in each part of the report, based on common patterns in Indian corporate disclosures.

```viz
type: heatmap
title: "Red-flag heatmap: where to look for which problem"
rows: ["Auditor report + CARO", "Related-party note", "Contingent liabilities", "Cash flow statement", "Segment note", "Governance report"]
cols: ["Earnings quality", "Promoter self-dealing", "Hidden leverage", "Going concern", "Accounting changes"]
values:
  - [4, 3, 3, 5, 4]
  - [2, 5, 3, 1, 1]
  - [1, 3, 5, 3, 1]
  - [5, 2, 3, 4, 2]
  - [3, 1, 1, 1, 5]
  - [1, 4, 1, 1, 2]
row_title: "Section"
col_title: "Type of problem"
low_color: "#1d3049"
caption: "Higher score = more likely to surface that problem. Illustrative weighting from analyst practice, not a statistical study. The cash flow statement and the auditor's report are the two most informative pages for earnings quality."
```

## The checklist, section by section

### 1. Independent auditor's report

- Is the opinion **unmodified, qualified, adverse or a disclaimer**? Anything other than unmodified is a serious flag.
- Read the **emphasis of matter** paragraphs. They often point at disputes, going-concern doubts or one-off accounting.
- Read the **key audit matters**. They show what the auditor worried about most, such as revenue recognition, impairment or inventory valuation.
- Check the **auditor's tenure and any change**. A mid-term resignation, especially with vague reasons, deserves a phone call.

### 2. The CARO annexure

The Companies (Auditor's Report) Order requires auditors to comment on specific matters. Adverse remarks to watch for include:

- Loans or advances to related parties that are **not repaid on schedule** or are **prejudicial to the company's interest**.
- **Undisputed statutory dues** (tax, PF, GST) outstanding for more than six months.
- **Defaults** in repaying lenders.
- Funds raised for one purpose being **used for another**.
- Reported **frauds**.

### 3. Related-party transactions

Look at the related-party note and at the separate approvals disclosed in governance filings. Build a small table: RPT purchases, sales, loans, guarantees and royalties, each as a percentage of revenue and of net worth, across three years. Growth that outpaces the business is the signal.

### 4. Contingent liabilities and commitments

Indian companies often carry large disputed tax demands and guarantees given on behalf of group companies. Neither sits on the balance sheet. Compare total contingent liabilities with net worth. Ask which items are **likely** to crystallise, not just which are possible.

### 5. Cash flow statement

```viz
type: line
title: "Illustrative: the classic earnings-quality warning"
x: ["FY21", "FY22", "FY23", "FY24", "FY25"]
series:
  - name: "Reported PAT"
    values: [100, 128, 160, 196, 240]
  - name: "Operating cash flow"
    values: [92, 101, 98, 104, 96]
    color: "#f87171"
prefix: "₹"
unit: " cr"
caption: "Hypothetical company. Profit grows at 24% a year while operating cash flow stays flat. The gap is usually explained by rising receivables or inventory, and it is the single most common warning sign of aggressive revenue recognition."
```

Sum five years of operating cash flow and compare it with five years of PAT. A ratio persistently below 0.7–0.8 in a business that is not capital-light needs explaining. Then look at **receivable days** and **inventory days**. If they rise every year, the profit is sitting on the balance sheet, not in the bank.

### 6. Segment and accounting-policy notes

Check whether segment definitions changed this year. If they did, rebuild the prior years on the new basis before comparing. Read the accounting-policy note for changes in revenue recognition, depreciation method or useful lives, capitalisation of borrowing costs, or development expenditure.

## Make it a template

The value of a reading order is that it can be taught and repeated. A good desk captures each section's findings in a fixed template, so a senior reviewer can see in five minutes what was checked and what was found. That is the difference between [institutional-grade research](/blog/institutional-grade-equity-research-india/) and a good read. Parts of this work, such as extracting related-party tables and tracking contingent liabilities across years, can be automated. We cover how in [AI for investment research](/blog/ai-investment-research-automation-india/).
