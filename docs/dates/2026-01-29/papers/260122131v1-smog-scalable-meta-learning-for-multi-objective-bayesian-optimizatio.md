---
layout: default
title: SMOG: Scalable Meta-Learning for Multi-Objective Bayesian Optimization
---

# SMOG: Scalable Meta-Learning for Multi-Objective Bayesian Optimization
**arXiv**：[2601.22131v1](https://arxiv.org/abs/2601.22131) · [PDF](https://arxiv.org/pdf/2601.22131.pdf)  
**作者**：Leonard Papenmeier, Petru Tighineanu  

**一句话要点**：提出SMOG模型，基于多输出高斯过程，为多目标贝叶斯优化提供可扩展的元学习先验。

**关键词**：多目标优化, 贝叶斯优化, 元学习, 高斯过程, 可扩展性

## 3 点简述
- 核心问题：多目标优化中，历史数据未被有效利用，元学习与多目标贝叶斯优化结合方法不足。
- 方法要点：构建结构化联合高斯过程先验，学习目标间相关性，支持分层并行训练以提升可扩展性。
- 实验或效果：模型与标准多目标贝叶斯优化采集函数无缝集成，未知具体性能提升。

## 摘要（原文）

> Multi-objective optimization aims to solve problems with competing objectives, often with only black-box access to a problem and a limited budget of measurements. In many applications, historical data from related optimization tasks is available, creating an opportunity for meta-learning to accelerate the optimization. Bayesian optimization, as a promising technique for black-box optimization, has been extended to meta-learning and multi-objective optimization independently, but methods that simultaneously address both settings - meta-learned priors for multi-objective Bayesian optimization - remain largely unexplored. We propose SMOG, a scalable and modular meta-learning model based on a multi-output Gaussian process that explicitly learns correlations between objectives. SMOG builds a structured joint Gaussian process prior across meta- and target tasks and, after conditioning on metadata, yields a closed-form target-task prior augmented by a flexible residual multi-output kernel. This construction propagates metadata uncertainty into the target surrogate in a principled way. SMOG supports hierarchical, parallel training: meta-task Gaussian processes are fit once and then cached, achieving linear scaling with the number of meta-tasks. The resulting surrogate integrates seamlessly with standard multi-objective Bayesian optimization acquisition functions.

