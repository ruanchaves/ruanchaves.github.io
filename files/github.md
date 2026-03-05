<h1 align="center">👋 Hi, I'm Ruan</h1>
<h3 align="center">Senior AI Engineer | Generative AI | RAG | LLMs | NLP | Python</h3>

<div align="center">

<a href="https://ruanchaves.github.io/">🌐 Personal Website</a>

</div>


---

## 🚀 Projects

- **[ruanchaves/hashformers](https://github.com/ruanchaves/hashformers)**: State-of-the-art framework for hashtag segmentation.
    - Recognized as state-of-the-art at **LREC 2022** in the paper *"HashSet — A Dataset For Hashtag Segmentation"* by researchers from IIT.
    - Leverages GPT-2 and beam search for accurate, multilingual hashtag and text segmentation.
    - Outperforms prior methods on standard benchmarks (STANsmall, BOUN).

- **[ruanchaves/napolab](https://github.com/ruanchaves/napolab)**: The Natural Portuguese Language Benchmark.
    - A curated collection of Portuguese datasets for rigorous LLM evaluation.
    - Key finding: the performance gap between general-purpose LLMs and Portuguese-specific models is smaller than previously believed—multilingual training is often sufficient.
    - Exposes systemic issues in LLM benchmarking (investigation gap, data contamination) that have inflated reported progress.
    - Browse the **[Napolab Leaderboard](https://huggingface.co/spaces/ruanchaves/napolab)** and stay up to date with the latest advancements in Portuguese language models.
    - Medium Article: [The Hidden Truth About LLM Performance: Why Your Benchmark Results Might Be Misleading](https://ruanchaves.medium.com/the-hidden-truth-about-llm-performance-why-your-benchmark-results-might-be-misleading-afd24f40a46c)
        - Explores how benchmark contamination and investigation gaps have inflated reported LLM progress, with a focus on Portuguese language evaluation.
    - Master Thesis: [Lessons learned from the evaluation of Portuguese language models](https://www.um.edu.mt/library/oar/handle/123456789/120557)
        - M.Sc. thesis (University of Malta, 2023). Traces Portuguese NLP from early embeddings to LLMs, presents Napolab as the main contribution, and concludes that multilingual models match Portuguese-specific ones.

<div align="center">
  <img src="benchmark.PNG" width="45%" alt="Napolab Leaderboard Interface">
  <img src="benchmark_radio.png" width="45%" alt="Model Performance Analysis">
</div>

---

## 🌟 Contributions

_Click on the links to view my pull requests._

- **[argilla-io/argilla](https://github.com/argilla-io/argilla/issues?q=author%3Aruanchaves+)**:
  - Fixed bugs and shipped features related to semi-supervised learning (SSL) during my internship at Argilla.
  - **Context:** Argilla is an open-source data curation and annotation platform for NLP. It was acquired by Hugging Face in June 2024 (~$10M deal) to strengthen their dataset tooling ecosystem.

- **[huggingface/transformers](https://github.com/huggingface/transformers/pull/10823)**:
  - Modified the Trainer class for simultaneous Ray Tune and Weights & Biases execution.
  - **Context:** Enabled parallel hyperparameter search with Ray Tune while logging all runs to W&B for experiment tracking—a common workflow for production model fine-tuning.

- **[nathanshartmann/portuguese_word_embeddings](https://github.com/nathanshartmann/portuguese_word_embeddings/pull/11)**:
  - Fixed a severe bug in the evaluation procedure.
  - Documented the bug fix in the research paper ["Portuguese language models..."](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3JDK8KEAAAAJ&citation_for_view=3JDK8KEAAAAJ:u-x6o8ySG0sC).
  - **Context:** This repository provides pre-trained word embeddings for Portuguese. The bug fix corrected an evaluation error that affected reported benchmark scores.

- **[facebookresearch/BLINK](https://github.com/facebookresearch/BLINK/pull/25)**:
  - Fixed a parameter bug in the script for the BLINK benchmark.
  - **Context:** BLINK is Meta AI's state-of-the-art entity linking system, using a bi-encoder + cross-encoder architecture over BERT to link text mentions to Wikipedia entities at scale (millions of candidates in milliseconds).

- **[awslabs/mlm-scoring](https://github.com/awslabs/mlm-scoring/pull/12)**:
  - Addressed an installation instruction issue for the mlm-scoring library.
  - **Context:** AWS Labs library for scoring sentences using masked language models (BERT, RoBERTa). Based on the ACL 2020 paper *"Masked Language Model Scoring"*—pseudo-log-likelihood scores outperform GPT-2 on acceptability judgments.

---

## 📖 Papers With Code

- **[neuralmind-ai/coliee](https://github.com/neuralmind-ai/coliee)**:
  - Code for ["To Tune or Not To Tune? Zero-shot Models for Legal Case Entailment"](https://arxiv.org/abs/2202.03120)
      - **1st place in COLIEE 2021 Task 2** (legal case entailment). Zero-shot model beat fine-tuned DeBERTa/monoT5 by 6+ points, demonstrating robustness with limited labeled data.
  - Code for ["Yes, BM25 is a Strong Baseline for Legal Case Retrieval"](https://arxiv.org/abs/2105.05686)
      - Showed that BM25 remains a competitive baseline for legal document retrieval, challenging assumptions about neural retrieval superiority in low-resource domains.

- **[ruanchaves/assin](https://github.com/ruanchaves/assin)**:
  - Code for ["Multilingual Transformer Ensembles for Portuguese Natural Language Tasks"](https://scholar.google.com/citations?view_op=view_citation&hl=pt-PT&user=3JDK8KEAAAAJ&citation_for_view=3JDK8KEAAAAJ:qjMakFHDy7sC).
  - **Context: ASSIN 2** (Avaliação de Similaridade Semântica e Inferência Textual) was a shared task at STIL 2019 focused on semantic similarity and textual entailment for Portuguese. 9 teams competed on ~10K annotated sentence pairs.

- **[ruanchaves/elmo](https://github.com/ruanchaves/elmo)**:
  - Code for ["Portuguese language models and word embeddings: evaluating on semantic similarity tasks"](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3JDK8KEAAAAJ&citation_for_view=3JDK8KEAAAAJ:u-x6o8ySG0sC).
  - **Context:** ELMo (Embeddings from Language Models) produces deeply contextualized word representations that capture syntax, semantics, and polysemy. This work trained and evaluated Portuguese ELMo models on semantic similarity benchmarks (ASSIN), comparing against static embeddings like Word2Vec and GloVe.

- **[ruanchaves/BERT-WS](https://github.com/ruanchaves/BERT-WS)**:
  - Code for ["Domain adaptation of transformers for english word segmentation"](https://scholar.google.com/citations?view_op=view_citation&hl=pt-PT&user=3JDK8KEAAAAJ&citation_for_view=3JDK8KEAAAAJ:9yKSN-GCB0IC).
  - **Context:** Word segmentation is challenging for compound words and domain-specific terms. This work applied domain adaptation techniques to BERT for English word segmentation, addressing tokenization limitations through continued pre-training and vocabulary expansion.

---

📧 **Email**: ruanchaves93@gmail.com
