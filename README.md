# Faker-Gap-Anaylsis
Quantifying the gap between Lee "Faker" Sang-hyeok and other world class midlaners in Faker's prime (2013-2016) using data driven analysis.

-------------

## Project Overview

This project attempts to measure how far ahead Faker was compared to other top mid laners during his peak years. Instead of relying on reputation or memory, the goal is to use objective metrics such as:

- Gold difference at 10 minutes
- XP and CS difference at 10 minutes
- Kill participation and damage share
- Solo kill rate and laning dominance
- Performance by season, patch, and event type

The final result is a set of visualizations and metrics that describe the “Faker gap” across time, regions, and rivals.

-------------

## Research Questions

1. How does Faker’s laning performance (gold/xp/cs diff @10) compare to other elite mid laners from 2013–2016?
2. In which seasons or tournaments is the “gap” between Faker and other mid laners the largest?
3. Does Faker outperform other mids equally in domestic leagues and international events?
4. How sensitive is the “gap” to different definitions of dominance (laning vs teamfight impact vs consistency)?

-------------
## Repository Structure

faker-gap-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/          # original data dumps (not committed)
│   ├── processed/    # cleaned datasets ready for analysis
│   └── external/     # manually downloaded or auxiliary datasets
├── src/              # reusable pipeline + metric code
├── notebooks/        # Jupyter notebooks for EDA and storytelling
├── reports/          # figures and summary reports
└── docs/             # detailed methodology and notes
