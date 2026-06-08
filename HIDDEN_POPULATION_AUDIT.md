# Hidden Population Audit
> **Objective:** Determine whether hard filters eliminated elite candidates.

**Filtered Candidates Analyzed:** 24813

## Top Candidates Blocked by Hard Filters

Found **45 candidates** who mathematically scored high enough to enter the Top 100 but were blocked by hard filters.

| Candidate ID | Title | Company | YoE | Unfiltered Score | Filter Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CAND_0030468 | Senior Applied Scientist | Swiggy | 5.4 | 0.5900 | Impossible Skill Duration |
| CAND_0086022 | Senior Applied Scientist | Sarvam AI | 5.3 | 0.6830 | Impossible Skill Duration |
| CAND_0064904 | AI Engineer | LinkedIn | 4.9 | 0.5544 | Impossible Skill Duration |
| CAND_0030031 | AI Engineer | Microsoft | 5.7 | 0.6496 | Impossible Skill Duration |
| CAND_0005260 | Senior NLP Engineer | Netflix | 5.2 | 0.6327 | Impossible Skill Duration |
| CAND_0055992 | AI Engineer | CRED | 16.9 | 0.5526 | Too Senior (>15.0 YoE) |
| CAND_0058575 | AI Engineer | Krutrim | 5.8 | 0.5107 | Impossible Skill Duration |
| CAND_0093547 | Senior Machine Learning Engineer | PhonePe | 2.9 | 0.5676 | Impossible Skill Duration, Too Junior (<3.5 YoE) |
| CAND_0039754 | Senior Applied Scientist | Meta | 16.2 | 0.7011 | Too Senior (>15.0 YoE) |
| CAND_0074225 | Machine Learning Engineer | Unacademy | 4.3 | 0.5582 | Impossible Skill Duration |
| CAND_0054123 | Applied ML Engineer | Meta | 4.7 | 0.5584 | Impossible Skill Duration |
| CAND_0061339 | Search Engineer | Rephrase.ai | 4.2 | 0.5433 | Impossible Skill Duration |
| CAND_0084819 | Search Engineer | Dream11 | 4.5 | 0.5279 | Impossible Skill Duration |
| CAND_0056881 | Machine Learning Engineer | Zomato | 4.5 | 0.4790 | Impossible Skill Duration |
| CAND_0051004 | Senior Data Scientist | CRED | 4.7 | 0.6377 | Impossible Skill Duration |
| CAND_0079064 | Senior Data Scientist | Niramai | 5.2 | 0.5156 | Impossible Skill Duration |
| CAND_0042506 | Search Engineer | Verloop.io | 4.2 | 0.5858 | Impossible Skill Duration |
| CAND_0001610 | Machine Learning Engineer | Dream11 | 3.0 | 0.4840 | Impossible Skill Duration, Too Junior (<3.5 YoE) |
| CAND_0032515 | Machine Learning Engineer | PharmEasy | 5.1 | 0.5674 | Impossible Skill Duration |
| CAND_0020877 | Applied ML Engineer | CRED | 5.1 | 0.5527 | Impossible Skill Duration |
| CAND_0079284 | Machine Learning Engineer | Google | 4.9 | 0.5728 | Impossible Skill Duration |
| CAND_0075439 | Machine Learning Engineer | Flipkart | 4.3 | 0.5719 | Impossible Skill Duration |
| CAND_0078042 | Applied ML Engineer | PolicyBazaar | 4.7 | 0.5902 | Impossible Skill Duration |
| CAND_0029367 | Senior Data Scientist | Rephrase.ai | 5.7 | 0.5426 | Impossible Skill Duration |
| CAND_0037944 | Senior Data Scientist | Vedantu | 4.9 | 0.5849 | Impossible Skill Duration |
| CAND_0099806 | AI Engineer | Mad Street Den | 4.6 | 0.6167 | Impossible Skill Duration |
| CAND_0040887 | Machine Learning Engineer | Netflix | 4.7 | 0.5528 | Impossible Skill Duration |
| CAND_0009024 | Search Engineer | Google | 5.2 | 0.5032 | Impossible Skill Duration |
| CAND_0091534 | AI Engineer | Flipkart | 16.6 | 0.5943 | Too Senior (>15.0 YoE) |
| CAND_0095619 | NLP Engineer | Nykaa | 15.6 | 0.5229 | Too Senior (>15.0 YoE) |
| CAND_0075574 | Machine Learning Engineer | Haptik | 5.7 | 0.5498 | Impossible Skill Duration |
| CAND_0006418 | Machine Learning Engineer | Verloop.io | 5.7 | 0.5845 | Impossible Skill Duration |
| CAND_0012957 | Search Engineer | Razorpay | 4.9 | 0.4868 | Impossible Skill Duration |
| CAND_0064270 | Applied ML Engineer | Verloop.io | 4.2 | 0.5098 | Impossible Skill Duration |
| CAND_0036437 | Search Engineer | Rephrase.ai | 4.8 | 0.5660 | Impossible Skill Duration |
| CAND_0013613 | Machine Learning Engineer | Adobe | 4.7 | 0.4752 | Impossible Skill Duration |
| CAND_0039521 | Search Engineer | Salesforce | 3.0 | 0.5024 | Impossible Skill Duration, Too Junior (<3.5 YoE) |
| CAND_0030348 | Machine Learning Engineer | BYJU'S | 4.5 | 0.5079 | Impossible Skill Duration |
| CAND_0093331 | NLP Engineer | Genpact AI | 16.1 | 0.5630 | Too Senior (>15.0 YoE) |
| CAND_0051615 | Search Engineer | Meta | 4.6 | 0.4861 | Impossible Skill Duration |
| CAND_0037000 | Search Engineer | Unacademy | 2.7 | 0.6021 | Impossible Skill Duration, Too Junior (<3.5 YoE) |
| CAND_0061655 | Machine Learning Engineer | Krutrim | 4.6 | 0.5476 | Impossible Skill Duration |
| CAND_0065195 | Search Engineer | CRED | 5.1 | 0.5728 | Impossible Skill Duration |
| CAND_0019480 | NLP Engineer | Meesho | 2.8 | 0.5019 | Impossible Skill Duration, Too Junior (<3.5 YoE) |
| CAND_0020708 | Search Engineer | PolicyBazaar | 4.2 | 0.4861 | Impossible Skill Duration |

## Categorization

### True Negatives (10)
Candidates correctly blocked because they violate strict non-negotiable JD requirements (e.g., YoE outside 3.5-15 bounds or CV/Robotics exclusivity).

### False Negatives (35)
Candidates with elite semantic, retrieval, and production signals blocked due to potentially aggressive heuristic filters (e.g., synthetic timeline artifacts).

### Potential Leaderboard Risks (35)
If the competition metric does not enforce these hard filters, these candidates represent lost leaderboard points.

## Final Verdict
**Did our filters accidentally remove elite retrieval/search engineers?**

**YES.**

We blocked 35 highly qualified engineers who possess strong semantic alignment, retrieval evidence, and production scale.

**Estimated Leaderboard Impact:** Potentially losing 20% of our Top 20 precision if the ground truth does not enforce 'Honeypot' logic.