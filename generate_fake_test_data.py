import json
import random

def create_base_candidate(cid, name, title, yoe, summary, country="India"):
    return {
        "candidate_id": cid,
        "profile": {
            "anonymized_name": name,
            "headline": f"{title} | {yoe} yrs",
            "summary": summary,
            "location": "Bangalore" if country=="India" else "San Francisco",
            "country": country,
            "years_of_experience": yoe,
            "current_title": title,
            "current_company": "Tech Corp",
            "current_company_size": "1001-5000",
            "current_industry": "Software"
        },
        "career_history": [
            {
                "company": "Tech Corp",
                "title": title,
                "start_date": "2020-01-01",
                "end_date": None,
                "duration_months": int(yoe*12),
                "is_current": True,
                "industry": "Software",
                "company_size": "1001-5000",
                "description": summary
            }
        ],
        "education": [],
        "skills": [],
        "redrob_signals": {
            "profile_completeness_score": 95.0,
            "recruiter_response_rate": 0.85,
            "interview_completion_rate": 0.90,
            "notice_period_days": 15,
            "github_activity_score": 8.0,
            "open_to_work_flag": True
        }
    }

candidates = []

# 1-5: True Elites (Deep RAG / Vector DB)
for i in range(1, 6):
    c = create_base_candidate(f"CAND_00000{i:02d}", f"Elite_{i}", "Senior AI Engineer", 7.0,
                              "Architected and built large scale RAG pipelines using FAISS, ElasticSearch, and Qdrant. "
                              "Led the deployment of dense vector retrieval systems using Kubernetes. "
                              "Expert in fine-tuning LLMs and measuring NDCG and MAP for search relevance.")
    c['skills'] = [
        {"name": "FAISS", "proficiency": "advanced", "endorsements": 45, "duration_months": 36},
        {"name": "Elasticsearch", "proficiency": "advanced", "endorsements": 60, "duration_months": 48},
        {"name": "Python", "proficiency": "advanced", "endorsements": 90, "duration_months": 84},
        {"name": "Kubernetes", "proficiency": "advanced", "endorsements": 30, "duration_months": 24}
    ]
    candidates.append(c)

# 6-10: Average ML Engineers (Good but not search-focused)
for i in range(6, 11):
    c = create_base_candidate(f"CAND_00000{i:02d}", f"AvgML_{i}", "Data Scientist", 5.0,
                              "Data Scientist working on predictive modeling and random forests. "
                              "Experienced in scikit-learn, pandas, and basic deep learning using PyTorch. "
                              "Trained image classification models.")
    c['skills'] = [
        {"name": "Python", "proficiency": "advanced", "endorsements": 45, "duration_months": 60},
        {"name": "PyTorch", "proficiency": "intermediate", "endorsements": 20, "duration_months": 24},
        {"name": "Machine Learning", "proficiency": "advanced", "endorsements": 50, "duration_months": 60}
    ]
    c['redrob_signals']['notice_period_days'] = 60 # Slightly worse behavioral
    candidates.append(c)

# 11: Honeypot 1 (Keyword stuffer: >=10 expert skills, >=5 with low duration, 0 endorsements)
c = create_base_candidate("CAND_0000011", "Stuffer_1", "Senior AI Engineer", 8.0,
                          "I am an expert in everything. FAISS, ElasticSearch, RAG, Pinecone, Qdrant, Milvus, Vector Search.")
c['skills'] = [
    {"name": f"Skill_{j}", "proficiency": "expert", "endorsements": 0, "duration_months": 2} for j in range(15)
]
candidates.append(c)

# 12: Honeypot 2 (Impossible LangChain duration: max_duration > YOE*12 + 24)
# YOE = 2.0 (max allowed = 48 months). LangChain duration = 90 months.
c = create_base_candidate("CAND_0000012", "Honeypot_Impossible_Langchain", "AI Engineer", 2.0,
                          "Built search systems using FAISS and LangChain.")
c['skills'] = [
    {"name": "LangChain", "proficiency": "advanced", "endorsements": 50, "duration_months": 90},
    {"name": "FAISS", "proficiency": "advanced", "endorsements": 50, "duration_months": 40}
]
candidates.append(c)

# 13: Honeypot 3 (Timeline contradiction: career duration - YOE > 5.0)
c = create_base_candidate("CAND_0000013", "Honeypot_Timeline_Error", "Machine Learning Engineer", 5.0,
                          "Built vector search.")
c['career_history'][0]['start_date'] = "2010-01-01"
c['career_history'][0]['end_date'] = "2024-01-01" 
c['career_history'][0]['duration_months'] = 168 # 14 years
c['skills'] = [{"name": "Python", "proficiency": "advanced", "endorsements": 40, "duration_months": 36}]
candidates.append(c)

# 14: Honeypot 4 (HR Manager keyword stuffer)
c = create_base_candidate("CAND_0000014", "HR_Stuffer", "HR Manager", 10.0,
                          "I hire for FAISS, Elasticsearch, RAG, and Vector databases. I am looking for NDCG and MAP experts.")
c['skills'] = [{"name": "Recruiting", "proficiency": "advanced", "endorsements": 100, "duration_months": 120}]
candidates.append(c)

# 15: Honeypot 5 (Entry Level keyword stuffer)
c = create_base_candidate("CAND_0000015", "Junior_Stuffer", "Intern", 0.5,
                          "Learned about FAISS, Elasticsearch, RAG, Vector Databases in my course.")
c['profile']['years_of_experience'] = 0.5
c['skills'] = [{"name": "Python", "proficiency": "beginner", "endorsements": 2, "duration_months": 6}]
candidates.append(c)

# 16-20: Pure Noise
for i in range(16, 21):
    c = create_base_candidate(f"CAND_00000{i:02d}", f"Noise_{i}", "Accountant", 8.0,
                              "Managed corporate ledger and accounts payable using SAP.")
    c['skills'] = [
        {"name": "Excel", "proficiency": "advanced", "endorsements": 45, "duration_months": 60},
        {"name": "SAP", "proficiency": "intermediate", "endorsements": 20, "duration_months": 24}
    ]
    candidates.append(c)

with open('f:/IND_RUN/fake_candidates.jsonl', 'w', encoding='utf-8') as f:
    for c in candidates:
        f.write(json.dumps(c) + '\n')
print(f"Generated {len(candidates)} fake candidates.")

# Generate labels for scoring
labels = {}
for i in range(1, 6): labels[f"CAND_00000{i:02d}"] = "Elite"
for i in range(6, 11): labels[f"CAND_00000{i:02d}"] = "AvgML"
labels["CAND_0000011"] = "Stuffer_0_Endorsements"
labels["CAND_0000012"] = "Honeypot_Impossible_Langchain"
labels["CAND_0000013"] = "Honeypot_Timeline_Error"
labels["CAND_0000014"] = "HR_Stuffer"
labels["CAND_0000015"] = "Intern_Stuffer"
for i in range(16, 21): labels[f"CAND_00000{i:02d}"] = "Noise"

with open('f:/IND_RUN/fake_labels.json', 'w') as f:
    json.dump(labels, f, indent=2)
