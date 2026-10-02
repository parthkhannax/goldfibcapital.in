---
slug: nse-bse-filings-research-data-pipeline
title: "Building a Research Data Pipeline from NSE and BSE Filings"
seo_title: "Research Data Pipeline from NSE & BSE Filings: A Blueprint"
short: "A data pipeline from NSE/BSE filings"
description: "A blueprint for a research data pipeline on Indian listed companies: what filings exist, when they land, how to store and verify them, and what it unlocks."
cluster: automation
order: 2
date: 2026-10-03
keywords: [NSE BSE filings data, corporate announcements India, XBRL financial data India, research data pipeline, quarterly results data India, shareholding pattern data]
answer: "A research data pipeline for Indian equities collects exchange filings (results, annual reports, shareholding patterns, transcripts and announcements) on a schedule. It stores the raw documents unchanged, extracts structured data into a database with source references, verifies material figures, and feeds models, screens and alerts. Use licensed vendors or official exchange channels for data, and follow each source's terms of use."
takeaways:
  - "Indian disclosure runs on a predictable calendar. Design the pipeline around it."
  - "Store raw documents permanently and unchanged. Every extracted number should point back to a file and page."
  - "Standalone vs consolidated, restatements and changing segments are the three things that break naive pipelines."
  - "Licensed data is often cheaper than it looks once you count the cost of maintaining your own collection scripts."
faq:
  - q: "Where can I get financial data for Indian listed companies?"
    a: "Primary sources are the NSE and BSE corporate filing pages, which carry results, annual reports, shareholding patterns and announcements, including XBRL-tagged financial filings. Licensed vendors such as institutional terminals and Indian database providers offer cleaned historical data. Many teams combine a vendor for history with exchange filings for timeliness."
  - q: "When do Indian companies publish quarterly results?"
    a: "Under SEBI's listing regulations, listed companies generally must publish quarterly results within 45 days of quarter end, and annual audited results within 60 days of the financial year end. That puts results seasons roughly in the six to eight weeks after each quarter closes."
  - q: "Is it legal to scrape NSE or BSE websites?"
    a: "Each website has its own terms of use, and some restrict automated access. Before automating collection, read the terms, prefer official data products or licensed vendors, rate-limit any permitted access, and take legal advice if in doubt. This guide does not recommend bypassing any access controls."
  - q: "What is XBRL in Indian financial filings?"
    a: "XBRL is a standard format for tagging financial statement data so machines can read it. Indian listed companies file certain financial results and disclosures in XBRL with the exchanges, which makes extraction more reliable than parsing PDFs."
cta:
  heading: "Want the pipeline without building it?"
  body: "Goldfib sets up and operates research data pipelines for family offices: filings ingestion, structured extraction with source references, verification and alerts across your coverage list."
  subject: "Research data pipeline enquiry"
---

Every institutional research process starts with data. For Indian equities the raw material is unusually rich: regulator-mandated, standardised and published on a predictable calendar. Most of the work in a data pipeline is not getting the data. It is keeping it **correct, traceable and comparable over time.**

This guide sets out a blueprint you can build in-house or hand to a partner.

## What gets filed, and when

Indian listed companies file on a predictable rhythm set mainly by SEBI's Listing Obligations and Disclosure Requirements (LODR) regulations.

```viz
type: timeline
title: "The disclosure calendar around each quarter"
events:
  - when: "Day 0"
    title: "Quarter ends"
    sub: "The clock starts for shareholding patterns and results."
  - when: "≤ Day 21"
    title: "Shareholding pattern filed"
    sub: "Promoter, institutional and public holdings, including encumbered promoter shares."
  - when: "≈ Day 15–45"
    title: "Quarterly results season"
    sub: "Results within 45 days of quarter end (60 days for the audited full-year results after Q4). Most mid and large caps report in the middle weeks."
    hl: true
  - when: "Within days"
    title: "Earnings call recordings and transcripts"
    sub: "Investor presentations are filed around the results. Call recordings and transcripts follow within a short window set by the disclosure rules."
  - when: "Continuous"
    title: "Corporate announcements"
    sub: "Board meetings, credit ratings, acquisitions, management changes, pledges and insider trades are filed as events occur."
  - when: "Annually"
    title: "Annual report"
    sub: "Full statements, notes, auditor's report and governance report, sent to shareholders ahead of the AGM."
caption: "Deadlines summarised from SEBI LODR at the time of writing. Rules are amended periodically, so verify current timelines before relying on them operationally."
```

## Pipeline architecture

```viz
type: tree
title: "Blueprint: from filings to research outputs"
node_width: 180
root:
  label: "Research data pipeline"
  children:
    - label: "Sources"
      children:
        - label: "Exchange filings (results, XBRL, announcements)"
        - label: "Annual reports and transcripts (PDF)"
        - label: "Licensed vendor history"
    - label: "Raw store"
      children:
        - label: "Unchanged originals, hashed and dated"
        - label: "Never overwritten; restatements are new versions"
    - label: "Structured layer"
      children:
        - label: "Financials: standalone + consolidated, per period"
        - label: "Ownership: promoter, pledge, FPI, DII"
        - label: "Text facts: guidance, RPTs, KPIs, with source page"
    - label: "Outputs"
      children:
        - label: "Model history updates"
        - label: "Screens and peer tables"
        - label: "Alerts and change logs"
caption: "Four layers. The raw store is the most important design decision: if you keep originals, every error downstream can be traced and fixed."
```

## The data you need, by type

| Data type | Typical source | Frequency | Main gotcha |
|---|---|---|---|
| Quarterly P&L | Results filing (PDF + XBRL) | Quarterly | Standalone vs consolidated; restated prior periods |
| Balance sheet & cash flow | Half-yearly / annual filings | Half-yearly / annual | Limited quarterly balance-sheet detail |
| Segment data | Results and annual report notes | Quarterly / annual | Segment definitions change |
| Shareholding & pledges | Shareholding pattern filings | Quarterly + events | Category definitions; encumbrance types |
| Guidance & KPIs | Transcripts, presentations | Quarterly | Unstructured; needs extraction and verification |
| Corporate actions | Announcements | Event-driven | Splits/bonuses must adjust per-share history |
| Prices & volumes | Exchange or vendor feed | Daily | Corporate-action adjustment |

## The three things that break naive pipelines

### 1. Standalone vs consolidated

Indian companies report both. Many PDF tables put them on adjacent pages with identical layouts. A pipeline that does not record which one it extracted will eventually mix them, and margins and growth rates will be quietly wrong. **Make "basis" a required field on every financial fact.**

### 2. Restatements

When a company restates prior periods after a merger, demerger or accounting change, the "same" quarter now has two values. Never overwrite. Store both, with the filing each came from, and choose explicitly which one a model uses.

### 3. Changing segments

Segments are reorganised more often than you would expect. Map old segment names to new ones in a lookup table, and flag any period where the mapping isn't clean.

## Verification: the step most pipelines skip

```viz
type: bars
title: "Illustrative: where extraction errors come from"
data:
  - ["Standalone / consolidated mix-up", 31]
  - ["Wrong period or column", 24]
  - ["Units (lakh vs crore vs million)", 17]
  - ["Restated vs original figures", 12]
  - ["Sign errors (expenses, other income)", 9]
  - ["Genuine OCR / parsing errors", 7]
highlight: ["Standalone / consolidated mix-up", "Wrong period or column"]
unit: "%"
caption: "Illustrative distribution based on common failure modes in PDF and table extraction. Most errors are structural, not OCR, so they can be caught with simple rules and spot-checks."
```

Simple automated checks catch most of these before a human ever looks:

- **Arithmetic identities.** Segment revenues sum to total. The balance sheet balances. Quarterly figures sum to annual.
- **Unit sanity.** Flag any value that differs from the prior period by more than 10×.
- **Basis consistency.** Alert when consolidated revenue is lower than standalone, which is possible but rare.
- **Cross-source match.** Compare the XBRL value with the PDF-extracted value where both exist.

Whatever is still flagged goes to an analyst, who checks it against the source page in seconds because the pipeline stored the reference.

## Build, buy or blend?

| Approach | Good for | Watch out for |
|---|---|---|
| Licensed vendor only | Fast start, deep history | Cost per seat; less control over text data |
| Build on exchange filings | Timeliness, text data, custom fields | Maintenance; terms-of-use compliance |
| Blend | Most serious desks | Reconciling the two sources |

Most teams end up blending: vendor data for deep, clean history, and their own extraction for timely and text-based data such as guidance, related-party transactions and pledge events.

## What it unlocks

Once the data layer is reliable, the rest of the research stack becomes cheap. Screens run in seconds. [Pledge monitors](/blog/promoter-pledging-shareholding-signals/) update themselves. [Transcript trackers](/blog/earnings-call-transcript-analysis-india/) fill as calls are filed. Analysts can spend the week on the judgement work described in our [guide to AI and research automation](/blog/ai-investment-research-automation-india/).
