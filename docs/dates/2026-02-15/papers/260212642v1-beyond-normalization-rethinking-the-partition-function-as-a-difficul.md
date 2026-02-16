---
layout: default
title: Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR
---

# Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR
**arXiv**：[2602.12642v1](https://arxiv.org/abs/2602.12642) · [PDF](https://arxiv.org/pdf/2602.12642.pdf)  
**作者**：Dohyung Kim, Minbeom Kim, Jeonghye Kim, Sangmook Lee, Sojeong Rhee, Kyomin Jung  

**一句话要点**：提出PACED-RL框架，将配分函数重释为在线准确率信号，以提升LLMs分布匹配训练的样本效率。

**关键词**：配分函数重释, 样本效率优化, 分布匹配训练, 强化学习后训练, 大语言模型推理, GFlowNets应用

## 3 点简述
- 核心问题：强化学习优化LLMs推理性能时，常导致输出多样性降低，现有方法忽略配分函数中的准确率信息。
- 方法要点：理论关联配分函数与每提示准确率估计，利用该信号优先训练信息量大的提示，并基于估计误差重放样本。
- 实验或效果：在多个基准测试中，相比GRPO和先前GFlowNet方法，PACED-RL显著提升性能，验证其样本效率优势。

## 摘要（原文）

> Reward-maximizing RL methods enhance the reasoning performance of LLMs, but often reduce the diversity among outputs. Recent works address this issue by adopting GFlowNets, training LLMs to match a target distribution while jointly learning its partition function. In contrast to prior works that treat this partition function solely as a normalizer, we reinterpret it as a per-prompt expected-reward (i.e., online accuracy) signal, leveraging this unused information to improve sample efficiency. Specifically, we first establish a theoretical relationship between the partition function and per-prompt accuracy estimates. Building on this key insight, we propose Partition Function-Guided RL (PACED-RL), a post-training framework that leverages accuracy estimates to prioritize informative question prompts during training, and further improves sample efficiency through an accuracy estimate error-prioritized replay. Crucially, both components reuse information already produced during GFlowNet training, effectively amortizing the compute overhead into the existing optimization process. Extensive experiments across diverse benchmarks demonstrate strong performance improvements over GRPO and prior GFlowNet approaches, highlighting PACED-RL as a promising direction for a more sample efficient distribution-matching training for LLMs.

