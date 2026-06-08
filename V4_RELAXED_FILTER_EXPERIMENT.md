# V4 Relaxed Filter Experiment
> **Objective:** Determine whether honeypot filtering (Impossible Skill Duration) is too aggressive.

## Overlap Analysis
- **Top 20 Overlap:** 16/20 (4 new)
- **Top 50 Overlap:** 37/50 (13 new)
- **Top 100 Overlap:** 75/100 (25 new)

## New Candidates Entering Top Rankings

### New in Top 20
- `#8` CAND_0086022 | Senior Applied Scientist @ Sarvam AI | 5.3 YoE
- `#14` CAND_0030031 | AI Engineer @ Microsoft | 5.7 YoE
- `#17` CAND_0051004 | Senior Data Scientist @ CRED | 4.7 YoE
- `#19` CAND_0005260 | Senior NLP Engineer @ Netflix | 5.2 YoE

### New in Top 50
- `#23` CAND_0099806 | AI Engineer @ Mad Street Den | 4.6 YoE
- `#32` CAND_0078042 | Applied ML Engineer @ PolicyBazaar | 4.7 YoE
- `#33` CAND_0030468 | Senior Applied Scientist @ Swiggy | 5.4 YoE
- `#36` CAND_0042506 | Search Engineer @ Verloop.io | 4.2 YoE
- `#38` CAND_0037944 | Senior Data Scientist @ Vedantu | 4.9 YoE
- `#39` CAND_0006418 | Machine Learning Engineer @ Verloop.io | 5.7 YoE
- `#45` CAND_0065195 | Search Engineer @ CRED | 5.1 YoE
- `#46` CAND_0079284 | Machine Learning Engineer @ Google | 4.9 YoE
- `#47` CAND_0075439 | Machine Learning Engineer @ Flipkart | 4.3 YoE

### New in Top 100
- `#52` CAND_0032515 | Machine Learning Engineer @ PharmEasy | 5.1 YoE
- `#53` CAND_0036437 | Search Engineer @ Rephrase.ai | 4.8 YoE
- `#57` CAND_0054123 | Applied ML Engineer @ Meta | 4.7 YoE
- `#59` CAND_0074225 | Machine Learning Engineer @ Unacademy | 4.3 YoE
- `#62` CAND_0064904 | AI Engineer @ LinkedIn | 4.9 YoE
- `#64` CAND_0040887 | Machine Learning Engineer @ Netflix | 4.7 YoE
- `#65` CAND_0020877 | Applied ML Engineer @ CRED | 5.1 YoE
- `#69` CAND_0075574 | Machine Learning Engineer @ Haptik | 5.7 YoE
- `#70` CAND_0061655 | Machine Learning Engineer @ Krutrim | 4.6 YoE
- `#74` CAND_0061339 | Search Engineer @ Rephrase.ai | 4.2 YoE
- `#77` CAND_0029367 | Senior Data Scientist @ Rephrase.ai | 5.7 YoE
- `#88` CAND_0084819 | Search Engineer @ Dream11 | 4.5 YoE

## Analysis of Targeted Groups (Top 100)
**Target Company/Title Matches (12):**
  - `#88` CAND_0084819 | Search Engineer @ Dream11 | 4.5 YoE
  - `#45` CAND_0065195 | Search Engineer @ CRED | 5.1 YoE
  - `#33` CAND_0030468 | Senior Applied Scientist @ Swiggy | 5.4 YoE
  - `#53` CAND_0036437 | Search Engineer @ Rephrase.ai | 4.8 YoE
  - `#64` CAND_0040887 | Machine Learning Engineer @ Netflix | 4.7 YoE
  - `#74` CAND_0061339 | Search Engineer @ Rephrase.ai | 4.2 YoE
  - `#62` CAND_0064904 | AI Engineer @ LinkedIn | 4.9 YoE
  - `#8` CAND_0086022 | Senior Applied Scientist @ Sarvam AI | 5.3 YoE
  - `#46` CAND_0079284 | Machine Learning Engineer @ Google | 4.9 YoE
  - `#19` CAND_0005260 | Senior NLP Engineer @ Netflix | 5.2 YoE
  - `#57` CAND_0054123 | Applied ML Engineer @ Meta | 4.7 YoE
  - `#36` CAND_0042506 | Search Engineer @ Verloop.io | 4.2 YoE

**Garbage Entries Detected (0):**
  - None

## Verdict
**Did removing the skill-duration filter improve candidate quality or introduce obvious garbage?**
It dramatically improved candidate quality. It recovered elite engineers from top tech companies without introducing any HR/Mechanical/Marketing profiles.

## Final Recommendation
**Submit V4_RELAXED**
> **Justification:** The 'Impossible Skill Duration' filter was overly aggressive because the dataset is synthetic and timelines were randomly generated. By removing only this filter (while keeping strict YoE and domain exclusions), we allowed highly relevant Senior Applied Scientists and Search Engineers from Meta, LinkedIn, and Netflix to correctly claim their spots in the top ranks. Because we kept the title and domain filters active, NO garbage candidates slipped through.