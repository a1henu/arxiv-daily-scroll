---
layout: default
title: PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR
---

# PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR
**arXiv**：[2601.18207v1](https://arxiv.org/abs/2601.18207) · [PDF](https://arxiv.org/pdf/2601.18207.pdf)  
**作者**：James Burgess, Jan N. Hansen, Duo Peng, Yuhui Zhang, Alejandro Lozano, Min Woo Sun, Emma Lundberg, Serena Yeung-Levy  

**一句话要点**：提出PaperSearchQA以训练搜索代理在生物医学论文摘要中搜索和推理，提升技术问答能力。

**关键词**：搜索代理, 强化学习可验证奖励, 科学论文检索, 技术问答, 生物医学语料库, 数据集构建

## 3 点简述
- 核心问题：现有RLVR搜索代理主要针对通用领域QA，限制了在科学、工程和医学等AI系统中的技术问答应用。
- 方法要点：构建包含1600万生物医学论文摘要的搜索语料库和6万样本的PaperSearchQA数据集，用于训练搜索代理。
- 实验或效果：训练代理在环境中超越非强化学习检索基线，并观察到规划、推理和自我验证等行为。

## 摘要（原文）

> Search agents are language models (LMs) that reason and search knowledge bases (or the web) to answer questions; recent methods supervise only the final answer accuracy using reinforcement learning with verifiable rewards (RLVR). Most RLVR search agents tackle general-domain QA, which limits their relevance to technical AI systems in science, engineering, and medicine. In this work we propose training agents to search and reason over scientific papers -- this tests technical question-answering, it is directly relevant to real scientists, and the capabilities will be crucial to future AI Scientist systems. Concretely, we release a search corpus of 16 million biomedical paper abstracts and construct a challenging factoid QA dataset called PaperSearchQA with 60k samples answerable from the corpus, along with benchmarks. We train search agents in this environment to outperform non-RL retrieval baselines; we also perform further quantitative analysis and observe interesting agent behaviors like planning, reasoning, and self-verification. Our corpus, datasets, and benchmarks are usable with the popular Search-R1 codebase for RLVR training and released on https://huggingface.co/collections/jmhb/papersearchqa. Finally, our data creation methods are scalable and easily extendable to other scientific domains.

