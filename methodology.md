# Methodology

## Design
A comparative mixed-methods design combines descriptive displacement statistics, conflict-event indicators, and computational analysis of geopolitical narratives.

### Unit of analysis
For narrative analysis, the default unit is a document/article. For conflict analysis, it is an event. For displacement analysis, it is a country-year observation.

## Workflow
1. Acquire data from documented sources.
2. Validate schemas, dates, missingness, and duplicate identifiers.
3. Normalize text and metadata.
4. Assign geopolitical frames using transparent keyword baselines and, where appropriate, supervised/embedding models.
5. Aggregate frame prevalence by case and time period.
6. Compare narrative indicators with conflict intensity and displacement measures.
7. Conduct qualitative case checks against primary/authoritative sources.
8. Report uncertainty, limitations, and source coverage.

## Baseline frame classifier
The v2.0 baseline is dictionary-based and interpretable. It is a research baseline, not proof of semantic framing. A future extension can use multilingual transformer models with a manually annotated validation set.

## Quantitative outputs
Recommended outputs include frame prevalence, temporal trends, conflict intensity, displacement trends, actor co-occurrence networks, and a transparent composite narrative index. The index should be treated as an exploratory measure and sensitivity-tested.
