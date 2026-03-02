---
layout: default
title: Moment Matters: Mean and Variance Causal Graph Discovery from Heteroscedastic Observational Data
---

# Moment Matters: Mean and Variance Causal Graph Discovery from Heteroscedastic Observational Data
**arXiv**：[2602.23602v1](https://arxiv.org/abs/2602.23602) · [PDF](https://arxiv.org/pdf/2602.23602.pdf)  
**作者**：Yoichi Chikahara  

**一句话要点**：提出贝叶斯矩驱动因果发现框架，从异方差观测数据中推断均值和方差因果图。

**关键词**：因果发现, 异方差数据, 贝叶斯推理, 矩分析, 变分推断, 不确定性量化

## 3 点简述
- 核心问题：标准因果发现无法区分影响均值与方差的因果，限制可解释性和干预设计。
- 方法要点：基于可识别性理论，开发变分推理方法学习两个图的后验分布，支持不确定性量化。
- 实验或效果：在合成、半合成和真实数据上准确恢复均值和方差结构，优于现有基线。

## 摘要（原文）

> Heteroscedasticity -- where the variance of a variable changes with other variables -- is pervasive in real data, and elucidating why it arises from the perspective of statistical moments is crucial in scientific knowledge discovery and decision-making. However, standard causal discovery does not reveal which causes act on the mean versus the variance, as it returns a single moment-agnostic graph, limiting interpretability and downstream intervention design. We propose a Bayesian, moment-driven causal discovery framework that infers separate \textit{mean} and \textit{variance} causal graphs from observational heteroscedastic data. We first derive the identification results by establishing sufficient conditions under which these two graphs are separately identifiable. Building on this theory, we develop a variational inference method that learns a posterior distribution over both graphs, enabling principled uncertainty quantification of structural features (e.g., edges, paths, and subgraphs). To address the challenges of parameter optimization in heteroscedastic models with two graph structures, we take a curvature-aware optimization approach and develop a prior incorporation technique that leverages domain knowledge on node orderings, improving sample efficiency. Experiments on synthetic, semi-synthetic, and real data show that our approach accurately recovers mean and variance structures and outperforms state-of-the-art baselines.

