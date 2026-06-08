# Feature Engineering Specification V3

This architecture builds upon V2 by incorporating critical recruiter psychology (dampening behavioral penalties) and explicitly extracting ownership signals to differentiate system *architects* from system *users*.

## Level A: Hard Filters (The Veto Layer)
Before continuous scoring occurs, candidates must pass Level A. Failure here results in a score of 0.

1. **The Honeypot Contradiction Filter:**
   - `IF (sum(career.duration_months) / 12) > (years_of_experience + 5)` -> **REJECT**
   - `IF ANY skill.duration_months > (years_of_experience * 12 + 24)` -> **REJECT**
2. **The Generic Irrelevance Filter:**
   - `IF Total_AI_IR_Keyword_Count == 0` -> **REJECT**
3. **The Domain Mismatch Filter:**
   - `IF Title contains ("Computer Vision" OR "Robotics") AND Title DOES NOT contain ("Search" OR "NLP")` -> **REJECT**
4. **Experience Bounds Filter:**
   - `IF years_of_experience < 3.5 OR years_of_experience > 15.0` -> **REJECT**

---

## Level B: Continuous Ranking (Technical vs. Behavioral)

### The Technical Core (75% of Final Score)

#### 1. Retrieval & Search Depth Score ($S_{retrieval}$)
* **Logic:** Sum of `duration_months` of all skills matching IR/Retrieval domains + frequency of target words in `career_history.description`.
* **Formula:** `min(1.0, (Sum of IR_Skill_Months / 60.0) * 0.5 + (IR_Keyword_Frequency_in_Career / 10) * 0.5)`
* **Weight:** 20%

#### 2. Evaluation Depth Score ($S_{eval}$)
* **Logic:** Searches for synonyms of evaluation ("A/B testing", "offline evaluation", "NDCG", "MRR", "MAP", "relevance ranking") within the `career_history.description`.
* **Formula:** `min(1.0, Eval_Keyword_Match_Count / 3.0)`
* **Weight:** 15%

#### 3. Production Deployment Score ($S_{prod}$)
* **Logic:** Scans career descriptions for scaling terms ("production", "scaled", "latency", "deployed", "users", "QPS").
* **Formula:** `min(1.0, Production_Keyword_Count / 5.0)`
* **Weight:** 10%

#### 4. Ownership & Architecture Score ($S_{own}$) -- *NEW*
* **Logic:** Differentiates an engineer who merely *used* Pinecone from one who *built* the platform. Scans career descriptions for high-agency verbs.
* **Keywords:** `led`, `architected`, `owned`, `designed`, `built from scratch`, `responsible for`, `drove`.
* **Formula:** `min(1.0, Ownership_Keyword_Count / 3.0)`
* **Weight:** 15%

#### 5. Career Stability & Progression Score ($S_{stability}$)
* **Logic:** Punish "title chasers" (job hopping < 1.5 years). Reward 3+ year tenures.
* **Formula:** `Average_Job_Duration_Months / 36.0` (Capped at 1.0).
* **Weight:** 5%

#### 6. Product Company Authenticity ($S_{dna}$)
* **Logic:** Calculates the percentage of total career months spent at non-service companies.
* **Formula:** `Total_Months_in_Product_Companies / Total_Career_Months`
* **Weight:** 10%

**Total Technical Score Calculation:**
$S_{tech} = 0.20(S_{retrieval}) + 0.15(S_{eval}) + 0.10(S_{prod}) + 0.15(S_{own}) + 0.05(S_{stability}) + 0.10(S_{dna})$
*(Note: Weights sum to 0.75 or are normalized to 1.0 before the final blend)*

---

### The Behavioral Component (25% of Final Score)

Rather than acting as a dangerous veto multiplier, behavioral signals contribute additively to give a strong boost to available candidates without destroying an elite technical profile who happens to have a 90-day notice period.

#### Behavioral Score ($S_{behavior}$)
* **Components:** Notice Period, Response Rate, Recency of Activity.
* **Formula:** 
  - `NP_Score = max(0, 1 - (Notice_Period_Days / 90))`
  - `Recency_Score = max(0, 1 - (Days_Since_Active / 90))`
  - $S_{behavior} = (0.4 \times NP\_Score) + (0.3 \times Response\_Rate) + (0.3 \times Recency\_Score)$

---

## Final V3 Scoring Formula

The additive formulation ensures that a 99th-percentile engineer with bad availability will still comfortably beat a 50th-percentile engineer who is available tomorrow, reflecting real-world recruiting psychology.

$Final\_Score = Level\_A\_Filter \times \Big( 0.75(S_{tech\_normalized}) + 0.25(S_{behavior}) \Big)$

### Simulation (The Danger Averted)
Let's revisit the user's hypothetical:
**Candidate A (The 10x Engineer):** 
Perfect technical score ($1.0$). Terrible notice period (90 days, so $S_{behavior} \approx 0.3$).
- V1/V2 (Multiplier): $1.0 \times 0.3 = 0.3$ (Devastating drop).
- V3 (Additive): $(0.75 \times 1.0) + (0.25 \times 0.3) = 0.75 + 0.075 = \mathbf{0.825}$.

**Candidate B (The Mediocre Engineer):** 
Average technical score ($0.5$). Perfect availability ($S_{behavior} = 1.0$).
- V1/V2 (Multiplier): $0.5 \times 1.0 = 0.5$ (Outranks A in extreme multiplier cases).
- V3 (Additive): $(0.75 \times 0.5) + (0.25 \times 1.0) = 0.375 + 0.25 = \mathbf{0.625}$.

**Verdict:** V3 correctly preserves Candidate A's superiority. A brilliant engineer with a 90-day notice period will still outrank an average engineer ready to start tomorrow. 
