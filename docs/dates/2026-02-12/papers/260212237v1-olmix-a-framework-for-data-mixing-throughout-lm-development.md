---
layout: default
title: Olmix: A Framework for Data Mixing Throughout LM Development
---

# Olmix: A Framework for Data Mixing Throughout LM Development
**arXiv**：[2602.12237v1](https://arxiv.org/abs/2602.12237) · [PDF](https://arxiv.org/pdf/2602.12237.pdf)  
**作者**：Mayee F. Chen, Tyler Murray, David Heineman, Matt Jordan, Hannaneh Hajishirzi, Christopher Ré, Luca Soldaini, Kyle Lo  

**一句话要点**：提出Olmix框架以解决语言模型开发中数据混合的配置挑战和动态域集更新问题

**关键词**：数据混合, 语言模型训练, 动态域集, 混合重用, 配置优化

## 3 点简述
- 核心问题：现有数据混合方法在真实LM开发中面临配置空间不明确和域集动态变化的挑战
- 方法要点：通过实证研究确定混合方法设计选择，并引入混合重用机制高效更新混合比例
- 实验或效果：在模拟真实开发的更新序列中，混合重用匹配全重算性能，计算减少74%，下游任务提升11.6%

## 摘要（原文）

> Data mixing -- determining the ratios of data from different domains -- is a first-order concern for training language models (LMs). While existing mixing methods show promise, they fall short when applied during real-world LM development. We present Olmix, a framework that addresses two such challenges. First, the configuration space for developing a mixing method is not well understood -- design choices across existing methods lack justification or consensus and overlook practical issues like data constraints. We conduct a comprehensive empirical study of this space, identifying which design choices lead to a strong mixing method. Second, in practice, the domain set evolves throughout LM development as datasets are added, removed, partitioned, and revised -- a problem setting largely unaddressed by existing works, which assume fixed domains. We study how to efficiently recompute the mixture after the domain set is updated, leveraging information from past mixtures. We introduce mixture reuse, a mechanism that reuses existing ratios and recomputes ratios only for domains affected by the update. Over a sequence of five domain-set updates mirroring real-world LM development, mixture reuse matches the performance of fully recomputing the mix after each update with 74% less compute and improves over training without mixing by 11.6% on downstream tasks.

