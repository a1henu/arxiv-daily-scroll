---
layout: default
title: C-kNN-LSH: A Nearest-Neighbor Algorithm for Sequential Counterfactual Inference
---

# C-kNN-LSH: A Nearest-Neighbor Algorithm for Sequential Counterfactual Inference
**arXiv**：[2602.02371v1](https://arxiv.org/abs/2602.02371) · [PDF](https://arxiv.org/pdf/2602.02371.pdf)  
**作者**：Jing Wang, Jie Shen, Qiaomin Xie, Jeremy C Weiss  

**一句话要点**：提出C-kNN-LSH算法，用于高维混杂序列因果推断，以优化临床决策。

**关键词**：序列因果推断, 最近邻算法, 局部敏感哈希, 临床决策优化, 长新冠分析

## 3 点简述
- 核心问题：从纵向轨迹估计因果效应，处理高维混杂和序列数据，如长新冠恢复。
- 方法要点：结合最近邻和局部敏感哈希，高效识别相似历史个体，进行局部效应估计和双重稳健校正。
- 实验或效果：在13,511名长新冠参与者数据上验证，性能优于基线，能捕捉恢复异质性。

## 摘要（原文）

> Estimating causal effects from longitudinal trajectories is central to understanding the progression of complex conditions and optimizing clinical decision-making, such as comorbidities and long COVID recovery. We introduce \emph{C-kNN--LSH}, a nearest-neighbor framework for sequential causal inference designed to handle such high-dimensional, confounded situations. By utilizing locality-sensitive hashing, we efficiently identify ``clinical twins'' with similar covariate histories, enabling local estimation of conditional treatment effects across evolving disease states. To mitigate bias from irregular sampling and shifting patient recovery profiles, we integrate neighborhood estimator with a doubly-robust correction.
>   Theoretical analysis guarantees our estimator is consistent and second-order robust to nuisance error.
>   Evaluated on a real-world Long COVID cohort with 13,511 participants, \emph{C-kNN-LSH} demonstrates superior performance in capturing recovery heterogeneity and estimating policy values compared to existing baselines.

