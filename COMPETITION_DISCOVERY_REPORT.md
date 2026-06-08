# Competition Discovery & Reconnaissance Report

## 1. Folder Structure
The competition bundle contains the following root structure:
- `README.docx`: Welcome guide, rules, and overview.
- `job_description.docx`: The target Job Description (Senior AI Engineer) against which candidates must be ranked.
- `redrob_signals_doc.docx`: Documentation detailing 23 behavioral signals that indicate candidate reliability.
- `submission_spec.docx`: Detailed submission rules, constraints (5 mins, CPU-only, 16GB), and evaluation metrics.
- `candidates.jsonl`: The primary dataset pool of 100,000 candidates (~465 MB uncompressed).
- `sample_candidates.json`: A subset of 50 candidates for quick schema inspection.
- `candidate_schema.json`: Strict JSON schema describing every field in the candidate records.
- `sample_submission.csv`: Example formatting of the expected 100-row ranking output.
- `submission_metadata_template.yaml`: Metadata required when uploading a submission.
- `validate_submission.py`: A local Python script to validate submission CSV format.

## 2. Dataset Inventory

### `candidates.jsonl`
- **Shape:** 100,000 rows, 8 top-level columns.
- **Data Types & Format:** JSON Lines format. Each line is a deeply nested JSON object.
- **Top-level Columns:** `candidate_id`, `profile`, `career_history`, `education`, `skills`, `certifications`, `languages`, `redrob_signals`.
- **Missing Values:** Based on the schema, `candidate_id`, `profile`, `career_history`, `education`, `skills`, and `redrob_signals` are strictly required (0 missing). `certifications` and `languages` may be empty lists or omitted.
- **Primary Key:** `candidate_id` (Format: `CAND_XXXXXXX`)
- **Foreign Keys / Joins:** None. The dataset is fully denormalized. Each line represents a complete candidate profile.

## 3. Data Dictionary
The `candidates.jsonl` file holds deeply nested documents. Based on the schema and sample rows, the key entities are:

1. **`candidate_id`**: Unique string identifier.
2. **`profile`**: Metadata about the candidate (e.g., `anonymized_name`, `headline`, `summary`, `location`, `years_of_experience`, `current_title`, `current_company`).
3. **`career_history`**: Array of past and current roles (`company`, `title`, `start_date`, `duration_months`, `description`).
4. **`education`**: Array of degrees (`institution`, `degree`, `field_of_study`, `tier`).
5. **`skills`**: Array of technical/soft skills (`name`, `proficiency`, `endorsements`, `duration_months`).
6. **`redrob_signals`**: A crucial object containing 23 behavioral/engagement metrics:
   - *Activity*: `last_active_date`, `profile_views_received_30d`, `search_appearance_30d`.
   - *Responsiveness*: `recruiter_response_rate`, `avg_response_time_hours`, `interview_completion_rate`.
   - *Expectations*: `notice_period_days`, `expected_salary_range_inr_lpa`.

## 4. Target & Task Variable Analysis
- **Task Type:** Ranking / Information Retrieval. This is not a standard classification or regression task.
- **Prediction Target:** There is no explicit labeled target variable provided in the data. The objective is to rank the top 100 most relevant candidates for a *single specific job description* (Senior AI Engineer).
- **Labels / Ground Truth:** Hidden. There are no training labels. It is an unsupervised/heuristic matching task evaluated against a hidden ground truth maintained by the organizers.
- **Train/Test Splits:** No split. The entire 100K pool is the inference set. 

## 5. Submission Format Analysis
- **What must be submitted:** A CSV containing exactly 100 rows (plus header).
- **Columns:**
  - `candidate_id`: The ID of the candidate.
  - `rank`: Integer from 1 to 100 (1 is best).
  - `score`: Float representing your internal model's confidence. Must be monotonically decreasing with rank.
  - `reasoning`: A 1-2 sentence generated explanation justifying the rank. Highly scrutinized during manual review.
- **Output implications:** The problem effectively boils down to finding the top 0.1% of the dataset and sorting them accurately.

## 6. Evaluation Analysis
- **Metrics:**
  - NDCG@10 (50% weight): Heavily rewards putting the absolute best fits in the top 10.
  - NDCG@50 (30% weight)
  - MAP (15% weight)
  - Precision@10 (5% weight)
- **Constraints:** 
  - Execution must take **≤ 5 minutes on a CPU** with **16GB RAM**. 
  - **No network calls** (no external LLM APIs during ranking).
- **Honeypot Traps:** The dataset explicitly contains ~80 "honeypots" with impossible profiles (e.g., 8 years of experience at a 3-year-old company, or "expert" in 10 skills with 0 years used). If >10% of your top 100 are honeypots, you are disqualified.

## 7. Reverse Engineering the Competition 
### The Actual Business Problem
The organizers (Redrob AI) are trying to solve the "keyword matching failure" in recruiting. Standard ATS systems rank candidates based on keyword frequency, missing great candidates whose resumes use different terminologies and heavily favoring candidates who "keyword stuff" their profiles. They want an intelligent semantic search system that captures *context* and *capability*, heavily modified by real-world *availability* and *engagement* signals.

### Available Signals & Noise
- **High-Signal Information:** 
  - Job Title progressions and tenure in `career_history`.
  - Alignment between `career_history.description` and the target JD.
  - Behavioral reliability (`redrob_signals.recruiter_response_rate`, `redrob_signals.last_active_date`).
  - True AI Engineering experience (building retrieval/ranking systems) vs. just listing LangChain/OpenAI as skills.
- **High-Noise / Trap Information:** 
  - `skills` array. Candidates with 50 AI skills but a "Marketing Manager" title are traps.
  - Candidates with perfect semantic alignment but terrible behavioral signals (e.g., haven't logged in for a year).

## 8. Recommended Next Steps (Modeling Strategy)
1. **Pre-computation (Offline Phase):** Since ranking must happen in under 5 minutes on CPU, large models cannot be run online. Extract JD embeddings and candidate profile embeddings entirely offline using a fast, high-quality embedding model (e.g., BGE, E5, MiniLM) and store them as lightweight vector indices (like FAISS) or pre-computed dense matrices.
2. **Two-Stage Ranking Pipeline:**
   - *Stage 1 (Retrieval):* Fast vector similarity search (JD vs. Candidates) or BM25 to narrow 100,000 down to the top 1,000.
   - *Stage 2 (Re-ranking):* Apply heuristic penalties to filter honeypots (e.g., sanity-check years of experience vs. skill durations). Apply behavioral multipliers based on `redrob_signals` to boost active candidates and penalize inactive/unresponsive ones.
3. **Reasoning Generation:** The `reasoning` column can be generated offline using a local, quantized LLM (e.g., Llama-3-8B-Instruct or Mistral via vLLM/Ollama) specifically for the top 100 candidates, since running an LLM for 100 candidates locally might just squeeze into a 5-minute CPU window if heavily optimized, OR it could be templated dynamically based on the highest-scoring extracted features.
4. **Honeypot Detection Heuristics:** Write explicit rules to flag impossible mathematical contradictions in candidate profiles (e.g., total experience > age, or skill experience > company lifespan) to avoid disqualification.
