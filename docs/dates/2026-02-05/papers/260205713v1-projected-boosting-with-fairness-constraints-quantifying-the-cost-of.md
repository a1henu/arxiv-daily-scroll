---
layout: default
title: Projected Boosting with Fairness Constraints: Quantifying the Cost of Fair Training Distributions
---

# Projected Boosting with Fairness Constraints: Quantifying the Cost of Fair Training Distributions
**arXiv**：[2602.05713v1](https://arxiv.org/abs/2602.05713) · [PDF](https://arxiv.org/pdf/2602.05713.pdf)  
**作者**：Amir Asiaee, Kaveh Aryan  

**一句话要点**：提出FairBoost方法，在Boosting中融入公平约束以量化公平训练分布的成本

**关键词**：Boosting算法, 公平机器学习, 训练分布投影, KL散度, 准确性-公平性权衡, 弱学习器边缘

## 3 点简述
- 研究如何在Boosting算法中整合群体公平约束，同时保持可分析训练动态
- 通过投影集成诱导的指数权重分布到满足公平约束的凸集，训练弱学习器
- 理论证明收敛率取决于弱学习器边缘减去公平成本项，实验验证公平-准确性权衡

## 摘要（原文）

> Boosting algorithms enjoy strong theoretical guarantees: when weak learners maintain positive edge, AdaBoost achieves geometric decrease of exponential loss. We study how to incorporate group fairness constraints into boosting while preserving analyzable training dynamics. Our approach, FairBoost, projects the ensemble-induced exponential-weights distribution onto a convex set of distributions satisfying fairness constraints (as a reweighting surrogate), then trains weak learners on this fair distribution. The key theoretical insight is that projecting the training distribution reduces the effective edge of weak learners by a quantity controlled by the KL-divergence of the projection. We prove an exponential-loss bound where the convergence rate depends on weak learner edge minus a "fairness cost" term $δ_t = \sqrt{\mathrm{KL}(w^t \\| q^t)/2}$. This directly quantifies the accuracy-fairness tradeoff in boosting dynamics. Experiments on standard benchmarks validate the theoretical predictions and demonstrate competitive fairness-accuracy tradeoffs with stable training curves.

