---
layout: default
title: Connect the Dots: Knowledge Graph-Guided Crawler Attack on Retrieval-Augmented Generation Systems
---

# Connect the Dots: Knowledge Graph-Guided Crawler Attack on Retrieval-Augmented Generation Systems
**arXiv**：[2601.15678v1](https://arxiv.org/abs/2601.15678) · [PDF](https://arxiv.org/pdf/2601.15678.pdf)  
**作者**：Mengyu Yao, Ziqi Zhang, Ning Luo, Shaofei Li, Yifeng Cai, Xiangqun Chen, Yao Guo, Ding Li  

**一句话要点**：提出RAGCRAWLER方法，基于知识图指导爬虫攻击，以解决检索增强生成系统的隐私泄露问题。

**关键词**：检索增强生成系统, 隐私攻击, 知识图, 自适应随机覆盖, 语义查询规划

## 3 点简述
- 核心问题：RAG系统存在隐私风险，现有攻击方法依赖启发式，缺乏长期规划能力。
- 方法要点：将攻击建模为自适应随机覆盖问题，利用知识图估计条件边际增益，在语义空间规划查询。
- 实验或效果：在多种RAG架构和数据集上，RAGCRAWLER覆盖率达84.4%，平均提升20.7%，保持高语义保真度。

## 摘要（原文）

> Retrieval-augmented generation (RAG) systems integrate document retrieval with large language models and have been widely adopted. However, in privacy-related scenarios, RAG introduces a new privacy risk: adversaries can issue carefully crafted queries to exfiltrate sensitive content from the underlying corpus gradually. Although recent studies have demonstrated multi-turn extraction attacks, they rely on heuristics and fail to perform long-term extraction planning. To address these limitations, we formulate the RAG extraction attack as an adaptive stochastic coverage problem (ASCP). In ASCP, each query is treated as a probabilistic action that aims to maximize conditional marginal gain (CMG), enabling principled long-term planning under uncertainty. However, integrating ASCP with practical RAG attack faces three key challenges: unobservable CMG, intractability in the action space, and feasibility constraints. To overcome these challenges, we maintain a global attacker-side state to guide the attack. Building on this idea, we introduce RAGCRAWLER, which builds a knowledge graph to represent revealed information, uses this global state to estimate CMG, and plans queries in semantic space that target unretrieved regions. In comprehensive experiments across diverse RAG architectures and datasets, our proposed method, RAGCRAWLER, consistently outperforms all baselines. It achieves up to 84.4% corpus coverage within a fixed query budget and deliver an average improvement of 20.7% over the top-performing baseline. It also maintains high semantic fidelity and strong content reconstruction accuracy with low attack cost. Crucially, RAGCRAWLER proves its robustness by maintaining effectiveness against advanced RAG systems employing query rewriting and multi-query retrieval strategies. Our work reveals significant security gaps and highlights the pressing need for stronger safeguards for RAG.

