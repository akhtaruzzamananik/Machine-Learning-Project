# BreastWise AI

**BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System**\
CSE431 Machine Learning · Fall 2026 · Group 05

## Project overview

BreastWise is a course project to compare machine-learning classifiers on the Wisconsin Diagnostic Breast Cancer (WDBC) tabular dataset, examine model behavior with explainability methods, and build an educational application around a saved fitted pipeline.

The prediction target is the benign/malignant label for a dataset record. This project is **not a medical device** and is not validated to diagnose, screen, guide treatment, or support patient-care decisions. Model scores are not clinical risk estimates.

> BreastWise AI is an educational machine-learning prototype built using a public research dataset. It is not a medical device and must not be used to diagnose, screen, or guide treatment. Any health concern should be discussed with a qualified healthcare professional.

## Current status

The single canonical STEP-001 scope document is `docs/scope.md`. Its course submission and approval status remain unconfirmed. No model-training results, fitted model, or working application are claimed as complete. Record actual progress and evidence as each step is completed.

## Planned course work

- Verify the official WDBC source, file schema, label mapping, terms, and data quality.
- Perform descriptive EDA and document the observations without clinical or causal overclaims.
- Create a stratified, leakage-controlled split and preprocessing pipelines.
- Compare the eight required estimators: Logistic Regression, K-Nearest Neighbours, Support Vector Machine, Decision Tree, Random Forest, Extra Trees, Gradient Boosting, and MLP Classifier.
- Tune at least three models using cross-validation on training data only.
- Report accuracy, malignant precision and recall/sensitivity, specificity, F1-score, and ROC-AUC with clear class/threshold definitions.
- Provide global and local explainability evidence where feasible.
- Build and test an educational app that loads the complete fitted preprocessing-plus-model pipeline.
- Prepare the course report, presentation, contribution record, AI-use declaration, and reproducible evidence.

These are planned deliverables, not completed results. The single [topic and problem scope document](./docs/scope.md) is in this repository. The [Research Operating System](./BREASTWISE_RESEARCH_OPERATING_SYSTEM.md) and [Project Execution Blueprint](./BREASTWISE_PROJECT_EXECUTION_BLUEPRINT.md) define the governance rules and dated execution steps.

## Dataset policy

The planned dataset is the [UCI Wisconsin Diagnostic Breast Cancer dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic). Verify the actual download and its terms before analysis. Dataset files, derived tables, and row-level records are not committed or pushed. Keep permitted local copies under the ignored `data/` directory and record source/version/hash in the dataset card.

Do not add real patient records or identifiers to the classroom demo. Use only permitted public benchmark records or synthetic/demo inputs. Do not redistribute dataset files unless their terms explicitly permit it.

## Paper and repository policy

Research-paper/manuscript files are excluded from commits and pushes. Project code, plans, documentation, app source, notebooks, and other permitted artifacts may be committed and pushed after checking data terms, privacy, and the staged-file list. Whether the CSE431 course report PDF is included under the “paper” exclusion is still an open decision; do not stage report PDFs until that is resolved.

## Planned repository layout

```text
data/                 # local dataset files; ignored by Git
notebooks/            # EDA and experiment notebooks
src/                  # ingestion, preprocessing, models, evaluation, XAI, inference
models/               # approved fitted-pipeline artifacts and metadata
app/                  # educational application and app checks
reports/              # permitted figures, tables, experiments, and evaluation evidence
docs/                 # decisions, dataset card, protocols, contributions, AI-use log
```

The project structure and environment may change after the team confirms the setup in STEP-004. Do not assume a training command or app command exists until it is documented here and verified from a clean environment.

## Team and responsible use

The team has five members. Confirm model-level ownership as a team before implementation; the original role proposals assigned some models differently. Log actual contributions with evidence. Confirm the instructor's current AI-use rule and declare any AI assistance accurately.

## Publication note

The course comparison does not by itself establish a novel Q1-journal contribution or clinical validity. Any separate paper requires a literature-supported research gap, an appropriate data/validation design, supervisor and author approval, and a separate go/no-go review. Journal acceptance cannot be guaranteed.
