---
slug: stock-screening-india-factor-models
title: "Building Stock Screens for Indian Markets: From Factor Ideas to a Shortlist Worth Researching"
seo_title: "Stock Screening for Indian Markets: A Factor-Based Guide"
short: "Stock screens for Indian markets"
description: "How to build stock screens for Indian equities: quality, value and momentum factors, India-specific governance and liquidity filters, and pitfalls."
cluster: automation
order: 4
date: 2026-10-03
keywords: [stock screener India, stock screening criteria, factor investing India, quality stocks screen, ROCE screen, small cap screen India]
answer: "A good stock screen for Indian markets narrows the listed universe to a shortlist worth researching, not to a buy list. Apply liquidity and size filters first, then quality factors (ROCE, cash conversion, leverage), governance filters (pledges, related-party transactions, auditor history), and finally value or momentum to rank what's left. Check for survivorship and look-ahead bias before trusting any backtest."
takeaways:
  - "A screen's job is to decide where analysts spend time. It doesn't make investment decisions."
  - "In India, governance and liquidity filters matter as much as financial factors."
  - "Order matters: filter out what you can't own or trust, then rank what's left."
  - "Most backtested screens look better than they are because of survivorship and look-ahead bias."
faq:
  - q: "What are good stock screening criteria for Indian stocks?"
    a: "A common starting point is a minimum market cap and traded value, return on capital employed above the cost of capital over several years, operating cash flow close to reported profit, moderate leverage, low or no promoter pledging, and a reasonable valuation relative to growth. The exact thresholds depend on your strategy and should be tested."
  - q: "What is ROCE and why does it matter in screening?"
    a: "Return on capital employed measures operating profit relative to the capital the business uses. Consistently high ROCE suggests a competitive advantage and efficient capital allocation. Use multi-year averages rather than a single year, because one year can be distorted by cycles or one-off items."
  - q: "What is survivorship bias in stock screening?"
    a: "It happens when a backtest uses only companies that exist today, ignoring those that were delisted, merged or went bankrupt. Because failed companies are excluded, the backtest overstates returns. A reliable backtest uses the universe as it existed at each historical date."
  - q: "Can stock screening be automated?"
    a: "Yes. Once financial, ownership and price data are in a structured database, screens can run automatically on a schedule and flag new entrants and exits. The analyst's time then goes on reviewing the shortlist rather than building it."
cta:
  heading: "Want a custom screen built and run for you?"
  body: "Goldfib builds and runs factor and governance screens on Indian equities for family offices, then writes two-page memos on the names worth a closer look. Tell us your strategy."
  subject: "Custom stock screen"
---

Screening is the cheapest research there is. A few rules run against a database cut thousands of companies to a few dozen, and decide where an analyst's expensive hours go. Done badly, a screen just recycles the same popular names everyone else already owns, or worse, surfaces companies whose numbers can't be trusted.

## Screens decide where to look, not what to buy

```viz
type: funnel
title: "A layered screen for Indian equities"
stages:
  - ["Listed universe", 5000, "All NSE/BSE equities"]
  - ["Can we own it?", 1100, "Market cap and daily traded value floors"]
  - ["Is it a good business?", 320, "5-yr ROCE, cash conversion, leverage"]
  - ["Can we trust it?", 180, "Pledges, RPTs, auditor, contingent liabilities"]
  - ["Is it attractive now?", 40, "Value and momentum ranking"]
caption: "Illustrative counts. Filters come first (what you can't own or trust), ranking comes last. Reversing the order fills the shortlist with cheap stocks that are cheap for a reason."
```

## The factor menu

| Layer | Factor | Typical rule (illustrative) | Why |
|---|---|---|---|
| Investability | Market cap | Above a size floor | Avoids untradeable micro caps |
| Investability | Liquidity | Median daily traded value above a floor | Ensures you can enter and exit |
| Quality | ROCE | 5-yr average above ~15% | Durable returns on capital |
| Quality | Cash conversion | 5-yr OCF / PAT above ~0.7 | Profit that turns into cash |
| Quality | Leverage | Net debt / EBITDA below ~2× | Survives a downturn |
| Governance | Promoter pledge | Low and not rising | Avoids forced-selling risk |
| Governance | Related parties | RPTs small vs revenue | Avoids value leakage |
| Value | Earnings yield / EV-EBITDA | Rank within sector | Price paid for quality |
| Momentum | 6–12 month return | Rank, excluding last month | Trend persistence |

Governance filters belong in the screen itself, not only in later research. Our guide to [promoter pledge signals](/blog/promoter-pledging-shareholding-signals/) explains why they matter so much in India.

## Why sector-relative ranking matters

Raw valuation ranks are dominated by sectors. Public-sector banks and commodity producers always look cheap, while consumer and IT companies always look expensive. Ranking **within sectors** surfaces the cheapest good business in each industry instead of the cheapest industry.

```viz
type: bars
title: "Illustrative: median EV/EBITDA by sector (why raw ranks mislead)"
data:
  - ["FMCG", 38]
  - ["IT services", 22]
  - ["Specialty chemicals", 20]
  - ["Capital goods", 26]
  - ["Cement", 14]
  - ["Metals", 6]
  - ["Oil & gas", 7]
unit: "×"
highlight: ["Metals", "Oil & gas"]
caption: "Illustrative multiples, not current market data. A raw 'cheapest 10%' screen would be filled with metals and energy names. Sector-relative ranking avoids this."
```

## Backtest traps

```viz
type: columns
title: "Illustrative: how biases inflate a backtested screen's annual return"
data:
  - ["Naive backtest", 24]
  - ["Fix survivorship", 19.5]
  - ["Fix look-ahead", 16.5]
  - ["Add costs & slippage", 14.5]
unit: "%"
decimals: 1
highlight: ["Add costs & slippage"]
caption: "Hypothetical screen. Each fix lowers the result: survivorship (using today's companies only), look-ahead (using data before it was published) and trading costs in illiquid names. Realistic results are often far below the first number."
```

- **Survivorship bias.** Use the universe as it existed on each date, including companies later delisted.
- **Look-ahead bias.** Use financials only after their actual filing date. Annual results can arrive up to 60 days after year end.
- **Costs and liquidity.** Small-cap screens look best on paper and trade worst. Model realistic impact costs.

## Automate the run, keep the review

Once the data layer exists (see [building a research data pipeline](/blog/nse-bse-filings-research-data-pipeline/)), a screen can run every week and report **what entered and what left**. The changes are more useful than the full list. The analyst then writes a two-page memo on each new entrant worth a look. That combination, an automated funnel feeding human judgement, is the core of the workflow in our [research automation guide](/blog/ai-investment-research-automation-india/), and the practical way to work [the coverage gap](/blog/coverage-gap-indian-small-caps/).
