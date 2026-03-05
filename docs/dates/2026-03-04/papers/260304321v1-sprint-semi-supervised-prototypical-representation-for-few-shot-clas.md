---
layout: default
title: SPRINT: Semi-supervised Prototypical Representation for Few-Shot Class-Incremental Tabular Learning
---

# SPRINT: Semi-supervised Prototypical Representation for Few-Shot Class-Incremental Tabular Learning
**arXiv**：[2603.04321v1](https://arxiv.org/abs/2603.04321) · [PDF](https://arxiv.org/pdf/2603.04321.pdf)  
**作者**：Umid Suleymanov, Murat Kantarcioglu, Kevin S Chan, Michael De Lucia, Kevin Hamlen, Latifur Khan, Sharad Mehrotra, Ananthram Swami, Bhavani Thuraisingham  

**一句话要点**：提出SPRINT框架以解决表格数据的小样本类增量学习问题

**关键词**：小样本学习, 类增量学习, 表格数据, 半监督学习, 伪标签, 跨领域鲁棒性

## 3 点简述
- 核心问题：表格数据的小样本类增量学习在现实应用中未被充分探索，现有视觉方法忽略其无标签数据丰富和存储成本低的特点。
- 方法要点：采用混合情景训练策略，结合置信度伪标签增强新类表示，并利用低存储成本保留基类历史。
- 实验或效果：在六个跨领域基准测试中，SPRINT实现77.37%的平均准确率（5-shot），优于最强基线4.45%。

## 摘要（原文）

> Real-world systems must continuously adapt to novel concepts from limited data without forgetting previously acquired knowledge. While Few-Shot Class-Incremental Learning (FSCIL) is established in computer vision, its application to tabular domains remains largely unexplored. Unlike images, tabular streams (e.g., logs, sensors) offer abundant unlabeled data, a scarcity of expert annotations and negligible storage costs, features ignored by existing vision-based methods that rely on restrictive buffers. We introduce SPRINT, the first FSCIL framework tailored for tabular distributions. SPRINT introduces a mixed episodic training strategy that leverages confidence-based pseudo-labeling to enrich novel class representations and exploits low storage costs to retain base class history. Extensive evaluation across six diverse benchmarks spanning cybersecurity, healthcare, and ecological domains, demonstrates SPRINT's cross-domain robustness. It achieves a state-of-the-art average accuracy of 77.37% (5-shot), outperforming the strongest incremental baseline by 4.45%.

