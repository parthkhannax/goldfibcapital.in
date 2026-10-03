---
slug: pms-vs-aif-vs-direct-equity-india
title: "PMS vs AIF vs Direct Equity: A Fee-Drag and Control Analysis for Indian HNIs"
seo_title: "PMS vs AIF vs Direct Equity in India: Fees and Control"
short: "PMS vs AIF vs direct equity"
description: "Compare PMS, AIFs and direct equity for Indian HNIs and family offices: minimums, structure, tax treatment, control, and an interactive fee-drag simulator."
cluster: family-office
order: 3
date: 2026-10-03
keywords: [PMS vs AIF, PMS vs direct equity, portfolio management services India, AIF category III, PMS fees performance fee, family office allocation India]
answer: "PMS (minimum ₹50 lakh) holds stocks in your own demat account with a manager deciding trades. AIFs (generally a ₹1 crore minimum) pool money in a fund. Direct equity means you or your research team pick and hold stocks yourselves. Fees compound: a 2% fixed fee plus a 20% performance fee can cost a significant share of terminal wealth over ten years, so the manager's edge must clearly exceed it."
takeaways:
  - "The real comparison is net-of-fee return per unit of effort and control, not headline returns."
  - "Over ten years, a 2% + 20% fee structure can cost several crore on a ₹10 crore corpus compared with a low-cost direct route."
  - "Direct equity has the lowest fees but the highest research load, which is where outsourced research and automation change the maths."
  - "Tax treatment differs by structure. Category III AIFs are taxed at fund level, while PMS and direct holdings are taxed in the investor's hands."
faq:
  - q: "What is the difference between PMS and AIF?"
    a: "In a PMS the securities are held in the investor's own demat account and the manager runs the portfolio under a mandate, with a SEBI minimum of ₹50 lakh. An AIF is a pooled fund, registered with SEBI as Category I, II or III, generally with a ₹1 crore minimum commitment. AIFs can invest in assets and strategies that PMS cannot, such as private companies or long-short strategies."
  - q: "How are PMS fees charged in India?"
    a: "PMS managers typically charge a fixed management fee, a performance fee above a hurdle, or a combination, plus brokerage and other expenses. SEBI requires performance fees to be charged on a high-water-mark basis and requires fee disclosure in the agreement. Check the exact structure, hurdle and expenses before investing."
  - q: "How is PMS taxed compared with an AIF?"
    a: "PMS investors are taxed directly on each transaction in their account, as if they held the shares themselves. Category I and II AIFs are largely pass-through for tax, so income is taxed in investors' hands. Category III AIFs are generally taxed at the fund level. Tax rules change, so confirm current treatment with a tax adviser."
  - q: "Is direct equity better than PMS for a family office?"
    a: "It can be if the family office has, or can access, strong research capacity. Direct equity avoids manager fees and gives full control, but the research and monitoring burden shifts to the family. Outsourced research or automation can make direct equity viable at a lower cost than manager fees."
cta:
  heading: "Running the direct route without a full desk?"
  body: "Goldfib provides the research layer for family offices that want direct-equity control without paying a manager's fees: initiations, monitoring and memos, delivered to your process. Email us your corpus and coverage needs."
  subject: "Direct equity research support"
---

For Indian HNIs and family offices, the choice between a **Portfolio Management Service (PMS)**, an **Alternative Investment Fund (AIF)** and **direct equity** often gets framed as "which manager has the best returns?". The better question is: **after fees and taxes, what do I get for the control I give up and the research work I avoid?**

## The three routes at a glance

| | PMS | AIF | Direct equity |
|---|---|---|---|
| SEBI minimum | ₹50 lakh | ₹1 crore (generally; lower for accredited investors) | None |
| Holding structure | Your own demat account | Units in a pooled fund | Your own demat account |
| Who decides trades | Manager (discretionary) | Manager | You / your team |
| Strategy range | Long-only listed equity mostly | Private equity, credit, long-short, real assets | Anything you can research |
| Tax | In your hands, per transaction | Cat I/II largely pass-through; Cat III at fund level | In your hands |
| Transparency | Full, holdings visible | Periodic reporting | Full |
| Typical fees | Fixed and/or performance fee | Management + performance (carry) | Research + execution costs |

*Regulatory minimums and tax rules as understood at the time of writing. Confirm current rules before investing.*

## Fee drag: where returns go

Fees compound just as returns do. The simulator below compares three routes on the same gross return:

- **Direct**, paying only research and execution costs.
- **Fixed fee** only.
- **Fixed + performance fee** above a hurdle (charged annually; real agreements use high-water marks and differ in detail).

```viz
type: widget
name: fee-drag
title: "Interactive: what do fees cost you over time?"
caption: "Illustrative model, same gross return for all three routes. It ignores taxes and assumes the manager earns exactly the same gross return as the direct route. In reality the manager may outperform or underperform."
```

At the defaults (₹10 crore, 14% gross, 10 years, 0.3% direct cost, 2% fixed fee, 20% performance fee over a 10% hurdle), the direct route ends at about **₹36.1 crore** versus about **₹30.0 crore** for the fixed + performance structure. That's a gap of roughly **₹6.1 crore**, about a sixth of the direct outcome.

```viz
type: columns
title: "₹10 crore after 10 years at 14% gross (default inputs)"
data:
  - ["Direct (0.3% cost)", 36.1]
  - ["2% fixed fee", 31.1]
  - ["2% + 20% over 10% hurdle", 30.0]
prefix: "₹"
unit: " cr"
decimals: 1
highlight: ["Direct (0.3% cost)"]
caption: "Computed from the simulator's default inputs, before tax. The 2% + 20% manager needs a gross return of about 16.6%, roughly 2.6 percentage points a year more than the direct route, just to match it."
```

The point is not that managers are bad value. Good ones can earn their fees many times over. The point is that the **hurdle is higher than it looks**, so manager selection deserves as much research as stock selection.

## Control and effort: the other axis

```viz
type: quadrant
title: "Control vs research effort required from the investor"
x_label: "Research effort required from you"
y_label: "Control over holdings"
quadrants: ["CONTROL, LIGHT EFFORT", "CONTROL, HEAVY EFFORT", "DELEGATED, LIGHT EFFORT", "DELEGATED, STILL EFFORTFUL"]
points:
  - {label: "Direct equity, self-researched", x: 0.86, y: 0.88}
  - {label: "Direct equity + outsourced research", x: 0.36, y: 0.8, hl: true}
  - {label: "PMS", x: 0.3, y: 0.5}
  - {label: "Cat III AIF", x: 0.24, y: 0.2}
  - {label: "Cat II AIF (private)", x: 0.6, y: 0.16}
caption: "Conceptual. Effort for PMS and AIFs isn't zero, because manager diligence and monitoring are real work. Outsourcing research moves direct equity left without losing control."
```

## Choosing a route

- **Choose a PMS** for a specific manager's listed-equity skill when you want holdings visible in your own name and can live with the fee hurdle.
- **Choose an AIF** for strategies you can't run yourself, such as private equity, private credit or long-short.
- **Choose direct equity** when control, tax efficiency and cost matter most, and you have, or can buy, the research capacity.

Many family offices blend all three. Whatever the mix, apply the same diligence discipline: [an investment memo](/blog/investment-memo-template-family-office/) for every allocation, and a research function [organised around an investment policy](/blog/family-office-research-function-india/).

:::note Manager diligence checklist
1. Net-of-fee track record across a full cycle, verified rather than taken from marketing material.
2. Style consistency: does the portfolio match the stated strategy?
3. Fee structure, hurdle, high-water mark and all expenses in writing.
4. Concentration, liquidity of holdings and capacity limits.
5. Team stability and key-person risk.
6. How the manager behaved in the last major drawdown.
:::
