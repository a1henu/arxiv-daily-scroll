---
layout: default
title: Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning
---

# Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning
**arXiv**：[2602.17565v1](https://arxiv.org/abs/2602.17565) · [PDF](https://arxiv.org/pdf/2602.17565.pdf)  
**作者**：Hien Dang, Pratik Patil, Alessandro Rinaldo  

**一句话要点**：提出无约束自蒸馏在岭回归中的严格改进理论、精确渐近分析与单次调优方法

**关键词**：自蒸馏, 岭回归, 泛化改进, 渐近分析, 最优调优, 无约束学习

## 3 点简述
- 研究无约束自蒸馏在岭回归中的泛化改进，允许混合权重超出单位区间
- 证明最优混合学生严格优于岭教师，推导闭式最优权重与精确渐近风险
- 提出一致单次调优方法估计最优权重，实验验证理论与方法有效性

## 摘要（原文）

> Self-distillation (SD) is the process of retraining a student on a mixture of ground-truth labels and the teacher's own predictions using the same architecture and training data. Although SD has been empirically shown to often improve generalization, its formal guarantees remain limited. We study SD for ridge regression in unconstrained setting in which the mixing weight $ξ$ may be outside the unit interval. Conditioned on the training data and without any distributional assumptions, we prove that for any squared prediction risk (including out-of-distribution), the optimally mixed student strictly improves upon the ridge teacher for every regularization level $λ> 0$ at which the teacher ridge risk $R(λ)$ is nonstationary (i.e., $R'(λ) \neq 0$). We obtain a closed-form expression for the optimal mixing weight $ξ^\star(λ)$ for any value of $λ$ and show that it obeys the sign rule: $\operatorname{sign}(ξ^\star(λ))=-\operatorname{sign}(R'(λ))$. In particular, $ξ^\star(λ)$ can be negative, which is the case in over-regularized regimes. To quantify the risk improvement due to SD, we derive exact deterministic equivalents for the optimal SD risk in the proportional asymptotics regime (where the sample and feature sizes $n$ and $p$ both diverge but their aspect ratio $p/n$ converges) under general anisotropic covariance and deterministic signals. Our asymptotic analysis extends standard second-order ridge deterministic equivalents to their fourth-order analogs using block linearization, which may be of independent interest. From a practical standpoint, we propose a consistent one-shot tuning method to estimate $ξ^\star$ without grid search, sample splitting, or refitting. Experiments on real-world datasets and pretrained neural network features support our theory and the one-shot tuning method.

