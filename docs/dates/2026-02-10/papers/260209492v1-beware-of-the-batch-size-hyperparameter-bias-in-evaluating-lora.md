---
layout: default
title: Beware of the Batch Size: Hyperparameter Bias in Evaluating LoRA
---

# Beware of the Batch Size: Hyperparameter Bias in Evaluating LoRA
**arXiv**：[2602.09492v1](https://arxiv.org/abs/2602.09492) · [PDF](https://arxiv.org/pdf/2602.09492.pdf)  
**作者**：Sangyoon Lee, Jaeho Lee  

**一句话要点**：揭示批次大小在LoRA评估中的超参数偏差，提出成本高效调优策略以提升评估可靠性。

**关键词**：低秩适应, 批次大小调优, 超参数偏差, 大语言模型微调, 评估可靠性

## 3 点简述
- 核心问题：LoRA变体在相同基准上报告矛盾结果，源于批次大小被忽视导致的超参数偏差。
- 方法要点：通过代理策略高效调优批次大小，分析秩、数据集大小和模型容量对最优批次大小的影响。
- 实验或效果：调优后，基础LoRA常匹配复杂变体性能，批次大小从次要细节提升为关键设计参数。

## 摘要（原文）

> Low-rank adaptation (LoRA) is a standard approach for fine-tuning large language models, yet its many variants report conflicting empirical gains, often on the same benchmarks. We show that these contradictions arise from a single overlooked factor: the batch size. When properly tuned, vanilla LoRA often matches the performance of more complex variants. We further propose a proxy-based, cost-efficient strategy for batch size tuning, revealing the impact of rank, dataset size, and model capacity on the optimal batch size. Our findings elevate batch size from a minor implementation detail to a first-order design parameter, reconciling prior inconsistencies and enabling more reliable evaluations of LoRA variants.

