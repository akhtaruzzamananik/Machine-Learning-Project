# CSE431 Topic and Problem Scope — Draft

**Status:** Draft prepared on 17 November 2026; team/instructor approval and course-submission status are not verified. This file is not a submission receipt.\
**Course:** CSE431 Machine Learning, Fall 2026\
**Team:** Group 05; five members are listed in Section 11 of the [Research Operating System](../BREASTWISE_RESEARCH_OPERATING_SYSTEM.md).\
**Industry domain:** Healthcare / Medical Data Analytics, as stated in the team plan.

## Project title

**BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System**

## Problem statement

The project will compare machine-learning methods for classifying a record from the Wisconsin Diagnostic Breast Cancer (WDBC) tabular dataset as benign or malignant, and will present model outputs with suitable explanatory information. The prediction target is the dataset's recorded label for a benchmark record.

This course prototype does not diagnose a person, screen a population, recommend treatment, or establish clinical usefulness. Model outputs are educational benchmark results, not medical advice or clinical risk estimates.

## Motivation

The assignment provides a bounded healthcare-data case for practicing data inspection, reproducible preprocessing, model comparison, evaluation, explainability and application integration. The project will report what the supplied benchmark supports and will state its limitations without inferring clinical benefit from benchmark performance.

## Objectives

1. Verify and document the official dataset source, terms, schema, target labels and data-quality findings.
2. Perform descriptive EDA and record evidence-backed observations.
3. Implement the eight course-required estimators across the required algorithm families using a shared evaluation protocol.
4. Tune at least three estimators with stratified cross-validation on training data only.
5. Evaluate a frozen selected model with the required classification metrics and explainability evidence.
6. Build and test an educational application that loads the complete fitted preprocessing-plus-model pipeline.
7. Prepare the course report, presentation, actual contribution log and AI-use declaration.

## Scope

**Included:** tabular WDBC records; benign/malignant classification; source verification and EDA; a stratified train/test design; leakage-safe preprocessing; Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Extra Trees, Gradient Boosting and MLP Classifier; training-only tuning of at least three models; accuracy, malignant precision, malignant recall/sensitivity, specificity, F1-score and ROC-AUC; global/local explainability where feasible; a non-clinical educational app; course documentation and presentation.

The course guide describes 569 records and 30 numeric predictors. These counts must be checked against the actual official download before the report states them as observed project data. The dataset itself is excluded from this repository and must not be committed or pushed.

**Outside scope:** clinical diagnosis, screening or treatment advice; real patient data or identifiers; medical-device deployment; image-based prediction; prospective clinical validation; and claims of generalization to current patient populations. A Q1 journal study is a separate post-course decision and is not promised by this scope.

## Team and work ownership

The five Group 05 members are recorded in the Research Operating System. The source documents disagree on ownership of LR/KNN/SVM and MLP; therefore, model-level assignments remain provisional until the team resolves D02 in STEP-002. The primary coordination roles in OS Section 11 are planning proposals, not evidence of completed contribution.

## Milestones

| Milestone | Official due date | Evidence required |
|---|---:|---|
| Topic and problem scope | 17 Nov 2026 | Final title, problem, objectives, scope, team/domain and accessible tracker evidence |
| Dataset and initial EDA | 21 Nov 2026 | Source record, dataset description, EDA notebook/charts and observations |
| Preprocessing and features | 25 Nov 2026 | Target/features, split strategy and leakage-safe pipeline |
| Eight models / five families | 30 Nov 2026 | Baseline results under one protocol |
| Tuning and explainability | 04 Dec 2026 | Three or more tuning records and explanation evidence |
| Working application | 08 Dec 2026 | Application using the saved fitted pipeline |
| Final testing | 10 Dec 2026 | Test report, screenshots, final package and submission evidence |

The exact deadline time and final evidence URL rules are not in the planning documents and must be confirmed with the instructor.

## Approval and submission status

- Team agreement on this draft: **Not recorded**.
- Instructor confirmation/approval: **Not recorded**.
- 17 Nov milestone submission status: **Unconfirmed**. No submission receipt or course-tracker link was found in the local workspace or project repository during STEP-001 preparation. The course portal/team tracker has not been independently checked here.
- Next action: M1 checks with the team and the actual submission channel, then records the receipt/link or the truthful not-submitted/late status in `docs/milestone_evidence.csv` and resolves D01 in `docs/decisions.md`.
