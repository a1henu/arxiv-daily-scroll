---
layout: default
title: The Wisdom of Many Queries: Complexity-Diversity Principle for Dense Retriever Training
---

# The Wisdom of Many Queries: Complexity-Diversity Principle for Dense Retriever Training
**arXiv**：[2602.09448v1](https://arxiv.org/abs/2602.09448) · [PDF](https://arxiv.org/pdf/2602.09448.pdf)  
**作者**：Xincan Feng, Noriki Nishida, Yusuke Sakai, Yuji Matsumoto  

**一句话要点**：提出复杂度-多样性原则以优化密集检索器训练中的查询多样性策略

**关键词**：密集检索, 查询多样性, 多跳检索, 复杂度-多样性原则, 合成数据生成, 零样本学习

## 3 点简述
- 核心问题：先前研究在密集检索的合成数据生成中关于查询多样性的影响存在矛盾结果
- 方法要点：设计Q-D指标量化多样性影响，并通过实验发现多样性对多跳检索特别有益
- 实验或效果：基于复杂度-多样性原则提出零样本多查询合成方法，在多跳任务中实现最先进性能

## 摘要（原文）

> Prior work reports conflicting results on query diversity in synthetic data generation for dense retrieval. We identify this conflict and design Q-D metrics to quantify diversity's impact, making the problem measurable. Through experiments on 4 benchmark types (31 datasets), we find query diversity especially benefits multi-hop retrieval. Deep analysis on multi-hop data reveals that diversity benefit correlates strongly with query complexity ($r$$\geq$0.95, $p$$<$0.05 in 12/14 conditions), measured by content words (CW). We formalize this as the Complexity-Diversity Principle (CDP): query complexity determines optimal diversity. CDP provides actionable thresholds (CW$>$10: use diversity; CW$<$7: avoid it). Guided by CDP, we propose zero-shot multi-query synthesis for multi-hop tasks, achieving state-of-the-art performance.

