# Fintech Customer Behavioural Segmentation
### *Who are our customers post-pivot? Which ones can we save?*

---

## The Business Problem

A Nigerian fintech company launched with an aggressive loan-first acquisition strategy — running a physical campaign that rapidly onboarded thousands of customers on the promise of accessible credit. Rising default rates made lending unsustainable. The company pivoted: loans were dropped entirely, and the product repositioned around savings, transfers, bill payments, and airtime.

The result was immediate. Customers who came for credit had no reason to stay. Transaction volume dropped **75%** in a single month. Dormancy spiked.

This project answers the question the product and growth team now faces:

> **Who are our customers post-pivot — and which ones can we save?**

---

## Project Overview

An end-to-end data science project covering the full analytical pipeline — from dirty raw data to actionable customer segments — built on a simulated dataset modelled on real Nigerian fintech dynamics.

| | |
|---|---|
| **Domain** | Nigerian Fintech |
| **Technique** | Unsupervised Machine Learning — K-Means Clustering |
| **Dataset** | 5,000 customers · 49,230 transactions · 1 year |
| **Tools** | Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn |
| **Output** | 5 actionable customer segments with business recommendations |

---

## The Dataset

Three relational tables simulated to reflect realistic Nigerian fintech behaviour — including deliberate data quality issues for cleaning demonstration.

| Table | Rows | Description |
|---|---|---|
| `customers.csv` | 5,000 | Customer demographics, KYC tier, acquisition channel, location |
| `loans.csv` | 5,000 | Loan uptake and repayment status per customer |
| `transactions.csv` | ~89,000 raw · 49,230 clean | All transactions Jan–Dec 2022 including system-generated rows |

**Timeline**
```
Jan 2022 ──────────────── Jun 2022 │ Jul 2022 ──────────────── Dec 2022
        PRE-PIVOT PERIOD           │         POST-PIVOT PERIOD
  Loans + Transactional Services   │    Transactional Services Only
```

**Data quality issues introduced for realistic cleaning practice:**
- Inconsistent `acquisition_channel` values — 25 variants of 5 valid values
- Logical contradiction — `loan_defaulted = Yes` where `loan_taken = No` (30 rows)
- Duplicate transactions — 31 rows from simulated ETL pipeline reruns
- Outlier transaction amounts — 15 erroneous entries up to ₦4,500,000

---

## Project Structure

```
fintech-customer-segmentation/
│
├── data/
│   ├── raw/                          # Original dirty source files
│   ├── cleaned/                      # Post-cleaning datasets
│   └── processed/                    # Feature matrix and segment assignments
│
├── notebooks/
│   ├── 01_data_validation.ipynb      # Structured audit — what is wrong?
│   ├── 02_data_cleaning.ipynb        # Fix issues, document every decision
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb  # 8 behavioural features per customer
│   ├── 05_segmentation_modelling.ipynb
│   └── 06_segment_profiling_and_insights.ipynb
│
├── src/
│   ├── settings.py                   # Paths, display settings
├── requirements.txt
└── README.md
```

---

## Analytical Pipeline

```
Raw Dirty Data
      │
      ▼
01 Data Validation ──── Identify 6 data quality issues across 3 tables
      │
      ▼
02 Data Cleaning ─────── Fix all issues · Save clean datasets
      │
      ▼
03 Exploratory Analysis ─ Customer profiles · Loan behaviour · Pivot story
      │
      ▼
04 Feature Engineering ── 8 behavioural features · 1 row per customer
      │
      ▼
05 Segmentation Model ─── K-Means K=5 · Elbow + Silhouette methods
      │
      ▼
06 Segment Profiling ──── Business labels · Recommendations · Insights
```

---

> **Design decision:** RFM features are calculated post-pivot only. The goal is to understand who customers are *now*, not who they were before the product changed. The pivot ratio bridges both periods by comparing pre and post-pivot activity directly.

---

## Segmentation Results

K-Means clustering with K=5, determined by the elbow method (bend at K=5) balanced against silhouette score (0.370 at K=5) and business interpretability.

### The 5 Segments

---

#### 🔵 Loyal Customers — 532 customers (10.6%)
*Action: **Reward***

The platform's most valuable customers. Never loan-dependent — they came for transactional services and stayed. Post-pivot they became *more* active.

| Metrics |
|------|
| Highest Monetary Value |
| Highest Frequency |
| Lowest Recency (recently active) |
| High Pivot Ratio |
| Highest Product Diversity |
| Very low loan dependency |
| Almost no defaults |

**Recommendation:** Introduce a loyalty programme — cashback on transfers, fee waivers, early access to new features. Do not over-communicate. Track monthly as an early warning signal.

---

#### 🟢 Adapted Customers — 1,184 customers (23.7%)
*Action: **Nurture***

Highly active pre-pivot customers who found reasons to stay. Mixed loan history but maintained a high percentage of pre-pivot activity post-pivot — the second most valuable segment.

| Metrics |
|------|
| High Monetary Value |
| Moderate-High Frequency |
| Low Recency (active) |
| Good Product Diversity |
| Strong Pre-Pivot Frequency |
| Many took loans |
| Few actually defaulted |
| Moderate Pivot Ratio |

**Recommendation:** Personalised product recommendations, savings incentives, transfer fee waivers. Monitor pivot ratio monthly for early churn signals.

---

#### 🟠 At-Risk Customers — 803 customers (16.1%)
*Action: **Retain — Time Sensitive***

Every customer in this segment took a loan and repaid it — 0% default rate. They left on good terms. But post-pivot engagement has nearly collapsed.

| Metrics |
|------|
| Low Monetary |
| Low Frequency |
| High Recency |
| Low Product Diversity |
| Loan Taken = 1 |
| Default rate: 0% — every customer repaid |

**Recommendation:** Personalised re-engagement acknowledging their responsible borrower status. Premium savings products. First in line if credit products return. Act immediately.

---

#### 🔴 Loan-Dependent Churners — 1,232 customers (24.6%)
*Action: **Reactivate if possible***

Came exclusively for loans. 100% loan uptake, 100% default rate. Essentially gone post-pivot.

| Metrics |
|------|
| Very low Monetary Value |
| Very low Frequency |
| Extremely High Recency |
| Almost zero Pivot Ratio |
| Minimal Product Diversity |
| Loan Taken = 1 |
| Loan Defaulted = 1 |

**Recommendation:** Low re-engagement investment. If attempting reactivation, use low-friction entry points — airtime, bill payment. Never offer credit. Deprioritise in marketing spend.

---

#### 🟣 Ghost Customers — 1,249 customers (25.0%)
*Action: **Deprioritize***

Never took a loan, barely engaged in either period. These customers were never truly acquired — they exist in the database but never formed a meaningful platform relationship.

| Metrics |
|------|
| Very low Monetary |
| Very low Frequency |
| High Recency |
| Minimal Product Diversity |
| Almost zero Pivot Ratio |
| Loan Taken = 0 |
| Loan Defaulted = 0 |

**Recommendation:** Single low-cost reactivation attempt then move on. Use as input to improve acquisition quality — fewer ghost accounts means better unit economics.

---

### Segment Distribution at a Glance

```
Ghost Customers          ████████████████████████  25.0% (1,249)
Loan-Dependent Churners  ███████████████████████   24.6% (1,232)
Adapted Customers        ██████████████████████    23.7% (1,184)
At-Risk Customers        ████████████████          16.1%   (803)
Loyal Customers          ██████████                10.6%   (532)
```

**Lost (49.6%)** — Ghost Customers + Loan-Dependent Churners  
**Salvageable (39.8%)** — Adapted Customers + At-Risk Customers  
**Core (10.6%)** — Loyal Customers

---

## Setup and Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/fintech-customer-segmentation
cd fintech-customer-segmentation

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook
```


> **Note:** Raw data files are not included in the repository. Place `customers.csv`, `loans.csv`, and `transactions.csv` in `data/raw/` before running the notebooks.

---

## Technical Stack

| Category | Tools |
|---|---|
| Data manipulation | Pandas, NumPy |
| Machine learning | Scikit-learn (KMeans, StandardScaler, silhouette_score) |
| Visualisation | Matplotlib, Seaborn |
| Environment | Python 3.11 · Jupyter Notebook · VS Code |

---

## About This Project

This project was built step by step as a portfolio piece demonstrating end-to-end data science capabilities in a Nigerian fintech context — from data simulation and quality issues through to business-ready segmentation insights.

The dataset was simulated with deliberate realism — including KYC-gated transaction access, CBN-compliant system charges (VAT, stamp duty, transfer fees), location-differentiated default rates, and realistic customer archetypes — to reflect the kind of data a data scientist would encounter working at a Nigerian fintech company.

---

*Built with domain knowledge from direct fintech industry experience.*
