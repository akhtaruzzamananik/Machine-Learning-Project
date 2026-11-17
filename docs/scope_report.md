# BreastWise Project Scope

**Course:** CSE431 Machine Learning, Fall 2026\
**Group:** 05\
**Industry domain:** Healthcare / Medical Data Analytics\
**Milestone due:** 17 November 2026

## Project title

BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System

## Problem statement

BreastWise asks whether standard machine-learning models can distinguish the benign and malignant labels in the Wisconsin Diagnostic Breast Cancer dataset using its numeric tumour measurements. The project will compare the eight models required by CSE431, examine which measurements influence their predictions, and present a small educational demo. It evaluates benchmark records, not patients, so results will not be framed as diagnoses or treatment guidance.

## Objectives

1. Check the official dataset source, labels and data quality, then describe the records with exploratory analysis.
2. Compare Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Extra Trees, Gradient Boosting and MLP Classifier; tune at least three using stratified cross-validation on training data only.
3. Evaluate a selected model using accuracy, malignant precision and recall/sensitivity, specificity, F1-score and ROC-AUC, and explain its errors.
4. Describe model behavior with global and local methods where feasible, then build an educational application using the saved fitted pipeline.

## Scope and boundaries

**Included:** Public WDBC tabular records; benign/malignant classification; data checks and EDA; a stratified split; leakage-safe preprocessing; eight required classifiers; training-only tuning; the required metrics; explainability; and an educational application.

**Excluded:** real patient records; diagnosis, screening, triage or treatment advice; image-based prediction; medical-device deployment; and claims that the benchmark establishes clinical validity or generalization to current patient populations.

## Dataset and evaluation plan

The course guide describes WDBC as 569 records with 30 numeric predictors. The team will verify the actual download, feature schema, class counts and terms before analysis. Malignant is the planned positive class. The team will record the split ratio, random seed, CV fold count and threshold policy before modeling, and will keep the held-out test set out of tuning and model selection.

## Team

| Student | ID |
|---|---|
| Al-Javin Nishu | 232-15-226 |
| Akhtaruzzaman Anik | 232-15-252 |
| Alzubair Ahmed | 232-15-591 |
| Rayan Ahmed | 232-15-847 |
| Nafis Sadiq | 232-15-895 |

## Non-clinical use

BreastWise is an educational machine-learning prototype built using a public research dataset. It is not a medical device and must not be used to diagnose, screen, or guide treatment. Anyone with a health concern should speak with a qualified healthcare professional.
