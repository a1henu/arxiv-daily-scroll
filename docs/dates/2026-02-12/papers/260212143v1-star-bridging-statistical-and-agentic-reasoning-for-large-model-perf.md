---
layout: default
title: STAR : Bridging Statistical and Agentic Reasoning for Large Model Performance Prediction
---

# STAR : Bridging Statistical and Agentic Reasoning for Large Model Performance Prediction
**arXiv**：[2602.12143v1](https://arxiv.org/abs/2602.12143) · [PDF](https://arxiv.org/pdf/2602.12143.pdf)  
**作者**：Xiaoxiao Wang, Chunxiao Li, Junying Wang, Yijin Guo, Zijian Chen, Chunyi Li, Xiaohong Liu, Zicheng Zhang, Guangtao Zhai  

**一句话要点**：提出STAR框架，结合统计与智能推理以预测大模型性能，解决评估成本高和数据稀疏问题。

**关键词**：大模型性能预测, 统计推理, 智能体推理, 约束概率矩阵分解, 期望违背理论, 稀疏数据评估

## 3 点简述
- 核心问题：大模型全面评估成本高昂，现有统计方法难以处理模式偏移、数据稀疏和缺乏解释性。
- 方法要点：STAR通过检索外部知识嵌入约束概率矩阵分解生成统计期望，并基于期望违背理论进行推理调整。
- 实验或效果：在极端稀疏条件下，STAR在得分和排名指标上优于基线，总得分提升14.46%。

## 摘要（原文）

> As comprehensive large model evaluation becomes prohibitively expensive, predicting model performance from limited observations has become essential. However, existing statistical methods struggle with pattern shifts, data sparsity, and lack of explanation, while pure LLM methods remain unreliable. We propose STAR, a framework that bridges data-driven STatistical expectations with knowledge-driven Agentic Reasoning. STAR leverages specialized retrievers to gather external knowledge and embeds semantic features into Constrained Probabilistic Matrix Factorization (CPMF) to generate statistical expectations with uncertainty. A reasoning module guided by Expectation Violation Theory (EVT) then refines predictions through intra-family analysis, cross-model comparison, and credibility-aware aggregation, producing adjustments with traceable explanations. Extensive experiments show that STAR consistently outperforms all baselines on both score-based and rank-based metrics, delivering a 14.46% gain in total score over the strongest statistical method under extreme sparsity, with only 1--2 observed scores per test model.

