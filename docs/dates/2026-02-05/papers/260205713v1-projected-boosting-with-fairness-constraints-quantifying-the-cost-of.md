---
layout: default
title: Projected Boosting with Fairness Constraints: Quantifying the Cost of Fair Training Distributions
---

# Projected Boosting with Fairness Constraints: Quantifying the Cost of Fair Training Distributions
**arXiv**：[2602.05713v1](https://arxiv.org/abs/2602.05713) · [PDF](https://arxiv.org/pdf/2602.05713.pdf)  
**作者**：Amir Asiaee, Kaveh Aryan  

**一句话要点**：提出FairBoost方法，通过投影训练分布融入公平约束，量化提升算法中的公平性成本。

**关键词**：提升算法, 公平机器学习, 分布投影, KL散度, 训练动态分析, 公平性成本量化

## 3 点简述
- 研究如何在提升算法中融入群体公平约束，同时保持可分析训练动态。
- 方法将集成诱导的指数权重分布投影到满足公平约束的凸集上，作为重加权代理。
- 理论证明收敛率依赖于弱学习器边缘减去公平成本项，实验验证了公平-准确性权衡。

## 摘要（原文）

> Boosting algorithms enjoy strong theoretical guarantees: when weak learners maintain positive edge, AdaBoost achieves geometric decrease of exponential loss. We study how to incorporate group fairness constraints into boosting while preserving analyzable training dynamics. Our approach, FairBoost, projects the ensemble-induced exponential-weights distribution onto a convex set of distributions satisfying fairness constraints (as a reweighting surrogate), then trains weak learners on this fair distribution. The key theoretical insight is that projecting the training distribution reduces the effective edge of weak learners by a quantity controlled by the KL-divergence of the projection. We prove an exponential-loss bound where the convergence rate depends on weak learner edge minus a "fairness cost" term $δ_t = \sqrt{\mathrm{KL}(w^t \\| q^t)/2}$. This directly quantifies the accuracy-fairness tradeoff in boosting dynamics. Experiments on standard benchmarks validate the theoretical predictions and demonstrate competitive fairness-accuracy tradeoffs with stable training curves.

