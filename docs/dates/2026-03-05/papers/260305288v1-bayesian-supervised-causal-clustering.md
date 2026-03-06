---
layout: default
title: Bayesian Supervised Causal Clustering
---

# Bayesian Supervised Causal Clustering
**arXiv**：[2603.05288v1](https://arxiv.org/abs/2603.05288) · [PDF](https://arxiv.org/pdf/2603.05288.pdf)  
**作者**：Luwei Wang, Nazir Lone, Sohan Seth  

**一句话要点**：提出贝叶斯监督因果聚类以识别治疗效应相似的患者亚组

**关键词**：贝叶斯聚类, 监督聚类, 因果推断, 患者亚组识别, 治疗效果异质性

## 3 点简述
- 核心问题：现有无监督聚类方法难以在特定结果背景下识别可操作的患者亚组
- 方法要点：基于贝叶斯框架，以治疗效果为监督信号，引导聚类过程，确保协变量和治疗效应均相似
- 实验或效果：在模拟数据和真实世界卒中试验数据上评估，验证了框架的实用性

## 摘要（原文）

> Finding patient subgroups with similar characteristics is crucial for personalized decision-making in various disciplines such as healthcare and policy evaluation. While most existing approaches rely on unsupervised clustering methods, there is a growing trend toward using supervised clustering methods that identify operationalizable subgroups in the context of a specific outcome of interest. We propose Bayesian Supervised Causal Clustering (BSCC), with treatment effect as outcome to guide the clustering process. BSCC identifies homogenous subgroups of individuals who are similar in their covariate profiles as well as their treatment effects. We evaluate BSCC on simulated datasets as well as real-world dataset from the third International Stroke Trial to assess the practical usefulness of the framework.

