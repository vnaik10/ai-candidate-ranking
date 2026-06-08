# Authenticity Audit Report

> This report evaluates the Top 100 candidates for logical inconsistencies,
> synthetic profile markers, and realism failures that an experienced recruiter
> would detect but a keyword-based pipeline would miss.

## Top 25 Most Suspicious Candidates

| Rank | ID | Title | Company | Auth Score | Primary Issue | Confidence | Recommended Penalty |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 87 | CAND_0070202 | Machine Learning Engineer | BYJU'S | 0.68 | Incoherent skill combination: {'robotics', 'vdb', 'cv'}; Suspiciously broad: 5 d... | LOW | Light (-5% to -15%) |
| 93 | CAND_0073504 | Junior ML Engineer | PolicyBazaar | 0.72 | Incoherent skill combination: {'robotics', 'vdb', 'cv'}; Suspiciously broad: 5 d... | LOW | Light (-5% to -15%) |
| 3 | CAND_0077337 | Staff Machine Learning Engineer | Paytm | 0.73 | pgvector claimed 75m, max realistic 66m (launched 2021); RAG claimed 77m, max re... | LOW | Light (-5% to -15%) |
| 44 | CAND_0041611 | Staff Machine Learning Engineer | Locobuzz | 0.73 | LangChain claimed 90m, max realistic 54m (launched 2022) | LOW | Light (-5% to -15%) |
| 61 | CAND_0013536 | Applied ML Engineer | Haptik | 0.73 | LlamaIndex claimed 82m, max realistic 54m (launched 2022) | LOW | Light (-5% to -15%) |
| 80 | CAND_0053605 | Senior Software Engineer (ML) | Verloop.io | 0.75 | Unknown company or title; cannot verify | LOW | Light (-5% to -15%) |
| 8 | CAND_0011687 | Senior NLP Engineer | Niramai | 0.76 | OpenSearch claimed 92m, max realistic 66m (launched 2021); LangChain claimed 63m... | LOW | Light (-5% to -15%) |
| 45 | CAND_0070398 | Machine Learning Engineer | Genpact AI | 0.76 | RAG claimed 72m, max realistic 42m (launched 2023) | LOW | Light (-5% to -15%) |
| 4 | CAND_0002025 | Senior AI Engineer | Apple | 0.76 | LangChain claimed 84m, max realistic 54m (launched 2022) | LOW | Light (-5% to -15%) |
| 21 | CAND_0045250 | Applied ML Engineer | Rephrase.ai | 0.77 | LangChain claimed 85m, max realistic 54m (launched 2022); Qdrant claimed 76m, ma... | LOW | Light (-5% to -15%) |
| 24 | CAND_0008425 | Senior NLP Engineer | Ola | 0.77 | Qdrant claimed 92m, max realistic 66m (launched 2021) | LOW | Light (-5% to -15%) |
| 31 | CAND_0098846 | AI Engineer | upGrad | 0.77 | Qdrant claimed 95m, max realistic 66m (launched 2021) | LOW | Light (-5% to -15%) |
| 35 | CAND_0076163 | NLP Engineer | Ola | 0.77 | LangChain claimed 75m, max realistic 54m (launched 2022); LlamaIndex claimed 86m... | LOW | Light (-5% to -15%) |
| 36 | CAND_0058688 | AI Engineer | Vedantu | 0.77 | LlamaIndex claimed 91m, max realistic 54m (launched 2022) | LOW | Light (-5% to -15%) |
| 41 | CAND_0005538 | Senior AI Engineer | Adobe | 0.77 | pgvector claimed 91m, max realistic 66m (launched 2021) | LOW | Light (-5% to -15%) |
| 46 | CAND_0044222 | AI Engineer | PolicyBazaar | 0.77 | LlamaIndex claimed 82m, max realistic 54m (launched 2022); OpenSearch claimed 75... | LOW | Light (-5% to -15%) |
| 60 | CAND_0057563 | NLP Engineer | Locobuzz | 0.77 | RAG claimed 68m, max realistic 42m (launched 2023); OpenSearch claimed 94m, max ... | LOW | Light (-5% to -15%) |
| 65 | CAND_0099401 | NLP Engineer | Dream11 | 0.77 | LlamaIndex claimed 81m, max realistic 54m (launched 2022) | LOW | Light (-5% to -15%) |
| 71 | CAND_0096172 | NLP Engineer | Krutrim | 0.77 | LangChain claimed 79m, max realistic 54m (launched 2022); RAG claimed 58m, max r... | LOW | Light (-5% to -15%) |
| 95 | CAND_0091909 | Machine Learning Engineer | Rephrase.ai | 0.77 | Pinecone claimed 84m, max realistic 66m (launched 2021); LangChain claimed 92m, ... | LOW | Light (-5% to -15%) |
| 9 | CAND_0079387 | AI Engineer | Microsoft | 0.77 | OpenSearch claimed 87m, max realistic 66m (launched 2021) | LOW | Light (-5% to -15%) |
| 51 | CAND_0083307 | Search Engineer | CRED | 0.78 | Weak alignment between search engineer and cred | LOW | Light (-5% to -15%) |
| 68 | CAND_0095528 | Senior Data Scientist | Netflix | 0.79 | RAG claimed 63m, max realistic 42m (launched 2023) | LOW | Light (-5% to -15%) |
| 15 | CAND_0068811 | Applied ML Engineer | Freshworks | 0.80 | Pinecone claimed 86m, max realistic 66m (launched 2021) | LOW | Light (-5% to -15%) |
| 1 | CAND_0018499 | Senior Machine Learning Engineer | Zomato | 0.80 | RAG claimed 94m, max realistic 42m (launched 2023) | LOW | Light (-5% to -15%) |

---

## Detailed Suspicious Candidate Profiles

### Rank 87: CAND_0070202 — Authenticity 0.68
- **Title:** Machine Learning Engineer
- **Company:** BYJU'S
- **YoE:** 5.1
- **Original Score:** 0.4910
- **Adjusted Score:** 0.4436
- **New Rank:** 100

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ⚠️ 0.50 | Unknown company or title; cannot verify |
| tech_timeline | ⚠️ 0.67 | RAG claimed 50m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ❌ 0.30 | Incoherent skill combination: {'robotics', 'vdb', 'cv'}; Suspiciously broad: 5 different skill clusters ({'robotics', 'vdb', 'cv', 'ir', 'nlp'}) |
| company_reputation | ⚠️ 0.50 | Unknown company: byju's |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 93: CAND_0073504 — Authenticity 0.72
- **Title:** Junior ML Engineer
- **Company:** PolicyBazaar
- **YoE:** 6.6
- **Original Score:** 0.4842
- **Adjusted Score:** 0.4442
- **New Rank:** 99

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ⚠️ 0.50 | Unknown company or title; cannot verify |
| tech_timeline | ✅ 1.00 | No timeline violations |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ❌ 0.30 | Incoherent skill combination: {'robotics', 'vdb', 'cv'}; Suspiciously broad: 5 different skill clusters ({'robotics', 'vdb', 'cv', 'web', 'ir'}) |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ⚠️ 0.60 | Junior title with 6.6 YoE — stagnant or mislabeled |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 3: CAND_0077337 — Authenticity 0.73
- **Title:** Staff Machine Learning Engineer
- **Company:** Paytm
- **YoE:** 7.0
- **Original Score:** 0.7388
- **Adjusted Score:** 0.6795
- **New Rank:** 5

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: staff machine learning engineer at paytm (overlap: {'recommendation', 'ai'}) |
| tech_timeline | ❌ 0.00 | pgvector claimed 75m, max realistic 66m (launched 2021); RAG claimed 77m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 4 vector databases (unusual) |

### Rank 44: CAND_0041611 — Authenticity 0.73
- **Title:** Staff Machine Learning Engineer
- **Company:** Locobuzz
- **YoE:** 6.4
- **Original Score:** 0.5555
- **Adjusted Score:** 0.5109
- **New Rank:** 64

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: staff machine learning engineer at locobuzz (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | LangChain claimed 90m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 4 vector databases (unusual) |

### Rank 61: CAND_0013536 — Authenticity 0.73
- **Title:** Applied ML Engineer
- **Company:** Haptik
- **YoE:** 14.1
- **Original Score:** 0.5326
- **Adjusted Score:** 0.4899
- **New Rank:** 77

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: applied ml engineer at haptik (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | LlamaIndex claimed 82m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 4 vector databases (unusual) |

### Rank 80: CAND_0053605 — Authenticity 0.75
- **Title:** Senior Software Engineer (ML)
- **Company:** Verloop.io
- **YoE:** 6.9
- **Original Score:** 0.5070
- **Adjusted Score:** 0.4690
- **New Rank:** 90

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ⚠️ 0.50 | Unknown company or title; cannot verify |
| tech_timeline | ⚠️ 0.50 | RAG claimed 54m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.50 | Unknown company: verloop.io |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 8: CAND_0011687 — Authenticity 0.76
- **Title:** Senior NLP Engineer
- **Company:** Niramai
- **YoE:** 7.8
- **Original Score:** 0.6760
- **Adjusted Score:** 0.6273
- **New Rank:** 13

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior nlp engineer at niramai (overlap: {'ai'}) |
| tech_timeline | ❌ 0.00 | OpenSearch claimed 92m, max realistic 66m (launched 2021); LangChain claimed 63m, max realistic 54m (launched 2022); LlamaIndex claimed 67m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.60 | AI company but no direct search/NLP signal |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 45: CAND_0070398 — Authenticity 0.76
- **Title:** Machine Learning Engineer
- **Company:** Genpact AI
- **YoE:** 7.2
- **Original Score:** 0.5535
- **Adjusted Score:** 0.5137
- **New Rank:** 61

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: machine learning engineer at genpact ai (overlap: {'ai'}) |
| tech_timeline | ❌ 0.00 | RAG claimed 72m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.60 | AI company but no direct search/NLP signal |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 4: CAND_0002025 — Authenticity 0.76
- **Title:** Senior AI Engineer
- **Company:** Apple
- **YoE:** 5.9
- **Original Score:** 0.7342
- **Adjusted Score:** 0.6818
- **New Rank:** 3

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior ai engineer at apple (overlap: {'nlp', 'ai', 'search'}) |
| tech_timeline | ❌ 0.00 | LangChain claimed 84m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ✅ 1.00 | Strong search/NLP alignment ({'nlp', 'search'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 4 vector databases (unusual) |

### Rank 21: CAND_0045250 — Authenticity 0.77
- **Title:** Applied ML Engineer
- **Company:** Rephrase.ai
- **YoE:** 6.6
- **Original Score:** 0.6128
- **Adjusted Score:** 0.5705
- **New Rank:** 27

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: applied ml engineer at rephrase.ai (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | LangChain claimed 85m, max realistic 54m (launched 2022); Qdrant claimed 76m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 24: CAND_0008425 — Authenticity 0.77
- **Title:** Senior NLP Engineer
- **Company:** Ola
- **YoE:** 7.8
- **Original Score:** 0.5993
- **Adjusted Score:** 0.5579
- **New Rank:** 32

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior nlp engineer at ola (overlap: {'ai'}) |
| tech_timeline | ❌ 0.00 | Qdrant claimed 92m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 31: CAND_0098846 — Authenticity 0.77
- **Title:** AI Engineer
- **Company:** upGrad
- **YoE:** 7.6
- **Original Score:** 0.5782
- **Adjusted Score:** 0.5383
- **New Rank:** 41

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: ai engineer at upgrad (overlap: {'recommendation', 'ai'}) |
| tech_timeline | ❌ 0.00 | Qdrant claimed 95m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 35: CAND_0076163 — Authenticity 0.77
- **Title:** NLP Engineer
- **Company:** Ola
- **YoE:** 6.9
- **Original Score:** 0.5712
- **Adjusted Score:** 0.5318
- **New Rank:** 43

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: nlp engineer at ola (overlap: {'ai'}) |
| tech_timeline | ❌ 0.00 | LangChain claimed 75m, max realistic 54m (launched 2022); LlamaIndex claimed 86m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 36: CAND_0058688 — Authenticity 0.77
- **Title:** AI Engineer
- **Company:** Vedantu
- **YoE:** 6.7
- **Original Score:** 0.5700
- **Adjusted Score:** 0.5307
- **New Rank:** 46

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: ai engineer at vedantu (overlap: {'recommendation', 'ai'}) |
| tech_timeline | ❌ 0.00 | LlamaIndex claimed 91m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 41: CAND_0005538 — Authenticity 0.77
- **Title:** Senior AI Engineer
- **Company:** Adobe
- **YoE:** 5.9
- **Original Score:** 0.5585
- **Adjusted Score:** 0.5199
- **New Rank:** 52

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior ai engineer at adobe (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | pgvector claimed 91m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 46: CAND_0044222 — Authenticity 0.77
- **Title:** AI Engineer
- **Company:** PolicyBazaar
- **YoE:** 7.7
- **Original Score:** 0.5521
- **Adjusted Score:** 0.5140
- **New Rank:** 59

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: ai engineer at policybazaar (overlap: {'recommendation', 'ai'}) |
| tech_timeline | ❌ 0.00 | LlamaIndex claimed 82m, max realistic 54m (launched 2022); OpenSearch claimed 75m, max realistic 66m (launched 2021); LangChain claimed 90m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 60: CAND_0057563 — Authenticity 0.77
- **Title:** NLP Engineer
- **Company:** Locobuzz
- **YoE:** 6.8
- **Original Score:** 0.5340
- **Adjusted Score:** 0.4971
- **New Rank:** 72

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: nlp engineer at locobuzz (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | RAG claimed 68m, max realistic 42m (launched 2023); OpenSearch claimed 94m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 65: CAND_0099401 — Authenticity 0.77
- **Title:** NLP Engineer
- **Company:** Dream11
- **YoE:** 7.7
- **Original Score:** 0.5250
- **Adjusted Score:** 0.4887
- **New Rank:** 78

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: nlp engineer at dream11 (overlap: {'ai'}) |
| tech_timeline | ❌ 0.00 | LlamaIndex claimed 81m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'recommendation'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 71: CAND_0096172 — Authenticity 0.77
- **Title:** NLP Engineer
- **Company:** Krutrim
- **YoE:** 5.2
- **Original Score:** 0.5199
- **Adjusted Score:** 0.4840
- **New Rank:** 84

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: nlp engineer at krutrim (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | LangChain claimed 79m, max realistic 54m (launched 2022); RAG claimed 58m, max realistic 42m (launched 2023); Qdrant claimed 76m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 95: CAND_0091909 — Authenticity 0.77
- **Title:** Machine Learning Engineer
- **Company:** Rephrase.ai
- **YoE:** 6.9
- **Original Score:** 0.4832
- **Adjusted Score:** 0.4498
- **New Rank:** 98

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: machine learning engineer at rephrase.ai (overlap: {'ai', 'nlp'}) |
| tech_timeline | ❌ 0.00 | Pinecone claimed 84m, max realistic 66m (launched 2021); LangChain claimed 92m, max realistic 54m (launched 2022) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.70 | Partial alignment ({'nlp'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 9: CAND_0079387 — Authenticity 0.77
- **Title:** AI Engineer
- **Company:** Microsoft
- **YoE:** 6.9
- **Original Score:** 0.6741
- **Adjusted Score:** 0.6281
- **New Rank:** 12

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: ai engineer at microsoft (overlap: {'nlp', 'ai', 'search'}) |
| tech_timeline | ❌ 0.12 | OpenSearch claimed 87m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ⚠️ 0.65 | Suspiciously broad: 5 different skill clusters ({'vdb', 'cv', 'web', 'ir', 'nlp'}) |
| company_reputation | ✅ 1.00 | Strong search/NLP alignment ({'nlp', 'search'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 51: CAND_0083307 — Authenticity 0.78
- **Title:** Search Engineer
- **Company:** CRED
- **YoE:** 7.8
- **Original Score:** 0.5455
- **Adjusted Score:** 0.5090
- **New Rank:** 66

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ⚠️ 0.50 | Weak alignment between search engineer and cred |
| tech_timeline | ⚠️ 0.58 | Pinecone claimed 76m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ⚠️ 0.60 | AI company but no direct search/NLP signal |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

### Rank 68: CAND_0095528 — Authenticity 0.79
- **Title:** Senior Data Scientist
- **Company:** Netflix
- **YoE:** 5.3
- **Original Score:** 0.5237
- **Adjusted Score:** 0.4904
- **New Rank:** 76

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior data scientist at netflix (overlap: {'recommendation', 'ai', 'search'}) |
| tech_timeline | ❌ 0.12 | RAG claimed 63m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ✅ 1.00 | Strong search/NLP alignment ({'recommendation', 'search'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 4 vector databases (unusual) |

### Rank 15: CAND_0068811 — Authenticity 0.80
- **Title:** Applied ML Engineer
- **Company:** Freshworks
- **YoE:** 8.0
- **Original Score:** 0.6356
- **Adjusted Score:** 0.5966
- **New Rank:** 19

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: applied ml engineer at freshworks (overlap: {'nlp', 'ai', 'search'}) |
| tech_timeline | ❌ 0.17 | Pinecone claimed 86m, max realistic 66m (launched 2021) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ✅ 1.00 | Strong search/NLP alignment ({'nlp', 'search'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ⚠️ 0.75 | Uses 5 different vector databases (unrealistic) |

### Rank 1: CAND_0018499 — Authenticity 0.80
- **Title:** Senior Machine Learning Engineer
- **Company:** Zomato
- **YoE:** 7.2
- **Original Score:** 0.7893
- **Adjusted Score:** 0.7420
- **New Rank:** 1

| Sub-Score | Value | Reason |
| :--- | :--- | :--- |
| company_domain | ✅ 1.00 | Good fit: senior machine learning engineer at zomato (overlap: {'recommendation', 'ai', 'search'}) |
| tech_timeline | ❌ 0.00 | RAG claimed 94m, max realistic 42m (launched 2023) |
| career_progression | ✅ 1.00 | Normal progression |
| skill_coherence | ✅ 1.00 | Coherent skill stack |
| company_reputation | ✅ 1.00 | Strong search/NLP alignment ({'recommendation', 'search'}) |
| seniority_consistency | ✅ 1.00 | Seniority is consistent |
| synthetic_risk | ✅ 1.00 | No synthetic signals detected |

---

## Rank Movement Simulation (After Authenticity Adjustment)

### Top 20 Changes
- **Removed from Top 20:** 0
- **Promoted into Top 20:** 0

### Top 50 Changes
- **Removed from Top 50:** 5
  - `CAND_0005538`: Senior AI Engineer @ Adobe (was #41, now #52, auth=0.77)
  - `CAND_0044222`: AI Engineer @ PolicyBazaar (was #46, now #59, auth=0.77)
  - `CAND_0070398`: Machine Learning Engineer @ Genpact AI (was #45, now #61, auth=0.76)
  - `CAND_0007412`: Applied ML Engineer @ Zoho (was #50, now #62, auth=0.80)
  - `CAND_0041611`: Staff Machine Learning Engineer @ Locobuzz (was #44, now #64, auth=0.73)
- **Promoted into Top 50:** 5
  - `CAND_0065786`: AI Specialist @ Swiggy (was #62, now #45, auth=1.00)
  - `CAND_0072660`: Machine Learning Engineer @ Unacademy (was #53, now #44, auth=0.93)
  - `CAND_0061257`: Staff Machine Learning Engineer @ LinkedIn (was #57, now #40, auth=1.00)
  - `CAND_0065878`: Senior Data Scientist @ Niramai (was #59, now #47, auth=0.96)
  - `CAND_0037980`: Senior Applied Scientist @ Niramai (was #54, now #48, auth=0.92)

---

## Authenticity Score Distribution (Top 100)

- **Min:** 0.68
- **Max:** 1.00
- **Mean:** 0.87
- **Median:** 0.87

| Bucket | Count |
| :--- | :--- |
| 0.0-0.3 | 0 |
| 0.3-0.5 | 0 |
| 0.5-0.7 | 1 |
| 0.7-0.9 | 57 |
| 0.9-1.0 | 42 |

---

## Full Top 100 Authenticity Scores

| Old Rank | New Rank | ID | Title | Company | Original Score | Auth Score | Adjusted Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 (0) | CAND_0018499 | Senior Machine Learning Engineer | Zomato | 0.7893 | 0.80 | 0.7420 |
| 2 | 2 (0) | CAND_0081846 | Lead AI Engineer | Razorpay | 0.7401 | 0.96 | 0.7312 |
| 3 | 5 (-2) | CAND_0077337 | Staff Machine Learning Engineer | Paytm | 0.7388 | 0.73 | 0.6795 |
| 4 | 3 (+1) | CAND_0002025 | Senior AI Engineer | Apple | 0.7342 | 0.76 | 0.6818 |
| 5 | 6 (-1) | CAND_0055905 | Senior Machine Learning Engineer | Flipkart | 0.7001 | 0.87 | 0.6721 |
| 6 | 4 (+2) | CAND_0071974 | Senior AI Engineer | Netflix | 0.6885 | 0.96 | 0.6808 |
| 7 | 9 (-2) | CAND_0046064 | Senior NLP Engineer | Salesforce | 0.6853 | 0.84 | 0.6528 |
| 8 | 13 (-5) | CAND_0011687 | Senior NLP Engineer | Niramai | 0.6760 | 0.76 | 0.6273 |
| 9 | 12 (-3) | CAND_0079387 | AI Engineer | Microsoft | 0.6741 | 0.77 | 0.6281 |
| 10 | 10 (0) | CAND_0046525 | Senior Machine Learning Engineer | Genpact AI | 0.6721 | 0.86 | 0.6439 |
| 11 | 7 (+4) | CAND_0094759 | Lead AI Engineer | Meta | 0.6682 | 1.00 | 0.6682 |
| 12 | 8 (+4) | CAND_0093912 | Senior Data Scientist | Razorpay | 0.6659 | 0.96 | 0.6579 |
| 13 | 14 (-1) | CAND_0033861 | Senior NLP Engineer | Mad Street Den | 0.6468 | 0.90 | 0.6264 |
| 14 | 11 (+3) | CAND_0049538 | Applied ML Engineer | Saarthi.ai | 0.6464 | 0.97 | 0.6405 |
| 15 | 19 (-4) | CAND_0068811 | Applied ML Engineer | Freshworks | 0.6356 | 0.80 | 0.5966 |
| 16 | 20 (-4) | CAND_0062247 | AI Engineer | Google | 0.6296 | 0.80 | 0.5919 |
| 17 | 15 (+2) | CAND_0027691 | NLP Engineer | Haptik | 0.6243 | 0.97 | 0.6187 |
| 18 | 16 (+2) | CAND_0081852 | Senior Data Scientist | Mad Street Den | 0.6214 | 0.97 | 0.6159 |
| 19 | 18 (+1) | CAND_0060054 | AI Engineer | Mad Street Den | 0.6151 | 0.97 | 0.6096 |
| 20 | 17 (+3) | CAND_0064326 | Search Engineer | Sarvam AI | 0.6133 | 1.00 | 0.6133 |
| 21 | 27 (-6) | CAND_0045250 | Applied ML Engineer | Rephrase.ai | 0.6128 | 0.77 | 0.5705 |
| 22 | 25 (-3) | CAND_0007411 | Senior Machine Learning Engineer | Amazon | 0.6062 | 0.83 | 0.5759 |
| 23 | 23 (0) | CAND_0043228 | Applied ML Engineer | Zoho | 0.6043 | 0.86 | 0.5797 |
| 24 | 32 (-8) | CAND_0008425 | Senior NLP Engineer | Ola | 0.5993 | 0.77 | 0.5579 |
| 25 | 22 (+3) | CAND_0080766 | Staff Machine Learning Engineer | Salesforce | 0.5977 | 0.91 | 0.5816 |
| 26 | 31 (-5) | CAND_0042029 | Senior Data Scientist | Flipkart | 0.5960 | 0.80 | 0.5602 |
| 27 | 24 (+3) | CAND_0015528 | Applied ML Engineer | Krutrim | 0.5889 | 0.93 | 0.5770 |
| 28 | 21 (+7) | CAND_0081686 | Search Engineer | Netflix | 0.5862 | 1.00 | 0.5862 |
| 29 | 28 (+1) | CAND_0005649 | Senior Data Scientist | Sarvam AI | 0.5850 | 0.90 | 0.5666 |
| 30 | 34 (-4) | CAND_0044855 | Senior Data Scientist | Flipkart | 0.5791 | 0.88 | 0.5574 |
| 31 | 41 (-10) | CAND_0098846 | AI Engineer | upGrad | 0.5782 | 0.77 | 0.5383 |
| 32 | 26 (+6) | CAND_0050454 | AI Engineer | Rephrase.ai | 0.5776 | 0.97 | 0.5724 |
| 33 | 39 (-6) | CAND_0051292 | Applied ML Engineer | Freshworks | 0.5759 | 0.80 | 0.5413 |
| 34 | 29 (+5) | CAND_0092278 | Senior NLP Engineer | Microsoft | 0.5754 | 0.94 | 0.5653 |
| 35 | 43 (-8) | CAND_0076163 | NLP Engineer | Ola | 0.5712 | 0.77 | 0.5318 |
| 36 | 46 (-10) | CAND_0058688 | AI Engineer | Vedantu | 0.5700 | 0.77 | 0.5307 |
| 37 | 36 (+1) | CAND_0068351 | Lead AI Engineer | Sarvam AI | 0.5697 | 0.90 | 0.5526 |
| 38 | 30 (+8) | CAND_0060072 | Staff Machine Learning Engineer | Amazon | 0.5692 | 0.96 | 0.5624 |
| 39 | 35 (+4) | CAND_0052682 | NLP Engineer | Aganitha | 0.5635 | 0.96 | 0.5568 |
| 40 | 37 (+3) | CAND_0053591 | AI Engineer | Ola | 0.5635 | 0.90 | 0.5458 |
| 41 | 52 (-11) | CAND_0005538 | Senior AI Engineer | Adobe | 0.5585 | 0.77 | 0.5199 |
| 42 | 49 (-7) | CAND_0039383 | Applied ML Engineer | Meesho | 0.5582 | 0.80 | 0.5247 |
| 43 | 33 (+10) | CAND_0069905 | Applied ML Engineer | Sarvam AI | 0.5579 | 1.00 | 0.5579 |
| 44 | 64 (-20) | CAND_0041611 | Staff Machine Learning Engineer | Locobuzz | 0.5555 | 0.73 | 0.5109 |
| 45 | 61 (-16) | CAND_0070398 | Machine Learning Engineer | Genpact AI | 0.5535 | 0.76 | 0.5137 |
| 46 | 59 (-13) | CAND_0044222 | AI Engineer | PolicyBazaar | 0.5521 | 0.77 | 0.5140 |
| 47 | 50 (-3) | CAND_0030953 | Search Engineer | Nykaa | 0.5521 | 0.83 | 0.5244 |
| 48 | 38 (+10) | CAND_0010257 | Senior Data Scientist | Google | 0.5507 | 0.96 | 0.5445 |
| 49 | 42 (+7) | CAND_0088025 | Staff Machine Learning Engineer | Yellow.ai | 0.5473 | 0.92 | 0.5337 |
| 50 | 62 (-12) | CAND_0007412 | Applied ML Engineer | Zoho | 0.5465 | 0.80 | 0.5137 |
| 51 | 66 (-15) | CAND_0083307 | Search Engineer | CRED | 0.5455 | 0.78 | 0.5090 |
| 52 | 60 (-8) | CAND_0074735 | Applied ML Engineer | Rephrase.ai | 0.5433 | 0.82 | 0.5139 |
| 53 | 44 (+9) | CAND_0072660 | Machine Learning Engineer | Unacademy | 0.5427 | 0.93 | 0.5317 |
| 54 | 48 (+6) | CAND_0037980 | Senior Applied Scientist | Niramai | 0.5411 | 0.92 | 0.5285 |
| 55 | 67 (-12) | CAND_0080534 | ML Engineer | Genpact AI | 0.5399 | 0.81 | 0.5088 |
| 56 | 69 (-13) | CAND_0037566 | Machine Learning Engineer | LinkedIn | 0.5393 | 0.80 | 0.5069 |
| 57 | 40 (+17) | CAND_0061257 | Staff Machine Learning Engineer | LinkedIn | 0.5387 | 1.00 | 0.5387 |
| 58 | 65 (-7) | CAND_0010685 | NLP Engineer | Rephrase.ai | 0.5371 | 0.83 | 0.5094 |
| 59 | 47 (+12) | CAND_0065878 | Senior Data Scientist | Niramai | 0.5357 | 0.96 | 0.5293 |
| 60 | 72 (-12) | CAND_0057563 | NLP Engineer | Locobuzz | 0.5340 | 0.77 | 0.4971 |
| 61 | 77 (-16) | CAND_0013536 | Applied ML Engineer | Haptik | 0.5326 | 0.73 | 0.4899 |
| 62 | 45 (+17) | CAND_0065786 | AI Specialist | Swiggy | 0.5316 | 1.00 | 0.5316 |
| 63 | 57 (+6) | CAND_0008239 | AI Engineer | Apple | 0.5309 | 0.90 | 0.5156 |
| 64 | 68 (-4) | CAND_0078002 | Machine Learning Engineer | Meta | 0.5279 | 0.88 | 0.5081 |
| 65 | 78 (-13) | CAND_0099401 | NLP Engineer | Dream11 | 0.5250 | 0.77 | 0.4887 |
| 66 | 53 (+13) | CAND_0094056 | NLP Engineer | Rephrase.ai | 0.5245 | 0.97 | 0.5198 |
| 67 | 51 (+16) | CAND_0028793 | Search Engineer | Google | 0.5240 | 1.00 | 0.5240 |
| 68 | 76 (-8) | CAND_0095528 | Senior Data Scientist | Netflix | 0.5237 | 0.79 | 0.4904 |
| 69 | 55 (+14) | CAND_0044883 | AI Engineer | Mad Street Den | 0.5231 | 0.97 | 0.5184 |
| 70 | 58 (+12) | CAND_0051630 | Machine Learning Engineer | Razorpay | 0.5218 | 0.96 | 0.5156 |
| 71 | 84 (-13) | CAND_0096172 | NLP Engineer | Krutrim | 0.5199 | 0.77 | 0.4840 |
| 72 | 54 (+18) | CAND_0020350 | AI Engineer | Zoho | 0.5198 | 1.00 | 0.5198 |
| 73 | 71 (+2) | CAND_0075249 | Applied ML Engineer | Zomato | 0.5185 | 0.88 | 0.5003 |
| 74 | 56 (+18) | CAND_0006567 | Senior AI Engineer | Meta | 0.5179 | 1.00 | 0.5179 |
| 75 | 63 (+12) | CAND_0016163 | Applied ML Engineer | Dream11 | 0.5178 | 0.97 | 0.5131 |
| 76 | 75 (+1) | CAND_0025640 | AI Research Engineer | HCL | 0.5135 | 0.85 | 0.4904 |
| 77 | 70 (+7) | CAND_0083879 | Machine Learning Engineer | Ola | 0.5104 | 0.97 | 0.5058 |
| 78 | 80 (-2) | CAND_0024620 | AI Engineer | PharmEasy | 0.5099 | 0.85 | 0.4869 |
| 79 | 82 (-3) | CAND_0027801 | NLP Engineer | InMobi | 0.5089 | 0.85 | 0.4860 |
| 80 | 90 (-10) | CAND_0053605 | Senior Software Engineer (ML) | Verloop.io | 0.5070 | 0.75 | 0.4690 |
| 81 | 74 (+7) | CAND_0017178 | ML Engineer | Swiggy | 0.5066 | 0.90 | 0.4914 |
| 82 | 88 (-6) | CAND_0007460 | AI Engineer | Salesforce | 0.5004 | 0.80 | 0.4703 |
| 83 | 73 (+10) | CAND_0005509 | Data Scientist | Ola | 0.4987 | 0.97 | 0.4943 |
| 84 | 83 (+1) | CAND_0096142 | Applied ML Engineer | upGrad | 0.4965 | 0.92 | 0.4842 |
| 85 | 91 (-6) | CAND_0081053 | NLP Engineer | Glance | 0.4952 | 0.81 | 0.4673 |
| 86 | 81 (+5) | CAND_0018888 | AI Research Engineer | Razorpay | 0.4921 | 0.96 | 0.4862 |
| 87 | 100 (-13) | CAND_0070202 | Machine Learning Engineer | BYJU'S | 0.4910 | 0.68 | 0.4436 |
| 88 | 89 (-1) | CAND_0068932 | ML Engineer | Krutrim | 0.4890 | 0.87 | 0.4700 |
| 89 | 79 (+10) | CAND_0050876 | Applied ML Engineer | Freshworks | 0.4884 | 1.00 | 0.4884 |
| 90 | 93 (-3) | CAND_0043860 | Junior ML Engineer | Aganitha | 0.4880 | 0.82 | 0.4617 |
| 91 | 87 (+4) | CAND_0022274 | AI Research Engineer | Yellow.ai | 0.4868 | 0.92 | 0.4747 |
| 92 | 92 (0) | CAND_0046132 | AI Research Engineer | Verloop.io | 0.4850 | 0.85 | 0.4632 |
| 93 | 99 (-6) | CAND_0073504 | Junior ML Engineer | PolicyBazaar | 0.4842 | 0.72 | 0.4442 |
| 94 | 94 (0) | CAND_0066690 | ML Engineer | Freshworks | 0.4837 | 0.85 | 0.4616 |
| 95 | 98 (-3) | CAND_0091909 | Machine Learning Engineer | Rephrase.ai | 0.4832 | 0.77 | 0.4498 |
| 96 | 86 (+10) | CAND_0044213 | AI Specialist | Haptik | 0.4827 | 0.97 | 0.4784 |
| 97 | 85 (+12) | CAND_0042100 | Machine Learning Engineer | Freshworks | 0.4799 | 1.00 | 0.4799 |
| 98 | 97 (+1) | CAND_0041568 | Search Engineer | Haptik | 0.4782 | 0.82 | 0.4520 |
| 99 | 96 (+3) | CAND_0043381 | AI Research Engineer | PharmEasy | 0.4766 | 0.85 | 0.4551 |
| 100 | 95 (+5) | CAND_0070525 | Senior Software Engineer (ML) | Mad Street Den | 0.4746 | 0.87 | 0.4561 |