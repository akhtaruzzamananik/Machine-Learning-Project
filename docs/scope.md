# BreastWise Project Scope

**Course:** CSE431 Machine Learning, Fall 2026\
**Team:** Group 05\
**Industry domain:** Healthcare / Medical Data Analytics\
**Scope milestone:** 17 November 2026

## Project title

**BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System**

## Problem statement

BreastWise asks whether machine-learning models can distinguish the benign and malignant labels in the Wisconsin Diagnostic Breast Cancer dataset using its numeric tumour measurements. The project will compare the models required by CSE431, examine their errors and explanations, and present an educational demo. The target is the label recorded for each benchmark row, not a person’s diagnosis.

## Motivation

This assignment gives the team a focused way to practice data inspection, reproducible preprocessing, model comparison, evaluation, explainability and application development. The report will describe what the benchmark supports and state its limits without claiming clinical benefit.

## Objectives

1. Verify the official dataset source, terms, target labels and data quality, then describe the records with exploratory analysis.
2. Compare Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Extra Trees, Gradient Boosting and MLP Classifier under one evaluation protocol.
3. Tune at least three models with stratified cross-validation using training data only.
4. Evaluate a selected model with the required metrics and explain its errors and behavior.
5. Build an educational application using the complete fitted preprocessing-plus-model pipeline, then prepare the course report and presentation.

## Project scope

The course guide describes the Wisconsin Diagnostic Breast Cancer dataset as 569 records with 30 numeric predictors. The team will verify the actual official download, feature schema, class counts and use terms before analysis.

The project includes benign-versus-malignant classification of tabular records, data checks and exploratory analysis, one stratified train/test split, leakage-safe preprocessing, the eight required models, training-only tuning, explainability and an educational application. The evaluation will report accuracy, malignant precision and recall or sensitivity, specificity, F1-score and ROC-AUC. Malignant is the planned positive class. The split ratio, random seed, cross-validation fold count and threshold policy will be recorded before modeling. The held-out test data will not be used for tuning or model selection.

The planned source is the [UCI Wisconsin Diagnostic Breast Cancer dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic). The dataset and derived record-level data are excluded from this GitHub repository.

## Scope limits

This is a course benchmark study, not a clinical evaluation. It does not include diagnosis, screening, triage, treatment advice, real patient records, image-based prediction, medical-device deployment or claims that results generalize to current patient populations. The application is for educational demonstration only.

## Planned evaluation

Malignant is the planned positive class. The final comparison will report accuracy, malignant precision and recall or sensitivity, specificity, F1-score and ROC-AUC. Before modeling, the team will record the split ratio, random seed, cross-validation folds and threshold policy. The held-out test set will not be used to tune models or choose features. Any score will be described as a benchmark result, not a clinical performance claim.

## Team

| Student | ID |
|---|---|
| Al-Javin Nishu | 232-15-226 |
| Akhtaruzzaman Anik | 232-15-252 |
| Alzubair Ahmed | 232-15-591 |
| Rayan Ahmed | 232-15-847 |
| Nafis Sadiq | 232-15-895 |

The team will confirm model-level ownership before implementation because the original role proposals assign some models differently.

## Milestone calendar

| Milestone | Due date |
|---|---:|
| Topic and problem scope | 17 Nov 2026 |
| Dataset and initial EDA | 21 Nov 2026 |
| Preprocessing and features | 25 Nov 2026 |
| Eight models across five or more families | 30 Nov 2026 |
| Tuning and explainability | 04 Dec 2026 |
| Working application | 08 Dec 2026 |
| Final testing and submission | 10 Dec 2026 |

## Educational use notice

BreastWise is an educational machine-learning prototype built using a public research dataset. It is not a medical device and must not be used to diagnose, screen, or guide treatment. Anyone with a health concern should speak with a qualified healthcare professional.
