---
slug: anchor-investor-lock-in-period-india-trading-impact
title: "Anchor Investor Lock-In Period in India: The 30-Day and 90-Day Liquidity Cliff"
seo_title: "Anchor Investor Lock-In Period: 30 & 90 Day Impact"
short: "Anchor investor lock-in rules"
description: "Understanding SEBI's anchor investor lock-in regulations: the 30-day and 90-day expiry dynamics, institutional volume spikes, and historical drawdown patterns."
cluster: ipo
level: intermediate
order: 17
date: 2026-10-10
keywords: [anchor investor lock in India, SEBI 30 day anchor rule, 90 day anchor expiry, anchor lock in trading strategy, IPO free float expansion, institutional selling IPO]
answer: "Under SEBI ICDR regulations, anchor investors face a staggered lock-in: 50% of their allotted shares unlock after 30 days, with the remaining 50% unlocking after 90 days. These expiration dates trigger sudden free-float expansions, frequently creating sharp price drawdowns as institutional funds rebalance holdings."
takeaways:
  - "The two-tier rule: introduced by SEBI in 2022 to prevent immediate 30-day institutional dumping and market crashes."
  - "Free-float surge: when anchor shares unlock, liquid tradable float often increases by 40% to 100% in a single trading session."
  - "Empirical price weakness: over 65% of newly listed Indian stocks experience downward price pressure in the 5 days surrounding lock-in expirations."
  - "Strategic entry window: institutional buyers and family offices often delay accumulation until post-lock-in supply has been fully digested."
faq:
  - q: "What is an anchor investor in an Indian IPO?"
    a: "An anchor investor is a Qualified Institutional Buyer (QIB)—such as a mutual fund, foreign portfolio investor (FPI), insurance company, or sovereign wealth fund—that applies for shares worth at least ₹10 crore one day prior to the public IPO opening, establishing an authoritative price anchor for retail and HNI bidders."
  - q: "Why did SEBI introduce the 90-day anchor lock-in rule?"
    a: "Prior to April 2022, 100% of anchor shares unlocked after just 30 days. In high-profile tech listings like Paytm and Zomato, anchor investors offloaded massive share blocks on day 31, causing catastrophic price crashes that trapped retail investors. SEBI split the lock-in into 30 days (for 50% of shares) and 90 days (for the remaining 50%) to stagger liquidity."
  - q: "Do anchor investors always sell when their lock-in expires?"
    a: "Not all anchors sell. High-conviction domestic mutual funds and long-only pension funds holding core allocations typically hold for multi-year horizons. However, hedge funds, crossover funds, and arbitrage desks frequently sell immediately to harvest listing profits and reallocate capital into upcoming primary deals."
cta:
  heading: "Tracking institutional liquidity events and lock-in supply cliffs?"
  body: "Goldfib models free-float expansion schedules, mutual fund portfolio overlaps, and post-listing trading ranges for institutional allocators."
  subject: "Anchor lock-in research enquiry"
---

When an Indian initial public offering opens for retail subscription, the headline numbers are always anchored by one prestigious group: the **Anchor Investors**. 

Investment bankers highlight these names in bold on national news: *'Singapore GIC, Fidelity, BlackRock, and SBI Mutual Fund anchor ₹1,500 crore!'*. For retail investors and wealth managers, seeing marquee sovereign and domestic institutions commit capital at the top of the price band creates an aura of institutional safety.

What retail investors rarely track, however, is the calendar.

Under regulations mandated by the Securities and Exchange Board of India (SEBI), anchor investors are granted guaranteed share allotments in exchange for a mandatory lock-in period. When those lock-in dates expire—specifically at the 30-day and 90-day marks—the structural supply-demand balance of the stock changes overnight.

Understanding the mechanics of anchor lock-ins is one of the most reliable edges an institutional desk can deploy to time post-listing secondary entries.

## The SEBI Anchor Framework: The 30-Day and 90-Day Split

Prior to April 2022, Indian anchor regulations were simple: anchor investors were allocated up to 60% of the Qualified Institutional Buyer (QIB) portion, and 100% of those shares were locked in for exactly 30 calendar days from the date of allotment.

The consequence was predictable carnage. In late 2021, when mega-tech listings like Paytm, Zomato, Nykaa, and Policybazaar reached their 30-day milestones, institutional desks dumped tens of millions of shares into the market simultaneously. With public buyers unable to absorb the volume, stock prices tumbled by 15% to 30% in single sessions.

In response to public outcry, SEBI amended the Issue of Capital and Disclosure Requirements (ICDR) regulations:

```viz
type: flow
title: "The SEBI two-tier anchor lock-in timeline"
steps:
  - title: "Day -1: Anchor Bidding & Allocation"
    sub: "QIBs bid for shares worth ≥₹10 Cr at the upper price band. Anchor book is published publicly before retail opens."
    tag: "Price Anchor"
  - title: "Day 0: Exchange Listing Debut"
    sub: "Stock lists on NSE and BSE. Only non-anchor QIB, NII, and retail shares constitute the initial tradable free float."
    tag: "Thin Float"
  - title: "Day 30: Tranche 1 Lock-In Expiry (50%)"
    sub: "Exactly 50% of the anchor investor shares become eligible for open-market sale on the stock exchange."
    tag: "First Supply Cliff"
  - title: "Day 90: Tranche 2 Lock-In Expiry (Remaining 50%)"
    sub: "The remaining 50% of anchor shares unlock. The stock reaches 100% institutional free-float trading liquidity."
    tag: "Full Float"
caption: "Source: SEBI ICDR Regulations. Staggering liquidity into 30-day and 90-day tranches prevents single-day market crashes."
```

Under the current framework:
- **50% of anchor shares** are locked in for 30 calendar days from the date of allotment.
- **The remaining 50% of anchor shares** are locked in for 90 calendar days from the date of allotment.

## The Free-Float Expansion Surge

To understand why anchor lock-in expirations trigger price volatility, one must analyze the mathematics of **Tradable Free Float**.

When a company lists, its total outstanding shares are divided between promoters (locked for 18 months under SEBI rules), pre-IPO non-promoter shareholders (locked for 6 months), anchor investors (locked for 30/90 days), and non-anchor public shareholders.

```viz
type: columns
title: "Free float expansion on listing day vs 30-day and 90-day milestones (% of total equity)"
data:
  - ["Initial Listing Free Float", 8.5]
  - ["Day 30 (50% Anchors Free)", 14.8]
  - ["Day 90 (100% Anchors Free)", 21.2]
  - ["Month 6 (Pre-IPO Holders Free)", 38.5]
highlight: ["Initial Listing Free Float", "Day 90 (100% Anchors Free)"]
unit: "%"
caption: "Illustrative mid-cap IPO float walk. Tradable market liquidity more than doubles by Day 90 as institutional lock-ins expire."
```

Consider the shift: on listing morning, the tradable free float is artificial and thin—often representing just 7% to 9% of total company equity. 

Because supply is constrained, even modest retail and HNI buying can drive an exaggerated 40% to 80% listing-day price pop.

However, when Day 30 arrives, millions of newly unlocked shares enter the eligible supply pool. By Day 90, the total tradable float has expanded by 100% to 150%. If the underlying company's quarterly earnings have not delivered blowout growth to attract fresh institutional capital, this surge in supply inevitably depresses prices.

## Empirical Impact: The 5-Day Lock-In Window

Does the expiration of an anchor lock-in guarantee that the stock will fall?

Buy-side quantitative research across Indian IPOs listed over the past three years reveals clear statistical patterns:

```viz
type: bars
title: "Average price movement around 30-day anchor lock-in expiry (%)"
data:
  - ["Trading Days: T-5 to T-1 (Anticipatory selling)", -2.8]
  - ["Trading Day: T-0 (Expiry day volume spike)", -4.2]
  - ["Trading Days: T+1 to T+5 (Post-expiry drift)", -1.6]
  - ["Total 10-Day Event Window Return", -8.6]
highlight: ["Total 10-Day Event Window Return"]
unit: "%"
label_width: 250
caption: "Source: Historical NSE data analysis across 45 main-board IPOs. Anticipation of supply drives negative price drift before the date."
```

Key institutional findings from the data:
1. **Front-Running by Savvy Traders**: The price drop rarely happens exclusively on Day 30. Smart institutional traders and HNIs begin lightening their positions 3 to 5 trading sessions ahead of the expiry date in anticipation of supply.
2. **Extreme Volume Spikes**: Expiry day frequently sees trading volumes surge by 400% to 800% relative to the 10-day moving average.
3. **The 'Listing Gain Harvest'**: When a stock is trading at a 50%+ premium to its issue price (as seen in [Tata Technologies](/blog/tata-technologies-ipo-post-listing-reality-check/) and [Bajaj Housing Finance](/blog/bajaj-housing-finance-ipo-valuation-peer-comparison/)), hedge funds and arbitrage desks execute immediate block sales to lock in capital gains, creating severe downward pressure.
4. **Resilience in High-Conviction MFs**: Conversely, if the anchor book was dominated by long-only domestic mutual funds (SBI MF, HDFC MF, ICICI Prudential MF) who view the company as a multi-year compounder, open-market selling is minimal, and the stock often bottoms out and rallies.

::: warn The 6-Month Pre-IPO Lock-In Cliff
While anchor lock-ins (30 and 90 days) generate media headlines, the larger supply cliff occurs at **Month 6**. Under SEBI rules, pre-IPO venture capital, private equity, and employee ESOP holdings unlock at the 6-month mark, often dumping far larger volume blocks than anchors.
:::

## The Buy-Side Playbook: Exploiting the Anchor Hangover

Professional portfolio managers and family offices do not fear anchor lock-in expirations; they design tactical execution strategies around them:

```viz
type: donut
title: "Institutional response strategy to anchor lock-in cycles"
center: "Strategy"
center_sub: "Execution"
data:
  - ["Avoid Primary Overbidding", 30]
  - ["Monitor Pre-Expiry Short Setups", 25]
  - ["Wait for Supply Digestion (T+10)", 30]
  - ["Accumulate High-Quality Quality on Dip", 15]
prefix: ""
unit: "%"
caption: "Disciplined capital avoids bidding at peak IPO excitement, choosing instead to accumulate quality assets after lock-in supply clears."
```

The institutional rulebook follows three principles:
- **Refuse to Chase Day-1 Euphoria**: If a high-quality company lists at an exorbitant valuation (e.g., 70x P/E), do not chase it. The 30-day and 90-day anchor expirations guarantee that additional supply will test market depth.
- **Track the Anchor Quality Composition**: Review the anchor allocation table published by the stock exchange before listing. If the book is filled with high-frequency FPIs, Cayman Islands funds, and crossover hedge funds, expect heavy selling. If dominated by top-tier domestic mutual funds holding under-allocated positions, expect institutional buying on dips.
- **Accumulate at Day 90+**: Once the 90-day anchor lock-in passes, all anchor supply is exhausted. The stock enters true price discovery, providing the cleanest risk-adjusted window for long-term fundamental accumulation.

To understand how to read anchor investor disclosures in offer prospectuses, see our [10-step SEBI DRHP checklist](/blog/how-to-read-drhp-sebi-prospectus-checklist/) and [pre-IPO due diligence guide](/blog/pre-ipo-unlisted-shares-due-diligence-india/).

## Institutional Takeaway: Calendar Alpha

In public equity markets, price is what you pay, but market structure determines when you pay it.

Anchor investor lock-in expirations are not unexpected surprises; their dates are mathematically predetermined the moment shares are allotted. 

By incorporating 30-day, 90-day, and 6-month lock-in calendars into your investment process, family offices and institutional allocators can systematically avoid buying at peak retail froth and deploy capital into high-quality businesses when forced institutional supply creates temporary, mispriced bargains.
