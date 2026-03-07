---
layout: default
title: Bayesian Supervised Causal Clustering
---

# Bayesian Supervised Causal Clustering
**arXiv**：[2603.05288v1](https://arxiv.org/abs/2603.05288) · [PDF](https://arxiv.org/pdf/2603.05288.pdf)  
**作者**：Luwei Wang, Nazir Lone, Sohan Seth  

**一句话要点**：提出贝叶斯监督因果聚类以识别具有相似协变量和因果效应的患者亚组

**关键词**：贝叶斯聚类, 因果推断, 监督学习, 患者亚组识别, 个性化决策

## 3 点简述
- 核心问题：现有聚类方法多无监督，需监督方法识别与特定结果相关的可操作亚组
- 方法要点：基于贝叶斯框架，以因果效应为监督信号，聚类个体协变量和因果效应
- 实验或效果：在模拟和真实卒中试验数据上评估，验证框架的实用性和有效性

## 摘要（原文）

> Finding patient subgroups with similar characteristics is crucial for personalized decision-making in various disciplines such as healthcare and policy evaluation. While most existing approaches rely on unsupervised clustering methods, there is a growing trend toward using supervised clustering methods that identify operationalizable subgroups in the context of a specific outcome of interest. We propose Bayesian Supervised Causal Clustering (BSCC), with treatment effect as outcome to guide the clustering process. BSCC identifies homogenous subgroups of individuals who are similar in their covariate profiles as well as their treatment effects. We evaluate BSCC on simulated datasets as well as real-world dataset from the third International Stroke Trial to assess the practical usefulness of the framework.

