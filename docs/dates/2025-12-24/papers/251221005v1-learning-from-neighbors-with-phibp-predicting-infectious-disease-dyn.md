---
layout: default
title: Learning from Neighbors with PHIBP: Predicting Infectious Disease Dynamics in Data-Sparse Environments
---

# Learning from Neighbors with PHIBP: Predicting Infectious Disease Dynamics in Data-Sparse Environments
**arXiv**：[2512.21005v1](https://arxiv.org/abs/2512.21005) · [PDF](https://arxiv.org/pdf/2512.21005.pdf)  
**作者**：Edwin Fong, Lancelot F. James, Juho Lee  

**一句话要点**：提出PHIBP框架以预测零病例地区的传染病爆发

**关键词**：稀疏计数数据, 传染病预测, 分层贝叶斯模型, 绝对丰度, 零病例处理, 流行病学建模

## 3 点简述
- 核心问题：处理稀疏计数数据，预测历史零病例地区的传染病动态。
- 方法要点：基于绝对丰度的泊松分层印度自助餐过程，从相关区域借统计强度。
- 实验或效果：在传染病数据上验证，提供稳健预测分布和流行病学洞见。

## 摘要（原文）

> Modeling sparse count data, which arise across numerous scientific fields, presents significant statistical challenges. This chapter addresses these challenges in the context of infectious disease prediction, with a focus on predicting outbreaks in geographic regions that have historically reported zero cases. To this end, we present the detailed computational framework and experimental application of the Poisson Hierarchical Indian Buffet Process (PHIBP), with demonstrated success in handling sparse count data in microbiome and ecological studies. The PHIBP's architecture, grounded in the concept of absolute abundance, systematically borrows statistical strength from related regions and circumvents the known sensitivities of relative-rate methods to zero counts. Through a series of experiments on infectious disease data, we show that this principled approach provides a robust foundation for generating coherent predictive distributions and for the effective use of comparative measures such as alpha and beta diversity. The chapter's emphasis on algorithmic implementation and experimental results confirms that this unified framework delivers both accurate outbreak predictions and meaningful epidemiological insights in data-sparse settings.

