---
layout: default
title: PRISM: Purified Representation and Integrated Semantic Modeling for Generative Sequential Recommendation
---

# PRISM: Purified Representation and Integrated Semantic Modeling for Generative Sequential Recommendation
**arXiv**：[2601.16556v1](https://arxiv.org/abs/2601.16556) · [PDF](https://arxiv.org/pdf/2601.16556.pdf)  
**作者**：Dengzhao Fang, Jingtong Gao, Yu Li, Xiangyu Zhao, Yi Chang  

**一句话要点**：提出PRISM框架，通过净化表示和集成语义建模解决生成式序列推荐中的语义歧义和信息损失问题。

**关键词**：生成式序列推荐, 语义量化, 语义建模, 推荐系统, 稀疏数据

## 3 点简述
- 核心问题：现有生成式序列推荐存在语义标记歧义和生成过程信息损失，影响推荐准确性。
- 方法要点：设计净化语义量化器增强语义区分度，集成语义推荐器补偿信息损失并强化逻辑结构。
- 实验或效果：在四个真实数据集上超越基线，尤其在稀疏场景下性能提升显著。

## 摘要（原文）

> Generative Sequential Recommendation (GSR) has emerged as a promising paradigm, reframing recommendation as an autoregressive sequence generation task over discrete Semantic IDs (SIDs), typically derived via codebook-based quantization. Despite its great potential in unifying retrieval and ranking, existing GSR frameworks still face two critical limitations: (1) impure and unstable semantic tokenization, where quantization methods struggle with interaction noise and codebook collapse, resulting in SIDs with ambiguous discrimination; and (2) lossy and weakly structured generation, where reliance solely on coarse-grained discrete tokens inevitably introduces information loss and neglects items' hierarchical logic. To address these issues, we propose a novel generative recommendation framework, PRISM, with Purified Representation and Integrated Semantic Modeling. Specifically, to ensure high-quality tokenization, we design a Purified Semantic Quantizer that constructs a robust codebook via adaptive collaborative denoising and hierarchical semantic anchoring mechanisms. To compensate for information loss during quantization, we further propose an Integrated Semantic Recommender, which incorporates a dynamic semantic integration mechanism to integrate fine-grained semantics and enforces logical validity through a semantic structure alignment objective. PRISM consistently outperforms state-of-the-art baselines across four real-world datasets, demonstrating substantial performance gains, particularly in high-sparsity scenarios.

