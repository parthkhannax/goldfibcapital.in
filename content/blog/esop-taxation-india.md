---
slug: esop-taxation-india
title: "ESOP Taxation in India: How Equity Compensation Is Taxed at Exercise and Sale"
seo_title: "ESOP Taxation in India: Exercise, Sale & Capital Gains"
short: "ESOP & equity compensation tax"
description: "How ESOPs and equity compensation are taxed in India: perquisite tax at exercise, capital gains at sale, startup deferral and foreign RSUs, with ₹ examples."
cluster: investor-tax
level: intermediate
pillar: true
order: 1
date: 2026-10-10
keywords: [ESOP taxation India, equity compensation India, ESOP tax at exercise, RSU tax India, ESOP capital gains, startup ESOP tax deferral, perquisite tax ESOP]
answer: "In India, ESOPs are taxed twice. At exercise, the gap between the share's fair market value and your exercise price is a perquisite, taxed as salary at your slab rate with TDS by the employer. At sale, the gain over that fair market value is a capital gain. For listed shares held over 12 months it is long-term and taxed at 12.5% above ₹1.25 lakh; otherwise short-term at 20%. Unlisted shares need 24 months for long-term treatment."
takeaways:
  - "The first tax bill arrives at exercise, before you have sold anything or received any cash."
  - "Your capital gains cost base is the fair market value on the exercise date, not the price you paid."
  - "The holding period starts at allotment, not at grant or vesting."
  - "Eligible DPIIT startups let employees defer the perquisite tax for up to 48 months, until exit, or until they leave."
  - "Foreign RSUs work the same way but must also be reported in Schedule FA every year."
faq:
  - q: "When are ESOPs taxed in India?"
    a: "ESOPs are taxed at two points. When you exercise, the difference between fair market value and exercise price is taxed as a salary perquisite. When you sell, the difference between the sale price and that fair market value is taxed as capital gains. Grant and vesting by themselves are not taxable events."
  - q: "What is the capital gains tax on ESOP shares?"
    a: "For listed shares sold on an exchange, gains are long-term if held more than 12 months from allotment and are taxed at 12.5% above an annual exemption of ₹1.25 lakh. Short-term gains are taxed at 20%. Unlisted shares need more than 24 months for long-term status (12.5%). Short-term gains on unlisted shares are taxed at slab rates. These are the rates for transfers on or after 23 July 2024."
  - q: "Can ESOP tax be deferred in India?"
    a: "Yes, for employees of DPIIT-recognised startups that are eligible under Section 80-IAC. TDS on the perquisite is deferred until the earliest of 48 months from the end of the assessment year, the sale of the shares, or leaving the company. Other employers must deduct TDS in the year of exercise."
  - q: "How are foreign RSUs taxed for Indian residents?"
    a: "RSUs from a foreign parent are taxed as a perquisite on vesting, at fair market value converted to rupees. The later sale is a capital gain on unlisted-in-India shares, so the 24-month rule applies. Resident taxpayers must also report the holding in Schedule FA and claim foreign tax credit on any tax withheld abroad using Form 67."
cta:
  heading: "Holding a concentrated ESOP position you can't value?"
  body: "Goldfib builds independent research on listed and pre-IPO companies, so founders, executives and family offices can decide what to hold, sell or hedge with real numbers behind the call."
  subject: "ESOP position research enquiry"
---

Equity compensation is now a large part of pay at Indian startups, listed tech companies and Indian arms of global firms. The tax rules are where most employees get caught out. **Tax is due when you exercise, often years before you can sell.**

This guide covers the two taxable events, the rates that apply after the July 2024 Budget, the startup deferral and foreign RSUs. It finishes with a worked example in rupees.

## The four dates that matter

An ESOP passes through four stages. Only two of them create tax.

```viz
type: timeline
title: "ESOP lifecycle: where tax actually hits"
events:
  - when: "Grant"
    title: "Options granted"
    sub: "You get the right to buy shares at a fixed exercise price. No tax."
  - when: "Vesting"
    title: "Options vest"
    sub: "After the cliff and schedule, you can exercise. Still no tax for Indian ESOPs. Foreign RSUs are taxed here because they convert to shares automatically."
  - when: "Exercise / allotment"
    title: "Tax event 1: perquisite"
    sub: "FMV minus exercise price is salary income. The employer deducts TDS at your slab rate. The capital gains holding period starts here."
    hl: true
  - when: "Sale"
    title: "Tax event 2: capital gains"
    sub: "Sale price minus FMV on the exercise date. Long-term or short-term depends on how long you held the shares after allotment."
    hl: true
caption: "Grant and vesting are paperwork events. Exercise and sale are tax events. Foreign RSUs are the one exception: they are taxed at vesting."
```

## Tax event 1: the perquisite at exercise

When you exercise, Section 17(2)(vi) of the Income-tax Act treats the discount as a perquisite:

**Perquisite = (FMV on exercise date − exercise price) × number of shares**

It is added to your salary and taxed at your slab rate. For a senior employee that is often 30% plus surcharge and cess. Your employer deducts TDS and shows it in Form 16.

How FMV is set depends on the listing:

| Share type | FMV for the perquisite |
|---|---|
| Listed in India | Average of opening and closing price on the exercise date (on the exchange with the higher volume) |
| Unlisted | Value set by a SEBI-registered Category I merchant banker, on the exercise date or within 180 days before it |
| Foreign parent (RSU/ESPP) | Market price on the vesting or exercise date, converted at the SBI TT buying rate |

::: warn The cash problem
You pay tax on a gain you have not received. At an unlisted startup, you may have no way to sell the shares for years. An employee who exercises ₹40 lakh of perquisite value in the 30% bracket owes about ₹12.5 lakh in tax, before cess, with no liquidity. Plan the cash before you exercise.
:::

## Tax event 2: capital gains at sale

At sale, your cost of acquisition is the **FMV used for the perquisite**, not the exercise price you paid. That prevents the same gain from being taxed twice.

**Capital gain = sale price − FMV on exercise date**

The rates below apply to transfers on or after 23 July 2024.

```viz
type: bars
title: "Capital gains tax on ESOP shares (transfers from 23 July 2024)"
data:
  - ["Listed, held > 12 months (LTCG, above ₹1.25 L)", 12.5]
  - ["Listed, held ≤ 12 months (STCG)", 20]
  - ["Unlisted, held > 24 months (LTCG)", 12.5]
  - ["Unlisted, held ≤ 24 months (slab, top rate)", 30]
highlight: ["Listed, held > 12 months (LTCG, above ₹1.25 L)", "Unlisted, held > 24 months (LTCG)"]
unit: "%"
decimals: 1
caption: "Base rates before surcharge and 4% cess. Short-term gains on unlisted shares are taxed at the slab rate; 30% is the top slab under the old regime. Securities transaction tax must be paid for the listed rates to apply."
```

The holding period starts on the **allotment date**. Many employees count from grant and sell too early.

## The startup deferral

The 2020 Budget added relief for employees of eligible startups. A startup recognised by DPIIT and certified under Section 80-IAC can defer the TDS on the perquisite. Tax becomes payable within 14 days of the **earliest** of:

1. 48 months from the end of the relevant assessment year,
2. the date you sell the shares, or
3. the date you leave the company.

The perquisite amount is fixed at exercise. Only the payment date moves. Only a minority of startups hold the 80-IAC certificate, so ask HR before you rely on it.

## Foreign RSUs and ESPPs

Many Indian employees hold RSUs in a US or European parent. Three rules differ:

- **Tax at vesting.** RSUs are allotted automatically, so the perquisite is taxed at vesting at FMV in rupees.
- **24-month holding rule.** The shares are not listed on an Indian exchange, so long-term status needs more than 24 months.
- **Disclosure.** Residents must report foreign shares in **Schedule FA** every year, even if nothing was sold. Missing it can attract a penalty under the Black Money Act. Tax withheld abroad is claimed as credit through Form 67.

Your broker's statement is not enough on its own. Keep a vest-by-vest log of dates, FMV, exchange rate and shares withheld for tax. For the Indian side, check the entries in your [Annual Information Statement](/blog/ais-form-26as-capital-gains-india/) against Form 16.

## Worked example in ₹

Priya works at a listed Indian company. She exercises 2,000 options at ₹200. The FMV on the exercise date is ₹1,200. She sells 15 months later at ₹1,800.

```viz
type: waterfall
title: "Illustrative: where Priya's ₹32 lakh gain goes"
steps:
  - ["Perquisite (₹1,000 × 2,000)", 20]
  - ["Capital gain (₹600 × 2,000)", 12]
  - ["=Total gain", 0]
  - ["Slab tax on perquisite @31.2%", -6.24]
  - ["LTCG tax @12.5% on ₹10.75 L", -1.34]
  - ["=Kept after tax", 0]
prefix: "₹"
unit: " L"
decimals: 2
caption: "Illustrative. Assumes the 30% slab plus 4% cess (31.2%), no surcharge, and that the ₹1.25 lakh LTCG exemption is unused. Cess on LTCG is ignored for simplicity. The perquisite is taxed at nearly 2.5 times the rate of the capital gain."
```

The pattern holds in general: **most of the tax comes from the exercise date, not the sale.** If you expect the stock to rise, exercising earlier at a lower FMV moves more of the gain into the lower capital gains rate. That carries risk. If the stock falls, you have already paid slab tax on value that no longer exists.

## A decision checklist before you exercise

```viz
type: flow
title: "Before you exercise: five checks"
steps:
  - title: "Know the FMV"
    sub: "Get the latest merchant banker valuation (unlisted) or the expected exchange price (listed). This sets the tax."
    tag: "Data"
  - title: "Size the tax"
    sub: "Perquisite × your marginal rate. Check whether the 80-IAC deferral applies."
    tag: "Cash"
  - title: "Check liquidity"
    sub: "Listed, a buyback, a secondary sale, or an IPO timeline? Unlisted shares can stay illiquid for years."
    tag: "Exit"
  - title: "Judge concentration"
    sub: "If one stock is more than 20–30% of your net worth, treat it as a research question, not a payroll one."
    tag: "Risk"
  - title: "Plan the sale date"
    sub: "Count 12 or 24 months from allotment for long-term rates, and use the ₹1.25 lakh exemption each year."
    tag: "Tax"
caption: "The tax is mechanical. Valuation, liquidity and concentration are the harder questions."
```

For pre-IPO holdings, the valuation question needs the same discipline as any private deal. Our [pre-IPO and unlisted shares due diligence guide](/blog/pre-ipo-unlisted-shares-due-diligence-india/) covers how to check one. If you are deciding how to deploy the proceeds, [PMS vs AIF vs direct equity](/blog/pms-vs-aif-vs-direct-equity-india/) compares the routes.


## Old vs new tax regime for ESOP income

The perquisite is salary income, so it is taxed under whichever regime you pick for the year. Under the new regime (the default from FY2023–24), the top slab rate is 30% on income above ₹24 lakh from FY2025–26, and the maximum surcharge is capped at 25%. Under the old regime, the top surcharge can reach 37% on income above ₹5 crore. A large one-time exercise can push you into a higher surcharge bracket, so model the total-income figure for the year, not just the perquisite.

Capital gains on listed shares carry a maximum surcharge of 15% under either regime. That is another reason gains taxed at sale tend to cost less than gains taxed at exercise.

## Common mistakes in ESOP filings

1. **Using the exercise price as cost.** This taxes the perquisite twice. Cost is the FMV used in Form 16.
2. **Counting holding period from grant or vesting.** For Indian ESOPs, it starts at allotment.
3. **Ignoring shares sold to cover tax.** Many plans sell a slice of shares at vesting to pay TDS. That is a sale, usually with a tiny gain or loss, and it still needs to be reported.
4. **Leaving foreign RSUs out of Schedule FA.** The disclosure applies even with no sale and no income.
5. **Wrong exchange rate.** Use the SBI TT buying rate on the date specified in the rules, not the rate your bank gave you.
6. **Not claiming foreign tax credit.** If US tax was withheld on dividends, file Form 67 before the return to claim the credit.

## Leaving the company: what happens to your options

Most plans give you a fixed window, often 30 to 90 days after you leave, to exercise vested options. Unvested options usually lapse. Some startups now offer extended windows of several years. If you exercise when you leave, the perquisite is taxed in that year, and for an eligible startup the deferred tax becomes payable within 14 days of the exit. **Check your exercise window and your cash before you resign.**

## Buybacks and secondary sales at startups

Unlisted startups increasingly run ESOP buybacks or secondary sales before an IPO. A buyback by the company is taxed under the buyback rules in force at the time; from 1 October 2024, buyback proceeds are taxed as a deemed dividend in the shareholder's hands at slab rates, with the cost of the shares allowed as a capital loss. A sale to a new investor is taxed as a capital gain on unlisted shares, which needs 24 months of holding for long-term treatment. The two routes can produce very different tax, so ask which one is being used.

::: note Rules change
Rates here reflect the Finance (No. 2) Act, 2024. Surcharge, the new tax regime and treaty relief can change your figures. Confirm with a chartered accountant before acting.
:::
