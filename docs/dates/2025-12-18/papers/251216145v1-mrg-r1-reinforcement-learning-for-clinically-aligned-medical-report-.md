---
layout: default
title: MRG-R1: Reinforcement Learning for Clinically Aligned Medical Report Generation
---

# MRG-R1: Reinforcement Learning for Clinically Aligned Medical Report Generation
**arXiv**：[2512.16145v1](https://arxiv.org/abs/2512.16145) · [PDF](https://arxiv.org/pdf/2512.16145.pdf)  
**作者**：Pengyu Wang, Shuchang Ye, Usman Naseem, Jinman Kim  

**一句话要点**：提出语义驱动强化学习方法MRG-R1，以提升医学报告生成的临床正确性。

**关键词**：医学报告生成, 强化学习, 临床正确性, 大型视觉语言模型, 语义驱动优化

## 3 点简述
- 现有医学报告生成方法依赖词级目标，导致临床准确性不足。
- 采用组相对策略优化和基于边缘余弦相似度的报告级奖励，直接对齐临床标签。
- 在IU X-Ray和MIMIC-CXR数据集上实现最优临床效能指标，验证语义强化优于词级监督。

## 摘要（原文）

> Medical report generation (MRG) aims to automatically derive radiology-style reports from medical images to aid in clinical decision-making. However, existing methods often generate text that mimics the linguistic style of radiologists but fails to guarantee clinical correctness, because they are trained on token-level objectives which focus on word-choice and sentence structure rather than actual medical accuracy. We propose a semantic-driven reinforcement learning (SRL) method for medical report generation, adopted on a large vision-language model (LVLM). SRL adopts Group Relative Policy Optimization (GRPO) to encourage clinical-correctness-guided learning beyond imitation of language style. Specifically, we optimise a report-level reward: a margin-based cosine similarity (MCCS) computed between key radiological findings extracted from generated and reference reports, thereby directly aligning clinical-label agreement and improving semantic correctness. A lightweight reasoning format constraint further guides the model to generate structured "thinking report" outputs. We evaluate Medical Report Generation with Sematic-driven Reinforment Learning (MRG-R1), on two datasets: IU X-Ray and MIMIC-CXR using clinical efficacy (CE) metrics. MRG-R1 achieves state-of-the-art performance with CE-F1 51.88 on IU X-Ray and 40.39 on MIMIC-CXR. We found that the label-semantic reinforcement is better than conventional token-level supervision. These results indicate that optimizing a clinically grounded, report-level reward rather than token overlap,meaningfully improves clinical correctness. This work is a prior to explore semantic-reinforcement in supervising medical correctness in medical Large vision-language model(Med-LVLM) training.

