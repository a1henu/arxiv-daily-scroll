---
layout: default
title: AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG
---

# AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG
**arXiv**：[2512.25052v1](https://arxiv.org/abs/2512.25052) · [PDF](https://arxiv.org/pdf/2512.25052.pdf)  
**作者**：Chao Peng, Bin Wang, Zhilei Long, Jinfang Sheng  

**一句话要点**：提出AdaGReS框架，通过冗余感知评分自适应选择上下文，以优化令牌预算下的检索增强生成。

**关键词**：检索增强生成, 冗余感知选择, 令牌预算优化, 自适应贪婪算法, 上下文质量提升

## 3 点简述
- 核心问题：标准top-k检索在RAG中常返回冗余块，浪费令牌预算并降低生成质量。
- 方法要点：基于查询-块相关性和集合内冗余惩罚的集合级目标，进行贪婪选择，并自适应校准权衡参数。
- 实验或效果：在开放域问答和生物医学语料上，提升冗余控制和上下文质量，改善端到端答案质量。

## 摘要（原文）

> Retrieval-augmented generation (RAG) is highly sensitive to the quality of selected context, yet standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation. We present AdaGReS, a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. AdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits. We further provide a theoretical analysis showing that the proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. Experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.

