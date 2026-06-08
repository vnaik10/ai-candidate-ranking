# Candidate Population Intelligence Report

## 1. Overview
The `candidates.jsonl` dataset contains exactly 100,000 candidate profiles. This report breaks down the macro-level structure of the candidate pool to identify what separates the top 1% from the remaining 99%.

## 2. Dataset-Wide Statistics

### Experience & Demographics
- **Total Candidates:** 100,000
- **Years of Experience (YoE):** Average: 7.17 | Median: 6.8 | 90th Percentile: 13.0
- **Geographic Distribution:** Heavily India-based (75.1%), followed by USA (10.0%), Australia (2.6%), Canada (2.5%), and the UK (2.5%).

### Top Job Titles (Generic Dominance)
The pool is predominantly generic, non-AI roles. The top 5 titles are:
1. Business Analyst (5,833)
2. HR Manager (5,830)
3. Mechanical Engineer (5,791)
4. Accountant (5,764)
5. Project Manager (5,754)
*Insight: True AI/ML roles are a distinct minority in this dataset.*

### Top Companies
The dataset includes heavy representation from major IT services firms and simulated/fictional product companies:
- Infosys (7,590)
- Wayne Enterprises (7,571)
- Wipro (7,566)
- Initech (7,528)
- Pied Piper (7,500)

### Top Skills & Education
- **Top Skills:** HTML, Databricks, Redux, Terraform, Angular, Figma. (Mostly Web Dev / Cloud infra).
- **Top Education:** Information Technology, Data Science, Machine Learning, Computer Engineering, Artificial Intelligence.

### Behavioral Signals (Crucial for Ranking)
- **Notice Period:** Average is **87.4 days**. (Finding someone with <30 days is rare and highly valuable).
- **Recruiter Response Rate:** Average is **43.7%**.
- **Platform Activity:** 
  - Over 90 days ago: 61,497 (Inactive majority)
  - 31-90 days ago: 28,315
  - 8-30 days ago: 10,188
  - 0-7 days ago: 0
*Insight: Over 61% of the candidate pool is inactive. A perfect resume with 90+ days of inactivity is a likely trap.*

## 3. JD Coverage (Hard Requirement Saturation)
Checking the 100,000 pool against the explicit Job Description requirements:

| JD Requirement | Match Count | Pool Percentage |
| :--- | :--- | :--- |
| **Product Company Experience** | 91,009 | 91.01% |
| **Retrieval / Search Systems** | 30,372 | 30.37% |
| **Open Source Activity (Score > 20)** | 22,846 | 22.85% |
| **Vector Databases (Pinecone, FAISS, etc.)** | 12,865 | 12.86% |
| **Embeddings (Sentence-Transformers, etc.)** | 5,177 | 5.18% |
| **NLP Specialization** | 2,275 | 2.27% |
| **Evaluation Metrics (NDCG, MRR, MAP)** | **100** | **0.10%** |
| **HR-Tech Experience** | 0 | 0.00% |

*Key Insight: Evaluation framework knowledge (NDCG/MRR) is the ultimate bottleneck. Only exactly 100 candidates possess this explicit keyword, strongly suggesting these 100 are the intended top-tier subset or "golden candidates."*

## 4. Candidate Segments
Based on heuristic tagging, the engineering/data population breaks down into:

- **Segment E (Generic SWE / Non-Tech):** ~54,477 candidates. The vast majority.
- **Segment B (LLM Engineers):** ~24,161 candidates. High keyword matches for GPT, LLM, LangChain. (The JD explicitly warned against these being the primary match).
- **Segment C (CV / Robotics):** ~11,092 candidates. Explicitly disqualified by the JD.
- **Segment A (Strong Retrieval Engineers):** ~7,317 candidates. (Has Retrieval AND Vector DB/Embeddings experience). The true target pool.
- **Segment D (Data Scientists):** ~2,953 candidates.

## 5. Honeypot Analysis
Simple heuristic checks (e.g., >50 years of experience, or >30 skills) returned 0 hits, meaning the ~80 honeypots mentioned in the documentation are constructed much more subtly. 

Given the rules, honeypots are likely:
1. **Mathematical Contradictions:** E.g., `duration_months` for a single skill vastly exceeding their total `years_of_experience`.
2. **Company Contradictions:** Claiming 8 years of experience at a company (like "OpenAI" or a fictional startup) that has only existed for 3 years.
3. **Keyword Stuffers:** Candidates in the "Generic SWE" or "LLM" segments who have 15 "expert" AI skills but titles like "HR Manager" or "Mechanical Engineer" (which we noted are in the top overall titles).

## 6. Shortlist Analysis (The Funnel)
If we apply hard filter heuristics (4-12 YoE + Embeddings/VectorDB + Retrieval + Product Company + Notice Period <= 30 days):

- **Top 1000 Candidates:** There are ~6,513 candidates who meet at least 4 out of 5 of the strict hard constraints.
- **Top 100 Candidates:** There are exactly **613 candidates** who perfectly hit all 5 strict hard constraints (Experience, Vector DB, Retrieval, Product Company, Immediate Notice Period). 
- **Top 10 Candidates:** To find the absolute top 10, we must filter those 613 candidates by the ultimate rarity: **Evaluation Metrics (NDCG/MAP)**. Since only 100 candidates in the entire pool possess evaluation metric experience, the Top 10 will exclusively be individuals who possess that knowledge AND have pristine behavioral scores (high response rate, recent activity).

## Conclusion: The Path to the Top 1%
To build the ranking system, we don't need a heavy LLM to score 100,000 candidates. The strategy should be:
1. **Filter the 99%:** Instantly down-rank the 54K generic candidates, the 11K CV/Robotics engineers, and the heavy IT-services/long-notice-period candidates.
2. **Isolate the 1%:** Use BM25/Vector search to extract the ~1,000 engineers with real Retrieval, Vector DB, and Evaluation Metric experience.
3. **Score the 1%:** Heavily penalize honeypots (check skill duration vs. experience). Multiply their semantic score by their `redrob_signals` (activity recency, response rate, notice period).
4. **Rank the Top 100:** The final 100 should be the ones with the deepest semantic alignment to the JD, completely clear of honeypot traps, with the best availability.
