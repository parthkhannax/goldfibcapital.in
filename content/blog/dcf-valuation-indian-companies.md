---
slug: dcf-valuation-indian-companies
title: "DCF Valuation for Indian Companies: Cost of Equity, Country Risk and the Terminal Value Trap"
seo_title: "DCF Valuation for Indian Companies: A Practitioner's Guide"
short: "DCF for Indian companies"
description: "How to build a DCF for an Indian company: rupee cost of equity, country risk without double-counting, terminal growth and an interactive tool."
cluster: research
order: 6
date: 2026-10-03
keywords: [DCF valuation India, cost of equity India, equity risk premium India, terminal growth rate India, WACC India, country risk premium]
answer: "A DCF for an Indian company should use rupee cash flows with a rupee discount rate. Build cost of equity from the government bond yield, a mature-market equity premium and a country risk premium, taking care not to double-count sovereign risk. Keep terminal growth below long-run nominal GDP growth. Always show a sensitivity table, because the terminal value usually drives most of the answer."
takeaways:
  - "Keep currencies consistent: rupee cash flows need a rupee risk-free rate and rupee inflation assumptions."
  - "The 10-year G-sec yield already contains some India sovereign risk, so adding a full country risk premium on top can double-count it."
  - "For growth companies the terminal value is often 60–80% of the DCF. Test it before trusting it."
  - "Show a WACC × growth grid and a bull/base/bear range. A single target price claims more precision than the model has."
faq:
  - q: "What is the cost of equity for Indian companies?"
    a: "It depends on the company's risk and the inputs chosen, but practitioners commonly arrive at roughly 11–14% in rupee terms for established companies, built from the 10-year government bond yield plus beta times an equity risk premium for India. Smaller or less liquid companies often warrant a higher rate. These are illustrative ranges, not a standard."
  - q: "What terminal growth rate should I use for an Indian company?"
    a: "Terminal growth is a perpetual nominal rupee rate, so it must stay below long-run nominal GDP growth. Many practitioners use roughly 4–6% nominal for mature Indian businesses. Higher rates imply the company eventually outgrows the economy, which is rarely defensible in perpetuity."
  - q: "Should I add a country risk premium when valuing Indian stocks?"
    a: "If you use a US dollar framework, yes: India's country risk must be priced. If you use the rupee G-sec yield as the risk-free rate, part of India's sovereign risk is already in that yield. Some practitioners strip out the default spread before adding a country premium to avoid double-counting."
  - q: "Why is the terminal value so large in a DCF?"
    a: "Because it captures every cash flow after the explicit forecast period. For companies still growing fast, most of the value sits in those distant years. That makes the DCF very sensitive to the discount rate and terminal growth, which is why a sensitivity table is essential."
cta:
  heading: "Want a valuation you can defend at an investment committee?"
  body: "Goldfib builds driver-based models and DCFs with full sensitivity ranges for Indian companies, with every input sourced and every assumption written down. Send us a name and a deadline."
  subject: "DCF / valuation request"
---

A discounted cash flow model is easy to build and easy to fool yourself with. In India there are three specific traps: mixing currencies, double-counting country risk, and letting a terminal value built on optimistic growth dominate the answer.

This guide walks through each one and ends with an interactive tool showing how much of a DCF's answer sits in the terminal year.

## Step 1: get the currency right

The rule is simple and often broken: **discount rupee cash flows at a rupee rate.**

- If your forecasts are in rupees, which they should be for a domestic business, use the Indian government bond yield as the base, not the US Treasury yield.
- Rupee inflation has historically run above US inflation. Rupee nominal growth rates and rupee discount rates are therefore both higher than their dollar equivalents. Mixing a dollar discount rate with rupee growth inflates value.
- For companies with large export revenues, such as IT services or pharma exporters, forecast in the reporting currency and treat the currency assumption explicitly.

## Step 2: build cost of equity without double-counting

The usual build is risk-free rate plus beta times an equity risk premium. In India the subtlety lies in where country risk enters.

```viz
type: waterfall
title: "Illustrative cost of equity build (rupee terms)"
steps:
  - ["10Y G-sec (risk-free)", 6.8]
  - ["β × mature-market ERP", 4.5]
  - ["β × India country premium", 1.5]
  - ["=Large-cap CoE", 0]
  - ["Size / liquidity premium", 1.5]
  - ["=Small-cap CoE", 0]
unit: "%"
decimals: 1
caption: "Illustrative inputs with β = 1.0. Large-cap cost of equity ≈ 12.8%, small-cap ≈ 14.3%. The G-sec yield and the premia change over time, so update them on the valuation date and source each one."
```

:::warn The double-counting problem
The rupee G-sec yield is not a pure risk-free rate. Part of it compensates for India's sovereign default risk. If you also add a full country risk premium, you count India's risk twice. One rigorous approach strips the sovereign default spread out of the G-sec yield first, then adds an equity risk premium that includes country risk. Whichever approach you use, write it down and apply it the same way to every company.
:::

Beta needs its own care. Regression betas for Indian small caps are noisy because of thin trading. Bottom-up betas built from comparable companies and adjusted for leverage are usually more stable.

## Step 3: respect the terminal value

Terminal growth is a **perpetual** rate. Nothing can grow faster than the economy forever, so terminal growth must stay below long-run nominal GDP growth in rupees. For mature businesses, many practitioners use roughly 4–6% nominal.

The grid below shows why the choice matters. It values a perpetuity of free cash flow (₹100 next year) at different discount rates and growth rates, using the Gordon growth formula.

```viz
type: heatmap
title: "Value of ₹100 of FCF in perpetuity (Gordon growth), ₹"
compute: gordon
params:
  fcf: 100
  wacc: [10, 11, 12, 13, 14]
  growth: [4, 5, 6, 7]
row_title: "WACC"
col_title: "Terminal growth"
base: [2, 1]
prefix: "₹"
decimals: 0
caption: "Computed: value = FCF × (1 + g) ÷ (WACC − g). A one-notch move on a single axis changes value by roughly 10–35%. The outlined cell (12% WACC, 5% growth) is a plausible base case. The corners differ by more than 3×."
```

Moving from the base case to 11% WACC and 6% growth, just one notch on each axis, lifts value by about 40%. Any DCF presented without this grid is hiding its most important assumption.

## Step 4: see how much is terminal value

For a company growing quickly, most of the DCF's value often comes from the terminal year. Use the tool below to see how the split changes with growth and discount rate assumptions.

```viz
type: widget
name: dcf-explorer
title: "Interactive: how much of your DCF is the terminal value?"
caption: "Two-stage model: today's FCF = 100, growing at the first rate for 10 years, then at terminal growth forever. All values are multiples of today's FCF. Try 20% growth at 11% WACC: most of the value lands in the terminal year."
```

When the terminal share passes 70–75%, the DCF mostly restates your terminal assumptions. In those cases, cross-check with:

- **An exit multiple** applied to year-10 earnings, compared with what mature peers trade at today.
- **A reverse DCF**: what growth does the current price imply? Is that plausible?
- **Scenario values** in place of a single point: bull, base and bear, each with a named driver.

## Step 5: present a range, not a number

```viz
type: bars
title: "Illustrative output: valuation range per share"
data:
  - ["Bear: margin stays at 14%", 610]
  - ["Base: margin reaches 17%", 840]
  - ["Bull: margin 19% + new segment", 1120]
  - ["Current price", 780]
highlight: ["Base: margin reaches 17%"]
prefix: "₹"
caption: "Hypothetical company. Showing the range and the driver behind each case lets an investment committee argue about the assumptions, which is where the argument should be."
```

## India-specific modelling notes

- **Standalone vs consolidated.** Value the consolidated entity unless there is a clear reason not to, and treat listed subsidiaries at market value with a holding-company discount where relevant.
- **Working capital.** Many Indian mid-caps run long receivable cycles, especially those selling to government. Model working capital days explicitly.
- **Capex cycles.** Capacity-led businesses such as cement, chemicals and metals invest in lumps. Normalise free cash flow over a cycle before capitalising it.
- **Minority interests and cross-holdings.** These are common in group structures. Subtract minorities and add investments at fair value.

A DCF is a tool for organising assumptions, not for producing truth. Used that way, with a sensitivity grid, a range and a clear variant view, it meets [institutional standards](/blog/institutional-grade-equity-research-india/). For how this fits into a decision document, see the investment memo template.
