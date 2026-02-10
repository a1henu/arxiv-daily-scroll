---
layout: default
title: FairRARI: A Plug and Play Framework for Fairness-Aware PageRank
---

# FairRARI: A Plug and Play Framework for Fairness-Aware PageRank
**arXiv**：[2602.08589v1](https://arxiv.org/abs/2602.08589) · [PDF](https://arxiv.org/pdf/2602.08589.pdf)  
**作者**：Emmanouil Kariotakis, Aritra Konar  

**一句话要点**：提出FairRARI框架，以凸优化方法解决PageRank算法中的群体公平性问题。

**关键词**：PageRank算法, 算法公平性, 凸优化, 图机器学习, 群体公平标准

## 3 点简述
- 核心问题：现有方法在PageRank中实现群体公平性时，缺乏保证目标公平水平或最优性的原则性算法。
- 方法要点：基于变分公式，通过强凸优化问题约束公平性，以“即插即用”方式处理多种公平标准。
- 实验或效果：在真实数据集上，FairRARI在保持实用性的同时达到目标公平水平，优于现有方法。

## 摘要（原文）

> PageRank (PR) is a fundamental algorithm in graph machine learning tasks. Owing to the increasing importance of algorithmic fairness, we consider the problem of computing PR vectors subject to various group-fairness criteria based on sensitive attributes of the vertices. At present, principled algorithms for this problem are lacking - some cannot guarantee that a target fairness level is achieved, while others do not feature optimality guarantees. In order to overcome these shortcomings, we put forth a unified in-processing convex optimization framework, termed FairRARI, for tackling different group-fairness criteria in a ``plug and play'' fashion. Leveraging a variational formulation of PR, the framework computes fair PR vectors by solving a strongly convex optimization problem with fairness constraints, thereby ensuring that a target fairness level is achieved. We further introduce three different fairness criteria which can be efficiently tackled using FairRARI to compute fair PR vectors with the same asymptotic time-complexity as the original PR algorithm. Extensive experiments on real-world datasets showcase that FairRARI outperforms existing methods in terms of utility, while achieving the desired fairness levels across multiple vertex groups; thereby highlighting its effectiveness.

