# Migration, Conflict & Geopolitical Narratives

**Scholarship-oriented, reproducible research project** at the intersection of Geopolitics, International Relations, Political Communication, Migration Studies, and Data Analysis.

> **Important research integrity note:** This repository does not fabricate empirical findings. Demo data are explicitly synthetic/illustrative. Real-data scripts are provided for reproducible analysis using public/authorized sources.

## Core research question
**How do geopolitical actors and media frame migration during periods of conflict, and how do these narratives vary across cases and over time?**

### Sub-questions
1. Which geopolitical frames (security, humanitarian, economic, border-control, responsibility) dominate during conflict-related migration crises?
2. How do narrative patterns change before, during, and after major conflict events?
3. How are countries, organizations, and political actors connected through migration/conflict narratives?
4. Do media narratives correlate with observed conflict intensity and displacement trends?

## Case-study design
The default study design supports three comparative cases:
- Russia–Ukraine war and European displacement
- Rohingya displacement / Bangladesh–Myanmar context
- A configurable Middle East conflict case

Cases can be changed through `configs/project.yaml` without changing the analysis code.

## Data sources
- **UNHCR Refugee Data Finder:** displacement and refugee indicators; API access is open. See `scripts/fetch_unhcr.py`.
- **World Bank WDI:** international migrant stock and socioeconomic indicators. See `scripts/fetch_world_bank.py`.
- **GDELT:** global news/event data for narrative and media analysis. See `scripts/fetch_gdelt.py`.
- **ACLED:** political violence/protest event data. ACLED access requires registration/authentication; see `scripts/fetch_acled.py`.

## Pipeline
`raw data → validation → preprocessing → frame detection → actor analysis → temporal/case comparison → figures → paper`

## Repository structure
```text
.
├── configs/project.yaml
├── data/{raw,processed}/
├── docs/{data_dictionary.md,methodology.md,ethics.md,limitations.md}
├── notebooks/01_data_validation.ipynb
├── paper/main.md
├── results/figures/
├── scripts/{fetch_unhcr.py,fetch_world_bank.py,fetch_gdelt.py,fetch_acled.py,run_pipeline.py}
├── src/{config.py,data_loader.py,validation.py,preprocess.py,narrative_analysis.py,actor_analysis.py,temporal_analysis.py,geopolitical_index.py,visualization.py}
├── tests/
└── requirements.txt
```

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_demo_data.py
python scripts/run_pipeline.py
pytest -q
```

The demo pipeline creates **illustrative** outputs only. For the actual study, acquire data according to each provider's terms and run the same pipeline.

## Reproducibility
- Configuration is centralized in `configs/project.yaml`.
- Randomness is controlled with a seed.
- Data provenance is recorded in `data/README.md`.
- Raw source files are intentionally not committed by default.
- No API credentials are stored in Git.

## License
MIT for the original code and documentation. External datasets remain subject to their own licenses/terms.
