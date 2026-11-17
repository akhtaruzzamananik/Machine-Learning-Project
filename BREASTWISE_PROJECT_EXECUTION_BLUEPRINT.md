# BREASTWISE AI — PROJECT EXECUTION BLUEPRINT

**Governing policy:** [BreastWise Research Operating System](./BREASTWISE_RESEARCH_OPERATING_SYSTEM.md)\
**Course:** CSE431 Machine Learning, Fall 2026\
**Official final-testing milestone:** Thursday, 10 December 2026; confirm the instructor's exact submission time and latest rubric.\
**Planning state:** future work; no step, result, app, or gate is marked complete by this blueprint.\
**Scope:** 49 focused step types across eight course/research stages.\
**Source status:** The supplied CSE431 guide and Group 05 team/deadline PDF were read for this plan, then removed from the workspace at the user's request on 17 November 2026. Their historical requirements and role conflict are summarized in the [OS source ledger/status](./BREASTWISE_RESEARCH_OPERATING_SYSTEM.md#appendix-f). The originals are not available locally; current instructor requirements still take precedence.
**Repository instruction:** User provided the GitHub remote and authorized pushing project artifacts except the paper and dataset; see OS Section 10.1 for the exact boundary and current remote-state note.
**Version/date:** v1.2.0 / 17 November 2026

## How to use this blueprint

1. Start at the earliest step whose prerequisites and quality gates are satisfied. A written plan or completed checklist is not evidence that a step has been executed.
2. The OS defines scope, data policy, ownership, quality rules and gates. This blueprint defines the execution sequence and handoffs.
3. The official due dates below come from the supplied Group 05 schedule. The internal target is the schedule's one-day buffer where supplied. Treat all clock times, tracker rules, report format and any rubric changes as instructor confirmations still required.
4. At every work session, record step ID, date, actual owner, reviewer, artifact/version, evidence link, decision, deviation, blocker and next action in the shared tracker. Use only the tracker status values `Not Started`, `In Progress`, `Completed`.
5. Steps may run in parallel only when their inputs are stable and no shared split/model/registry is being changed concurrently. Assign one editor for shared canonical records.
6. Do not use held-out test observations to tune, select features, choose an explanation, or choose a threshold. Freeze the selection protocol first. If the test has been used to influence a change, record exposure and treat that test estimate as exploratory.
7. Each step inherits the full evidence and handoff rules in the OS. A blocked task does not block independent work, but it must not be silently marked complete.
8. The Q1 publication path begins after the course submission. Course completion is not journal readiness and no outcome in this plan guarantees acceptance.

## Stage map and calendar

| Stage | Steps | Due date / internal target | Exit gate |
|---|---|---|---|
| S01 Kickoff, scope and operating setup | 001–004 | 17 Nov 2026; scope due today | G01 |
| S02 Dataset intake, audit and EDA | 005–011 | 21 Nov; internal 20 Nov | G02 |
| S03 Target, split and leakage-safe preprocessing | 012–017 | 25 Nov; internal 24 Nov | G03 |
| S04 Eight baseline models and comparable metrics | 018–026 | 30 Nov; internal 29 Nov | G04 |
| S05 Tuning, explainability and selection freeze | 027–035 | 04 Dec; internal 03 Dec | G05, G06 |
| S06 Application and integration | 036–041 | 08 Dec; internal 07 Dec | G07 (app readiness) |
| S07 Final test, report, presentation and release | 042–046 | 10 Dec; internal 09 Dec | G07, G08 |
| S08 Publication-readiness study | 047–049 | After course hand-in; schedule with supervisor | G09 |

**Date reality check:** The topic/scope deadline is Tuesday 17 Nov 2026, the current planning date. STEP-001 therefore begins with status verification and recovery if needed; do not backdate a submission. The PDFs do not give a final hand-in time. If a milestone is missed, contact the instructor/team, record the true status and follow the confirmed recovery date. Do not re-label an old deadline as an internal target after it has passed.

## Dependency chain

```text
001–004/G01 → 005–011/G02 → 012–017/G03 → 018–026/G04
→ 027–034/G05 → 035/G06 (freeze) → 036–041/G07 (application ready)
→ 042 final held-out test → 043–046/G08 (submission)
→ 047–049/G09 (separate journal go/no-go)
```

The app can be scaffolded before model selection, but it cannot display final metrics or use the final artifact until STEP-035. EDA and report writing can proceed in parallel after source facts are verified. Model owners can implement independent estimator code in parallel after STEP-012 defines the common data contract. Final test execution cannot run in parallel with model/threshold selection.

## Universal session record and artifact contract

For every STEP, the owner records: **STEP ID; date/session ID; objective; actual owner/reviewer; inputs and hashes; procedure/code revision; output paths; data/model/split versions; decisions/deviations; verification evidence; status; blocker; recovery; next handoff.** Every output named below has one canonical home. If the course repository differs from the suggested OS layout, record the chosen mapping once in `docs/repository_map.md`; do not create duplicate registries.

Classify each statement as COURSE REQUIREMENT, PLANNING RECOMMENDATION or OPEN DECISION. Never invent results, source dates, project completion, approvals, contribution evidence, ethical clearance, citations, performance or clinical validation. Generated artifacts and raw data follow dataset terms and the OS data policy. Screenshots and links must be accessible to the instructor.

## Gate register summary

| Gate | Minimum evidence to pass | Reassessment trigger |
|---|---|---|
| G01 Scope/roles | Scope and title approved; actual team IDs; responsibility conflict resolved; rubric/deadline questions recorded; shared tracker/repo works | Any scope, role or rubric change |
| G02 Data/EDA | Source and terms recorded; immutable raw source identified; schema/class/quality counts reconciled; four required chart types and 3–5 bounded observations reviewed | Source file, cleaning rule or target changes |
| G03 Data protocol | Target/features defined; stratified split/seed fixed; leakage-safe pipelines; train/test disjointness and fit boundaries evidenced | Split, feature, preprocessing or CV change |
| G04 Baselines | Eight named estimators across required families run on common protocol; all failures and metrics traceable | Any model, data, metric or split change |
| G05 Tuning/XAI | At least three training-only CV searches; before/after evidence; explanation corresponds to candidate and has limitations | Search, XAI background, candidate or metric change |
| G06 Freeze | Candidate, pipeline, threshold policy, split and code/artifact IDs frozen before test access | Any choice after test exposure |
| G07 Application | Clean run loads full fitted pipeline; input validation, parity, disclaimer and permitted demo verified | Artifact, feature order or application code change |
| G08 Course submission | Report/slides/tests/references/contributions/AI declaration/repository release complete and consistent; evidence links accessible | Any submission replacement or result correction |
| G09 Publication go/no-go | Novel gap, viable design/data, supervisor/author agreement, reporting and bias/applicability review, journal fit | Scope/data/venue change or adverse review |

---

# S01 — Kickoff, scope and operating setup (17 November)

## STEP-001 — Verify the scope milestone and recover the schedule

**Objective:** Establish the truthful current state of the topic/scope milestone and a usable remaining calendar.\
**Why:** The official 17 Nov due date is today; the plan must distinguish submitted, late, incomplete and unverified work.\
**Owner/reviewer/deadline:** M1 Al-Javin Nishu / all four members review / 17 Nov, exact time OPEN DECISION.\
**Prerequisites:** OS source facts/decision ledger (RF01–RF18, D01–D14), current tracker or instructor message. The supplied PDFs were read and later removed at the user's request; request an authorized copy only if a source-dependent ambiguity cannot be resolved from the recorded summary.\
**Effort/parallel work:** 30–60 minutes; no parallel status editing. M1 asks each member for current evidence independently.\
**Inputs:** title/scope requirement, actual submitted file/link, deadline instructions, team roster.\
**Outputs and canonical records:** one canonical `docs/scope.md` scope document; `docs/milestone_evidence.csv` row for scope; `docs/decisions.md` entry for any uncertainty; timestamped submission receipt/link or explicit unconfirmed/not-submitted status.\
**Procedure:** (1) Search the tracker/email/team channel for actual submission evidence and permission state. (2) Ask all members whether any item was submitted. (3) If missing, assemble a concise minimum package from the official scope, submit only through the authorized route, and ask instructor how to handle lateness. (4) Record the real submission time, receipt and next action.\
**Planning prompt:** “Compare current scope evidence with the exact course requirement; list omissions and deadline uncertainties without claiming completion.”\
**Implementation prompt:** “Prepare only the missing truthful scope artifact; preserve an unedited copy of anything already submitted.”\
**Human decisions:** M1 confirms the tracker; instructor confirms late handling, exact submission time and whether the scope has been accepted.\
**Version control/evidence:** Save the receipt or link and a local version identifier; do not overwrite the submitted file.\
**Documentation updates:** tracker, project status, decision log and next-day schedule.\
**Verification:** title/domain/problem/objective/team match the required scope; evidence opens for the team; completion is not inferred from a draft.\
**Common mistakes:** backdating; treating a saved draft as submitted; silently changing the official deadline.\
**Recovery:** contact instructor/team promptly; record late status and revised action; continue independent repository/data work.\
**Definition of Done:** actual scope status is evidenced, all missing actions have owners/dates, and no false completion claim remains.\
**Next:** STEP-002.

## STEP-002 — Reconcile role and model ownership conflicts

**Objective:** Give every model and shared deliverable one accountable implementation owner, reviewer and deadline.\
**Why:** The team plan assigns LR/KNN/SVM to M4 while the course guide assigns them to M2; MLP belongs to M5 in the team plan and M4 in the guide.\
**Owner/reviewer/deadline:** all five members; M1 facilitates and records / 17 Nov.\
**Prerequisites:** STEP-001; OS Sections 1.1, 1.5 and 11.2 contain the recorded historical role proposals and conflict. Original PDFs are no longer available locally.\
**Effort/parallel work:** 45–90 minutes in one meeting; model coding waits until ownership is recorded.\
**Inputs:** OS RF16 and Section 11.2 historical role summary, member availability/strengths, workload, required model list. If exact source wording is disputed, ask the user to reattach an authorized copy.\
**Outputs:** `docs/responsibility_matrix.csv` with implementation owner, tuning owner, reviewer, report owner and backup for each model/task; D02 resolution.\
**Procedure:** (1) Review the two recorded source allocations in OS RF16/Section 11.2. (2) Separate implementation from tuning/evaluation so one member may own a baseline while another tunes it. (3) Agree one owner for each of eight models; record the final map and changes. (4) Check that M1 has scope/data, M2 preprocessing, M3 tree models, M4 evaluation/tuning, M5 MLP/XAI/app coverage or document an agreed alternative. (5) Assign every report section and presentation speaking portion.\
**Planning prompt:** “Identify duplicate and uncovered tasks in the two role proposals; propose a workload-balanced matrix and label all deviations.”\
**Implementation prompt:** “Update the responsibility matrix and tracker with the team-agreed names; preserve the historical source summary and do not claim the PDFs already contained the team's new allocation.”\
**Human decisions:** all five agree; no ownership is silently imposed.\
**Version control/evidence:** commit matrix and meeting note; retain attribution to both source proposals.\
**Documentation updates:** tracker, contribution register, communication and meeting cadence.\
**Verification:** every deliverable has exactly one accountable owner, at least one reviewer, and a due date; all five have presentation duties.\
**Common mistakes:** assigning all analysis to M4; counting model ownership as completed contribution; leaving app/report integration ownerless.\
**Recovery:** if a member is unavailable, reassign explicitly, preserve the decision history and inform the affected member.\
**Definition of Done:** D02 is resolved and the matrix is visible to all members.\
**Next:** STEP-003.

## STEP-003 — Confirm rubric, AI policy and submission instructions

**Objective:** Resolve course-level rules that affect the package before large-scale work begins.\
**Why:** The guide refers to a below-25% AI-generated contribution rule “if that is the stated course rule”; it does not define measurement or format.\
**Owner/reviewer/deadline:** M1 with instructor / all members verify / 17 Nov, update when instructor responds.\
**Prerequisites:** OS RF01–RF18 and current tracker/instructor channel; the original course guide was read but is no longer present locally.\
**Effort/parallel work:** 30 minutes to prepare questions; independent code work may continue.\
**Inputs:** latest rubric, assignment announcement, submission platform instructions, AI policy.\
**Outputs:** `docs/course_requirements.md`; dated answers or open questions with owner and follow-up date.\
**Procedure:** Confirm report format/length, final hand-in time, whether app must be hosted or demonstrated locally, required evidence links, AI declaration format/threshold definition, reference style, presentation duration and late policy. Record exact wording/source and access date.\
**Planning prompt:** “Compare the latest instructor requirements with the historical guide requirements summarized in the OS and identify changed or missing requirements.”\
**Implementation prompt:** “Update only the requirement register; if no authoritative reply exists, leave the item OPEN.”\
**Human decisions:** instructor is authority for rubric interpretation; students confirm they understand the rule.\
**Version control/evidence:** store permitted announcement screenshot/PDF or message locator; no private instructor message published outside team.\
**Documentation updates:** milestone tracker, report checklist, AI-use log.\
**Verification:** each question has source, answer/open status, owner and impact; no policy inferred from hearsay.\
**Common mistakes:** assume AI threshold is an exact percent of words/code; assume slides replace PDF report.\
**Recovery:** seek clarification; conservatively log AI assistance by artifact while waiting.\
**Definition of Done:** course instructions are recorded and all still-open items have response deadlines.\
**Next:** STEP-004.

## STEP-004 — Create repository, tracker and contribution evidence system

**Objective:** Establish shared, accessible homes for source, code, evidence and work attribution.\
**Why:** Milestone links and contributions must be recoverable and reviewable.\
**Owner/reviewer/deadline:** M1 setup / M2 and M5 access review / 17 Nov.\
**Prerequisites:** STEP-002 role matrix; STEP-003 rules sufficiently known.\
**Effort/parallel work:** 1–2 hours; repository permission setup serialized.\
**Inputs:** OS recommended layout, member accounts, evidence-link policy.\
**Outputs:** shared repository/task board; `docs/decisions.md`, `docs/milestone_evidence.csv`, `docs/contributions.csv`, `docs/ai_use.md`, README and environment record.\
**Procedure:** (1) Recheck the user-provided remote; the 17 Nov read-only inspection returned no refs, so verify that it is still the intended empty remote before first push. (2) Initialize the local repository in the agreed project workspace and configure that URL as `origin`; do not create a second GitHub repository or force-push. (3) Confirm branch name, repository visibility and team access. (4) Add folders `data/`, `notebooks/`, `src/`, `models/`, `app/`, `reports/`, `docs/`. (5) Add README with setup/data source/non-clinical notice. (6) Add precise ignore rules for the dataset, paper-manuscript home, local secrets, caches and unapproved large artifacts; do not use a blanket PDF ignore rule. (7) Create milestone rows and evidence columns: step, owner, reviewer, status, URL, last verified, blocker. (8) Inspect staged files before the first commit and push; verify all allowed artifacts and exclude paper/dataset. Resolve D15 before staging any course report PDF. (9) Test that a second member can clone/open the committed non-restricted evidence.\
**Planning prompt:** “Map the OS artifact homes to the actual repository and identify sensitive or large artifacts.”\
**Implementation prompt:** “Connect the agreed workspace to the user's supplied GitHub remote, create the approved skeleton/tracker and contribution/AI logs, add precise exclusions, inspect the staged inventory, and push only authorized files. Do not add paper-manuscript or dataset bytes, credentials, or a course report PDF while D15 is open.”\
**Human decisions:** confirm the remote is correct, branch name, visibility/team access, source/data terms, and whether the course report is included under the paper exclusion.\
**Version control/evidence:** initial commit/push only after STEP-001–003 are evidenced and data terms reviewed; save commit hash, remote URL and push result. Do not force-push.\
**Documentation updates:** repository map, install steps, branch/PR convention, check-in cadence.\
**Verification:** `git status` and staged diff are reviewed; `origin` is the intended URL; all members have appropriate access; task status vocabulary matches source plan; URLs open; no dataset, paper manuscript, unauthorized report PDF, secrets or row-level records are staged.\
**Common mistakes:** creating a duplicate remote; initializing against the wrong folder; pushing paper/dataset or a private artifact; using a blanket `*.pdf` ignore; assuming ignore rules remove already-tracked files; contribution log filled retroactively without evidence.\
**Recovery:** restrict access, remove/disclose exposed material according to policy, inspect history and document actual state.\
**Definition of Done:** one functioning source of truth and accessible evidence workflow exists.\
**Next:** STEP-005.

# S02 — Dataset intake, audit and EDA (official due 21 November; internal 20 November)

## STEP-005 — Record dataset source, terms and provenance

**Objective:** Verify the chosen dataset and preserve provenance before analysis.\
**Why:** The guide recommends UCI WDBC but requires its properties and usage terms to be verified.\
**Owner/reviewer/deadline:** M1 / M2 / 20 Nov internal, 21 Nov official.\
**Prerequisites:** G01; repository and access policy.\
**Effort/parallel work:** 1–2 hours; can proceed alongside STEP-006 only if both use same downloaded source.\
**Inputs:** official UCI dataset page and accompanying documentation/file.\
**Outputs:** `docs/dataset_card.md` with publisher, official URL, access date, license/terms evidence, citation, file identity/version, format and known provenance.\
**Procedure:** (1) Retrieve from official source, not an unattributed mirror. (2) Save the exact download name and hash. (3) Read target/feature documentation and note any representation differences. (4) Record whether terms allow redistribution; separate permission to use from permission to republish. (5) Link source page in report reference manager.\
**Planning prompt:** “Verify the WDBC source, version, target definition, feature schema and terms using primary dataset documentation.”\
**Implementation prompt:** “Write the provenance record from retrieved evidence; do not infer a license or source date.”\
**Human decisions:** M1 proposes; team confirms source; instructor resolves accepted citation format.\
**Version control/evidence:** commit metadata and hash only; retain raw data in permitted location and never alter it in place.\
**Documentation updates:** dataset card, EDA notebook header, README.\
**Verification:** source URL opens; citation resolves; hash matches downloaded file; terms are explicit or marked unresolved.\
**Common mistakes:** use a Kaggle mirror without checking original; cite web page but not file/version; call de-identified data unrestricted.\
**Recovery:** replace with official source before continuing; regenerate hash and annotate any difference.\
**Definition of Done:** dataset identity, terms and provenance are evidenced.\
**Next:** STEP-006.

## STEP-006 — Preserve raw data and create a reproducible intake script

**Objective:** Protect the source bytes and create a deterministic read-only ingestion path.\
**Why:** Cleaning or reformatting must never erase the input needed to reproduce findings.\
**Owner/reviewer/deadline:** M1 / M2 / 20 Nov.\
**Prerequisites:** STEP-005 source and terms.\
**Effort/parallel work:** 1–2 hours; separate from EDA code after initial data interface agreed.\
**Inputs:** raw download, documented encoding/delimiter, expected schema.\
**Outputs:** immutable raw location/hash; `src/data/load_wdbc.py` or equivalent; derived clean copy location.\
**Procedure:** (1) Read without writing to original. (2) Explicitly state delimiter, header, missing tokens, column names and dtypes. (3) Fail loudly on unexpected schema. (4) Log source hash with every derived artifact. (5) Keep raw data out of public Git unless terms and team approval explicitly permit it.\
**Planning prompt:** “Specify an ingestion contract that fails on changed columns, encoding or target values.”\
**Implementation prompt:** “Implement read-only loading and validation; no silent row drops or column renaming.”\
**Human decisions:** choose storage access consistent with source terms.\
**Version control/evidence:** code and metadata can be committed; data content is governed separately.\
**Documentation updates:** dataset card and setup steps.\
**Verification:** reload produces same shape/schema/hash reference; raw hash unchanged after all operations.\
**Common mistakes:** save cleaned data over raw file; use a guessed header; rely on environment-specific paths.\
**Recovery:** recover original from official source, record replacement hash and rerun all descendants.\
**Definition of Done:** a deterministic intake script and protected raw artifact exist.\
**Next:** STEP-007.

## STEP-007 — Audit schema, labels and dataset counts

**Objective:** Reconcile actual file structure with official documentation before descriptive analysis.\
**Why:** The guide's 569-row/30-predictor description is a check target, not a substitute for inspecting the downloaded file.\
**Owner/reviewer/deadline:** M1 / M2 / 20 Nov.\
**Prerequisites:** STEP-006.\
**Effort/parallel work:** 45–90 minutes; same person maintains canonical count report.\
**Inputs:** validated table, dataset documentation.\
**Outputs:** schema audit with rows, columns, IDs, target labels, numeric/categorical types and class counts.\
**Procedure:** (1) Assert target values are only documented classes. (2) Count ID, target and predictor columns separately. (3) Check each expected feature name and target convention. (4) Report row/column totals and per-class counts. (5) Stop if a mismatch cannot be explained from provenance.\
**Planning prompt:** “Compare actual schema and counts with official documentation and list discrepancies.”\
**Implementation prompt:** “Generate an auditable schema report with assertions, not a screenshot-only summary.”\
**Human decisions:** M1 resolves source discrepancy with M2 and source documentation.\
**Version control/evidence:** store script/report; omit identifiers from public outputs if they could identify a subject under project terms.\
**Documentation updates:** dataset card and EDA notebook.\
**Verification:** totals reconcile, class labels and feature set explicit, ID excluded from candidate predictors.\
**Common mistakes:** mistakenly call 32 columns “32 predictors”; silently drop ID without explaining; hard-code expected counts as output.\
**Recovery:** return to STEP-005/006 if source mismatch; version any justified schema mapping.\
**Definition of Done:** actual dataset contract is independently reviewable.\
**Next:** STEP-008.

## STEP-008 — Audit missingness, duplicates, invalid values and outliers

**Objective:** Characterize quality issues before selecting cleaning actions.\
**Why:** Outlier handling or row removal can change an already-small dataset and must be justified.\
**Owner/reviewer/deadline:** M1 analysis / M2 pipeline review / 20 Nov.\
**Prerequisites:** STEP-007.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** schema-valid frame and ID/target rules.\
**Outputs:** per-column missingness report, duplicate-row/ID report, finite/range checks, outlier summaries.\
**Procedure:** (1) Check nulls, sentinel strings, infinities and nonnumeric cells. (2) Distinguish duplicate identifiers from duplicate predictor vectors and exact duplicate rows. (3) Inspect outliers using distributions/quantiles, without deleting solely for statistical extremeness. (4) Record every proposed repair/exclusion and its scientific/data reason. (5) Defer learned imputation to train-only Pipeline.\
**Planning prompt:** “Classify each data-quality finding as a verified issue, benign property or unresolved question.”\
**Implementation prompt:** “Produce quality summaries without modifying the raw or analysis frame.”\
**Human decisions:** M1 proposes any row exclusion; M2/M4 review impact before processing.\
**Version control/evidence:** save report and cleaning decision IDs.\
**Documentation updates:** dataset card, quality register and report methods notes.\
**Verification:** counts before/after are explicit; no undocumented deletion; missingness handling occurs within folds if learned.\
**Common mistakes:** automatic outlier clipping; dropping all duplicates without understanding IDs; claiming “no issues” from a single null count.\
**Recovery:** restore raw rows and rerun audit; supersede prior quality report.\
**Definition of Done:** audit and any cleaning decisions are recorded; no data is silently altered.\
**Next:** STEP-009.

## STEP-009 — Produce the required EDA summaries and charts

**Objective:** Describe target balance, predictor distributions and relationships in a reproducible notebook.\
**Why:** The course requires initial EDA and at least four useful chart types.\
**Owner/reviewer/deadline:** M1 / M2 and M4 / 20 Nov internal.\
**Prerequisites:** STEP-007 and STEP-008.\
**Effort/parallel work:** 2–4 hours; plots may be divided by feature group but one notebook owner merges them.\
**Inputs:** audited unmodified analysis view; target/ID contract.\
**Outputs:** executed `notebooks/01_eda.ipynb`; chart files for target distribution, selected feature distributions, correlation heatmap and boxplots.\
**Procedure:** (1) Plot class counts with counts and labels. (2) Show selected, named features with scale/units as supplied (do not invent clinical units). (3) Create correlation heatmap and disclose correlation is not causation. (4) Show boxplots split by class only as descriptive dataset patterns. (5) Avoid using test split to choose features or make model decisions.\
**Planning prompt:** “Choose visualizations that answer specified descriptive questions and note scaling/selection limits.”\
**Implementation prompt:** “Generate deterministic publication-readable figures with captions and source/version metadata.”\
**Human decisions:** M1/M4 review plot selection and wording.\
**Version control/evidence:** commit notebook and rendered charts; record environment and random seed where jitter/sampling occurs.\
**Documentation updates:** evidence tracker and draft dataset/EDA section.\
**Verification:** four required chart types exist, axes and legends are legible, counts tie to STEP-007.\
**Common mistakes:** claim clinical causality; show unexplained feature subsets; use charts with mislabeled classes.\
**Recovery:** rerun notebook from clean kernel, fix captions/schema and regenerate.\
**Definition of Done:** reproducible EDA outputs are ready for instructor review.\
**Next:** STEP-010.

## STEP-010 — Write bounded EDA observations and dataset limitations

**Objective:** Convert descriptive output into accurate prose without inferring clinical validity.\
**Why:** A plot is not an interpretation; small benchmark data limits claims.\
**Owner/reviewer/deadline:** M1 / M4 / 20 Nov draft, 21 Nov official.\
**Prerequisites:** STEP-009.\
**Effort/parallel work:** 1–2 hours; can begin report shell in parallel.\
**Inputs:** dataset card, audit, charts.\
**Outputs:** three to five numbered EDA observations, dataset description and limitations note.\
**Procedure:** Each observation names a measured pattern and evidence figure/table; distinguish description from explanation; mention source/population/provenance limits from actual documentation; state unverified facts as unknown.\
**Planning prompt:** “Audit every EDA sentence against the table/plot and remove causal or clinical language.”\
**Implementation prompt:** “Draft only claims supported by the verified dataset report; keep citation and figure identifiers.”\
**Human decisions:** M1 authors; M2 and M4 fact-check.\
**Version control/evidence:** draft uses stable figure/table IDs and reference keys.\
**Documentation updates:** report dataset/EDA chapter and evidence tracker.\
**Verification:** 3–5 observations; no unsupported demographic or clinical generalization; numbers reconcile.\
**Common mistakes:** turn class separation into diagnostic deployment claim; infer patient-level benefit from tabular feature clusters.\
**Recovery:** retract or qualify unsupported sentence and record correction.\
**Definition of Done:** EDA package has both reproducible outputs and reviewed interpretation.\
**Next:** STEP-011.

## STEP-011 — Assess G02 and close the dataset/EDA milestone

**Objective:** Release the team to define preprocessing only after data facts are trustworthy.\
**Why:** Any later split/model inherits the source and quality contract.\
**Owner/reviewer/deadline:** M1 assesses / M2 verifies / 21 Nov official.\
**Prerequisites:** STEP-005–010 outputs.\
**Effort/parallel work:** 30–60 minutes; evidence review is serialized.\
**Inputs:** dataset card, raw hash, intake/schema/quality reports, EDA notebook/plots/prose.\
**Outputs:** G02 assessment with PASS/FAIL/OPEN and exact source/data versions; milestone evidence links.\
**Procedure:** Check provenance/terms, raw preservation, counts, ID handling, data-quality decisions, required chart set, 3–5 observations and evidence access. Record any justified departures.\
**Planning prompt:** “Review G02 against actual artifacts and list blockers by owner.”\
**Implementation prompt:** “Update gate and tracker only with verified evidence; do not mark PASS based on planned work.”\
**Human decisions:** M1 signs coordination status; team approves material cleaning choices; instructor receives required links.\
**Version control/evidence:** preserve assessment and submitted URLs.\
**Documentation updates:** tracker status and risk log.\
**Verification:** all links open; findings point to exact versions; no missing licensing/term issue concealed.\
**Common mistakes:** use empty notebook as evidence; assume file count means data audit complete.\
**Recovery:** gate stays OPEN; assign minimal corrective tasks and record any due-date communication.\
**Definition of Done:** G02 PASS or explicitly blocked with a recovery owner; downstream preprocessing cannot be marked complete on a failed input.\
**Next:** STEP-012.

# S03 — Target, split and leakage-safe preprocessing (official due 25 November; internal 24 November)

## STEP-012 — Define the prediction target and feature contract

**Objective:** Specify the exact row-level task and 30 predictor input contract.\
**Why:** Identifiers, label polarity and feature order affect all results and the application.\
**Owner/reviewer/deadline:** M2 / M1 and M4 / 22 Nov.\
**Prerequisites:** G02 PASS; source schema verified.\
**Effort/parallel work:** 45–90 minutes.\
**Inputs:** official schema, data audit, project scope.\
**Outputs:** `docs/feature_contract.md` with target column, mapping B/M, positive label M, predictor names/order/types, ID exclusion and input shape.\
**Procedure:** (1) State unit of prediction as one WDBC record. (2) Map target string values to explicit labels; assert no other label. (3) Remove identifier from predictors with rationale. (4) Record all feature names exactly as source. (5) Clarify that probabilities are model outputs, not clinical risk estimates.\
**Planning prompt:** “Check that target and input contract can be applied identically in scripts, metric code and app.”\
**Implementation prompt:** “Create constants/schema validation from the approved contract; fail on missing/extra/reordered fields unless explicitly aligned by name.”\
**Human decisions:** all agree target and positive-class wording.\
**Version control/evidence:** hash feature list and reference it in run manifests.\
**Documentation updates:** dataset card, README, app spec.\
**Verification:** ID absent; positive class is malignant; exactly documented predictors; no label leakage.\
**Common mistakes:** alphabetical column reorder in app; inverse class encoding; using ID because it improves score.\
**Recovery:** supersede contract and rebuild all downstream artifacts if schema changes.\
**Definition of Done:** one versioned feature/target contract is accepted.\
**Next:** STEP-013.

## STEP-013 — Preregister split and model-comparison protocol

**Objective:** Decide split, CV and metric rules before training.\
**Why:** Repeatedly trying seeds/splits until a good score is test leakage.\
**Owner/reviewer/deadline:** M2 drafts / M4 review / all approve / 23 Nov.\
**Prerequisites:** STEP-012; G02.\
**Effort/parallel work:** 1 hour decision plus 1 hour protocol.\
**Inputs:** class counts, course rubric, model list.\
**Outputs:** `docs/evaluation_protocol_v1.md`: stratification, train/test proportion, seed, CV folds/seed, scoring metric, probability handling, threshold policy, metric implementation and planned plots.\
**Procedure:** (1) Select a stratified holdout design appropriate to sample size and assignment; record rationale. (2) Select stratified CV folds for training-only development. (3) Name malignant as positive. (4) Decide if default threshold is used or a threshold is selected from training-only CV predictions. (5) Define F1 averaging and specificity calculation. (6) No test result is viewed until selection freeze.\
**Planning prompt:** “Review protocol for ambiguities and ensure no decision depends on test outcomes.”\
**Implementation prompt:** “Implement the approved protocol as configuration; refuse unspecified thresholds/labels.”\
**Human decisions:** M2/M4 propose; all approve; instructor priority if rubric is prescriptive.\
**Version control/evidence:** protocol commit precedes model runs.\
**Documentation updates:** decision log, metric contract, tracker.\
**Verification:** every required metric has a definition and positive class; one split/seed fixed; no repeated holdout search.\
**Common mistakes:** choose split seed after seeing score; compare different folds; mix macro-F1 and malignant F1 without labels.\
**Recovery:** if protocol changed before test access, issue v2 and rerun all relevant baselines; after test access mark old result exploratory.\
**Definition of Done:** evaluation protocol is versioned and signed before training.\
**Next:** STEP-014.

## STEP-014 — Create and verify the locked stratified split

**Objective:** Produce a stable, disjoint development/test partition.\
**Why:** All comparisons must use the same rows and test must remain untouched.\
**Owner/reviewer/deadline:** M2 / M4 / 24 Nov internal.\
**Prerequisites:** STEP-012–013.\
**Effort/parallel work:** 45–90 minutes; split creation is a single-owner action.\
**Inputs:** immutable raw hash, feature contract and protocol.\
**Outputs:** split manifest with row identifiers/hash, partition, class counts, seed, code revision and source hash; restricted if IDs require it.\
**Procedure:** Use stratified split once; preserve indices; verify disjoint membership and class representation; record exact counts and proportions; restrict access to test labels/results until STEP-042.\
**Planning prompt:** “Inspect split creation and confirm no group/row overlap and correct stratification.”\
**Implementation prompt:** “Create deterministic split from the approved config, save manifest and hash, and add assertions.”\
**Human decisions:** team accepts approximate proportion due to integer counts; do not alter after scoring.\
**Version control/evidence:** commit code/protocol; store row-level manifest according to data handling decision; no public identifiers.\
**Documentation updates:** dataset release ID, evaluation protocol and tracker.\
**Verification:** train/test disjoint; counts reconcile; seed/config/source hash resolve; test labels not used in transformations.\
**Common mistakes:** make new split inside every model notebook; commit identifiable row IDs publicly; rebalance test set.\
**Recovery:** regenerate only before modeling if manifest invalid; issue new split version and invalidate all descendants.\
**Definition of Done:** locked split can be recreated and independently checked.\
**Next:** STEP-015.

## STEP-015 — Decide data cleaning and class-imbalance handling

**Objective:** Turn the quality audit into explicit modeling choices.\
**Why:** Automatic cleaning or rebalancing can alter prevalence and metrics.\
**Owner/reviewer/deadline:** M2 / M1 and M4 / 24 Nov.\
**Prerequisites:** STEP-008 and STEP-014.\
**Effort/parallel work:** 45 minutes; choices documented before fitting.\
**Inputs:** quality report, class counts per split, protocol.\
**Outputs:** decision entries for missing values, duplicates, invalid records, outliers, class weights/resampling adoption or non-adoption.\
**Procedure:** For each issue, choose retain, correct, exclude or impute; provide evidence/rationale. Prefer no unnecessary intervention. If class weighting/resampling is explored, fit it inside training folds and keep test prevalence unchanged. Record changes to effective sample counts.\
**Planning prompt:** “Assess whether an observed data issue requires intervention and what evidence supports the choice.”\
**Implementation prompt:** “Add only approved transformations to training pipelines; keep baseline/no-intervention comparison where meaningful.”\
**Human decisions:** M1/M2 propose; M4 reviews impact on positive-class recall and specificity.\
**Version control/evidence:** version decision and transformation config.\
**Documentation updates:** preprocessing rationale, limitation notes.\
**Verification:** every transformation has rationale and fit boundary; test data not rebalanced.\
**Common mistakes:** SMOTE before split; remove legitimate extremes; use class weighting because imbalance “looks bad” without comparison.\
**Recovery:** revert the unsupported transformation and rerun affected experiments under new IDs.\
**Definition of Done:** all cleaning/imbalance choices are explicit and reproducible.\
**Next:** STEP-016.

## STEP-016 — Implement model-specific leakage-safe Pipelines

**Objective:** Build the common preprocessing interface with transformations inside cross-validation.\
**Why:** Scaling on all data leaks held-out fold information and distorts performance.\
**Owner/reviewer/deadline:** M2 / M4 / 24 Nov.\
**Prerequisites:** STEP-012–015.\
**Effort/parallel work:** 2–3 hours; model owners can review the stable interface.\
**Inputs:** feature contract, split, approved cleaning choices, package version.\
**Outputs:** reusable pipeline factory; scaled branches for LR/KNN/SVM/MLP; unscaled tree branches unless a justified operation requires otherwise; saved config.\
**Procedure:** (1) Use `Pipeline`/`ColumnTransformer` with exact feature contract. (2) Put scaler/imputer/selector within the pipeline. (3) If resampling is adopted, use a CV-compatible training-fold-only mechanism. (4) Avoid global feature selection or preprocessing fit. (5) Fit only on training portion per fold. (6) Keep output feature names traceable for XAI.\
**Planning prompt:** “Trace each learned transformation to the rows on which it is fitted.”\
**Implementation prompt:** “Implement estimator pipelines that expose estimator parameters for search and preserve feature names.”\
**Human decisions:** M2 determines engineering implementation; M4 approves protocol compliance.\
**Version control/evidence:** code commit and lockfile/version note; no fitted object yet.\
**Documentation updates:** pipeline architecture and installation instructions.\
**Verification:** a fresh fold refits all learned transforms; scaler statistics do not include test; named features preserved.\
**Common mistakes:** fit scaler before `cross_val_score`; fit imputer once globally; transform app inputs separately from pipeline.\
**Recovery:** rebuild pipeline and invalidate affected baselines/tuning.\
**Definition of Done:** all required estimator families can use the same leakage-safe contract.\
**Next:** STEP-017.

## STEP-017 — Verify preprocessing and split invariants; pass G03

**Objective:** Independently confirm split and transform boundaries before baseline training.\
**Why:** G03 blocks expensive/duplicated model runs if data contracts are wrong.\
**Owner/reviewer/deadline:** M2 produces / M4 audits / 24 Nov internal, 25 Nov official.\
**Prerequisites:** STEP-012–016.\
**Effort/parallel work:** 1 hour; audit separate from implementation owner.\
**Inputs:** split manifest, pipeline code, protocol, quality decisions.\
**Outputs:** leakage audit report and G03 assessment.\
**Procedure:** Review random seed/stratification, manifest disjointness, ID removal, positive label, pipeline fit placement, CV refitting, transform behavior and test access controls. Run synthetic/small-data fit-boundary checks where possible.\
**Planning prompt:** “Try to identify any path by which test rows or labels affect fitted preprocessing or selection.”\
**Implementation prompt:** “Fix confirmed leaks, bump protocol/code version and rerun the audit.”\
**Human decisions:** M4 signs technical review; team accepts G03 only from actual evidence.\
**Version control/evidence:** audit points to code commit and manifest hash.\
**Documentation updates:** gate register, experiment README, tracker.\
**Verification:** no unresolved leakage path; any ambiguity stays OPEN.\
**Common mistakes:** consider a stratified split alone proof of no leakage; rely on notebook cell order without clean run.\
**Recovery:** reset G03 and rerun from STEP-013/016 as affected.\
**Definition of Done:** G03 PASS for exact protocol and code revision.\
**Next:** STEP-018.

# S04 — Eight baseline models and comparable metrics (official due 30 November; internal 29 November)

## STEP-018 — Define baseline model contract and common run interface

**Objective:** Ensure every implementation is comparable and traceable.\
**Why:** Eight differently structured notebooks can otherwise use different data, metrics or preprocessing.\
**Owner/reviewer/deadline:** M4 design / M2 implement shared interface / 26 Nov.\
**Prerequisites:** G03.\
**Effort/parallel work:** 1–2 hours; contract must precede parallel coding.\
**Inputs:** OS model list, protocol, feature/pipeline interface.\
**Outputs:** model registry/config with model ID, estimator family, preprocessing branch, baseline parameters, seed support, prediction output contract and artifacts.\
**Procedure:** Define training call, probability/decision-score availability, class order, prediction schema, metric function and output paths. Record package versions and baseline settings chosen by the team; no library default is left implicit in report.\
**Planning prompt:** “Check every model can emit consistent labels/scores and use the same split.”\
**Implementation prompt:** “Add each estimator through the shared interface and preserve explicit configuration.”\
**Human decisions:** M4 approves metric contract; each model owner proposes baseline parameters.\
**Version control/evidence:** version config before first baseline.\
**Documentation updates:** model catalog and tracker ownership.\
**Verification:** all eight named; consistent class mapping; run artifacts resolvable.\
**Common mistakes:** one notebook drops missing rows differently; probability column order assumed.\
**Recovery:** standardize wrapper and rerun all affected models.\
**Definition of Done:** one common execution/output contract is ready.\
**Next:** STEP-019.

## STEP-019 — Implement Logistic Regression baseline

**Objective:** Establish the linear/statistical reference model.\
**Owner/reviewer/deadline:** M2 (or final assigned owner from STEP-002) / M4 / 27 Nov.\
**Prerequisites:** STEP-018.\
**Effort/parallel work:** 1–2 hours, parallel with STEPs 020–022 after interface stable.\
**Inputs:** training split, LR pipeline, explicit baseline config.\
**Outputs:** reproducible fit/run record, CV or train-only development score, held-out test prediction artifact withheld for final evaluation (baseline predictions on test must not be viewed for selection).\
**Procedure:** Use standardized pipeline; record solver/regularization/class weighting explicitly; train on permitted development data; persist random/package/config info; save decision scores/probabilities with class order.\
**Planning prompt:** “Review LR settings for convergence and class mapping without selecting from test performance.”\
**Implementation prompt:** “Implement LR through the shared pipeline and record warnings/convergence.”\
**Human decisions:** baseline setting and class weights are documented decisions.\
**Version control/evidence:** code commit and run ID; no fitted artifact overwritten.\
**Docs:** model card and results registry.\
**Verification:** convergence/status captured; input/output schema correct; pipeline scaling fit only within training folds.\
**Common mistakes:** report default threshold without defining it; ignore convergence warning.\
**Recovery:** adjust only under recorded baseline policy, rerun and retain earlier run.\
**Definition of Done:** LR run is reproducible and traceable.\
**Next:** STEP-020.

## STEP-020 — Implement KNN and SVM baselines

**Objective:** Complete distance-based and kernel-based baseline families.\
**Owner/reviewer/deadline:** assigned model owner (provisional M2) / M4 / 27 Nov.\
**Prerequisites:** STEP-018–019 contract.\
**Effort/parallel work:** 2–3 hours, parallel with tree implementations.\
**Inputs:** scaled pipeline, protocol, explicit baseline K and SVM kernel/C settings.\
**Outputs:** two run records, predictions/scores, runtime and warnings.\
**Procedure:** Build KNN and SVM each with scaling inside Pipeline. Define neighbors/weight/distance for KNN and kernel/C/class-weight/probability or decision-function handling for SVM. Do not enable expensive probability calibration silently. Record all settings and class order.\
**Planning prompt:** “Check whether scores are comparable and how SVM probabilities are obtained.”\
**Implementation prompt:** “Run both on identical folds/split and report failures/warnings.”\
**Human decisions:** choose explicit simple baselines; calibration procedure is separately approved if needed.\
**Version control/evidence:** run manifests and config hashes retained.\
**Docs:** baseline model notes.\
**Verification:** scaling is fold-local; no test-based choice of K/C/kernel; score type identified.\
**Common mistakes:** scale before split; equate SVM margin with calibrated probability.\
**Recovery:** rebuild pipeline/config, rerun and supersede affected runs.\
**Definition of Done:** KNN/SVM outputs satisfy common run contract.\
**Next:** STEP-021.

## STEP-021 — Implement Decision Tree and Random Forest baselines

**Objective:** Establish single-tree and bagging ensemble baselines.\
**Owner/reviewer/deadline:** M3 / M4 / 27 Nov.\
**Prerequisites:** STEP-018.\
**Effort/parallel work:** 1–2 hours; parallel with STEP-022.\
**Inputs:** unscaled pipeline, approved seed, model contract.\
**Outputs:** two model configs/runs, predicted labels and positive-class scores.\
**Procedure:** Set random state where applicable; specify tree criteria and relevant regularization/leaf constraints; document forest estimator count, feature-sampling and depth policy. Keep baseline values distinct from later tuning ranges.\
**Planning prompt:** “Confirm tree models do not use test information and all randomness is recorded.”\
**Implementation prompt:** “Implement unscaled model pipelines and persist probabilities/classes.”\
**Human decisions:** M3 selects baseline configuration; M4 reviews common protocol.\
**Version control/evidence:** each run has unique ID and config hash.\
**Docs:** model catalog and family map.\
**Verification:** ensemble/tree included; seed recorded; positive score column correctly mapped.\
**Common mistakes:** report feature importance as causal explanation; use training score as comparison result.\
**Recovery:** correct code and regenerate run record; keep old result for audit.\
**Definition of Done:** both baseline runs are traceable.\
**Next:** STEP-022.

## STEP-022 — Implement Extra Trees and Gradient Boosting baselines

**Objective:** Complete randomized-tree and boosting ensembles.\
**Owner/reviewer/deadline:** M3 / M4 / 28 Nov.\
**Prerequisites:** STEP-018 and STEP-021.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** tree pipeline, explicit baseline config, random seed.\
**Outputs:** two runs and score artifacts.\
**Procedure:** Specify estimator count, depth/leaf settings, learning rate/estimators for boosting, and random state. Record convergence/runtime/warnings. No feature selection based on test.\
**Planning prompt:** “Review boosting parameters and identify whether the baseline is reproducible and feasible.”\
**Implementation prompt:** “Implement with explicit parameters and common prediction schema.”\
**Human decisions:** M3 owns estimator defaults; M4 approves comparison policy.\
**Version control/evidence:** record package versions and config hashes.\
**Docs:** model-family coverage map.\
**Verification:** both ensemble variants distinct and run; outputs aligned with model contract.\
**Common mistakes:** call Extra Trees and Random Forest the same family without describing differences; use unspecified library defaults.\
**Recovery:** state baseline values, rerun and update comparison.\
**Definition of Done:** both ensemble baselines are registered.\
**Next:** STEP-023.

## STEP-023 — Implement the MLP Classifier baseline

**Objective:** Satisfy neural-network model requirement with reproducible scaling/training.\
**Owner/reviewer/deadline:** M5 or agreed owner / M4 / 28 Nov.\
**Prerequisites:** STEP-018; scaled Pipeline branch.\
**Effort/parallel work:** 1–2 hours, parallel with other baseline runs.\
**Inputs:** feature contract, explicit hidden-layer/solver/regularization/max-iteration/seed configuration.\
**Outputs:** MLP baseline run, convergence record and probability outputs.\
**Procedure:** Scale within Pipeline; record initialization/random seed, solver, hidden layers, alpha and stopping settings; capture convergence warning and iteration count; run twice only if replication policy is preregistered.\
**Planning prompt:** “Check whether the MLP converged and which parameters are required for an interpretable baseline.”\
**Implementation prompt:** “Run with explicit settings and surface convergence warnings instead of suppressing them.”\
**Human decisions:** M5 selects modest baseline capacity; M4 reviews feasibility.\
**Version control/evidence:** unique run/config; save environment lock.\
**Docs:** MLP methods note.\
**Verification:** Pipeline scaling fold-local; no warning hidden; class probabilities align with positive label.\
**Common mistakes:** claim neural network superiority from one seed; ignore non-convergence.\
**Recovery:** increase iteration budget or adjust under a documented policy, retain original run and rerun.\
**Definition of Done:** MLP baseline result is valid or failure is recorded and repaired.\
**Next:** STEP-024.

## STEP-024 — Implement and unit-check the metric contract

**Objective:** Ensure all models use one verified metric implementation.\
**Owner/reviewer/deadline:** M4 / M2 / 28 Nov.\
**Prerequisites:** STEP-013 protocol and model output contract.\
**Effort/parallel work:** 1–2 hours; independent reviewer creates hand-check case.\
**Inputs:** confusion-matrix convention, labels, positive class, score outputs.\
**Outputs:** reusable metric script and small hand-calculated validation example.\
**Procedure:** Define TP/FP/FN/TN orientation; compute accuracy, malignant precision, recall/sensitivity, specificity, malignant F1 and ROC-AUC; state threshold and handling of tied/non-probability scores. Compute ROC-AUC from continuous scores, not predicted labels.\
**Planning prompt:** “Trace formulas and positive class through every metric and plot.”\
**Implementation prompt:** “Implement named metrics, assert class order and check against a hand-computed confusion matrix.”\
**Human decisions:** M4 proposes averaging and undefined-metric policy; team approves.\
**Version control/evidence:** metric code commit and review note.\
**Docs:** evaluation glossary and methods draft.\
**Verification:** hand-computed values match; all model reports use identical definitions; no metric silently omitted.\
**Common mistakes:** calculate specificity for malignant class; report ROC-AUC on hard labels; hide undefined results.\
**Recovery:** correct code and recompute every affected table/plot.\
**Definition of Done:** metric contract passes independent calculation review.\
**Next:** STEP-025.

## STEP-025 — Run all eight baseline models under one protocol

**Objective:** Generate the required eight-model/five-family baseline evidence.\
**Owner:** model owners execute; M4 coordinates; M2 controls data version. **Due:** 29 Nov internal / 30 Nov official.\
**Prerequisites:** G03; STEP-018–024.\
**Effort/parallel work:** 3–6 hours depending on compute; independent models can train in parallel after configs are frozen, but not edit shared split.\
**Inputs:** locked split, pipeline/model configs, metric implementation, dependency lock.\
**Outputs:** eight run records, predictions/continuous scores, logs, failure notes and baseline table/plots.\
**Procedure:** (1) Snapshot code/config/data/split hashes. (2) Run the common runner for each model. (3) Record start/end, status, warnings, seed and package versions. (4) Compute development/CV metrics consistently. (5) If holdout predictions are generated for assignment comparison, lock and do not inspect until STEP-042.\
**Planning prompt:** “Audit that all eight runs use identical rows, folds, positive class and metric code.”\
**Implementation prompt:** “Execute registered configs, preserve failed runs and write machine-readable outputs.”\
**Human decisions:** M4 coordinates retry policy; model owner signs own run metadata.\
**Version control/evidence:** code/notebooks committed; large predictions/models stored under approved artifact home with hashes.\
**Docs:** tracker, run registry, model-family chart.\
**Verification:** 8/8 named, family count meets requirement, no data/protocol divergence, failure statuses visible.\
**Common mistakes:** report only successful models; use individual notebook split; overwrite run outputs.\
**Recovery:** rerun only after cause recorded, new run ID; invalidate any comparison built on inconsistent protocol.\
**Definition of Done:** baseline evidence exists for every required model or a documented blocker escalated to instructor.\
**Next:** STEP-026.

## STEP-026 — Build baseline comparison and assess G04

**Objective:** Close the model-coverage milestone with a reproducible comparison.\
**Owner:** M4 / M2 audit / all model owners review / 29–30 Nov.\
**Prerequisites:** STEP-024–025.\
**Effort/parallel work:** 1–2 hours; review is serialized.\
**Inputs:** run records, metric outputs, family map, logs.\
**Outputs:** baseline table, confusion matrices/ROC comparisons for the shortlist, G04 assessment and tracker evidence.\
**Procedure:** Compare using common split/protocol; include counts/positive class, not accuracy alone; discuss malignant false negatives and false alarms; state if results are CV-only or held-out. Keep conclusion descriptive; do not declare a winner before the tuning/selection protocol.\
**Planning prompt:** “Inspect baseline table for denominator mismatch, test exposure and claims that exceed evidence.”\
**Implementation prompt:** “Generate tables/plots from registry data, not manually retyped spreadsheet values.”\
**Human decisions:** M4 recommends tuning candidates; team approves three-model list at STEP-029.\
**Version control/evidence:** output generator and versioned assets; evidence URLs checked.\
**Docs:** report methods/results draft and milestone tracker.\
**Verification:** eight models present, common protocol, family coverage correct, metric code resolves, negative/failed runs included.\
**Common mistakes:** rank by one metric only; compare CV score to test score; visually imply tiny differences are meaningful.\
**Recovery:** rebuild table from raw metric artifacts; correct captions and rerun review.\
**Definition of Done:** G04 PASS with exact run and protocol IDs or held OPEN with named recovery.\
**Next:** STEP-027.

# S05 — Hyperparameter tuning, explainability and freeze (official due 04 December; internal 03 December)

## STEP-027 — Select tuning candidates and define search budgets

**Objective:** Meet the three-model tuning requirement without uncontrolled search.\
**Why:** Search spaces, scoring and compute budget must be fixed before comparing outcomes.\
**Owner/reviewer/deadline:** M4 / M2 and model owners / 01 Dec.\
**Prerequisites:** G04 and baseline results.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** baseline comparison, assignment examples, compute/time available.\
**Outputs:** tuning plan for at least three models (suggested SVM, Random Forest, MLP), parameter ranges, CV, scoring rule, seed, budget and tie policy.\
**Procedure:** Choose candidates based on scientific/computational rationale, not test score. Declare whether scoring emphasizes malignant recall or another rubric-supported metric; include secondary metrics. Set plausible parameter ranges and search count; avoid huge grids.\
**Planning prompt:** “Review whether the selected tuning task answers the project question and is feasible by 03 Dec.”\
**Implementation prompt:** “Record the exact search configuration and do not start until protocol review.”\
**Human decisions:** M4 proposes; team approves scoring objective and compute budget.\
**Version control/evidence:** tune plan committed before any search.\
**Docs:** decision log, tuning tracker.\
**Verification:** ≥3 distinct models; training-only CV; estimator params exposed through pipeline; before/after metrics specified.\
**Common mistakes:** tune based on test score; search many models without time; choose metric after observing rankings.\
**Recovery:** narrow search prospectively and record; do not hide incomplete search.\
**Definition of Done:** preregistered, feasible tuning plan signed.\
**Next:** STEP-028.

## STEP-028 — Specify CV search implementation and preserve every trial

**Objective:** Make tuning reproducible and failure-aware.\
**Owner/reviewer/deadline:** M4 / M2 / 01 Dec.\
**Prerequisites:** STEP-027.\
**Effort/parallel work:** 1 hour; code work can be parallel by estimator owner.\
**Inputs:** approved search plan, pipelines, package lock.\
**Outputs:** search config, search log schema, run ID format, error/timeout handling.\
**Procedure:** Use stratified CV within training data and complete Pipeline; explicitly fix random states where possible; log candidate count/folds/score/timing/warnings. Record all attempted configurations including failures. Set refit policy and retain CV results table.\
**Planning prompt:** “Trace each search split to training rows only and verify transformations are refit per fold.”\
**Implementation prompt:** “Implement searches with deterministic config/logging and no test object passed to search.”\
**Human decisions:** M4 signs search reproducibility; model owners verify parameter names.\
**Version control/evidence:** config and code commit before run; raw search output stored read-only after completion.\
**Docs:** experiment registry and package versions.\
**Verification:** fold class counts, parameters, seeds, scores and failures recoverable; no hidden manual trial.\
**Common mistakes:** pipeline search params misnamed; keep only `best_params_`; oversample before CV.\
**Recovery:** fix wrapper and rerun as new search ID; preserve earlier log.\
**Definition of Done:** all searches will write complete per-candidate evidence.\
**Next:** STEP-029.

## STEP-029 — Tune model 1 and review the search result

**Objective:** Execute the first approved model search.\
**Owner/reviewer/deadline:** assigned estimator owner / M4 / 02 Dec.\
**Prerequisites:** STEP-027–028; G03.\
**Effort/parallel work:** 1–3 hours depending on search.\
**Inputs:** model-1 tuning config, training folds, pipeline.\
**Outputs:** full CV results, best parameters, baseline/tuned comparison and warnings.\
**Procedure:** Run once from clean state; confirm fold-local transforms; inspect convergence and search boundary hits; report training-CV metrics only. If best parameter lies at edge, record as a follow-up question rather than expanding search secretly.\
**Planning prompt:** “Review the search log, not only the winner, and identify instability or failed candidates.”\
**Implementation prompt:** “Persist complete CV results and best estimator with config and code hash.”\
**Human decisions:** M4 decides whether a preregistered rerun is necessary; no test access.\
**Version control/evidence:** unique EXP/TUNE ID; never overwrite.\
**Docs:** tuning results table.\
**Verification:** selected model and baseline compare on same CV protocol; full candidate data accessible.\
**Common mistakes:** label CV score as test score; expand parameter space after seeing result without recording.\
**Recovery:** register expanded search as new exploratory search and disclose.\
**Definition of Done:** first model tuning is traceable and reviewed.\
**Next:** STEP-030.

## STEP-030 — Tune models 2 and 3 and confirm required coverage

**Objective:** Complete at least three independently tuned estimators.\
**Owner/reviewer/deadline:** M4 coordinates; relevant owners execute / M2 audits / 03 Dec internal, 04 Dec official.\
**Prerequisites:** STEP-028 and model-specific configs.\
**Effort/parallel work:** 2–4 hours; independent searches may run in parallel if compute permits.\
**Inputs:** second/third search configs, fixed training split/CV.\
**Outputs:** two full search logs, best parameters, before/after CV results, failure record.\
**Procedure:** Run each under approved plan, preserve unsuccessful trials, note convergence/runtime; do not compare scores from different scoring definitions. Confirm three unique model families/estimators are tuned as required.\
**Planning prompt:** “Verify all tuning evidence is generated from training folds under the same protocol.”\
**Implementation prompt:** “Run remaining searches and merge machine-readable records without manual score transcription.”\
**Human decisions:** M4 determines search completion; team approves if compute limits force documented narrowing.\
**Version control/evidence:** unique run IDs, config hashes and environment.\
**Docs:** tuning registry and tracker.\
**Verification:** at least three models; best params and search spaces recorded; no test data used.\
**Common mistakes:** report only before/after accuracy; count repeated searches of one estimator as three models.\
**Recovery:** tune an additional model under a preregistered plan or disclose unmet requirement to instructor.\
**Definition of Done:** required tuning evidence is complete or accurately marked blocked.\
**Next:** STEP-031.

## STEP-031 — Consolidate tuning comparisons and assess model stability

**Objective:** Compare baseline and tuned candidates without overinterpreting small differences.\
**Owner/reviewer/deadline:** M4 / M2 / 03 Dec.\
**Prerequisites:** STEP-029–030.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** baseline and tuning logs, metric contract, CV results.\
**Outputs:** common before/after table, selected-score distribution/fold summary, candidate shortlist and trade-off note.\
**Procedure:** Align folds/scoring; report mean and fold variability where available; identify overfit signs; describe malignant recall vs specificity tradeoff; do not treat tiny CV gaps as certain superiority.\
**Planning prompt:** “Check whether any claimed improvement survives fold-level comparison and is practically interpretable.”\
**Implementation prompt:** “Build comparison figures from registry outputs and retain all metric names/units.”\
**Human decisions:** M4 recommends shortlist; team chooses XAI candidate(s) and selection criterion.\
**Version control/evidence:** figure spec and generated outputs trace to EXP IDs.\
**Docs:** report methods/results draft.\
**Verification:** three+ tuned models represented; no mixing CV and test estimates; false negatives discussed.\
**Common mistakes:** call a higher mean proof of generalization; show only favorable metrics.\
**Recovery:** label preliminary, recheck raw fold metrics and correct narrative.\
**Definition of Done:** reviewed tuning comparison supports a transparent selection meeting.\
**Next:** STEP-032.

## STEP-032 — Define explainability method and cases before generating output

**Objective:** Choose explanation procedure consistent with selected estimator and feature pipeline.\
**Why:** SHAP outputs depend on explainer, background and transformed feature alignment.\
**Owner/reviewer/deadline:** M5 / M2 and M4 / 03 Dec.\
**Prerequisites:** STEP-031 candidate shortlist.\
**Effort/parallel work:** 1 hour.\
**Inputs:** candidate estimators, feature names, training data and explanation guidance.\
**Outputs:** XAI protocol specifying SHAP or permutation, global sample/background, local benign/malignant case-selection rule, random seed and interpretation limits.\
**Procedure:** Prefer SHAP if compatible and feasible; use permutation importance as alternative. Select background/reference from training data only. Choose local cases by transparent rule, not surprising explanations. Declare correlated predictors and model dependence.\
**Planning prompt:** “Check explainer compatibility, feature-name mapping and risk of test-informed case selection.”\
**Implementation prompt:** “Implement the approved explanation wrapper against the complete fitted pipeline.”\
**Human decisions:** M5 chooses tooling; M4 approves case-selection independence; team approves narrative.\
**Version control/evidence:** protocol committed before output creation.\
**Docs:** XAI methods note and decision log.\
**Verification:** method is estimator-compatible; background/cases are documented; feature order is explicit.\
**Common mistakes:** label attribution as causation; choose local examples after seeing test results.\
**Recovery:** redesign protocol before final test; if test cases already inspected, label exploratory.\
**Definition of Done:** XAI procedure is reproducible and bounded.\
**Next:** STEP-033.

## STEP-033 — Generate global and local explainability evidence

**Objective:** Produce understandable global behavior and one local example per class when feasible.\
**Owner/reviewer/deadline:** M5 / M4 / 04 Dec.\
**Prerequisites:** STEP-032 and candidate pipeline.\
**Effort/parallel work:** 1–3 hours.\
**Inputs:** candidate model, training-only reference/background, case selection protocol.\
**Outputs:** global importance/SHAP summary; benign and malignant local explanation(s); feature mapping audit.\
**Procedure:** Execute from clean code; verify transformed feature names; generate plots and numeric values; interpret direction/magnitude as influence on this fitted model, not biology or causality; note correlated-feature and sample limitations.\
**Planning prompt:** “Audit whether captions correctly describe the prediction output and feature semantics.”\
**Implementation prompt:** “Save explanation objects/config, plots and runtime; fail if feature names/order cannot be reconciled.”\
**Human decisions:** M5 interprets; M2 checks mapping; M4 checks selected estimator.\
**Version control/evidence:** record model/checkpoint/data/XAI protocol IDs; no manual image edits that alter values.\
**Docs:** report XAI section and limitations.\
**Verification:** outputs are from registered candidate; at least one global and local cases where feasible; no causal language.\
**Common mistakes:** display global importance as patient-specific reason; mix model versions.\
**Recovery:** rerun after fixing mapping and version outputs; retract invalid explanation.\
**Definition of Done:** XAI evidence and cautious interpretation are reviewed.\
**Next:** STEP-034.

## STEP-034 — Hold selection review and freeze candidate before final test

**Objective:** Record the final candidate and all selection choices before test inspection.\
**Why:** The held-out score is meaningful only after model selection is complete.\
**Owner/reviewer/deadline:** M4 presents / all five approve / 04 Dec.\
**Prerequisites:** STEP-031–033; G03–G05 evidence.\
**Effort/parallel work:** 45–90 minutes; freeze meeting is serialized.\
**Inputs:** baseline/tuning comparison, XAI, selection metric, threshold protocol, saved artifacts.\
**Outputs:** signed model-selection record with model/config/pipeline hash, class/feature order, threshold rule, selection reason and known limitations; G05 result.\
**Procedure:** Compare only development/CV evidence; discuss malignant recall, specificity, ROC-AUC, false-negative tradeoff, calibration limitations and XAI fit. Select candidate under predeclared criterion. Record threshold (or default threshold rationale) without reference to test. Freeze code and candidate artifact.\
**Planning prompt:** “Check decision is supported by development evidence and that the test remains unopened.”\
**Implementation prompt:** “Write a freeze manifest with exact hashes and refuse silent artifact replacement.”\
**Human decisions:** all five confirm for course; M4 signs metric rationale.\
**Version control/evidence:** tag/commit; freeze record stored before test run.\
**Docs:** tracker, results narrative and model card.\
**Verification:** candidate and threshold recorded; no test metrics cited; G05 PASS.\
**Common mistakes:** choose a model after viewing test results; pick best accuracy despite agreed malignant-recall priority.\
**Recovery:** if test was viewed, document exposure and designate it exploratory; seek new independent evaluation for claims.\
**Definition of Done:** candidate selection is locked and G06 PASS for exact artifact.\
**Next:** STEP-035.

## STEP-035 — Package the frozen model artifact and interface contract

**Objective:** Serialize the complete selected preprocessing-plus-model pipeline for application use.\
**Why:** Saving only the estimator risks app/training mismatch.\
**Owner/reviewer/deadline:** M2/M5 / M4 / 05 Dec.\
**Prerequisites:** STEP-034.\
**Effort/parallel work:** 1–2 hours; artifact produced once.\
**Inputs:** selected pipeline, feature contract, dependencies, model ID and freeze manifest.\
**Outputs:** versioned fitted pipeline (joblib or equivalent), hash, load instructions, class order and model card.\
**Procedure:** Serialize full fitted object using trusted package versions; reload in clean process; compare predictions/scores on fixed permitted examples; verify feature order, positive label and threshold metadata. Do not modify model post-freeze.\
**Planning prompt:** “Review artifact portability and risks of pickle/joblib trust boundary.”\
**Implementation prompt:** “Save, hash, reload and parity-check the exact frozen pipeline; fail on version/hash mismatch.”\
**Human decisions:** M5 chooses supported serialization; team approves where artifact is stored/linked.\
**Version control/evidence:** artifact location/hash; avoid committing large binaries if repository or policy disallows.\
**Docs:** install guide, model card, app integration contract.\
**Verification:** reloaded pipeline output matches in-process output; class order/feature order exact; G06 remains valid.\
**Common mistakes:** serialize just estimator; train again during app startup; expose unsafe deserialization to untrusted users.\
**Recovery:** regenerate from frozen run under new artifact ID and rerun parity; preserve old artifact record.\
**Definition of Done:** application can load the exact registered fitted pipeline.\
**Next:** STEP-036.

# S06 — Application and integration (official due 08 December; internal 07 December)

## STEP-036 — Approve app behavior, screen flow and safety copy

**Objective:** Define the minimum functional interface before implementation.\
**Owner/reviewer/deadline:** M5 / M1 and M4 / 05 Dec.\
**Prerequisites:** OS app policy and STEP-012 feature contract.\
**Effort/parallel work:** 1 hour; UI styling can follow in parallel with artifact wrapper.\
**Inputs:** guide screen recommendations, app requirement, feature contract, model card.\
**Outputs:** app specification: Home, Predict, Result, Performance and Dataset/About sections; disclaimer location; accepted input mode; output labels; error states.\
**Procedure:** Decide form vs CSV upload (avoid optional complexity if deadline); define exact feature labels/order, required values and validation; show model selection/held-out metrics with source; label probabilities as model outputs; forbid diagnosis or treatment language.\
**Planning prompt:** “Review the screen flow for non-clinical wording, accessibility and unsupported claims.”\
**Implementation prompt:** “Implement only agreed screens and copy the exact disclaimer approved in the guide/OS.”\
**Human decisions:** M5 proposes; M1/M4 approve accuracy; instructor confirms hosted vs local demonstration requirement.\
**Version control/evidence:** app spec and copy committed.\
**Docs:** README and user guide.\
**Verification:** all screens have source for displayed value; non-clinical notice visible before prediction.\
**Common mistakes:** “cancer risk” label; display test metrics before final evaluation exists.\
**Recovery:** remove unsupported screen/value; update spec before demo.\
**Definition of Done:** app requirements are clear and testable.\
**Next:** STEP-037.

## STEP-037 — Build the inference wrapper and artifact loader

**Objective:** Provide one app-callable function that uses the saved pipeline unchanged.\
**Owner/reviewer/deadline:** M5 / M2 / 06 Dec.\
**Prerequisites:** STEP-035.\
**Effort/parallel work:** 2–3 hours; UI shell can proceed concurrently using a stub.\
**Inputs:** artifact/hash, feature contract, threshold/class mapping, package lock.\
**Outputs:** inference module, startup hash/version checks, structured output schema, safe error types.\
**Procedure:** Load the approved artifact once; validate required columns and order; call pipeline prediction/probability method; map encoded labels correctly; return model ID, class, score type and threshold metadata. Avoid duplicate scaling or estimator logic.\
**Planning prompt:** “Compare wrapper transformations with training pipeline and identify any duplicated or implicit preprocessing.”\
**Implementation prompt:** “Call the serialized pipeline directly; reject missing artifact/hash mismatch and return structured errors.”\
**Human decisions:** M2 confirms schema; M4 confirms threshold/metric provenance.\
**Version control/evidence:** commit wrapper; artifact separately addressed by hash.\
**Docs:** inference interface and run guide.\
**Verification:** fixed-input output matches STEP-035 parity; wrong hash fails closed; no retraining on launch.\
**Common mistakes:** alter threshold for more appealing predictions; map `predict_proba` columns by assumption.\
**Recovery:** stop app release; fix mapping/wrapper and rerun parity.\
**Definition of Done:** stable, hash-verified inference entry point exists.\
**Next:** STEP-038.

## STEP-038 — Implement the user interface and results presentation

**Objective:** Deliver the minimum useful CSE431 application.\
**Owner/reviewer/deadline:** M5 / M1 / 07 Dec internal.\
**Prerequisites:** STEP-036–037.\
**Effort/parallel work:** 3–5 hours; independent styling permitted after output schema fixed.\
**Inputs:** app spec, inference wrapper, approved screenshots/data examples.\
**Outputs:** Streamlit or instructor-approved app; pages/sections; visible disclaimer; performance and dataset reference panels.\
**Procedure:** Build inputs from feature contract; prevent stale values; display predicted label and clearly labeled model score/probability; show class order and selected model; display global/local explanation with caveat; link performance values to the registered evaluation record.\
**Planning prompt:** “Review visual hierarchy and ensure a user cannot mistake the output for a clinical diagnosis.”\
**Implementation prompt:** “Connect UI only to wrapper; never duplicate feature scaling, class mapping or metric values manually.”\
**Human decisions:** M1/M4 review content; M5 owns implementation.\
**Version control/evidence:** commit source; retain non-sensitive screenshots.\
**Docs:** app readme, screenshots index.\
**Verification:** full disclaimer, correct units/labels, no inaccessible control, no unsupported metric.\
**Common mistakes:** expose a probability as clinical confidence; hard-code expected score; choose an illustrative example without labeling it.\
**Recovery:** remove/fix misleading component; retest integration.\
**Definition of Done:** primary user flow works on the registered model.\
**Next:** STEP-039.

## STEP-039 — Implement input validation and safe failure states

**Objective:** Reject malformed inputs clearly and avoid ambiguous inference.\
**Owner/reviewer/deadline:** M5 / M2 / 07 Dec.\
**Prerequisites:** STEP-037–038; STEP-003 confirms CSV/demo rules.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** feature schema, sample valid/invalid inputs, app spec.\
**Outputs:** validation module and case matrix for missing, extra, reordered, nonnumeric, nonfinite and malformed CSV fields.\
**Procedure:** Validate by column name then reorder only if specification permits; reject missing/extra fields unless allowed by documented policy; reject nonnumeric/NaN/inf; provide safe messages without traceback or stored user input. Keep application examples synthetic/public only.\
**Planning prompt:** “Enumerate invalid conditions and define a distinct, understandable message for each.”\
**Implementation prompt:** “Add validation before model invocation; never silently fill or coerce unsupported input.”\
**Human decisions:** M5 defines UI behavior; M2 approves feature semantics.\
**Version control/evidence:** cases linked in app test matrix.\
**Docs:** user guide and data policy.\
**Verification:** invalid rows do not reach model; valid input follows the same wrapper; errors do not expose paths/secrets.\
**Common mistakes:** reorder columns positionally without checks; drop invalid CSV rows silently.\
**Recovery:** fix validator and repeat the full matrix; document any accepted CSV schema.\
**Definition of Done:** invalid-input behavior is predictable and evidenced.\
**Next:** STEP-040.

## STEP-040 — Integrate app, exact model and evaluation displays

**Objective:** Join interface, pipeline and registered result values without version drift.\
**Owner/reviewer/deadline:** M5 integration / M4 metric audit / 07 Dec.\
**Prerequisites:** STEP-035 and STEP-037–039.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** frozen model ID, metrics artifact (if final test not yet completed, use development values clearly marked provisional or omit), class/feature contract.\
**Outputs:** integrated runnable build; model/version banner; metrics source manifest.\
**Procedure:** Read model identity and metrics from registries/artifacts; distinguish validation/CV/test estimates; do not populate final-test panel until STEP-042. Verify all result charts correspond to the same model and class mapping.\
**Planning prompt:** “Trace each app result/metric to its source file and evaluation partition.”\
**Implementation prompt:** “Bind metrics to evaluation ID and hide final-test fields until the actual evaluation is approved.”\
**Human decisions:** M4 approves metric displays; M5 approves app behavior.\
**Version control/evidence:** build commit and config hash.\
**Docs:** interface version and data source.\
**Verification:** model ID exact; no manually retyped score; no provisional number mislabeled final.\
**Common mistakes:** show benchmark score from a public paper as app result; show test metric before test run.\
**Recovery:** remove incorrect panel and regenerate from source record.\
**Definition of Done:** all app outputs have traceable sources and partition labels.\
**Next:** STEP-041.

## STEP-041 — Clean-run, parity and application readiness gate

**Objective:** Demonstrate the app can be reproduced outside the author's active environment.\
**Owner/reviewer/deadline:** M5 / M2 and M4 / 07 Dec internal, 08 Dec official.\
**Prerequisites:** STEP-037–040.\
**Effort/parallel work:** 2–3 hours; clean environment controlled by a second member.\
**Inputs:** requirements lock, run guide, fixed permitted example inputs, saved pipeline.\
**Outputs:** clean install/run record, inference parity report, app test matrix, screenshots/demo link if requested.\
**Procedure:** Fresh clone/environment; install documented requirements; launch app; compare direct pipeline and app result on fixed cases; run valid/invalid inputs; check disclaimer and links; capture error fixes.\
**Planning prompt:** “Review whether another teammate can reproduce the demo with only the repository guide.”\
**Implementation prompt:** “Run the clean setup, resolve issues, then repeat full parity and validation checks.”\
**Human decisions:** M1 confirms instructor access to demo; M4 checks metric parity.\
**Version control/evidence:** final app commit and immutable evidence captures.\
**Docs:** install/run guide, test evidence, G07 assessment.\
**Verification:** no hidden dependency; output parity; model/hash check passes; disclaimer/validation clear.\
**Common mistakes:** test only in existing notebook environment; count an app screenshot as proof of correct pipeline.\
**Recovery:** simplify dependency/setup, update lock, repeat clean run; do not claim ready until pass.\
**Definition of Done:** G07 app readiness PASS or an explicit local fallback and blocker plan are approved.\
**Next:** STEP-042.

# S07 — Final test, report and course release (official due 10 December; internal 09 December)

## STEP-042 — Reconfirm freeze and authorize held-out test access

**Objective:** Verify the locked candidate has not changed before the one planned final test run.\
**Why:** Test use after selection can no longer serve as independent confirmation.\
**Owner/reviewer/deadline:** M4 / M2 and all / 09 Dec internal.\
**Prerequisites:** G06; candidate/pipeline/hash; test manifest.\
**Effort/parallel work:** 30–60 minutes; serialized signoff.\
**Inputs:** freeze record, source/split/protocol hashes, test access history.\
**Outputs:** test authorization note; confirmation that the chosen model, preprocessing, threshold and metrics are frozen.\
**Procedure:** Compare artifact hashes and configuration to STEP-034/035; ask each member whether any test output was previously viewed; record exposure; verify no post-test change influenced selection.\
**Planning prompt:** “Audit test-set access and identify any post-freeze decision that used it.”\
**Implementation prompt:** “Refuse final evaluation if hashes differ or test exposure is unexplained.”\
**Human decisions:** M4 and team decide whether test remains confirmatory; any exposure downgrades claim.\
**Version control/evidence:** signed record precedes metrics run.\
**Docs:** gate register and evaluation tracker.\
**Verification:** exact model/data/split/protocol IDs; no unresolved exposure.\
**Common mistakes:** test metrics were viewed informally but not logged; select threshold after test results.\
**Recovery:** classify existing holdout as exploratory and arrange new independent data or report limitation.\
**Definition of Done:** test authorization is evidence-based and freeze is intact.\
**Next:** STEP-043.

## STEP-043 — Evaluate the frozen model on the untouched test partition

**Objective:** Produce the final course held-out evaluation exactly once under the frozen protocol.\
**Owner/reviewer/deadline:** M4 / M2 / 09–10 Dec.\
**Prerequisites:** STEP-042.\
**Effort/parallel work:** 1–2 hours; final scoring run must not overlap with model selection.\
**Inputs:** frozen model/pipeline, locked test manifest, metric implementation, threshold record.\
**Outputs:** predictions/scores, confusion counts, required metrics, ROC curve data, evaluation report and hashes.\
**Procedure:** Run inference only; save positive-class scores and labels; calculate accuracy, malignant precision/recall, specificity, F1 and ROC-AUC; record denominators and threshold; create confusion matrix and ROC chart. Do not change model afterward based on these observations.\
**Planning prompt:** “Check the evaluation command uses only the registered test partition and fixed threshold.”\
**Implementation prompt:** “Generate final outputs from the frozen artifact and write a machine-readable evaluation record.”\
**Human decisions:** M4 signs metric outputs; team decides wording, not model updates.\
**Version control/evidence:** prediction artifact storage follows policy; logs and report IDs retained.\
**Docs:** evaluation registry, report result table, tracker.\
**Verification:** test counts reconcile; score/label columns correct; metric script and table agree.\
**Common mistakes:** evaluate multiple versions and report the best; tune threshold from test; infer precision from accuracy.\
**Recovery:** if bug is purely computational, disclose and rerun with correction; if result influenced a change, downgrade to exploratory and seek new validation data.\
**Definition of Done:** one traceable final evaluation exists with limitations.\
**Next:** STEP-044.

## STEP-044 — Interpret uncertainty, errors and limits

**Objective:** Turn final metrics into accurate, bounded conclusions.\
**Owner/reviewer/deadline:** M4 / M1 and M2 / 10 Dec.\
**Prerequisites:** STEP-043.\
**Effort/parallel work:** 1–2 hours.\
**Inputs:** confusion matrix, predictions, protocol, error cases and dataset card.\
**Outputs:** performance discussion, false-negative/false-positive analysis, uncertainty note, limitations and conclusion draft.\
**Procedure:** Explain sensitivity/recall for malignant class and specificity for benign; report counts alongside rates; describe selected errors without asserting clinical cause; use uncertainty intervals if method is justified and feasible; state small dataset/single benchmark/split limits.\
**Planning prompt:** “Audit that each conclusion is no stronger than the design and denominator permit.”\
**Implementation prompt:** “Create error summary from registered predictions and avoid patient identity or fabricated examples.”\
**Human decisions:** M4 and all authors approve wording.\
**Version control/evidence:** claims reference evaluation ID and figure/table ID.\
**Docs:** abstract, results, discussion, limitations.\
**Verification:** every result matches STEP-043; no clinical efficacy or Q1 novelty claim.\
**Common mistakes:** call recall “safety”; interpret one missed record clinically; omit denominator.\
**Recovery:** correct narrative, preserve prior draft in revision history, fact-check again.\
**Definition of Done:** evidence-aligned discussion is approved.\
**Next:** STEP-045.

## STEP-045 — Draft and cross-check the final course report

**Objective:** Produce a complete report that follows instructor format and matches actual execution.\
**Owner:** M1 coordinates; section authors per responsibility matrix; **review:** all five / 10 Dec.\
**Prerequisites:** G02–G07, STEP-043–044; report format confirmed.\
**Effort/parallel work:** section writing parallel; one editor controls final merge/citations.\
**Inputs:** verified source notes, experiment registry, metrics, XAI, app screenshots, contribution/AI logs.\
**Outputs:** final report PDF and editable source, reference list, figure/table list, claim-to-evidence cross-check.\
**Procedure:** Use guide structure: title/abstract/keywords; intro/problem/objectives/scope; related work; dataset/EDA; preprocessing and leakage prevention; model lineup/families; tuning/searches; metrics/results/errors; XAI; application/testing; limitations/ethics/future work; conclusion; references; contribution and AI-use. Map every empirical statement to a run/evaluation ID; every citation to source.\
**Planning prompt:** “Review the report against course checklist, source facts, evidence and non-clinical wording.”\
**Implementation prompt:** “Assemble only verified results and figures; mark missing items rather than inventing.”\
**Human decisions:** all authors approve content, names/IDs, authorship and declaration; instructor rules override format assumptions.\
**Version control/evidence:** tag report version and source revision; keep final PDF bytes identifiable.\
**Docs:** tracker, report release note, claims map.\
**Verification:** consistent title, scope, model, metrics and app; refs open; AI-use/contribution accurate.\
**Common mistakes:** paper-style conclusions unsupported by class project; placeholder citations; copy chart numbers manually.\
**Recovery:** block submission package, correct from canonical evidence, repeat cross-check.\
**Definition of Done:** report matches actual evidence and course format.\
**Next:** STEP-046.

## STEP-046 — Prepare slides, contribution/AI declarations, clean release and submit (G08)

**Objective:** Package, rehearse, test and submit all course deliverables with accessible evidence.\
**Owner:** M1 coordinates; M5 app/demo; M4 metrics; all five present/review / 09 internal, 10 Dec official.\
**Prerequisites:** STEP-041–045 and current instructor submission instructions.\
**Effort/parallel work:** slide drafting and clean-environment check can run in parallel; final release and upload serialized.\
**Inputs:** final report, app, experiment evidence, roster, contributions, AI log, submission portal.\
**Outputs:** slide deck/PDF, final repository release, test report, screenshots/demo, contribution matrix, AI declaration, submission receipt and G08 assessment.\
**Procedure:** (1) Put all five full names/IDs on title slide and full IDs in footer of every slide. (2) Assign all five speaking sections and rehearse transitions/Q&A. (3) Run app from clean environment and test valid/missing/nonnumeric/CSV cases, model load, charts, explanation, metrics. (4) Verify every evidence URL opens with instructor permissions. (5) Freeze exact files and repository tag. (6) Submit according to confirmed route/time and save receipt.\
**Planning prompt:** “Run a submission checklist and identify blockers, including inaccessible links and missing IDs.”\
**Implementation prompt:** “Make only verified corrections, regenerate PDFs/screenshots, record final hashes and submit the package.”\
**Human decisions:** all five approve contributions/AI declaration; instructor confirms any late/revised submission route.\
**Version control/evidence:** final release tag plus upload receipt; no secrets or restricted data in public release.\
**Docs:** README, release notes, contribution log, AI-use statement, milestone evidence.\
**Verification:** clean run, no critical bug, all required model/metric/evidence items present, all five participate, final files exact.\
**Common mistakes:** slides without footer IDs; private evidence links; declare contributions not supported by log; assume upload succeeded.\
**Recovery:** correct package and resubmit only through allowed route; keep both submission records.\
**Definition of Done:** G08 PASS with package hash, accessible evidence and receipt; no Q1-readiness inference.\
**Next:** STEP-047 if publication work is separately approved.

# S08 — Separate journal-readiness track (after course submission)

## STEP-047 — Search literature and test whether a publishable gap exists

**Objective:** Determine whether there is a novel, answerable research question beyond repeating WDBC model comparisons.\
**Why:** A Q1 journal requires a contribution that the supplied assignment does not establish.\
**Owner/reviewer/deadline:** M1 leads search; all authors screen; supervisor reviews / schedule after 10 Dec.\
**Prerequisites:** G08 course package frozen; supervisor agrees to explore publication.\
**Effort/parallel work:** several days to weeks; screening can be divided with duplicate independent decisions.\
**Inputs:** current primary literature, model/data search terms, existing report and results.\
**Outputs:** protocol, search log, deduplicated paper set, extraction table (task/data/split/validation/metrics/XAI/limitations/contribution), gap memo.\
**Procedure:** Search recent and seminal studies; include direct WDBC reuse and adjacent tabular diagnostic ML work; screen titles/abstracts/full text with inclusion reasons; verify each bibliographic record; record contradictory evidence; map the proposed claim to prior art.\
**Planning prompt:** “Test whether the intended novelty is already reported and identify stronger alternatives.”\
**Implementation prompt:** “Build a source-linked literature matrix; no claim enters the gap memo without primary-source evidence.”\
**Human decisions:** supervisor approves scope and novelty interpretation; all authors verify key studies.\
**Version control/evidence:** search strings, access date and screening decisions versioned.\
**Docs:** literature registry and research-question proposal.\
**Verification:** search is reproducible; direct and contradictory papers included; gap is narrow and evidence-supported.\
**Common mistakes:** claim “first” based on a quick search; count another model comparison as novelty; cite abstracts only for methods.\
**Recovery:** broaden search, revise gap, or stop publication track.\
**Definition of Done:** supervisor-reviewed gap memo states what is new and what evidence supports it.\
**Next:** STEP-048.

## STEP-048 — Design a publication-grade study and assess bias/applicability

**Objective:** Decide whether data and evaluation can support the proposed journal claims.\
**Owner:** M4 methods; M2 data; M5 XAI/app; M1 governance; all authors review / schedule after STEP-047.\
**Prerequisites:** approved gap memo.\
**Effort/parallel work:** protocol design can run in parallel with data-access feasibility, but no new restricted data is acquired without approvals.\
**Inputs:** gap memo, data rights/ethics rules, supervisor/statistician input, reporting guidance.\
**Outputs:** preregistered or versioned study protocol, sample-size/data adequacy rationale, validation plan, analysis plan, ethics/license record, risk-of-bias/applicability assessment.\
**Procedure:** Determine if WDBC alone can answer the question. If not, identify independent data source, permission, ethics and acquisition feasibility. Plan internal resampling/nested tuning or independent/external evaluation as question requires; define thresholds, calibration, uncertainty, subgroup/fairness analyses only where supported by data. Use TRIPOD+AI for reporting and PROBAST+AI for study design/applicability review where relevant.\
**Planning prompt:** “Identify what evidence is needed to make each proposed conclusion, and whether the available data can deliver it.”\
**Implementation prompt:** “Write the protocol and gates; do not run analyses on new data before access/ethics decisions.”\
**Human decisions:** supervisor, institution/data custodian and all authors approve scope, data and protocol; clinical interpretation requires qualified expertise.\
**Version control/evidence:** freeze protocol prior to outcomes where feasible; document amendments.\
**Docs:** ethics/access records, analysis protocol, risk register, reporting checklist.\
**Verification:** valid independent validation plan, leakage control, outcome/participant definitions, calibration/uncertainty scope, reproducibility.\
**Common mistakes:** use same WDBC test set for a second confirmatory study; call random CV external validation; imply guideline compliance proves validity.\
**Recovery:** narrow claims, obtain suitable data/approval, redesign or cancel journal study.\
**Definition of Done:** protocol and resource/approval feasibility reviewed; no unresolved critical bias issue.\
**Next:** STEP-049.

## STEP-049 — Select venue and make the final manuscript go/no-go decision (G09)

**Objective:** Submit only a credible, transparent manuscript to a current, suitable journal.\
**Owner:** corresponding author appointed by agreement; supervisor/all authors approve / timing set by study plan.\
**Prerequisites:** STEP-047–048 PASS; full study evidence available; authorship/contributions agreed.\
**Effort/parallel work:** journal search and manuscript drafting can overlap after protocol/results stabilize; final audit is serialized.\
**Inputs:** complete study/report, current journal scopes and author rules, verified indexing/quartile source, data/code availability, reporting checklist.\
**Outputs:** journal fit memo, completed manuscript/checklists, author declarations, or a documented no-go/redesign decision.\
**Procedure:** Compare candidate venues for scope, methods fit, article type, indexing/category/quartile as of the check date, fees, data/code requirements and review policy. Avoid predatory venues and quartile guarantees. Complete all applicable reporting items, verify every reference/claim/number, obtain all-author and supervisor approval, and state limitations plainly.\
**Planning prompt:** “Evaluate venue fit and manuscript evidence independently of the desired quartile.”\
**Implementation prompt:** “Prepare a submission package only after all evidence and author declarations are final; record venue checks with date.”\
**Human decisions:** all authors approve authorship/order, conflicts, funding, AI use, data/code availability and submission; corresponding author submits.\
**Version control/evidence:** immutable submitted manuscript and receipt; journal correspondence archived.\
**Docs:** G09 assessment, venue memo, data/code statement, author contribution statement.\
**Verification:** novel contribution supported; analysis matches protocol; reporting and bias review complete; current venue status checked; no invented clinical promise.\
**Common mistakes:** equate Q1 with acceptance; target quartile before verifying fit; submit course report unchanged as research article.\
**Recovery:** no-go, revise the question/design or choose a more suitable venue; disclose rejection and respond scientifically to reviews.\
**Definition of Done:** G09 PASS authorizes submission only; editorial acceptance is external and cannot be guaranteed.\
**Next:** follow journal review/revision process under a separately dated plan.

## Final completion and handoff checklist

- [ ] STEP-001 records the true 17 Nov status and any deadline recovery.
- [ ] STEP-002 resolves model ownership conflict and gives every artifact an owner/reviewer.
- [ ] G02 source/schema/EDA evidence is complete; raw data remains unchanged.
- [ ] G03 split, feature contract, metric protocol and pipelines are leakage-safe.
- [ ] G04 covers all eight required estimators and families using one comparison protocol.
- [ ] G05 records three or more training-CV searches and XAI evidence.
- [ ] G06 freeze precedes final test access; final scores are not used to retune.
- [ ] G07 app uses the saved full pipeline and passes clean-run/input checks.
- [ ] G08 report, slides, IDs, tests, contributions, AI declaration, evidence URLs and receipt are verified.
- [ ] G09 is treated as a separate post-course publication decision; no acceptance promise or unsupported clinical claim is made.

---

# Appendix A — Day-by-day work calendar and handoffs

The table converts the seven supplied milestone dates and one-day buffers into daily control points. It is a coordination proposal, not a changed due-date schedule. If a member has unavailable dates, record a reassignment during STEP-002. A short daily async update is sufficient; hold a live review at each gate.

| Date | Main work and accountable lead | Handoff / evidence due by end of day |
|---|---|---|
| Tue 17 Nov | M1 confirms topic submission; all five resolve roles; M1 confirms rubric and creates tracker/repo | Scope status/receipt, D02 owner matrix, open questions, repo link |
| Wed 18 Nov | M1 retrieves official source and documents terms; M2 reviews source and builds intake contract | Dataset URL/access date, raw source hash, terms status |
| Thu 19 Nov | M1/M2 schema, class, missingness, duplicate and validity audit | Verified schema/count report; unresolved discrepancies assigned |
| Fri 20 Nov | M1 completes four EDA chart types and 3–5 observations; M4 reviews claims | EDA notebook, chart files, dataset card, internal evidence URLs |
| Sat 21 Nov | All review G02 and submit dataset/EDA milestone | G02 assessment and accessible official milestone evidence |
| Sun 22 Nov | M2 defines target/feature contract; M4 drafts evaluation definitions | Feature contract, positive label, metric questions |
| Mon 23 Nov | M2/M4 settle stratified split/CV/threshold policy; team signs protocol | Evaluation protocol v1 before modeling |
| Tue 24 Nov | M2 creates locked split and pipelines; M4 audits leakage boundaries | Split manifest, pipeline commit, G03 evidence (internal target) |
| Wed 25 Nov | Team closes preprocessing milestone and submits evidence | G03 PASS/blocked record; preprocessing code and rationale |
| Thu 26 Nov | M4/M2 model run interface; M3/M5 prepare model configs | Model registry, shared output schema and environment record |
| Fri 27 Nov | LR/KNN/SVM + Decision Tree/Random Forest implementation and first runs | Run IDs, explicit baseline settings, warnings |
| Sat 28 Nov | Extra Trees/Gradient Boosting/MLP implementations; metric function review | Eight model map, MLP convergence status, metric hand-check |
| Sun 29 Nov | M4 consolidates baseline results; team checks protocol equality | Internal baseline table, unresolved run list |
| Mon 30 Nov | Close G04 and submit eight-model milestone | Eight model outputs, common metrics, accessible evidence |
| Tue 01 Dec | M4 fixes three-model tuning plan and CV/search budgets; M5 defines XAI protocol | Frozen search spaces, metric objective, XAI method/case rule |
| Wed 02 Dec | Run first approved tuning search; independently review full fold log | Search log, CV results, before/after row |
| Thu 03 Dec | Run remaining searches; consolidate comparisons; produce global/local XAI | Three-model tuning bundle and XAI draft (internal target) |
| Fri 04 Dec | Review G05; hold candidate selection and freeze before test | Tuning/XAI evidence, signed selection/freeze, G06 PASS |
| Sat 05 Dec | M5 app flow specification; M2/M5 serialize/reload exact pipeline | App spec, model hash, clean-load check |
| Sun 06 Dec | Build inference wrapper and user interface; M2 validates schema | Wrapper commit, screen flow, initial valid-input parity |
| Mon 07 Dec | Complete validation/error cases, metric integration and clean-clone run | Test matrix, app/demo link, G07 internal review |
| Tue 08 Dec | Submit working application milestone; all members rehearse | App evidence, disclaimer check, run guide, screenshots |
| Wed 09 Dec | Reconfirm test freeze; M4 runs final test once; M1 assembles report/slides | Test outputs, report draft, slides, contribution/AI logs |
| Thu 10 Dec | Clean-environment test, cross-author review, final upload and receipt | G08, exact submitted files, final repo tag, submission receipt |
| After 10 Dec | Only with supervisor approval: literature search, study redesign, journal fit | D08 decision and separately dated G09 workplan |

**Daily cutoff rule:** by the end of each workday, the owner either posts (a) evidence link and Completed, (b) partial evidence and In Progress with a next action/date, or (c) blocker and requested help. “Done on my laptop” without a reproducible artifact is not a handoff.

# Appendix B — Responsibility and review matrix

The entries marked “provisional” are not source facts; the source PDFs' role proposals conflict and the originals were removed at the user's request after being read. The OS records the historical discrepancy in RF16 and Section 11.2. The team must finalize ownership in STEP-002. Student numbers are abbreviated here as M1–M5 only after the full mapping in the OS has been checked.

| Work package | Accountable owner (provisional) | Reviewer | Supporting roles | Evidence owned |
|---|---|---|---|---|
| Scope, instructor questions, schedule, tracker | M1 | All five | All provide current status | Scope receipt, decisions, milestone links |
| Source, dataset card, raw file and EDA | M1 | M2, M4 | M5 reviews app-ready naming | Hash, schema/quality audit, notebook, charts |
| Target, feature contract, split, preprocessing | M2 | M4 | M1 validates source semantics | Protocol, split manifest, pipeline code |
| Logistic Regression, KNN, SVM baselines | M2 (resolve against team-plan M4 assignment) | M4 | M1 checks report wording | Configs, run logs, outputs |
| Decision Tree, Random Forest, Extra Trees, Gradient Boosting | M3 | M4 | M2 checks shared pipeline | Configs, run logs, outputs |
| MLP baseline | M5 (resolve against guide's M4 assignment) | M4 | M2 checks scaling | Config, convergence record, outputs |
| Metric implementation and common comparison | M4 | M2 | Model owners inspect own outputs | Metric code, baseline table, confusion/ROC outputs |
| Hyperparameter search | M4 owns plan/results; model owner implements | M2 | M3/M5 execute their candidate searches | Search space, fold log, best params, before/after table |
| Global/local explainability | M5 | M2 feature mapping, M4 candidate lineage | M1 edits interpretation | Protocol, plots, case IDs/selection rule |
| Candidate selection and freeze | M4 convenes; all five approve | All five | M2/M5 provide lineage | Signed freeze manifest, model hash |
| Inference package and application | M5 | M2 pipeline parity, M4 metric lineage | M1 content review | Wrapper, app tests, disclaimer, screenshots |
| Report/editorial integration | M1 coordinates; each member owns assigned section | All five | M4 fact-checks results | PDF, sources, claim/evidence map |
| Presentation | Each member speaks; M1 coordinates | All five | M5 demo rehearsal | Slides with required IDs, rehearsal record |
| Course submission | M1 coordinates upload; all approve | M1 + one independent final checker | M4 checks metrics, M5 tests app | Receipt, release tag, evidence URLs |
| Publication study | To be reappointed after course; supervisor-approved | All authors | Qualified statistical/clinical review if required | Protocol, gap review, approvals, manuscript decision |

**Contribution-credit rule:** the owner field identifies accountability, not proof of authorship effort. The contribution log records actual work: `Date,MemberID,TaskID,Action,Artifact/Commit,Reviewer,Status,Minutes(optional),AI assistance,Verification`. An owner who did not complete work is recorded accurately; completed peer review is also a contribution.

# Appendix C — Canonical artifact and registry contracts

Adapt paths if the group uses a different repository layout, but record one mapping and keep one canonical record per entity.

| Record | Canonical suggested path | Minimum fields |
|---|---|---|
| Course decisions | `docs/decisions.md` | ID, question, evidence, options, decision/open state, approver, date, affected steps |
| Responsibilities | `docs/responsibility_matrix.csv` | Deliverable, owner, reviewer, backup, due date, decision ID |
| Milestone evidence | `docs/milestone_evidence.csv` | Milestone, due date, status, owner, artifact, URL, access checked, reviewer, blocker |
| Contributions | `docs/contributions.csv` | Member/ID, date, task, action, evidence, reviewer, actual status |
| AI use | `docs/ai_use.md` or CSV | Tool/use, artifact, extent/role, human verification, disclosure location; follow confirmed course method |
| Dataset card | `docs/dataset_card.md` | Source/version/hash, terms, access date, rows/columns/target, provenance, limitations |
| Data quality audit | `reports/data_quality_v1.md` | Counts, checks, findings, cleaning decision IDs, code revision |
| Feature contract | `docs/feature_contract.md` | Target mapping, positive class, predictor names/order/types, ID exclusion, schema hash |
| Split manifest | `reports/splits/SPLIT001.csv` or restricted store | Row key/hash, partition, class, source hash; no public direct identifiers |
| Evaluation protocol | `docs/evaluation_protocol_v1.md` | Holdout, stratification, seed, CV, metric definitions, threshold, access policy |
| Model config | `src/configs/MODEL###.yaml` | Estimator, explicit parameters, preprocessing, seed, package versions, owner |
| Experiment run | `reports/experiments/RUN####.md` | Data/split/config/code hashes, folds, start/end, status, outputs, warnings, deviations |
| Predictions/metrics | `reports/evaluations/EVAL###/` | Partition, row key/hash, labels/scores, threshold, counts, metrics, script/version |
| XAI record | `reports/explainability/XAI###.md` | Model ID, explainer, reference/background, feature mapping, case rule, artifacts, limits |
| Fitted pipeline | `models/MODEL_FINAL/` restricted/approved | Serialized full pipeline, hash, class order, feature order, dependencies, freeze ID |
| App tests | `app/tests/` + `reports/app_test_matrix.md` | Case ID, input condition, expected, actual, result, build/model hash |
| Report assets | `reports/figures/`, `reports/tables/` | Asset ID, source run/eval ID, generation command, caption, version |
| Submission release | `reports/releases/COURSE_FINAL/` | Exact report/slides/source hash, evidence links, upload receipt, date/time |

**Identifier convention:** use immutable identifiers such as `DEC001`, `DS001`, `SPLIT001`, `MODEL-LR-BASE`, `RUN001`, `EVAL001`, `XAI001`, `APP001`. Never recycle an ID after failure; mark its status and superseding ID. Store absolute machine paths only in local configs, not shared notebooks or report prose.

# Appendix D — Experiment protocol and estimator-specific control points

## D.1 Shared controls for every model

Every model run must state: input feature contract version; train/CV partition; class encoding; preprocessor; estimator name/version; explicit parameters; random seed (where relevant); scoring metric; class order; software versions; runtime/warnings; output hash. Model owners must not change the split or independently drop records. Distinguish baseline parameters from tuning search values. A failed convergence/run remains recorded and is not replaced silently.

## D.2 Model-specific implementation review

| Estimator | Must be explicit in baseline/tuning record | Pipeline control | Reviewer question |
|---|---|---|---|
| Logistic Regression | Solver, penalty/regularization, class weight, iterations, seed if used | Standardization inside fold | Did convergence occur, and does regularization match solver? |
| KNN | Neighbors, weights, distance/Minkowski settings | Standardization inside fold | Are neighborhood/distance settings comparable and explicit? |
| SVM | Kernel, C, gamma where applicable, class weights, probability/score mode | Standardization inside fold | Is reported ROC-AUC based on continuous decision scores/probabilities? |
| Decision Tree | Criterion, depth/leaf controls, class weight, seed | Scaling generally unnecessary | Is single-tree variance described and seed recorded? |
| Random Forest | Tree count, depth/leaf, feature sampling, class weight, seed | Scaling generally unnecessary | Are all randomized parameters and seed recorded? |
| Extra Trees | Tree count, split randomization, depth/leaf, feature sampling, seed | Scaling generally unnecessary | Is its distinct randomized split behavior clear? |
| Gradient Boosting | Estimator count, learning rate, depth/leaf controls, seed | Scaling generally unnecessary | Are iteration/runtime and overfit controls recorded? |
| MLP Classifier | Hidden layers, solver, alpha, learning rate, max iterations, seed, early-stopping policy | Standardization inside fold | Did it converge; are warnings and seed variability disclosed? |

These are reporting fields, not fixed hyperparameter values. The team decides values in STEP-018/027, before respective runs. No universal “best” settings are prescribed by the PDFs.

## D.3 Trial accounting

Each search has `SearchID`, target model, owner, objective metric, CV definition, candidate count, parameter bounds, start/end, full CV results path, best candidate, baseline link, failures and deviations. If a search is expanded after seeing results, retain the first search and register the expansion as a new exploratory search. Do not call an unplanned search preregistered.

# Appendix E — Metric definitions and application test matrix

## E.1 Metric contract checklist

Before presenting a metric, record positive class and threshold:

- **Accuracy:** `(TP + TN) / (TP + TN + FP + FN)` over the stated evaluation partition.
- **Malignant precision:** `TP / (TP + FP)` where malignant is positive.
- **Malignant recall/sensitivity:** `TP / (TP + FN)`; explicitly discuss false negatives and denominator.
- **Specificity:** `TN / (TN + FP)` for benign records under the same binary threshold.
- **F1:** `2 × precision × recall / (precision + recall)` for malignant class unless another averaging rule is explicitly stated.
- **ROC-AUC:** computed from continuous malignant scores; describe it as ranking/discrimination, not a selected operating-point measure.

Undefined denominators, class ordering and threshold are reported explicitly. The model score/probability is not clinical risk. If probability calibration is not evaluated, say so in report and app. No threshold is selected using the test partition.

## E.2 Minimum app validation matrix

| Case | Example condition | Expected behavior | Evidence |
|---|---|---|---|
| A01 Valid record | Exactly all required features, numeric finite values | Prediction and model score shown with disclaimer | Screenshot/result record |
| A02 Missing feature | One required feature absent | Reject with named missing column; no prediction | Test output |
| A03 Extra column | Unexpected field present | Reject or documented safe handling; never accidentally use as predictor | Test output |
| A04 Reordered columns | Correct names in different order | Align by approved names or reject; never positional misprediction | Test output |
| A05 Nonnumeric value | Text in a numeric feature | Clear validation message; model not called | Test output |
| A06 NaN/infinity | Nonfinite feature value | Reject unless explicit pipeline policy permits it | Test output |
| A07 Invalid CSV shape | Wrong row/column layout or missing header | Safe error; do not silently drop rows | Test output |
| A08 Batch input | Multiple valid records if supported | Stable row order and per-row result | Test output |
| A09 Model file missing | Artifact path absent | Startup/inference fails clearly; no fallback to unapproved model | Log/screenshot |
| A10 Hash mismatch | Artifact bytes differ from registered hash | Fail closed; do not serve different model | Test output |
| A11 Pipeline parity | Fixed examples through direct pipeline and app | Same class/scores within serialization/rounding tolerance approved in test spec | Parity report |
| A12 Disclaimer | Home/predict/results screens | Non-clinical notice visible before/with output | Screenshot review |

Tests use public de-identified benchmark rows or synthetic examples only. Never solicit real patient data. If the app accepts uploads, document file retention; default to in-memory processing and do not store uploaded examples.

# Appendix F — Report and presentation evidence map

| Report section | Evidence source | Primary author/reviewer |
|---|---|---|
| Title, abstract, keywords, course context | Approved title, roster, actual results only | M1 / all |
| Problem, objectives, scope | STEP-001/OS scope | M1 / all |
| Related work/context | Verified source records and concise literature matrix | M1 / M4 |
| Dataset and provenance | Dataset card, source hash, schema audit | M1 / M2 |
| EDA | STEP-008–010 notebook/figures | M1 / M4 |
| Preprocessing/features | Feature contract, cleaning decisions, Pipeline code | M2 / M4 |
| Leakage/split | Protocol and split manifest, audit G03 | M2 / M4 |
| Model lineup | Model catalog and eight run IDs | M2/M3/M5 / M4 |
| Tuning | Search spaces, folds, full trial summary, before/after table | M4 / model owners |
| Evaluation | EVAL ID, metric contract, confusion/ROC outputs | M4 / M2 |
| Explainability | XAI protocol, global/local artifacts, feature mapping | M5 / M2/M4 |
| App | Architecture, saved artifact hash, test matrix, screenshots | M5 / M2 |
| Limitations/ethics | Dataset card, evaluation design, app disclaimer | M1 / all |
| Contributions/AI use | Dated evidence logs and confirmed course rule | M1 coordinates / each member validates own row |
| References | Verified primary/official sources and access dates | Section authors / M1 checks |

Each reported number must point to one canonical evaluation record; each figure/table gets an ID and caption; each citation is checked against the cited work. In the slide deck, all five full names and IDs appear on the title slide and all full IDs appear in every slide footer as stated in the guide. Allocate speaking sections, transition lines and fallback demo before rehearsal; ensure each member can explain data, leakage, chosen model and limitations, not only their own slide.

# Appendix G — Publication-readiness audit and stop rules

The course project produces an educational classifier on a small, public benchmark. A journal paper needs an answerable research contribution and evidence proportionate to its claims. Apply the following sequential checks after STEP-046:

1. **Question check:** state one primary research question and the new knowledge expected. “Which of eight common models scores highest on WDBC?” alone is not accepted as a novelty statement without a literature-supported reason it matters.
2. **Prior-art check:** search original papers and recent systematic/methodological work; include positive, null and contradictory studies; document search dates, strings, inclusion decisions and full-text access.
3. **Data check:** explain cohort/source/provenance, outcome, predictors, missingness, eligibility and limitations. Decide whether the current dataset answers the question; if new data are needed, pause until permissions, ethics and access are documented.
4. **Design check:** define development/evaluation cohorts, nested/appropriate resampling, independent validation if needed, threshold selection, calibration, uncertainty and subgroup analyses only where sample support is defensible. No reuse of the same course holdout as a fresh confirmatory set.
5. **Bias/applicability check:** complete a PROBAST+AI-informed appraisal; identify concerns and mitigating evidence. A checklist does not repair weak data or design.
6. **Reporting check:** use applicable TRIPOD+AI items for prediction-model development/evaluation reporting. Make methods, code, data-access limits and deviations transparent.
7. **Contribution check:** compare the planned analysis with existing WDBC benchmarks. If novelty depends on clinical value, do not claim it without appropriate target data, expertise and validation.
8. **Venue check:** inspect current journal scope, article type, author instructions, indexing/category/quartile source, fees, data/code policies and editorial legitimacy on the decision date. Quartile is category- and year-dependent; record exact source/date. Do not select by quartile alone.
9. **Author check:** all authors approve contribution, order, funding/conflicts, AI use, data availability and final manuscript; corresponding author maintains records.
10. **Stop rule:** if novelty, data adequacy, validation, approvals or author agreement is unresolved, record G09 FAIL/OPEN and do not submit. Revise the study or retain the work as course output. Acceptance remains a journal decision.

# Appendix H — Session note and gate assessment templates

## H.1 Work-session note

```text
STEP / session ID:
Date and timezone:
Owner / reviewer:
Objective and prerequisite gate(s):
Input artifact IDs and hashes:
Code/config/environment revision:
Actions completed (ordered):
Outputs and locations:
Verification performed and evidence URL:
Decisions/deviations (ID, approver, reason):
Actual status: Not Started / In Progress / Completed
Blocker and recovery owner/date:
Next step and handoff recipient:
```

## H.2 Gate assessment

```text
Gate ID and date:
Assessor(s):
Exact data/split/code/model/report versions reviewed:
Criterion-by-criterion evidence links:
Unresolved issues and impact:
Outcome: PASS / FAIL / OPEN / STALE
Approval and approver:
Supersedes/invalidates:
Next dependent step authorized:
```

A gate is PASS only for the versions assessed. Any changed upstream artifact can make downstream gates STALE. Preserve earlier assessments and make a new dated assessment rather than editing history.

*End of BreastWise Project Execution Blueprint — 49 focused steps across eight stages.*
