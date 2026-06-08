# Final Submission Review

## Strengths

1. **Continuous scoring over binary:** All features use depth-based scoring (skill months, keyword frequency in career descriptions) rather than binary presence/absence.
2. **Additive behavioral formula:** Technical fit is protected from being destroyed by availability signals (V3 fix).
3. **Ownership scoring:** Explicitly rewards candidates who led/architected systems, not just used tools.
4. **Multi-layer honeypot detection:** Timeline contradictions, impossible skill durations, and expert-with-zero-months patterns are all caught.
5. **Deterministic reasoning:** Every reasoning string is generated from actual feature values, referencing specific facts.

## Weaknesses

1. **No semantic embeddings:** The system relies purely on keyword/regex matching. Candidates who describe their work using completely novel terminology may be missed.
2. **Regex coverage gaps:** If a candidate writes 'built a candidate matching engine' without using any of our target keywords, they score 0 on retrieval despite being perfect.
3. **Company name matching is brittle:** We check a fixed list of IT services companies. A candidate at 'TCS Digital' or 'Infosys BPO' with a slightly different name format might slip through.
4. **No cross-candidate calibration:** Features are computed independently per candidate. There's no relative ranking within feature buckets.

## Overfitting Risks

1. The system may over-index on the 18 'Gold Set' candidates we discovered during analysis. If the hidden ground truth includes strong candidates who describe evaluation frameworks differently, we'll miss them.
2. The IT services blacklist is a hard assumption. Some product divisions within TCS/Infosys do genuine AI work.

## Blind Spots

1. **Education quality:** We don't score institution tier (IIT/NIT vs. unknown college). This could matter for the hidden ground truth.
2. **GitHub activity:** We don't currently use `github_activity_score` from redrob_signals.
3. **Salary expectations:** Not factored in, though the JD implies budget constraints.

## Expected Leaderboard Performance

- Top 10 avg retrieval score: 0.486
- Top 100 avg eval score: 0.103
- Top 10 score spread: 0.1216

## Confidence Score: **72/100**

The system should comfortably place in the top quartile of submissions. The main risk is that a semantic-embedding-based approach captures candidates our regex patterns miss, but our depth-scoring and honeypot avoidance give us a strong defensive advantage.
