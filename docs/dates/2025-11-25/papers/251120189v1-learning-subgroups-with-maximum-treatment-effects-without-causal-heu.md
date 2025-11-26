---
layout: default
title: Learning Subgroups with Maximum Treatment Effects without Causal Heuristics
---

# Learning Subgroups with Maximum Treatment Effects without Causal Heuristics
**arXiv**：[2511.20189v1](https://arxiv.org/abs/2511.20189) · [PDF](https://arxiv.org/pdf/2511.20189.pdf)  
**作者**：Lincen Yang, Zhong Li, Matthijs van Leeuwen, Saber Salehkaleybar  

**一句话要点**：提出基于结构因果模型的子群发现方法，用于精准决策场景

**关键词**：子群发现, 结构因果模型, 平均处理效应, 决策树, 监督学习

## 3 点简述
- 核心问题：现有方法依赖点估计或启发式，难以准确发现最大平均处理效应子群
- 方法要点：在SCM框架下，将子群发现转化为标准监督学习问题
- 实验或效果：在合成和半合成数据集上，比基线更准确识别子群

## 摘要（原文）

> Discovering subgroups with the maximum average treatment effect is crucial for targeted decision making in domains such as precision medicine, public policy, and education. While most prior work is formulated in the potential outcome framework, the corresponding structural causal model (SCM) for this task has been largely overlooked. In practice, two approaches dominate. The first estimates pointwise conditional treatment effects and then fits a tree on those estimates, effectively turning subgroup estimation into the harder problem of accurate pointwise estimation. The second constructs decision trees or rule sets with ad-hoc 'causal' heuristics, typically without rigorous justification for why a given heuristic may be used or whether such heuristics are necessary at all. We address these issues by studying the problem directly under the SCM framework. Under the assumption of a partition-based model, we show that optimal subgroup discovery reduces to recovering the data-generating models and hence a standard supervised learning problem (regression or classification). This allows us to adopt any partition-based methods to learn the subgroup from data. We instantiate the approach with CART, arguably one of the most widely used tree-based methods, to learn the subgroup with maximum treatment effect. Finally, on a large collection of synthetic and semi-synthetic datasets, we compare our method against a wide range of baselines and find that our approach, which avoids such causal heuristics, more accurately identifies subgroups with maximum treatment effect. Our source code is available at https://github.com/ylincen/causal-subgroup.

