---
slug: foreign-tax-credit-ftc-form-67-india
title: 'Foreign Tax Credit (FTC) & Form 67 in India: Claiming US Dividend Withholding
  Tax Relief'
seo_title: Foreign Tax Credit & Form 67 in India (US Stocks)
short: Foreign Tax Credit (FTC) & Form 67 in India
description: 'How Indian residents investing in US equities claim Foreign Tax Credit
  (FTC) under Rule 128: Form 67 filing deadlines, DTAA Article 25, and tax relief.'
cluster: investor-tax
level: intermediate
order: 45
date: '2026-11-02'
keywords:
- foreign tax credit form 67 india
- rule 128 income tax foreign tax credit
- us dividend withholding tax 25 percent dtaa
- avoiding double taxation us stocks lrs
- schedule tr schedule fsi itr-2 itr-3
- irs form 1042-s foreign tax credit claim
- cross border global investing tax compliance india
answer: Indian resident investors claim Foreign Tax Credit (FTC) under Rule 128 and
  Section 90 of the Income-tax Act to prevent double taxation on foreign income, such
  as the 25% US withholding tax deducted on US stock dividends. To claim FTC, taxpayers
  must file Form 67 online before filing their annual Income Tax Return.
takeaways:
- US dividends paid to Indian residents suffer a 25% withholding tax deducted at source
  under the India-US DTAA (Article 10).
- Under Section 90 and Rule 128, Indian taxpayers can claim Foreign Tax Credit (FTC)
  to offset foreign taxes against Indian tax liabilities.
- Form 67 must be filed electronically on the income tax portal on or before the due
  date of filing the ITR under Section 139(1).
- Foreign assets and foreign source income must be meticulously disclosed in Schedule
  FA and Schedule FSI to avoid Black Money Act penalties.
faq:
- q: What is the US withholding tax rate on dividends paid to Indian resident investors?
  a: Under Article 10 of the India-US Double Taxation Avoidance Agreement (DTAA),
    the standard US dividend withholding tax rate for individual Indian residents
    is 25% (reduced from the US domestic rate of 30% upon submitting a valid Form
    W-8BEN to the US broker). This tax is withheld directly by the US broker before
    cash hits the investor's brokerage account.
- q: What happens if Form 67 is filed after the Income Tax Return is submitted?
  a: Historically, assessing officers routinely disallowed FTC if Form 67 was not
    filed prior to the ITR. Following recent judicial rulings from ITAT benches and
    CBDT amendments, filing Form 67 before the end of the relevant assessment year
    or during belated return filing is generally accepted as directory rather than
    mandatory; however, filing Form 67 before the ITR remains the safest compliance
    practice to prevent automated CPC tax demand notices.
- q: How is the allowable Foreign Tax Credit computed in India?
  a: 'Under Rule 128(3), the Foreign Tax Credit is restricted to the lower of: (a)
    the actual tax paid in the foreign country, or (b) the Indian income tax payable
    on that specific foreign income. If the foreign tax rate exceeds the applicable
    Indian tax slab rate, the excess foreign tax credit cannot be refunded or carried
    forward.'
cta:
  heading: Managing cross-border US stock portfolios and LRS tax compliance?
  body: Goldfib Capital builds automated foreign dividend reconciliation tools, IRS
    1042-S parsers, and Form 67 / Schedule FA compliance generators for Indian investors.
  subject: Foreign tax credit automation enquiry
---

Under the Reserve Bank of India's Liberalised Remittance Scheme (LRS), thousands of Indian high-net-worth individuals and family offices invest in US technology giants—such as Microsoft, Apple, and Alphabet—via overseas brokerages.

However, cross-border equity investing introduces **cross-border double taxation friction**.

When a US corporation distributes a dividend to an Indian resident shareholder, the US Internal Revenue Service (IRS) automatically deducts a **25% withholding tax** at source under the India-US Double Taxation Avoidance Agreement (DTAA).

Without filing for **Foreign Tax Credit (FTC)** in India, the investor risks paying Indian slab-rate income tax (up to 39%) on top of the 25% already withheld in the US, resulting in a confiscatory combined tax rate exceeding 50%.

```viz
type: flow
title: "The cross-border US dividend tax and FTC credit workflow"
steps:
  - title: "US Dividend Declaration"
    sub: "US corporation declares $1,000 dividend to Indian resident shareholder."
    tag: "Gross Income"
  - title: "US IRS Withholding at Source"
    sub: "US broker deducts 25% ($250) under DTAA Article 10; remits $750 net cash. Broker issues IRS Form 1042-S."
    tag: "Foreign Tax Paid"
  - title: "File Form 67 on Indian Tax Portal"
    sub: "File Form 67 online attaching Form 1042-S / broker withholding statement prior to filing annual ITR."
    tag: "FTC Application"
  - title: "File ITR with Schedule FSI & TR"
    sub: "Report $1,000 gross dividend in Schedule FSI and claim $250 credit in Schedule TR, offsetting Indian tax payable."
    tag: "Zero Double Tax"
```

## The Mechanics of Rule 128 Foreign Tax Credit

Under **Rule 128 of the Income-tax Rules, 1962**, an Indian resident taxpayer is entitled to claim credit for any foreign tax paid in a country with which India has entered into a DTAA (Section 90) or in a non-DTAA country (Section 91).

The credit is calculated on a **source-by-source and country-by-country basis**:

$$\text{Allowable FTC} = \min(\text{Foreign Tax Paid}, \text{Indian Tax Payable on that Foreign Income})$$

```viz
type: columns
title: "Foreign Tax Credit math: Effective tax burden with vs without Form 67"
unit: " USD"
data:
  - ["Gross US Dividend Income", 1000.0]
  - ["US Tax Withheld at Source (25%)", 250.0]
  - ["Indian Tax Payable at 30% Slab", 300.0]
  - ["Without FTC: Double Tax Paid (US $250 + IND $300)", 550.0]
  - ["With FTC: IND Tax Payable After Credit ($300 - $250)", 50.0]
caption: "Double taxation relief: Claiming FTC reduces Indian tax from $300 to $50, ensuring total global tax does not exceed the Indian 30% slab rate."
```

In this example, because the Indian tax payable ($300) exceeds the US tax withheld ($250), the taxpayer receives full credit for the $250 paid abroad and pays only the incremental $50 to the Indian Income Tax Department.

## The Mandatory Requirement: Form 67 Compliance

To claim Foreign Tax Credit, **Rule 128(8) mandates the electronic filing of Form 67**.

Form 67 requires taxpayers to disclose:
- The country where income originated (e.g., United States).
- The specific Article of the DTAA governing the tax credit (e.g., Article 10 for Dividends, Article 25 for FTC).
- The exact amount of foreign income converted to Indian Rupees using the **SBI Telegraphic Transfer (TT) Buying Rate** on the last day of the month preceding income receipt.
- Proof of tax withholding: **IRS Form 1042-S**, broker dividend confirmation slips, or tax withholding certificates.

```viz
type: bars
title: "Cross-border tax compliance risk points for Indian global investors"
unit: " risk"
data:
  - ["Schedule FA (Foreign Assets) Disclosure Omission", 95.0]
  - ["Failure to File Form 67 Prior to ITR Deadline", 88.0]
  - ["Incorrect TT Buying Rate Exchange Conversion", 65.0]
  - ["Failure to Reconcile Broker Form 1042-S with AIS", 72.0]
caption: "Compliance hazards: Schedule FA omissions carry severe criminal scrutiny under the Black Money Act; Form 67 delays lead to automatic CPC tax notices."
```

## The Ultimate Trap: Schedule FA and the Black Money Act

While claiming Foreign Tax Credit is financially rewarding, it carries an enormous regulatory responsibility: **Schedule Foreign Assets (Schedule FA)**.

Under the **Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015**:
- Any Indian resident who owns foreign shares, units in an offshore fund, or an overseas bank/brokerage account **must disclose them in Schedule FA of ITR-2 or ITR-3**, regardless of whether they earned any income during the year.
- **The Penalty for Non-Disclosure**: Even if the foreign investment was legally funded via verified banking channels under LRS and fully disclosed on bank statements, failure to fill Schedule FA carries a **mandatory penalty of ₹10 lakh per assessment year** and potential prosecution.

When claiming FTC in Form 67, the Income Tax Department's automated CPC systems cross-reference the foreign income reported in Schedule FSI against the assets declared in Schedule FA.

If an investor claims $250 of US dividend tax credit but failed to declare their US brokerage account in Schedule FA, an automated scrutiny notice is triggered.

<p>Automating global investment tax reporting and Form 67 filing? <strong><a href="/contact/">Connect with Goldfib Capital</a></strong> to deploy automated IRS Form 1042-S reconciliation, foreign currency conversion engines, and Schedule FA compliance modules.</p>

By establishing systematic Form 67 filing protocols and rigorous Schedule FA recordkeeping, global investors enjoy international equity diversification without double taxation friction or regulatory penalties.

For related frameworks, read our guide on [AIS and Form 26AS Capital Gains Reconciliation](/blog/ais-form-26as-capital-gains-india/) and [Family Office Offshore Banking and Custody](/blog/family-office-offshore-banking-custody/).
