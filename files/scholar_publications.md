# Google Scholar Publications (compiled from files/linkedin.md and files/github.md)

**Profile**: https://scholar.google.com/citations?user=3JDK8KEAAAAJ&hl=en

Note: Google Scholar blocked web scraping. This data is compiled from LinkedIn profile and GitHub README which list all publications.

## Publications

### 1. Construcao de Datasets para Segmentacao Automatica de Hashtags
- **Year**: 2020
- **Venue**: EnAComp 2020
- **Description**: Proposes a heuristic method for building hashtag segmentation datasets from tweets, statistically improving deep learning models.
- **Code**: https://github.com/ruanchaves/hashformers

### 2. Domain Adaptation of Transformers for English Word Segmentation
- **Year**: 2020
- **Venue**: BRACIS 2020
- **Description**: Applies continued pre-training and vocabulary expansion to BERT for compound word segmentation.
- **Code**: https://github.com/ruanchaves/BERT-WS
- **Talk**: BRACIS 2020 presentation

### 3. Multilingual Transformer Ensembles for Portuguese Natural Language Tasks
- **Year**: 2020
- **Venue**: ASSIN 2 workshop (STIL 2019/2020)
- **Description**: Ensemble of translated English and Portuguese Transformers achieved best RTE results, outperforming BERT-multilingual without task-specific preprocessing.
- **Code**: https://github.com/ruanchaves/assin
- **Context**: ASSIN 2 shared task at STIL 2019. 9 teams competed on ~10K annotated Portuguese sentence pairs.

### 4. Portuguese Language Models and Word Embeddings: Evaluating on Semantic Similarity Tasks
- **Year**: ~2020
- **Venue**: (from Google Scholar)
- **Description**: Trained and evaluated Portuguese ELMo models on semantic similarity benchmarks (ASSIN), comparing against static embeddings like Word2Vec and GloVe. Also documented a bug fix in the portuguese_word_embeddings evaluation procedure.
- **Code**: https://github.com/ruanchaves/elmo

### 5. Yes, BM25 is a Strong Baseline for Legal Case Retrieval
- **Year**: 2021
- **Venue**: COLIEE 2021 workshop
- **ArXiv**: https://arxiv.org/abs/2105.05686
- **Description**: Showed that BM25 remains a competitive baseline for legal document retrieval, challenging assumptions about neural retrieval superiority in low-resource domains.
- **Code**: https://github.com/neuralmind-ai/coliee

### 6. To Tune or Not To Tune? Zero-shot Models for Legal Case Entailment
- **Year**: 2021/2022
- **Venue**: COLIEE 2021 (competition paper)
- **ArXiv**: https://arxiv.org/abs/2202.03120
- **Description**: 1st place in COLIEE 2021 Task 2 (legal case entailment). Zero-shot model beat fine-tuned DeBERTa/monoT5 by 6+ points.
- **Code**: https://github.com/neuralmind-ai/coliee

### 7. Deep Learning Brasil at ABSAPT 2022: Portuguese Transformer Ensemble Approaches
- **Year**: 2022
- **Venue**: IberLEF 2022
- **Description**: State-of-the-art results on aspect term extraction (RoBERTa + mDeBERTa) and sentiment orientation (PTT5 voting ensemble). 1st place, beating second-place team by 3.5%.

### 8. Lessons Learned from the Evaluation of Portuguese Language Models (Master Thesis)
- **Year**: 2023
- **Venue**: University of Malta (M.Sc. thesis)
- **URL**: https://www.um.edu.mt/library/oar/handle/123456789/120557
- **Description**: Traces Portuguese NLP from early embeddings to LLMs, presents Napolab as the main contribution, and concludes that multilingual models match Portuguese-specific ones.

## Awards / Competition Wins

1. **1st place - ASSIN 2 (2019)**: Semantic Textual Similarity and Textual Inference in Portuguese. Led a stacking ensemble of multiple Transformer models. Competition organized by the Brazilian Computer Society (SBC). University Council's Certificate of Honours.

2. **1st place - COLIEE 2021 Task 2**: Legal case entailment. Organized by the Alberta Machine Intelligence Institute (Amii) at the University of Alberta. Zero-shot model outperformed fine-tuned DeBERTa/monoT5 by 6+ points.

3. **1st place - ABSAPT @ IberLEF 2022**: Aspect-Based Sentiment Analysis in Portuguese. Organized by the Spanish Society for NLP (SEPLN). Achieved 0.82 balanced accuracy, beating 4 other teams.
