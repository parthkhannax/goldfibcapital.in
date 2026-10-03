---
slug: research-desk-cost-india
title: "What a Research Desk Really Costs in India (and the Leaner Alternatives)"
seo_title: "What an In-House Research Desk Costs in India"
short: "What a research desk really costs"
description: "The full cost of an in-house equity research desk in India: salaries, data, overheads and review time, with an interactive cost-per-report calculator."
cluster: automation
level: beginner
order: 3
date: 2026-10-03
keywords: [research desk cost India, equity research analyst salary India, outsource investment research, cost of in-house research, family office research cost, research outsourcing India]
answer: "An in-house equity research desk costs far more than analyst salaries. Add data and tool licences, recruitment and attrition, office overheads and the senior time spent reviewing work, and a two-analyst desk in India can cost several times the base payroll. Divide that by the number of finished reports and the cost per report is often much higher than teams expect. Calculate it before deciding to build, outsource or blend."
takeaways:
  - "Salary is usually only part of the true cost. Data, overheads, attrition and senior review add the rest."
  - "Cost per finished report is the metric that matters, and it falls sharply with automation and a steady flow of work."
  - "Small desks carry fixed costs that don't shrink with output: terminals, a reviewer and hiring cycles."
  - "Leaner models include outsourced desks, student-led desks with senior review, and automation-first workflows."
faq:
  - q: "How much does an equity research analyst cost in India?"
    a: "Compensation varies widely by city, firm type and experience, from entry-level packages at brokerages to much higher pay on the buy side. The fully loaded cost is meaningfully higher than salary once data tools, office space, recruitment, attrition and supervision are added. Use the calculator in this article with your own numbers."
  - q: "Is it cheaper to outsource investment research?"
    a: "Often, for teams that need research intermittently or across many companies, because outsourcing turns fixed costs into variable ones. The trade-offs are control, confidentiality and continuity. The right comparison is cost per finished, decision-ready report, not hourly rates."
  - q: "What data tools does a research desk in India need?"
    a: "At minimum, a source of clean historical financials, access to exchange filings, a spreadsheet modelling environment and a way to track news and announcements. Global terminals are expensive per seat; Indian database providers and filings-based pipelines can cover much of the need for domestic equities at lower cost."
  - q: "How many reports can one analyst produce per year?"
    a: "It depends on depth. A full initiation with a model can take two to four weeks, while updates take days. Many analysts produce roughly ten to twenty full reports a year alongside ongoing updates. Automation of data work can raise that materially."
cta:
  heading: "Want to compare your number with ours?"
  body: "Run the calculator, then email us your cost per report. Goldfib will tell you plainly whether a student-led desk with senior review and automation would cost less for your coverage, and if it wouldn't, we'll say so."
  subject: "Research cost comparison"
---

Family offices and smaller investment teams often decide to "hire an analyst" because the salary looks affordable. The full cost of a research function is a different number, and the cost of each **finished, decision-ready report** is different again.

This guide breaks down the full cost and gives you a calculator to run with your own inputs.

## The five cost buckets

| Bucket | What it includes | Often forgotten? |
|---|---|---|
| Compensation | Fixed pay, bonus, benefits | No |
| Data & tools | Terminals, databases, filings access, software | Sometimes |
| Overheads | Office space, hardware, recruitment fees, attrition and re-training | Usually |
| Senior review | PM or CIO time spent supervising and checking work | Almost always |
| Idle capacity | Analyst time between mandates or waiting for data | Almost always |

Senior review is the cost most teams leave out. If a CIO spends a day a week checking an analyst's models, that is a fifth of a very expensive person's time.

## Calculate your cost per report

```viz
type: widget
name: desk-cost
title: "Interactive: what does one finished report cost your desk?"
caption: "Default inputs are illustrative, not market benchmarks. Replace them with your own. Senior review is priced as a share of a portfolio manager costing ₹80 lakh a year. The output divides total annual cost by the number of full reports."
```

## Where the money goes

With the calculator's default inputs, a two-analyst desk looks like this:

```viz
type: stacked
title: "Illustrative annual cost of a two-analyst desk (₹ lakh)"
series: ["Salaries", "Data & tools", "Overheads", "Senior review"]
rows:
  - {label: "Two-analyst desk", values: [44, 12, 13.2, 12]}
unit: ""
caption: "Using the calculator defaults: ₹22 lakh CTC per analyst, ₹6 lakh data per seat, 30% overheads and 15% of a PM's time. Total ≈ ₹81 lakh a year. Salaries are only about 54% of the cost."
```

At 24 full reports a year, that is about **₹3.4 lakh per report**. If the desk only produces 12, because analysts are pulled into ad-hoc tasks, the cost per report doubles.

## Why small desks are expensive per unit

Fixed costs dominate small teams. A reviewer is needed whether the desk has one analyst or four. Data licences are priced per seat with minimums. Each departure restarts a hiring and training cycle.

```viz
type: columns
title: "Illustrative: cost per report falls as output rises"
data:
  - ["8 reports/yr", 10.1]
  - ["12", 6.8]
  - ["24", 3.4]
  - ["36", 2.3]
  - ["48", 1.7]
highlight: ["24"]
prefix: "₹"
unit: "L"
decimals: 1
caption: "Same ₹81 lakh desk, different output. Raising throughput, mainly by automating data collection and extraction, is the biggest lever on cost per report."
```

## The leaner alternatives

```viz
type: quadrant
title: "Research models by cost and control"
x_label: "Cost per report (low → high)"
y_label: "Control & customisation"
quadrants: ["LEAN AND TAILORED", "TAILORED BUT COSTLY", "CHEAP BUT GENERIC", "COSTLY AND GENERIC"]
points:
  - {label: "In-house desk", x: 0.82, y: 0.86}
  - {label: "Large KPO / outsourcing firm", x: 0.6, y: 0.48}
  - {label: "Free broker research", x: 0.08, y: 0.12}
  - {label: "Student-led desk + senior review + automation", x: 0.24, y: 0.74, hl: true}
  - {label: "Paid research subscriptions", x: 0.3, y: 0.28}
caption: "Conceptual positioning. Each model can sit elsewhere depending on how it's run."
```

- **Broker and subscription research** is cheap or free, but it is written for everyone, so it rarely fits your mandate.
- **Large outsourcing firms** add scale, but their pricing and processes are built for big institutions.
- **Student-led desks with senior review** combine motivated, recently trained analysts with a strict review process and automation. Done well, they deliver tailored work at a fraction of in-house cost. We explain how the model works in [student-led equity research](/blog/student-led-equity-research-model/).
- **Blended setups** keep one in-house person to own the thesis and outsource the volume work.

## How to decide

1. Run the calculator with honest inputs, including review time.
2. Count how many **decision-ready** reports you actually need a year.
3. Compare cost per report across options, and add a penalty for any option you can't control.
4. Ask whether automation alone would change the answer. Our [guide to research automation](/blog/ai-investment-research-automation-india/) covers what is realistic.

Whatever you choose, keep the [institutional-grade standard](/blog/institutional-grade-equity-research-india/) as the bar for every report you pay for.
