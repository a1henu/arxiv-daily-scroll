---
layout: default
title: Causal-driven attribution (CDA): Estimating channel influence without user-level data
---

# Causal-driven attribution (CDA): Estimating channel influence without user-level data
**arXiv**：[2512.21211v1](https://arxiv.org/abs/2512.21211) · [PDF](https://arxiv.org/pdf/2512.21211.pdf)  
**作者**：Georgios Filippou, Boi Mai Quach, Diana Lenghel, Arthur White, Ashish Kumar Jha  

**一句话要点**：提出因果驱动归因框架，利用聚合数据解决隐私限制下的营销渠道影响评估问题

**关键词**：因果归因, 营销分析, 隐私保护, 结构因果模型, 时序因果发现

## 3 点简述
- 核心问题：传统归因模型依赖用户级路径数据，但隐私法规和平台限制使其难以获取
- 方法要点：结合时序因果发现和结构因果模型，从聚合印象数据推断渠道关系和贡献
- 实验或效果：在合成数据上，给定真实因果图时相对RMSE为9.50%，预测图时为24.23%，显示高准确性和鲁棒性

## 摘要（原文）

> Attribution modelling lies at the heart of marketing effectiveness, yet most existing approaches depend on user-level path data, which are increasingly inaccessible due to privacy regulations and platform restrictions. This paper introduces a Causal-Driven Attribution (CDA) framework that infers channel influence using only aggregated impression-level data, avoiding any reliance on user identifiers or click-path tracking. CDA integrates temporal causal discovery (using PCMCI) with causal effect estimation via a Structural Causal Model to recover directional channel relationships and quantify their contributions to conversions. Using large-scale synthetic data designed to replicate real marketing dynamics, we show that CDA achieves an average relative RMSE of 9.50% when given the true causal graph, and 24.23% when using the predicted graph, demonstrating strong accuracy under correct structure and meaningful signal recovery even under structural uncertainty. CDA captures cross-channel interdependencies while providing interpretable, privacy-preserving attribution insights, offering a scalable and future-proof alternative to traditional path-based models.

