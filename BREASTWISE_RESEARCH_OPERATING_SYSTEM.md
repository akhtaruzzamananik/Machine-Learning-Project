# BREASTWISE AI — RESEARCH OPERATING SYSTEM

## Cover page

**Course title:** BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System\
**Course:** CSE431 Machine Learning, Fall 2026\
**Project type:** Healthcare-focused machine-learning coursework and educational prototype\
**Primary dataset:** Wisconsin Diagnostic Breast Cancer (WDBC), tabular record-level data\
**Version/date:** v1.2.0 / 17 November 2026\
**Status:** Governance and planning baseline; execution is NOT VERIFIED; course rules, responsibilities and data choices retain open decisions until evidenced\
**Team:** Five students; names/IDs and role proposal recorded in Section 11\
**Operational owner:** M1 coordinates team records; every work package has a distinct accountable member and reviewer\
**Scientific authority:** Latest instructor rubric/announcement, then supplied CSE431 guide within that rubric\
**Execution companion:** [BreastWise Project Execution Blueprint](./BREASTWISE_PROJECT_EXECUTION_BLUEPRINT.md)\
**Intended output:** Reproducible comparison of eight tabular classifiers, explainability evidence and a working educational application using a saved fitted pipeline\
**Clinical status:** Not a medical device, not validated for diagnosis, screening, prognosis, treatment or patient care

The title is retained because it appears in the supplied CSE431 guide. “Decision support” in the title does not grant clinical decision authority. The working system is limited to classifying records represented in the public benchmark and must display the non-clinical-use notice.

## Version history

| Version | Date | Change | Approval state |
|---|---|---|---|
| v1.0.0 | 2026-11-17 | Detailed governance baseline aligned to the supplied guide, team schedule and 49-step execution blueprint | Planning recommendation; team/instructor decisions remain open |
| v1.1.0 | 2026-11-17 | Recorded user-requested deletion of the two supplied source PDFs; removed dead local links and retained historical source/page locators. Audited OS/blueprint stage, step and gate alignment. No scientific scope changed. | Editorial correction authorized by user; source PDFs no longer retained locally |
| v1.2.0 | 2026-11-17 | Recorded the user-provided GitHub remote and commit/push boundary: project artifacts may be pushed except research-paper files and dataset files; added initial remote-state observation and exclusion controls | User-directed repository policy; first Git initialization/push still awaits STEP-001–004 prerequisites |
| v1.3.0 | Pending | Record any scope, course-rule, data, model or reporting change with affected decisions, steps and gates | Do not assign until change occurs |

Record author, date, reason, evidence, affected D/STEP/G IDs, reviewer and approval for every revision. A typo correction does not change scientific commitments; a target, split, metric, dataset, model-selection or clinical-claim change does.

## Table of contents

[Executive summary](#executive-summary)
1. [Project constitution, source authority and scope](#os-01)
2. [Repository architecture and folder contracts](#os-02)
3. [Research question, literature and claim workflow](#os-03)
4. [Dataset source, privacy and data handling](#os-04)
5. [Preprocessing, split and leakage prevention](#os-05)
6. [Models, experiments and comparison](#os-06)
7. [Evaluation protocol and interpretation](#os-07)
8. [Explainability and application operating rules](#os-08)
9. [Writing, presentation and submission](#os-09)
10. [Version control, artifacts and reproducibility](#os-10)
11. [Roles, review and human decisions](#os-11)
12. [Daily research operations and milestone control](#os-12)
13. [Quality gates, risks and completion](#os-13)
14. [Template library and session forms](#os-14)
[Appendix A. Canonical definitions](#appendix-a)
[Appendix B. Registry catalog and schemas](#appendix-b)
[Appendix C. Stage map and dependency chain](#appendix-c)
[Appendix D. Metric and model-family reference](#appendix-d)
[Appendix E. Acronyms and glossary](#appendix-e)
[Appendix F. Source coverage and planning self-review](#appendix-f)
[Appendix G. Publication-readiness checklist](#appendix-g)

<a id="executive-summary"></a>
## Executive summary

This handbook sets the governance rules for Group 05's CSE431 project: scope, source authority, data provenance, EDA, stratified splitting, leakage-safe preprocessing, eight common ML baselines, tuning, explainability, app integration, final testing, reporting, team contributions and course submission. Detailed work order and owner/deadline handoffs are in the [49-step execution blueprint](./BREASTWISE_PROJECT_EXECUTION_BLUEPRINT.md).

The supplied course guide describes 569 WDBC records with 30 numeric predictors and a benign/malignant target. These are source-stated expectations, not permission to skip inspection. The downloaded file's source, schema, target encoding, class counts, missing conventions and terms must be checked against official documentation and recorded before modeling.

The course requires eight named estimators (Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Extra Trees, Gradient Boosting and MLP Classifier), coverage of at least five algorithm families, tuning at least three estimators using training-only stratified cross-validation, an appropriate metric set, explainability evidence and a functional app using the saved fitted pipeline. The metric set includes accuracy, malignant precision, malignant recall/sensitivity, specificity, F1 and ROC-AUC. The evaluation threshold, split ratio, seed, CV fold count, scoring choice, averaging and app deployment requirement are not fixed by the two PDFs; resolve these as decisions rather than silently adopting defaults.

The team plan's seven milestones run from 17 November to 10 December 2026. The topic/scope milestone is due 17 November, the current planning date. Confirm actual submission status immediately. The final testing milestone is 10 December, but no time of day or final upload rule is supplied. The team plan says its role breakdown is proposed; it conflicts with the guide on ownership of LR/KNN/SVM and MLP. Resolve the conflict in STEP-002 and the decision register before implementation.

Course completion is not Q1 journal readiness. The course brief asks for a benchmark comparison on a small familiar dataset; that alone does not establish novelty, clinical validity, external generalizability or journal acceptance. A separate post-course publication track requires a current literature gap, feasible data and validation, uncertainty/calibration/bias analysis, supervisor and author review, and journal-fit checks. No process can guarantee acceptance.

All work begins NOT STARTED unless evidence says otherwise. A planned file, empty register, notebook draft, screenshot or high score is not by itself a passed gate. Preserve failed and negative runs, state limitations and never fabricate results, sources, contribution credit, AI-use declarations or approvals.

## Authority and evidence labels

Use these labels consistently in the tracker, reports, decisions, code comments and review notes:

- **COURSE REQUIREMENT:** Explicitly stated in the supplied course guide/team milestone plan or latest instructor instruction. Cite the document/page or announcement.
- **PLANNING RECOMMENDATION:** A method/governance rule proposed in this OS to make the work more reproducible or defensible. Adopt it through a recorded team decision when it affects scope or time.
- **SOURCE FACT:** A statement actually supported by official dataset documentation or an inspected dataset file. Include locator/version/access date.
- **OPEN DECISION:** Missing, ambiguous, conflicting or not-yet-approved detail. Name decision owner, blocking step and resolution evidence.
- **EXECUTION EVIDENCE:** A saved output tied to exact code/data/config/model version. A planned output is never execution evidence.

Authority order: (1) current instructor rubric and announcements; (2) supplied CSE431 guide; (3) supplied Group 05 schedule, except its role plan is explicitly proposed and may be changed by team agreement; (4) team-recorded decisions within instructor rules; (5) this OS; (6) execution blueprint; (7) code and notebook defaults. If authorities conflict, stop the affected work, record the conflict and ask the instructor where course interpretation is involved. Do not use a lower-level code default to override a governing decision.

<a id="os-01"></a>
# 1. Project constitution, source authority and scope

## 1.1 Source-grounded facts ledger

The two PDF sources were supplied and read during planning, then removed from the workspace at the user's request on 17 November 2026. The PDF page numbers below refer to their printed page sequence and preserve a historical source record; they are not live links or a substitute for the originals. If a future decision requires independent reinspection of a PDF, request an authorized copy or obtain documented instructor clarification. Dataset properties still require independent source/file verification.

| ID | Source-backed statement | Locator | Operating implication |
|---|---|---|---|
| RF01 | Exact course title is “BreastWise: An Explainable Machine Learning-Based Breast Cancer Classification and Decision Support System” | Course Guide p.1–2; Team Plan p.1,4 | Keep title consistent; contextualize “decision support” as educational prototype |
| RF02 | Course CSE431, Fall 2026, team size five | Guide p.1; Team Plan p.1–2 | Verify five full names and IDs in report/slides |
| RF03 | WDBC is the recommended primary dataset; guide describes 569 records, 30 numeric predictors and benign/malignant labels | Guide p.2 | Verify actual retrieved source/schema/counts before reporting |
| RF04 | Task is classification of dataset-style records and explanation of influential features | Guide p.2 | No patient diagnosis or symptom-based inference |
| RF05 | Required models are LR, KNN, SVM, Decision Tree, Random Forest, Extra Trees, Gradient Boosting and MLP Classifier | Guide p.3–4; Team Plan p.4,6 | Register all eight, with consistent data and metric contracts |
| RF06 | At least five algorithm families and at least one ensemble and one neural-network model are required | Guide p.2–4; Team Plan p.4,7 | Document family mapping and model count |
| RF07 | Tune at least three models; suggested SVM, Random Forest, MLP; use stratified CV on training data | Guide p.3–4; Team Plan p.3–4 | Freeze search plan; never pass test data to tuning |
| RF08 | Required metrics include accuracy, precision, malignant recall/sensitivity, specificity, F1 and ROC-AUC | Guide p.4; Team Plan p.3,7 | Define positive class and threshold; report denominators |
| RF09 | Global explanation and local examples are expected where feasible; SHAP or permutation importance acceptable | Guide p.4–5; Team Plan p.3–4 | Verify feature mapping and describe model behavior, not cause |
| RF10 | App should use a saved fitted preprocessing-plus-model pipeline, validate input and display a clear academic/non-clinical disclaimer | Guide p.5; Team Plan p.3–5 | Keep training/inference preprocessing identical; test errors and disclaimer |
| RF11 | Report sections, slides, contribution table, references and AI-use declaration are required; slide title/footer IDs are specified | Guide p.6; Team Plan p.5–6 | Check full roster/title and full ID footer on every slide |
| RF12 | AI-generated contribution below 25% is mentioned only “if that is the stated course rule”; declaration is required | Guide p.6 | Confirm instructor definition, denominator and declaration format; do not assume a calculation |
| RF13 | Official milestone dates are 17, 21, 25, 30 Nov; 4, 8 and 10 Dec 2026 | Team Plan p.2 | Preserve dates; confirm time of day and current rubric |
| RF14 | Internal buffers are 20, 24, 29 Nov and 3, 7 Dec | Team Plan p.7 | Use as handoffs, not replacement official deadlines |
| RF15 | Team plan roles are a proposal, not an immutable source assignment | Team Plan p.7 | Team can resolve owner conflicts and document changes |
| RF16 | Team plan assigns LR/KNN/SVM to M4, while guide assigns them to M2; MLP ownership also differs | Team Plan p.3,6; Guide p.5 | Resolve D02 before work; distinguish implementation/tuning/review owners |
| RF17 | Dataset, tool and AI declarations must be honest; do not invent experiments, scores, citations or clinical claims | Guide p.6; Team Plan p.5–7 | Evidence and author review required for every final claim |
| RF18 | Public de-identified or synthetic/demo inputs only; the classroom app must not collect real identifiers/medical records | Guide p.5 | No real patient data or clinical use in demo |

## 1.2 Binding course scope

**Included:** WDBC source verification and description; descriptive EDA; target and predictor definition; one approved stratified train/test design; reproducible leakage-safe preprocessing; eight prescribed classifier implementations; common baseline comparison; at least three tuned models; held-out final test after selection freeze; required classification metrics/plots; explainability; saved full inference pipeline; functional application; report, slides, contribution and AI-use records; final clean-environment testing.

**Not included in the course claim:** clinical diagnosis, screening, treatment recommendations, patient-level risk prediction, medical-device deployment, prospective evaluation, image-based classification, guaranteed clinical utility or external validation. These are separate research questions and cannot be implied by the title, dataset or a good benchmark score.

**Output unit:** one WDBC tabular record with 30 numeric predictor fields, subject to verified schema. The target is its recorded B/M label. The classifier is not trained to diagnose a person from symptoms, examination or imaging.

## 1.3 Candidate objectives and research questions

Course objectives in operational form:

| Objective | Operational interpretation | Evidence required |
|---|---|---|
| CO1 Explore and prepare dataset | Verify source/schema/terms, report EDA and build one reproducible feature/target contract | Source card, audit, charts, split and transform records |
| CO2 Compare required ML methods | Run eight named models under a shared protocol and tune at least three using training-only CV | Model registry, run logs, search records, common metric table |
| CO3 Evaluate with appropriate metrics | Report class-specific errors, ranking metric, threshold and test estimate transparently | Locked protocol, predictions/counts, metric script and plots |
| CO4 Explain behavior | Provide global and local model explanations with correct feature names and caveats | XAI protocol, plots, examples and interpretation review |
| CO5 Deliver usable classroom demo | Serve frozen full pipeline through an app with input validation and disclosure | Model artifact hash, parity check, input test matrix, screenshots |

Candidate course question (PLANNING RECOMMENDATION): **Under one leakage-controlled evaluation protocol, how do the eight prescribed classical and neural-network classifiers compare on the WDBC benign/malignant record-label task, and what trade-offs are observed in malignant sensitivity, specificity, ROC-AUC, explainability and app reproducibility?**

This is a course comparison question, not a novelty claim. The literature review must establish whether a separate journal question is useful. Do not replace a null or unfavorable answer with a stronger claim.

## 1.4 Claims boundary and approved language

Allowed wording, if evidenced: “The model classified records from the WDBC benchmark”; “malignant-class sensitivity on the stated held-out partition was …”; “the fitted model assigned importance to …”; “the prototype demonstrates an educational inference path.”

Disallowed without separate clinical evidence and approval: “diagnoses breast cancer”; “detects cancer in patients”; “clinically safe/accurate”; “reduces missed diagnoses”; “works for all populations”; “explains why a tumour is malignant”; “validated clinical decision support.”

The user interface must use the full disclaimer specified in the course guide or an instructor-approved equivalent:

> BreastWise AI is an educational machine-learning prototype built using a public research dataset. It is not a medical device and must not be used to diagnose, screen, or guide treatment. Any health concern should be discussed with a qualified healthcare professional.

Display it on Home and Predict/Result views before the user interprets output. In reports, state that feature attributions describe the fitted model and do not establish biological causation.

## 1.5 Source and approval decisions at initialization

All rows are **OPEN DECISION** until evidence is recorded. The execution blueprint maps them to STEP IDs.

| ID | Decision / missing evidence | Owner | Resolve by | Required resolution |
|---|---|---|---|---|
| D01 | Whether the 17 Nov topic/scope item was submitted; exact submission time/evidence URL rules | M1 + all | Immediately | Receipt/link or truthful missing/late record; instructor instruction |
| D02 | Model ownership conflict; implementation vs tuning vs review ownership | All five; M1 records | STEP-002 / 17 Nov | Agreed responsibility matrix and meeting note |
| D03 | Latest rubric, report format, slide rules, AI limit definition, app hosting/demo requirement | M1 with instructor | STEP-003 / 17 Nov | Source-linked course-requirements note |
| D04 | Exact dataset retrieval, file/version, terms and raw-data storage/redistribution | M1; M2 reviews | STEP-005 / 20–21 Nov | Official source record, checksum, terms note |
| D05 | Holdout ratio, random seed, CV folds, scoring objective, threshold and metric conventions | M2/M4; team approves | STEP-013 / 23 Nov | Versioned evaluation protocol |
| D06 | Cleaning/outlier/duplicate/imbalance handling | M1/M2; M4 reviews | STEP-015 / 24 Nov | Decisions with counts and rationale |
| D07 | Model baseline settings and tuning budget/search spaces | Model owners; M4 coordinates | STEP-018/027 | Versioned model/search configs before runs |
| D08 | Explanation method, reference set, local case selection and feature mapping | M5/M2/M4 | STEP-032 / 3 Dec | XAI protocol with limitation note |
| D09 | Probability calibration and any threshold selection method | M4; team approves | STEP-013/034 | Explicit protocol; if not evaluated, say so |
| D10 | Report reference style, length, final submission time and upload route | M1 with instructor | STEP-003 | Current instruction locator and package checklist |
| D11 | Contribution evidence and authorship expectations for course report | M1 + members | STEP-004 | Actual dated contribution matrix reviewed by all |
| D12 | AI-use threshold calculation and declaration form | M1 with instructor; each member logs | STEP-003 / 17 Nov | Written definition or explicit “unresolved”; accurate usage log |
| D13 | App technology and whether local demo, hosted link or both required | M5/M1 with instructor | STEP-036 / 5 Dec | Approved app/deployment decision and backup |
| D14 | Whether a separate journal study is feasible and supervisor-supported | All + supervisor | After STEP-046 | Signed G09 planning decision; not implied by course result |
| D15 | Does “paper” exclusion mean the journal manuscript only, or also the CSE431 course report PDF? | User/M1 | Before any report PDF is staged | Recorded answer; until then, keep all manuscript/report PDFs unstaged |

Decision records include source evidence, options considered, selected route, approver, date, affected artifacts/steps, conditions and superseding ID. A “yes” in chat without a locator/decision record is not durable approval for a material research decision.

<a id="os-02"></a>
# 2. Repository architecture and folder contracts

## 2.1 Canonical repository layout

Use this layout or record a justified mapping before creating artifacts. Do not create parallel “final_final” folders or multiple competing registries.

```text
BreastWise-AI/
  README.md
  requirements.txt                 # or approved environment/lock files
  .gitignore
  data/
    raw/                            # immutable source; restricted/not committed as terms require
    interim/                        # temporary derived files; normally reproducible
    processed/                      # derived artifacts with provenance and permissions
  notebooks/
    01_eda.ipynb
    02_baselines.ipynb               # if notebook form is used
    03_tuning.ipynb
    04_explainability.ipynb
  src/
    data/                            # load/schema validation
    preprocessing/                  # feature contract and Pipeline factory
    models/                          # estimator catalog/config construction
    evaluation/                      # metrics, plots, uncertainty helpers
    explainability/                  # XAI wrappers and feature mapping
    inference/                       # shared model loader/inference entry point
  app/
    app.py                           # Streamlit or approved app entry point
    tests/                           # automated/manual test definitions
    assets/                          # non-sensitive UI assets/disclaimer
  models/
    registry/                        # metadata/cards; weights separately controlled
  reports/
    figures/
    tables/
    experiments/
    evaluations/
    explainability/
    app_tests/
    releases/
  docs/
    decisions.md
    responsibility_matrix.csv
    milestone_evidence.csv
    contributions.csv
    ai_use.md
    dataset_card.md
    feature_contract.md
    evaluation_protocol_v1.md
    repository_map.md
    course_requirements.md
```

## 2.2 Folder contracts

| Home | Contains | Must not contain |
|---|---|---|
| `data/raw/` | Original UCI file and source/checksum metadata in permitted storage | Edited version of raw file, public identifiers without approval |
| `data/interim/` | Re-creatable transformations for analysis | Sole copy of raw data or untracked manual edits |
| `data/processed/` | Manifest-linked split/feature files where allowed | Unlabeled or mixed-version records |
| `notebooks/` | EDA, modeling/review notebooks with execution order and source IDs | Hidden state needed to get reported result; private credentials/data |
| `src/` | Reusable, reviewed ingestion/pipeline/model/metric/XAI/inference code | Duplicated app-only preprocessing or result numbers hardcoded as science |
| `models/registry/` | Model card, ID, hash, dependencies, intended use and lineage | Unreviewed weights or secret tokens |
| `app/` | UI, inference wrapper, validation and app-specific test cases | Real patient records, identifiers, or training logic that changes final model |
| `reports/` | Generated figures/tables, run logs, test/release reports and exact submission package | Hand-edited metrics with no source; duplicate canonical evidence |
| `docs/` | Decisions, policy, provenance, roles, tracker schemas | Claims of approval or completion without evidence |

## 2.3 Root-file contracts

- `README.md`: project scope, setup, dataset source/terms note, reproducible commands, app launch, disclaimer and limitations. It must not imply clinical validation.
- `requirements.txt` or lock file: package names and versions sufficient to recreate the environment. Record the Python version and install command. A list of unpinned packages is not a reproducibility lock.
- `.gitignore`: local environments, cache, secrets, restricted raw data, generated large model files and temporary outputs. Inspect tracked files as well as ignore patterns; ignore does not remove an already tracked artifact.
- `docs/repository_map.md`: actual chosen path for each canonical registry/artifact if it differs from this OS.
- `docs/course_requirements.md`: instructor-confirmed format, deadlines, AI declaration, evidence URL and demo rules.

## 2.4 Storage and access tiers

1. **Public source-controlled metadata:** code, non-sensitive documentation, plots permitted by source/license, run metadata with no private identifiers.
2. **Team-restricted artifacts:** raw dataset if redistribution is restricted, row-level split map if it could expose identity, fitted models, detailed prediction records and instructor-only evidence.
3. **Secrets:** access tokens/passwords stored only in approved secret manager; never in notebooks, commit history, screenshots or app code.
4. **Temporary:** caches/rendered notebook intermediates; reproducible and cleaned per team policy after final evidence is preserved.

Data terms must be checked before copying or publicizing. Public availability does not automatically grant rights to redistribute the dataset, fitted artifact or derived records. The group should avoid storing any real patient identifiers; the assignment says to use the public de-identified dataset or synthetic/demo inputs.

## 2.5 Repository readiness review

Before STEP-025 baselines, M1/M2 verify: all five have access; source code is versioned; environment is recorded; current raw data is not accidentally in public Git; one canonical split/protocol path exists; app model artifacts are addressed by hash; contribution/AI/milestone logs are usable. Record G01 and later G02/G03 separately; repository setup alone does not pass data or method gates.

<a id="os-03"></a>
# 3. Research question, literature and claim workflow

## 3.1 Course-level literature expectation

The supplied guide calls for a brief related-work section. For coursework, provide a focused, source-verified context: what the WDBC dataset represents, what common tabular classifiers do, why the chosen metric and explanation method are relevant, and what the benchmark cannot establish. Cite primary sources and official documentation. Do not inflate a short context section into a novelty claim.

## 3.2 Source search and screening protocol

For each search session, record:

1. Search date, database/site, exact query and filters.
2. Inclusion question: WDBC/tabular breast-record classification, model evaluation, explainability, validation, or methodology relevant to the chosen question.
3. Exclusion criteria and reason (wrong modality/outcome, duplicate, non-primary or insufficiently relevant).
4. Bibliographic metadata and DOI/official URL verified against the publisher/primary source where available.
5. Full-text status, extraction date and any missing method details.
6. Conflict handling: a second member reviews key papers and resolves disagreements in the screening log.

Do not present another paper's score as directly comparable unless source, split, preprocessing, target mapping and metrics are comparable. Do not claim “first,” “novel,” “state of the art,” or “best” from a convenience search.

## 3.3 Claim-to-evidence rule

Every empirical or methodological claim in the report has one or more of:

- `RF##` source fact with PDF/page or official dataset locator;
- `RUN####`/`EVAL####` record with code/data/model/split versions;
- `FIG##`/`TAB##` artifact generated from those records;
- a clearly labeled interpretation with uncertainty/limits;
- an explicit source citation for external literature.

Claim categories:

| Category | Example | Required support |
|---|---|---|
| Dataset fact | Number of rows/features/classes | Official data documentation + actual file audit |
| Method fact | Pipeline/scaler fitted inside folds | Code inspection and run configuration |
| Result | Malignant recall is X on holdout | EVAL record, counts, threshold and metric script |
| Interpretation | One model had higher recall but lower specificity | Matched metrics and error counts; limited wording |
| Clinical claim | Tool can support a clinician | Outside course scope; requires separate clinically appropriate study and approval |
| Novelty claim | First method to do X | Search strategy, complete prior-art assessment and supervisor review |

## 3.4 Post-course research gap workflow

The Q1 track follows the blueprint STEP-047–049 only after course freeze. Search current literature; include contrary results; map prior datasets/splits/methods/validation; state one contribution; test data adequacy; create a new protocol; and obtain supervisor/author approval. The course holdout may not be reused as a second untouched confirmatory evaluation. A new independent data source requires documented rights/access and any institutional determination before acquisition.

Use [TRIPOD+AI](https://www.bmj.com/content/385/bmj-2023-078378) when its prediction-model reporting scope applies and [PROBAST+AI](https://www.bmj.com/content/388/bmj-2024-082505) for risk-of-bias/applicability assessment. These are reporting/appraisal supports; they do not establish novelty, cure a weak study or predict acceptance. A journal's current scope, indexing and quartile must be checked at venue-selection time with a recorded authoritative source/date.

<a id="os-04"></a>
# 4. Dataset source, privacy and data handling

## 4.1 Source verification and dataset card

The guide's dataset page is [UCI WDBC](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic). Before analysis, verify the actual file using the official repository entry and associated data documentation. Dataset card `docs/dataset_card.md` must include:

| Field | Required record |
|---|---|
| Dataset identity | Official title, publisher, official URL, access date |
| File provenance | Download filename, format, version/last-updated metadata if supplied, SHA-256 |
| Use terms | License/usage terms locator, redistribution status, unresolved restrictions |
| Data shape | Actual row count, column count, predictor count, ID/target columns |
| Target | Source label values, encoding map, positive class definition |
| Predictors | Exact names, types, feature group descriptions as documentation supports |
| Quality | Missing tokens, duplicate checks, invalid values, outlier review, findings |
| Population/provenance | What source documentation states; explicitly unknowns and limits |
| Transform history | Derived version ID, parent hash, operation, code revision |
| Access/storage | Canonical raw location, visibility, backup, allowed sharing |

The 569-row and 30-predictor counts are in the course guide and must be verified against the acquired file. Do not fill counts from memory or an unofficial copy if the actual file differs.

## 4.2 Immutable raw and derived releases

Raw source is read-only after intake. Cleaning creates a new derived file with parent hash and transform record. Do not overwrite raw bytes, alter original labels in place, or manually delete records without a `DEC` ID and before/after count. Keep the dataset ID and exact source version attached to every split, run, evaluation and model.

Data release key: `DS###` for source intake; `REL###` for a processed release combining dataset version, target/feature contract, split, preprocessing ID and manifest hash. For a coursework project, a simple manifest and checksums may be sufficient; it must still make clear which file generated results.

## 4.3 Quality audit policy

Check rows/columns/dtypes; target labels; class counts; unique IDs; exact duplicate records; duplicate predictor vectors; missing/null/sentinel values; non-finite values; unexpected categories; ranges/outliers; column name/order. Report each separately. A duplicate ID is not necessarily an exact duplicate record; a large feature value is not necessarily invalid.

Cleaning response classes:

- **Retain:** no evidence of invalidity; include in analysis.
- **Correct:** only with authoritative correction/provenance; preserve parent value and reason.
- **Exclude:** only with explicit pre-model rule, count, reason and sensitivity note when material.
- **Impute:** learned imputation belongs inside a training-fold pipeline; do not fit globally.
- **Defer:** uncertainty remains; record as a limitation and avoid an unsupported transformation.

## 4.4 Privacy and disclosure

The course guide says not to collect real identifiers/personal medical records for the classroom demo. Use public dataset records or synthetic values. Do not request uploads of patient records. If a user can upload a CSV, validate it in memory and do not retain it after response; do not log row values, file name if sensitive, identifiers or raw request body. Public or restricted artifact handling follows the official data terms and team/instructor decision.

Any suspected accidental disclosure triggers immediate access restriction, evidence preservation, owner notification and the institution/course's required response. Do not conceal the incident or silently rewrite history.

<a id="os-05"></a>
# 5. Preprocessing, split and leakage prevention

## 5.1 Target and feature contract

Create one `feature_contract.md` before model runs. It specifies:

- prediction unit: one benchmark record;
- target column and mapping of source labels to `benign`/`malignant`;
- positive class for precision/recall/F1 and ROC-AUC: malignant (M), unless the instructor explicitly mandates another convention;
- predictor names/order/types taken from actual source, with identifier excluded;
- accepted app schema and class/probability order;
- treatment of missing, invalid and unknown fields;
- version/hash and approver.

Feature selection is not a course requirement by itself. If explored, it is a development-only procedure inside cross-validation and is separately recorded. Never include ID or target-derived information among predictors.

## 5.2 Split protocol

The two PDFs require stratification and leakage control, but do not set a train/test percentage, random seed or fold count. Decide these in D05, using the rubric and sample size, then prerecord them. A recommendation is one fixed stratified holdout for course reporting plus stratified training-only CV for tuning. Do not search multiple random splits and choose the highest score. Do not change the test composition after seeing metrics.

Store a split manifest with row key/hash, partition, target class, source hash, split algorithm/version and seed. Avoid publishing direct identifiers. Verify train/test disjointness and class counts. Treat the test data/results as restricted within the team until STEP-042; only the evaluation owner opens them after G06.

## 5.3 Pipeline fit boundaries

All fitted transformations are part of a Scikit-learn `Pipeline` or equivalent:

| Model family | Candidate preprocessing | Fit boundary |
|---|---|---|
| LR | Standardization; approved imputation if needed | Fit within each training fold |
| KNN | Standardization; approved imputation if needed | Fit within each training fold |
| SVM | Standardization; approved imputation if needed | Fit within each training fold |
| MLP | Standardization; approved imputation if needed | Fit within each training fold |
| Decision Tree | Usually no scale; approved imputation if needed | Any learned transform remains fold-local |
| Random Forest | Usually no scale; approved imputation if needed | Any learned transform remains fold-local |
| Extra Trees | Usually no scale; approved imputation if needed | Any learned transform remains fold-local |
| Gradient Boosting | Usually no scale; approved imputation if needed | Any learned transform remains fold-local |

Fit scalers, imputers, selectors and resampling only on training folds. The test partition is transformed by the fitted training pipeline, never used to estimate transformation parameters. The app loads the full fitted pipeline and does not reimplement preprocessing.

## 5.4 Leakage audit questions

Before G03, reviewer answers and links evidence for each:

1. Was the test partition created before transformations were fit?
2. Does any scaler/imputer/selector learn from the full table before CV?
3. Does any target-informed feature selection or threshold tuning inspect the test labels?
4. Does resampling occur only inside each training fold?
5. Are repeated records/IDs present on both sides? What is known from source documentation?
6. Do all models use identical split rows, class mapping and metric implementation?
7. Is the evaluation command given test data only for frozen inference/evaluation?
8. Can the reported result be regenerated from source/config/code hashes?

Any “unknown” with plausible leakage impact keeps G03 OPEN until resolved or the limitation is explicitly accepted by the supervisor/instructor. A correct stratified split alone is not proof of no leakage.

## 5.5 Version changes and invalidation

A target map, split seed/ratio, feature set, data cleaning, preprocessing method, threshold policy or CV design creates a new protocol/release version. Reassess G03 and rerun affected downstream model comparisons. Keep previous outputs as superseded/exploratory; do not overwrite metrics or call them the result of the new design.

<a id="os-06"></a>
# 6. Models, experiments and comparison

## 6.1 Required model catalog

The model list is a COURSE REQUIREMENT. One row per estimator records owner, family, baseline config, preprocessing, random-state behavior, package/version, score interface, tuning status and run IDs.

| Required estimator | Family label for report | Typical preprocessing note from guide | Implementation owner |
|---|---|---|---|
| Logistic Regression | Linear/statistical | Standardize; consider class weight | D02 to resolve; provisional M2 |
| K-Nearest Neighbours | Distance-based | Standardize; tune neighbor/distance settings | D02 to resolve; provisional M2 |
| Support Vector Machine | Kernel-based | Standardize; tune C/kernel parameters | D02 to resolve; provisional M2 |
| Decision Tree | Tree-based | Scaling generally unnecessary; control complexity | M3 proposal |
| Random Forest | Ensemble, bagging | Record tree count/depth/feature sampling | M3 proposal |
| Extra Trees | Randomized tree ensemble | Record count/depth/feature sampling | M3 proposal |
| Gradient Boosting | Ensemble, boosting | Record learning rate/estimators/depth | M3 proposal |
| MLP Classifier | Neural network | Scale inside Pipeline; track convergence | D02 to resolve; provisional M5 |

The PDF sources differ on some model owners. The table above is provisional until D02 is approved. Model implementation owner, tuning owner and metric reviewer can be different people.

## 6.2 Experiment identity and immutable records

Each baseline/tuning run gets a unique `RUN####` or `EXP####` and records: question/purpose; dataset/split/feature contract IDs; model/config/hash; code revision; environment; seed; CV folds; scoring; start/end; warnings/errors; output paths/hashes; metric script; status; deviations; reviewer; conclusion. Never replace a run ID or erase a failed attempt.

Baseline configs make all relevant settings explicit, including solver, kernel, tree count, MLP architecture, stopping and seed behavior. Library defaults may be used only when recorded by name/version and intentionally accepted. Do not claim one model superior solely from its training score or one metric.

## 6.3 Baseline protocol

After G03, run all eight models under one common split and metric protocol. Save continuous scores for ROC-AUC where the estimator provides a decision score/probability. Record unavailable scores or convergence failures as failures; do not silently exclude the model. Results from cross-validation and held-out test must have different partition labels and cannot be mixed in one unannotated column.

Minimum comparison table columns: model/family; config ID; evaluation partition; positive class; accuracy; malignant precision; malignant recall; specificity; malignant F1; ROC-AUC; sample counts; threshold if threshold metrics; warning/status; run/eval ID. State whether result is baseline CV/development estimate or final test.

## 6.4 Hyperparameter tuning

At least three models must be tuned. Suggested models in course guide are SVM, Random Forest and MLP; the team may choose other required estimators with rationale. Before each search, record:

- Search ID and model/config parent;
- parameter space/ranges and total candidate count;
- stratified CV method/fold count/seed;
- primary selection score and secondary metrics;
- random-state policy, compute/time budget and failure policy;
- complete pipeline and fit boundaries;
- baseline to compare and method for resolving ties.

Use GridSearchCV/RandomizedSearchCV or an equivalent transparent procedure. Keep the test set out of search. Keep all candidate results, errors, best params, CV scores and warnings. If expanding a search after seeing output, create a new exploratory search ID. Do not call an adaptive search preregistered.

## 6.5 Run comparison and model selection

Compare matched estimates from the same training CV design. Discuss malignant-class recall/false negatives, specificity/false positives, ROC-AUC and any agreed primary criterion. Account for fold variability and the small dataset; do not present close scores as certainly different. The team chooses a final model based on a written rationale before test access. If probabilities are displayed, state whether calibration was evaluated; otherwise label them model outputs and note calibration was not assessed.

<a id="os-07"></a>
# 7. Evaluation protocol and interpretation

## 7.1 Required metrics

Use the exact formulas and conventions in Appendix D and the evaluation protocol. At minimum, report accuracy, malignant precision, malignant recall/sensitivity, specificity, F1 and ROC-AUC. Show confusion counts and define M as positive. ROC-AUC uses continuous scores, not hard labels. Threshold-based metrics require a named threshold and selection source.

## 7.2 Threshold policy

The course PDFs do not specify a threshold. Before tuning or final test, decide whether to use the estimator's documented default or select a threshold from training-only cross-validated predictions. Record the objective, allowed candidates, tie handling and metric tradeoff. Do not choose the threshold to improve the held-out test. A threshold chosen to improve malignant recall may also increase false positives; report both sides.

## 7.3 Final test freeze

G06 requires exact model/pipeline/config hash, split hash, threshold policy, metric code and test access history to be recorded before the evaluation owner opens the holdout result. Run the final test once after selection. If a computational bug is corrected without a model/decision change, document the bug and rerun transparently. If test results influence a model/threshold/feature change, the original test is now exploratory; do not reuse it as an untouched confirmatory estimate.

## 7.4 Uncertainty and small-sample interpretation

Always show numerator/denominator for malignant recall and specificity. If confidence intervals or bootstrap intervals are included, describe resampling unit, method, seed and assumptions. With a small fixed holdout, intervals can be wide and unstable. Do not imply that a single split estimates population performance precisely. If uncertainty analysis is omitted due to course scope/time, say so and list it as a limitation.

## 7.5 Error review

Review false positives and false negatives using only permitted benchmark examples. Avoid reverse-engineering a clinical explanation from feature attribution. Do not publish record IDs or values in public figures unless allowed. Error analysis after the final test can describe findings but cannot feed back to candidate selection without changing the status of the test estimate.

<a id="os-08"></a>
# 8. Explainability and application operating rules

## 8.1 Explainability protocol

Course expectation: show global behavior and local examples where feasible; SHAP or permutation importance is acceptable. Create `XAI###` record with model ID/hash; method/library version; exact fitted pipeline; feature names before/after transform; background/reference subset and source partition; local example-selection rule; outputs; caveats; reviewer. Use training data for reference/background unless another choice is justified. A local case must not be selected because its test result looks impressive.

Explainability review asks:

1. Does the output correspond to the exact candidate model used in evaluation?
2. Are transformed feature names and original feature semantics aligned?
3. Is the scale/meaning of attribution described correctly?
4. Are correlated predictors and method dependence acknowledged?
5. Does text avoid causal, biological and clinical claims?
6. Are one benign and one malignant example included where feasible, with selection reason?

## 8.2 Prototype boundary

The app is a classroom presentation layer over the same registered fitted pipeline. It is not clinical deployment. The interface must show non-clinical use notice, input expectations, model identity and limits. It should not imply that “benign” means a user is healthy or that a missed/zero output clears a person.

## 8.3 Minimum app contract

Recommended framework is Streamlit; instructor may approve Gradio/Flask/FastAPI. Minimum pages/sections:

| View | Required content |
|---|---|
| Home | Project purpose, WDBC dataset summary, prominent non-clinical disclaimer |
| Predict | Validated form or schema-checked CSV using exact 30 feature contract |
| Result | Model output label and score/probability clearly described; selected model/version; explanation if verified |
| Performance | Registered final held-out metrics, confusion matrix, ROC curve and partition label; do not show final metrics before STEP-043 |
| Dataset/About | Official source, feature/target context, provenance and limitations |

Do not start training on app startup. Load the full serialized preprocessing-plus-model object. Check file/hash/version; fail clearly if it is missing or mismatched. Do not duplicate scaler logic or reorder inputs silently. Any displayed result/metric has a source ID.

## 8.4 Input, error and upload policy

Check required fields, names/order, numeric type, missing/nonfinite values and CSV layout before inference. Reject unsupported input with an understandable message. Do not silently impute, drop rows or coerce strings beyond the approved Pipeline. Test valid input, missing field, extra field, reordered field, nonnumeric, NaN/inf, malformed CSV, missing model and hash mismatch. If uploads are supported, process in memory and discard after request; do not log feature values or identifiers. Never invite real patient records.

## 8.5 Parity and app readiness

For fixed permitted examples, call the registered inference wrapper directly and via the app. Compare class, scores and model metadata under an explicit tolerance/rounding rule. Record build commit, model artifact hash and environment. Run from a clean clone/environment using the documented command. Screenshots demonstrate UI only; they do not establish model correctness without parity/test evidence.

<a id="os-09"></a>
# 9. Writing, presentation and submission

## 9.1 Report structure

Follow latest instructor format. If no conflicting template is supplied, use the guide's suggested structure:

1. Title page: exact title, course/semester, five full names/IDs, instructor, submission date.
2. Abstract and keywords.
3. Introduction, motivation, problem, objectives and explicit scope.
4. Related work / brief literature review with verified sources.
5. Dataset source, provenance, target labels, feature descriptions and limitations.
6. EDA methods, findings and figures.
7. Preprocessing, feature/target contract, split and leakage prevention.
8. Eight model descriptions and family coverage.
9. Tuning methodology: search ranges, CV, scoring and before/after comparison for ≥3 models.
10. Evaluation metrics, threshold, counts, results, confusion matrices, ROC curves and discussion.
11. Explainability methods/results, global/local outputs and interpretive limits.
12. App architecture, saved artifact, input validation, screenshots and testing.
13. Limitations, ethics/responsible use, future work, conclusion.
14. References, team contribution table and AI-use declaration.

Course-guide section list is not a page-count or journal-paper template. Confirm formatting, reference style, required appendices and final PDF instructions under D03/D10.

## 9.2 Figures, tables and reproducibility captions

Each figure/table gets a stable ID, title/caption, source artifact IDs, partition, units/labels, generator command/code revision and reviewer. Re-generate plots from machine-readable results, not manually copied spreadsheet values. Axes and legends must be legible. Include denominators/threshold in metric tables. Avoid unlabeled feature names or overly dense correlation plots.

## 9.3 Presentation obligations

Title slide lists all full names and student IDs. Full IDs appear in the footer of every slide per the guide. Presentation explains problem, data, workflow, leakage-safe evaluation, model families, tuning, result trade-offs, XAI limits and live app. All five members speak. Rehearse transitions, question handoff, demo inputs and offline/screenshot fallback if hosting is unreliable. Don't present app response time as research inference benchmark unless separately measured.

## 9.4 Contribution and AI-use declaration

Contribution log is evidence-based and dated. Each person confirms their entry. A member's assigned ownership is not proof of completed work. AI assistance must be logged by artifact/task and accurately declared; verify and understand generated code/prose. Confirm with instructor what “below 25%” measures before computing any ratio. Until clarified, do not claim compliance with a numerical threshold; retain usage notes and disclose honestly using the instructor's format.

## 9.5 Submission package and receipt

Before upload, verify the exact report PDF, slide deck, repository state, evidence link permissions, app demo/recording if required, contribution log, references, AI declaration, screenshots and test report. Record file hashes, timestamp, submission channel and receipt. If a late or replacement upload is needed, retain both attempts and instructor communication.

<a id="os-10"></a>
# 10. Version control, artifacts and reproducibility

## 10.1 Git conventions

- Use named branches or small commits with meaningful descriptions; one member owns integration of shared registries.
- Review changes to feature contract, split, metric code, app class mapping and model-selection logic before merge.
- Do not commit secrets, unrestricted raw data, unsupported weights or user uploads.
- `.gitignore` must be checked against tracked files and repository history; ignore patterns do not remove previously committed content.
- Tag course submission release and record exact commit in report/release note.
- Do not rewrite history to conceal errors, missed deadlines or exposure. Correct forward with a superseding record.

### User-approved remote and push boundary

- Intended remote: [Machine-Learning-Project GitHub repository](https://github.com/akhtaruzzamananik/Machine-Learning-Project.git).
- Read-only inspection on 17 Nov 2026: this workspace was not a Git repository; `git ls-remote --symref ... HEAD` exited successfully and returned no refs. Treat the remote as empty at that observation time; verify again before first push because its state can change.
- The user authorized committing and pushing project artifacts except the **paper** and the **dataset**. Before STEP-004, interpret this as excluding research-paper/manuscript files and raw/processed dataset contents. Do not add a broad `*.pdf` ignore rule: the course report, slides and other PDFs may be distinct deliverables. D15 must be resolved before staging any course report PDF.
- Code, plans, notebooks, app source, documentation, tests and permitted generated reports/figures may be committed and pushed after checking the exclusion list, data terms, privacy and repository status. A file is not publishable merely because it is not named “paper” or “dataset”; row-level data, predictions or identifiers remain subject to the data policy.
- At STEP-004, initialize the local repository and set the supplied URL as `origin` only after STEP-001–003 are complete. Do not create a second GitHub repository or force-push. Confirm branch name, team access and remote visibility; protect the initial push with a staged-file inventory.
- Before every commit and push, inspect both staged and already-tracked files. Keep manuscript and dataset paths in designated excluded homes (for example `reports/publication/` and `data/`) and add precise ignore rules. Verify `git status`, staged diff, file list, and remote target; preserve the commit hash and push result in the tracker.

## 10.2 Reproducibility manifest

Every result-producing command or notebook records:

| Component | Minimum identity |
|---|---|
| Data | dataset ID, source checksum, derived version, split ID |
| Features | feature contract version/hash, target mapping and positive class |
| Code | Git commit or source archive checksum, notebook/script entry point |
| Environment | Python and package versions, OS/runtime where relevant |
| Randomness | split seed, model seed, CV splitter seed and other stochastic settings |
| Method | preprocessing, estimator/config, search space, scoring/threshold |
| Output | run/evaluation ID, prediction/metric/figure hash/path, status and warnings |
| Review | reviewer, date, decision/deviation IDs |

## 10.3 Model artifact card

For each persisted fitted pipeline, record model ID; parent training run; source/split/feature contract; estimator and parameters; preprocessing; class order; threshold policy; package versions; artifact hash/size/location; intended use; limitations; evaluation IDs; app commit; and a restore/load check. The object is a research artifact, not an approved medical device. Use a trusted artifact source and never deserialize arbitrary untrusted upload content.

## 10.4 Backups and retention

Maintain one approved backup of code/metadata and permitted artifacts in team-controlled storage; verify restore for the final release. Do not sync restricted data or weights to a consumer cloud without checking terms and access. Record who can access and how long copies are retained. If the course provides no retention rule, keep only what is permitted and ask instructor before deletion of submitted evidence.

<a id="os-11"></a>
# 11. Roles, review and human decisions

## 11.1 Named team roster and primary roles

| Member | Student | Plan role | Independent review duty |
|---|---|---|---|
| M1 | Al-Javin Nishu — 232-15-226 | Coordination, scope, dataset/EDA | Verify evidence links and report-source claims |
| M2 | Akhtaruzzaman Anik — 232-15-252 | Preprocessing, feature pipeline, reproducibility | Audit split, fit boundaries and feature order |
| M3 | Alzubair Ahmed — 232-15-591 | Core tree/ensemble model implementation | Review another model family's configs/results |
| M4 | Rayan Ahmed — 232-15-847 | Tuning, evaluation, metric comparison | Audit positive class, thresholds and held-out isolation |
| M5 | Nafis Sadiq — 232-15-895 | MLP, XAI and application integration | Clean-run app and check disclaimer/schema |

Names/IDs are transcribed from the supplied team plan; verify spelling and ID before formal submission. The table describes proposed primary roles; the team can reassign by written agreement.

## 11.2 Resolving the source role conflict

Team Plan p.3/p.6 gives LR/KNN/SVM to Member 4; Guide p.5 gives those models to Member 2 and MLP/tuning/evaluation to Member 4. Team Plan gives MLP to Member 5. Resolve in STEP-002. Recommended separation:

- **Implementation owner:** code/config for a model.
- **Tuning owner:** search design and execution across chosen models.
- **Evaluation owner:** shared metric code and comparison table.
- **Reviewer:** independently checks run/data/protocol lineage.
- **Report owner:** writes section and links claims to evidence.

Provisional allocation pending approval: M2 LR/KNN/SVM + preprocessing; M3 four tree/ensemble models; M5 MLP + XAI + app; M4 tuning/common evaluation; M1 dataset/EDA/coordination. This recommendation is not a source fact. Record any different team decision with names, dates, backups and affected STEP IDs.

## 11.3 Human-only approvals

The following require human team/instructor/supervisor decisions; software defaults or AI suggestions are not approval:

| Decision | Approver |
|---|---|
| Course requirements, deadline exceptions, AI-use rule, report and slide format | Instructor; M1 records |
| Role changes, title and scope | All five; instructor if rubric scope changes |
| Data terms and public redistribution | Data owner/source terms; instructor/team confirms compliance |
| Split, metric, threshold and selection protocol | M2/M4 propose; all approve before runs |
| Cleaning/exclusion/imbalance choices | M1/M2 propose; M4 reviews impact; all record material choices |
| Final selected model and results wording | All five review; M4 documents rationale |
| App disclaimer, hosting, data retention | Instructor/team; no clinical use |
| Authorship/contributions/AI declaration | Each member confirms own work; all authors approve report |
| New data, clinical claim, journal scope | Supervisor/institution/data custodian as applicable |
| Journal submission and corresponding author | All authors + supervisor approve; corresponding author submits |

## 11.4 Meeting and escalation

Hold brief milestone check-ins at least once after each gate and async daily status as needed. Each meeting note captures completed evidence, blocker, next owner, deadline, decisions and changed risk. Escalate a missing dependency on the same day it threatens a milestone. Redistribution occurs early and is recorded; do not wait until a due date to discover an owner is blocked.

<a id="os-12"></a>
# 12. Daily research operations and milestone control

## 12.1 Milestone calendar

| Milestone | Official due | Internal handoff | Gate/steps | Required package |
|---|---|---|---|---|
| Topic/problem scope | Tue 17 Nov | Same-day status recovery | G01 / 001–004 | Title, problem, objectives, scope, names/domain, tracker/repo |
| Dataset/initial EDA | Sat 21 Nov | Fri 20 Nov | G02 / 005–011 | Official source, data description, audit, notebook, ≥4 charts, 3–5 observations |
| Preprocessing/features | Wed 25 Nov | Tue 24 Nov | G03 / 012–017 | Target/features, split, leakage-safe pipelines, rationale |
| Eight models/five families | Mon 30 Nov | Sun 29 Nov | G04 / 018–026 | All eight baseline runs, comparable metrics, evidence links |
| Tuning/explainability | Fri 04 Dec | Thu 03 Dec | G05/G06 / 027–035 | ≥3 tuned models, before/after, SHAP/permutation evidence, selection freeze |
| Working application | Tue 08 Dec | Mon 07 Dec | G07 / 036–041 | Saved fitted pipeline app, inputs validated, clean-run/demo evidence |
| Final testing/submission | Thu 10 Dec | Wed 09 Dec | G08 / 042–046 | Final test, report, references, contribution/AI declarations, slides, release |

If any internal handoff is missed, record the true state and carry forward the risk. Do not present buffer date as a new official deadline. Final submission hour and course platform remain D01/D10 until confirmed.

## 12.2 Daily status rules

Every active workday, each owner posts one concise update:

```text
STEP / artifact:
Status: Not Started | In Progress | Completed
What changed and evidence link:
Reviewer / review needed:
Blocker and owner:
Next action and due time:
```

If no evidence exists, status cannot be Completed. If the task is blocked, identify an independent task that may proceed without crossing a gate. Only M1 edits milestone-level status; individual owners supply evidence and blockers.

## 12.3 Tracker access and evidence URLs

Each evidence URL must open for the instructor using the intended account. Before submission, test private-link permissions in a second account/member session. Avoid URL shorteners and personal-drive links that expire without notice. Where file sharing is disallowed, provide the repository path or approved portal locator. Preserve a local snapshot of submitted files and receipt.

## 12.4 Workload and member absences

If a member is blocked/unavailable: notify team, name the affected deliverables and deadline, assign a backup/reviewer, record the reassignment and preserve actual contribution history. Do not delete the original owner's row. Ensure all five remain prepared for presentation and Q&A; review/integration work is shared even when implementation is owned by one person.

## 12.5 Disagreement and change control

For disagreements about a course requirement, consult the instructor. For a method choice not fixed by the rubric, write options, impact, evidence and decision owner; agree before execution. A midstream change gets a new decision/version and invalidation list. Do not cherry-pick the plan version that makes old results look compliant.

<a id="os-13"></a>
# 13. Quality gates, risks and completion

## 13.1 Gate state model

- **NOT ASSESSED:** no evidence review has occurred; dependent work is blocked.
- **OPEN:** evidence exists but a criterion remains unresolved.
- **PASS:** all criteria for exact artifact versions are evidenced and reviewed.
- **FAIL:** a criterion failed; dependent work stops pending recovery.
- **STALE:** an upstream version changed after assessment; reassess affected gates.

Record assessor, date, exact code/data/model/report versions, criterion evidence, outcome, approval, superseded assessment and impacted gates. A written plan is never a PASS. Re-evaluate after data, split, preprocessing, metric, model, threshold or app changes.

## 13.2 Gate matrix

| Gate | Assessment step | Pass criteria | Blocks / invalidation |
|---|---|---|---|
| G01 Scope and governance | STEP-004 | True milestone status; title/scope/team/domain; D02 owner conflict resolved; current course rules recorded; shared repository/tracker accessible | Data/report claims; stale on scope/role/rubric change |
| G02 Dataset and EDA | STEP-011 | Source/terms/hash; raw preserved; schema/count/target audit; quality report; ≥4 required charts; 3–5 reviewed observations | Split/model work; stale on data/schema/cleaning change |
| G03 Data protocol | STEP-017 | Feature contract; fixed stratified split; seed/manifest; no ID; Pipeline fit boundaries; metric/threshold policy; leakage audit | Baselines/tuning; stale on split/transform/target change |
| G04 Baselines | STEP-026 | Eight named estimators; ≥5 families; common protocol; run logs/output; metric definitions and failures reported | Tuning/selection; stale on model/data/protocol change |
| G05 Tuning/XAI | STEP-034 | ≥3 models searched using training-only CV; ranges/best params/before-after; global/local XAI where feasible; limitations | Final freeze; stale on search/candidate/XAI change |
| G06 Candidate freeze | STEP-034/035 | Exact candidate/config/pipeline/threshold/split/metric/artifact hashes recorded before test access; selection rationale | Final test; any post-test model/threshold decision makes test estimate exploratory |
| G07 Application readiness | STEP-041 | Full fitted pipeline loads; feature/class mapping correct; invalid-input cases; parity; disclaimer; clean run; no real patient data | App milestone/report claim; stale on app/model/artifact change |
| G08 Course submission | STEP-046 | Report/slides/tests/evidence/references/contributions/AI declaration; IDs; exact release/receipt; all members participate | Course project declared complete |
| G09 Publication go/no-go | STEP-049 | Current literature gap; approved research question; adequate data/permissions; defensible design/validation; bias/reporting review; all author/supervisor approvals; current venue fit | Journal submission only; no guarantee of acceptance |

## 13.3 Risk register

| ID | Risk/trigger | Likelihood/impact assessment | Prevention | Contingency/recovery | Owner |
|---|---|---|---|---|---|
| R01 | Nov 17 scope item missing/late | assess now; high deadline impact | STEP-001 status check and immediate instructor query | Truthful late submission/status; record response; reprioritize | M1 |
| R02 | Role conflict leaves duplicated/unowned models | medium/high | D02 matrix with separate implementation/tuning/review owners | Reassign early; preserve contribution history | M1/all |
| R03 | Data source/file mismatch | unknown/high | Official provenance/hash/schema audit | Stop modeling; reacquire/resolve; invalidate descendants | M1/M2 |
| R04 | License/redistribution unclear | unknown/high | Verify terms before public repo or app publication | Keep data restricted; ask source/instructor | M1 |
| R05 | Leakage produces inflated result | medium/high | G03, Pipeline, code review and locked test | Mark exposed result exploratory; rebuild protocol/obtain new independent evidence | M2/M4 |
| R06 | Eight models use different split/metrics | medium/high | Shared runner, split manifest, metric code | Recompute all comparisons under common protocol | M4 |
| R07 | Tuning runs past internal deadline | medium/medium | Predefine search budget; parallelize independent estimators | Narrow prospective search; disclose incomplete coverage | M4 |
| R08 | MLP non-convergence/variance | medium/medium | Explicit seed, convergence logging, reasonable search | Record failure; adjust prospectively; no hidden retry | M5 |
| R09 | Test selected model/threshold | medium/high | G06 lock and test access control | Downgrade test to exploratory; use new evaluation if available | M4 |
| R10 | SHAP mismatch/wrong feature order | medium/high | XAI contract, feature map review | Retract plot and regenerate against exact pipeline | M5/M2 |
| R11 | App preprocessing differs from training | medium/high | Use full serialized pipeline and parity tests | Stop demo release; correct wrapper and re-run G07 | M5/M2 |
| R12 | App output overstates clinical meaning | medium/high | Approved disclaimer and copy review | Remove claim, correct screenshots/report | M1/M5 |
| R13 | Private evidence URL inaccessible | medium/medium | Second-account link check before milestone | Re-share via approved route and keep receipt | M1 |
| R14 | AI-use contribution rule misunderstood | unknown/high | Confirm definition; log per artifact | Ask instructor; disclose uncertainty and actual use accurately | M1/all |
| R15 | Q1 expectation outruns data/novelty | high/high | Separate G09; prior-art and study-adequacy checks | No-go or redesign with supervisor; no acceptance promise | All/supervisor |
| R16 | Deadline compression/absence | medium/high | Daily status, internal buffer, backup owner | Reassign early; reduce optional scope, not required integrity | M1 |

Probability/impact ratings are initial qualitative estimates, not measured frequencies. Review at each milestone and assign a due date to mitigation.

## 13.4 Failure, deviation and recovery rules

1. Preserve the failed artifact/log and assign a failure ID.
2. State which criterion failed and whether it affected data integrity, protocol, result or deadline.
3. Identify the earliest upstream step that must be repeated.
4. Create new version/run IDs; retain the old result as failed, superseded or exploratory.
5. Re-run only affected descendants and reassess every invalidated gate.
6. Update report/tracker and notify instructor if milestone impact is material.

Do not overwrite output, conceal a test exposure, silently change class mapping or report a failed step as completed after a superficial patch.

## 13.5 Universal Definition of Done

A STEP is Done only when its objective and outputs are met; actual inputs/method/config are recorded; verification evidence exists; required human decisions are recorded; applicable gates are current PASS; canonical registries and docs are updated; artifact locations/permissions are valid; status/evidence link are posted; and the next owner can continue without oral-only context. Where a source fact or approval is unavailable, mark OPEN and block only dependent work.

## 13.6 Project completion states

- **Course project complete:** G01–G08 PASS; exact submitted package/release and receipt retained; claims match evidence; all five members can explain the pipeline; AI use/contribution declared; course no longer has required deliverables outstanding.
- **Journal-ready submission authorized:** G09 PASS for the manuscript version and venue decision. This means team/supervisor authorize submission, not that the journal will accept it.
- **Journal accepted:** only after an actual editor decision/acceptance record. No plan or model score may be used to claim acceptance in advance.

<a id="os-14"></a>
# 14. Template library and session forms

The following templates are canonical starting points. Copy into the owning folder and fill only with actual information. Mark unknown fields `OPEN`; do not leave a blank field that could be mistaken for zero or approval.

## 14.1 T01 — Project scope brief

```text
Exact course title:
Course/semester/instructor:
Problem and prediction unit:
Target and positive class:
Dataset source/version (or OPEN):
Objectives:
Included work:
Explicit exclusions/clinical boundary:
Required models/metrics/app/report:
Team roster/IDs and role matrix link:
Official due dates/source:
Open course decisions and owners:
Approval/evidence/date:
```

## 14.2 T02 — Decision record

```text
Decision ID / date:
Question and why it matters:
Authority label: COURSE REQUIREMENT / PLANNING RECOMMENDATION / OPEN DECISION
Source evidence/locator:
Options considered and trade-offs:
Decision and rationale:
Approver(s):
Blocks/affects STEP IDs, artifacts and gates:
Review/reopen trigger:
Supersedes:
```

## 14.3 T03 — Dataset card

Use the fields in Section 4.1 plus source URL, access date, file hash, label definition, class counts, permission, raw path, derived versions and known limitations. Include an explicit statement when a field is not reported by the source.

## 14.4 T04 — Data-quality audit

```text
Dataset/source hash:
Rows/columns before analysis:
Target values and counts:
ID uniqueness and predictor exclusion:
Missing/sentinel/nonfinite audit:
Duplicate-row / duplicate-ID audit:
Outlier summary (no automatic exclusion):
Discrepancies vs source documentation:
Cleaning decisions (DEC IDs) and before/after counts:
Reviewer/date/evidence:
```

## 14.5 T05 — Evaluation protocol

```text
Protocol ID/version:
Dataset/source/split ID:
Prediction unit / target mapping / positive class:
Train/test design, stratification, seed and reason:
CV splitter/folds/seed:
Pipeline fit boundary:
Primary tuning score and secondary measures:
Threshold source/rule (never test-selected):
Metric formulas and averaging:
Probability calibration plan or explicit non-assessment:
Test access rule and freeze authorization:
Approvers/date/change history:
```

## 14.6 T06 — Model and experiment record

```text
MODEL/RUN/EXP ID:
Owner/reviewer/date/status:
Research/course purpose:
Data, feature, split and protocol IDs/hashes:
Estimator/family/preprocessor:
Explicit baseline/search parameters:
Random state and CV folds:
Python/package versions and code commit:
Start/end, runtime, warnings/errors:
Predictions/metrics/plots paths and hashes:
Deviations, interpretation and next action:
```

## 14.7 T07 — Explainability record

```text
XAI ID / exact model hash:
Method/library version:
Reference/background partition and selection:
Feature mapping before/after transform:
Local case selection rule and class:
Outputs and generator code:
Interpretation limits/correlated features:
Reviewer and evidence:
```

## 14.8 T08 — App test and parity record

```text
APP/build commit and dependency lock:
Model artifact ID/hash:
Input schema and class order:
Case ID / input category:
Expected behavior:
Actual behavior/result:
Direct-pipeline vs app comparison/tolerance:
Disclaimer/privacy/error handling check:
Tester/date/environment/evidence:
Defect and recovery:
```

## 14.9 T09 — Contribution and AI-use entry

```text
Date/member ID/task or STEP:
Actual contribution and artifact/commit:
Human verification/review evidence:
AI tool/use (if any) and affected artifact:
How output was checked/changed/understood:
Disclosure location and course rule status:
Member confirmation/date:
```

## 14.10 T10 — Gate assessment and session note

Gate assessment fields and STEP session fields are prescribed in Appendix B/H and the execution blueprint's Appendix H. Assess only exact versions, include failed/open criteria and do not treat this blank template as a passed review.

## 14.11 T11 — Report claim/asset map

```text
Claim or figure/table ID:
Report section:
Source locator or RUN/EVAL/XAI/APP IDs:
Exact data/model/split version:
Caption/units/partition:
Limitation/uncertainty:
Author/reviewer/date:
```

## 14.12 T12 — Publication go/no-go memo

```text
Primary question/contribution:
Prior-art search date and protocol:
Direct/contradicting evidence:
Data adequacy and permissions:
Validation/calibration/uncertainty plan:
Risk-of-bias/applicability review:
Reporting checklist status:
Current journal fit/indexing/quartile source/date:
Authors/supervisor decision:
Go / revise / stop and reason:
```

<a id="appendix-a"></a>
# Appendix A. Canonical definitions

- **Course benchmark:** WDBC data used for the assignment; not a clinical cohort established by this project.
- **Prediction unit:** one row/record as delivered by the dataset.
- **Positive class:** malignant (M) for the project metrics unless a current instructor requirement overrides and the change is documented.
- **Preprocessing pipeline:** fitted transformations plus estimator serialized as one inference artifact.
- **Training data:** records/folds used to fit a model or choose hyperparameters.
- **Validation/CV estimate:** development evidence used during model selection; not the final held-out test estimate.
- **Held-out test:** partition kept out of all model/feature/threshold decisions until freeze.
- **Leakage:** information from evaluation rows/labels enters training, preprocessing, selection or threshold decisions improperly.
- **Threshold:** decision boundary used to turn a continuous score into a class; must be fixed without test tuning.
- **Calibration:** agreement between predicted probabilities and observed frequencies under a specified population; not established by showing `predict_proba`.
- **Explainability:** descriptive account of fitted model behavior; not a causal explanation or medical fact.
- **Clinical validation:** evaluation in an appropriate intended-use population/workflow; outside this course project's evidence.
- **Gate:** evidence-based permission to proceed for specified artifact versions.
- **Release:** exact code/docs/model/report package identified by IDs/hashes and a date.
- **Q1:** a journal category/quartile designation that must be checked against the relevant current source/year/category; it is not a quality guarantee or acceptance outcome.

<a id="appendix-b"></a>
# Appendix B. Registry catalog and minimum schemas

Every registry uses UTF-8, one header row, explicit field names and dates in ISO format where possible. Empty value means unknown only if documented; use `OPEN`, `NOT REPORTED`, `NOT APPLICABLE` or measured `0` distinctly. Multi-value fields use semicolon delimiter or linked child records. Protect identifiers/row-level outputs according to the data terms.

| Registry | Key/owner | Minimum columns |
|---|---|---|
| Decisions `docs/decisions.md` | D / M1 | ID, question, authority label, source, options, decision, approver, date, affected STEP/gates, supersedes |
| Risks `docs/risk_register.csv` | R / M1 | ID, description, trigger, likelihood, impact, mitigation, contingency, owner, review date, status |
| Gates `docs/gates.csv` | G / reviewer | GateID, versions, criteria, outcome, assessor, approval, date, evidence, invalidates, supersedes |
| Milestones `docs/milestone_evidence.csv` | Milestone / M1 | Due, status, owner, reviewer, evidence URL, permission checked, blocker, actual submitted time |
| Responsibilities `docs/responsibility_matrix.csv` | Task / M1 | TaskID, member, role (implement/tune/review/report), due, backup, decision ID, status |
| Contributions `docs/contributions.csv` | EntryID / each member | Date, MemberID, STEP, action, artifact/commit, reviewer, verification, member confirmation |
| AI use `docs/ai_use.md` | Entry / each member | Tool, task, artifact, role, human verification, estimated extent if required, disclosure location |
| Papers `reports/literature/papers.csv` | P / M1 | Title, authors, year, journal, DOI/URL, access date, task, data, validation, metrics, limitations, verified by |
| Screening `reports/literature/screening.csv` | SCR / M1 | PaperID, stage, decision, reason, reviewer, conflict resolution, duplicate ID |
| Dataset `docs/dataset_card.md` | DS / M1 | Source, version, hash, permission, access date, rows/features/target, quality, storage, limitation |
| Splits `reports/splits/` | SPLIT / M2 | Row key/hash, source hash, target class, partition, algorithm, seed, manifest hash |
| Models `models/registry/model_registry.csv` | MODEL / owner | Family, implementation, version, preprocessing, params/config, parent run, artifact hash, intended use |
| Experiments `reports/experiments/` | RUN / model owner | Data/split/protocol IDs, config, code commit, seed, folds, status, outputs, warnings, conclusion |
| Evaluations `reports/evaluations/` | EVAL / M4 | Model, partition, protocol hash, threshold, prediction hash, counts, metrics, script, reviewer |
| Explanations `reports/explainability/` | XAI / M5 | Model ID, method, background, mapping, case selection, output IDs, limitations, reviewer |
| App tests `reports/app_tests/` | APP / M5 | Build/model hash, test case, input class, expected/actual, status, tester/date |
| Assets `reports/figures/`/`tables/` | FIG/TAB / author | Source IDs, data hash, spec/code revision, output, caption, partition, reviewer |
| Releases `reports/releases/` | REL / M1 | Report/slides/code hashes, date, upload route, evidence URLs, permission check, receipt |
| Publication decisions `docs/publication/` | PUB / corresponding author | Question, gap evidence, protocol, approvals, venue source/date, go/no-go |

## B.1 Traceability rules

Every model resolves to a run/config and feature contract. Every run resolves to data/split/protocol/code/environment. Every evaluation resolves to a frozen model, partition, metric script and threshold. Every app display resolves to model/evaluation IDs. Every empirical report claim resolves to an EVAL/RUN and asset ID. Every contribution claim resolves to a dated artifact or review record. Any unresolved pointer is a verification failure, not harmless bookkeeping.

<a id="appendix-c"></a>
# Appendix C. Canonical stage map and dependency chain

The detailed procedure lives in the [Execution Blueprint](./BREASTWISE_PROJECT_EXECUTION_BLUEPRINT.md); this table is the governing navigation map. Keep the step/gate numbers stable. A future edit must update both documents together.

| Stage | Steps | Governing OS sections | Exit gate |
|---|---|---|---|
| S01 Kickoff/scope/repository | 001–004 | 1, 2, 11, 12 | G01 |
| S02 Dataset intake/audit/EDA | 005–011 | 4, 12 | G02 |
| S03 Target/split/preprocessing | 012–017 | 5, 7 | G03 |
| S04 Baseline models/metrics | 018–026 | 6, 7 | G04 |
| S05 Tuning/XAI/freeze | 027–035 | 6, 7, 8, 10 | G05, G06 |
| S06 App/integration | 036–041 | 8, 10 | G07 |
| S07 Test/report/submission | 042–046 | 7, 9–13 | G08 |
| S08 Publication readiness | 047–049 | 3, 7, 9, 13 | G09 |

```text
001–004/G01 → 005–011/G02 → 012–017/G03 → 018–026/G04
→ 027–034/G05 → 035/G06 → 036–041/G07 → 042–046/G08
→ 047–049/G09 (separate, post-course journal go/no-go)
```

Parallel work is permitted only when inputs are fixed: EDA prose/report shell can proceed after source facts; model implementations can proceed in parallel after G03 and the shared model contract; app scaffolding may proceed with a stub before final freeze. Final test and candidate selection are sequential. All report, app and publication steps that depend on final outputs wait for those artifacts.

<a id="appendix-d"></a>
# Appendix D. Metric and model-family reference

Let `M` be malignant and the positive class; `B` be benign. At a fixed threshold:

| Metric | Definition | Required interpretive note |
|---|---|---|
| Accuracy | (TP + TN) / (TP + TN + FP + FN) | Overall fraction correct; does not reveal class-specific misses |
| Malignant precision | TP / (TP + FP) | Of records called malignant, fraction labeled malignant in this benchmark |
| Malignant recall/sensitivity | TP / (TP + FN) | Of malignant-labeled records, fraction detected; show FN and denominator |
| Specificity | TN / (TN + FP) | Of benign-labeled records, fraction predicted benign; show FP and denominator |
| Malignant F1 | 2 × precision × recall / (precision + recall) | Class-specific balance; name averaging rule |
| ROC-AUC | Area under ROC from continuous score | Ranking across thresholds; not a selected-threshold performance measure |

If a denominator is zero, report undefined/NA and explain, not zero. Report threshold and positive class. ROC-AUC must use probability or continuous decision scores and class column order must be verified. Calibration is a separate property; `predict_proba` output is not automatically calibrated.

| Family | Required members | General preprocessing fact (confirm actual implementation) |
|---|---|---|
| Linear/statistical | Logistic Regression | Scale numeric features inside pipeline |
| Distance-based | KNN | Scale; distance/neighborhood sensitive to scale |
| Kernel-based | SVM | Scale; specify kernel/C and score interpretation |
| Tree-based | Decision Tree | Scaling usually unnecessary; control complexity |
| Ensembles | Random Forest, Extra Trees, Gradient Boosting | Explain bagging/randomized trees/boosting distinction; record random settings |
| Neural network | MLP Classifier | Scale inside pipeline; record convergence and seeds |

<a id="appendix-e"></a>
# Appendix E. Acronyms and glossary

| Term | Meaning in this project |
|---|---|
| AI | Artificial intelligence; disclose assistance under confirmed course rule |
| AUC / ROC-AUC | Area under receiver operating characteristic curve from continuous scores |
| CV | Cross-validation confined to training data for tuning |
| EDA | Exploratory data analysis |
| FN / FP / TN / TP | False negative / false positive / true negative / true positive |
| F1 | Harmonic mean of precision and recall for a named class/averaging rule |
| G | Evidence-based quality gate |
| ID | Dataset row identifier; exclude from predictors unless source/rubric indicates otherwise (default plan excludes) |
| MLP | Multi-layer perceptron classifier |
| OS | This BreastWise Research Operating System |
| Q1 | Journal quartile in a specified subject category and year; verify current source at selection time |
| RQ | Research question |
| STEP | Stable execution unit in the companion blueprint |
| WDBC | Wisconsin Diagnostic Breast Cancer dataset |
| XAI | Explainable AI / explainability methods |

- **Benchmark record:** row from the source dataset, not necessarily a current patient record or clinical encounter.
- **Calibration:** probabilistic accuracy against observed outcome rates under a target population; not established here unless evaluated.
- **Class imbalance:** differing label counts; quantify from actual file and preserve natural test distribution.
- **Leakage:** unwanted information transfer from held-out rows/labels into fitting, tuning or decisions.
- **Operating threshold:** threshold fixed without test data for classification metrics.
- **Pipeline:** preprocessing and estimator saved and used as one inference unit.
- **Source hash:** cryptographic digest identifying exact bytes; changing bytes changes the artifact identity.
- **External validation:** evaluation on an independent dataset/population; not part of the course requirement and not implied by a random holdout.
- **Human decision:** choice that must be approved and recorded by named team/instructor/supervisor rather than inferred from code defaults.

<a id="appendix-f"></a>
# Appendix F. Source coverage and planning self-review

## F.1 Supplied sources

1. `BreastWise_ML_Project_Guide_CSE431.pdf` (8 pages; removed from workspace at the user's request after it was read): project scope/title, dataset recommendation, end-to-end workflow, model list, metrics, XAI, app, five-member role suggestion, report/presentation and AI/ethics requirements.
2. `BreastWise_Group05_Team_Task_and_Deadline_Plan.pdf` (7 pages; removed from workspace at the user's request after it was read): named team, official due dates, proposed owner assignments, internal handoff dates, milestone evidence, meeting rhythm and completion checklist.

### Current source availability — 2026-11-17

The supplied PDFs are no longer present in the workspace, and no backup is claimed. RF01–RF18, the page locators and this summary preserve what was read for planning; they do not replace the original documents for a new independent review. The source deletion does not itself change the course scope or invalidate these historical planning decisions. Reattach an authorized original or obtain an instructor clarification if a later unresolved question depends on exact source wording.

The actual data file is not one of these planning PDFs. Dataset facts such as actual counts/terms are not independently asserted until the official dataset entry/file is checked under STEP-005–007.

## F.2 Fidelity and open issues audit

| Check | Treatment in this OS |
|---|---|
| Exact project title | Preserved from both PDFs |
| WDBC tabular scope | Preserved; 569/30 are guide-stated values to verify against file |
| Eight required estimators and five+ families | Listed individually and mapped to execution steps |
| Tuning requirement | At least three; stratified training-only CV; suggested candidates not mandatory |
| Required metrics | Accuracy, malignant precision/recall, specificity, F1, ROC-AUC; definitions supplied |
| Leakage prevention | Split before fitting; transforms refit per training fold; test withheld until freeze |
| XAI | Global/local where feasible; model behavior, no causal claim |
| App | Saved full Pipeline; schema validation; academic disclaimer; no real patient inputs |
| Team schedule | All seven official milestone dates retained; internal buffers remain internal |
| Team ownership discrepancy | D02 open until agreed; provisional allocation labeled as recommendation |
| AI threshold | “Below 25% if that is the stated rule”; instructor must define calculation |
| Q1 aspiration | Separate G09 post-course; no novelty or acceptance claim inferred |
| Current status | All gates start NOT ASSESSED; no execution inferred |

## F.3 Planning review scope

This OS and companion blueprint are planning instruments only. Their completeness does not establish that the dataset was downloaded, terms approved, experiments run, app deployed, report submitted or journal accepted. Begin at STEP-001 and update records using actual evidence.

<a id="appendix-g"></a>
# Appendix G. Publication-readiness checklist

This checklist is independent of course G01–G08. Do not start a journal submission merely because the course package is polished.

| Domain | Minimum evidence before G09 PASS |
|---|---|
| Novel question | A narrow primary question and distinct contribution supported by a reproducible literature search, including conflicting/directly similar work |
| Data | Adequacy for the intended question; documented source/population/eligibility, rights/access/ethics; rationale for using or supplementing WDBC |
| Design | Predefined development/evaluation plan, appropriate resampling, independent evaluation where needed, no reuse of exposed course test as confirmatory |
| Analysis | Threshold policy, calibration where probabilities/clinical risk are claimed, uncertainty, missingness/sensitivity and supported subgroup analyses |
| Bias/applicability | Completed PROBAST+AI-informed review or documented applicability; identified concerns addressed or limitations narrowed |
| Reporting | Applicable TRIPOD+AI items reviewed; complete methods, data and code statements; all deviations reported |
| Reproducibility | Frozen code/config/data lineage; scripts recreate tables/figures; no unrecoverable manual results |
| Clinical language | Claims match data/setting; clinical framing reviewed by qualified supervisor; no patient care recommendation without appropriate validation |
| Authorship | Contributions, author order, conflicts/funding, AI declaration and final manuscript approved by all authors |
| Venue | Current journal aims/scope, article type, indexing/quartile category/year, fees, policies and legitimacy checked from authoritative sources on dated memo |
| Decision | Go / revise / no-go recorded; submission approval is not acceptance guarantee |

*End of BreastWise Research Operating System — v1.2.0.*
