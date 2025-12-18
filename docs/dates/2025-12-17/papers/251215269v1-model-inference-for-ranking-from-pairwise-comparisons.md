---
layout: default
title: Model inference for ranking from pairwise comparisons
---

# Model inference for ranking from pairwise comparisons
**arXiv**：[2512.15269v1](https://arxiv.org/abs/2512.15269) · [PDF](https://arxiv.org/pdf/2512.15269.pdf)  
**作者**：Daniel Sánchez Catalina, George T. Cantwell  

**一句话要点**：提出贝叶斯算法以从噪声成对比较中推断排名和映射函数

**关键词**：成对比较排名, 贝叶斯推断, 模型不确定性, 强度映射函数, 真实数据案例

## 3 点简述
- 核心问题：从噪声成对比较中排名对象，如网球选手排名，未知强度如何影响比较结果
- 方法要点：同时推断未观测强度和强度到概率的映射函数，采用贝叶斯方法处理模型不确定性
- 实验或效果：实验显示结论对不同模型设定稳健，案例研究验证了真实数据集上的应用

## 摘要（原文）

> We consider the problem of ranking objects from noisy pairwise comparisons, for example, ranking tennis players from the outcomes of matches. We follow a standard approach to this problem and assume that each object has an unobserved strength and that the outcome of each comparison depends probabilistically on the strengths of the comparands. However, we do not assume to know a priori how skills affect outcomes. Instead, we present an efficient algorithm for simultaneously inferring both the unobserved strengths and the function that maps strengths to probabilities. Despite this problem being under-constrained, we present experimental evidence that the conclusions of our Bayesian approach are robust to different model specifications. We include several case studies to exemplify the method on real-world data sets.

