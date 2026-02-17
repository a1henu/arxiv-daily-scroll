---
layout: default
title: Covariance-Aware Transformers for Quadratic Programming and Decision Making
---

# Covariance-Aware Transformers for Quadratic Programming and Decision Making
**arXiv**：[2602.14506v1](https://arxiv.org/abs/2602.14506) · [PDF](https://arxiv.org/pdf/2602.14506.pdf)  
**作者**：Kutay Tire, Yufan Zhang, Ege Onur Taga, Samet Oymak  

**一句话要点**：提出Covariance-Aware Transformers以解决二次规划和涉及协方差的决策问题

**关键词**：Transformer, 二次规划, 协方差矩阵, 决策制定, 投资组合优化, 时间序列模型

## 3 点简述
- 核心问题：探索Transformer如何有效解决二次规划问题，并应用于涉及协方差矩阵的决策任务。
- 方法要点：通过线性注意力机制模拟梯度下降，结合MLP处理ℓ1惩罚和约束的二次规划，并引入Time2Decide方法增强时间序列基础模型。
- 实验或效果：Time2Decide在投资组合优化中优于基础模型和预测后优化方法，证明Transformer能利用二阶统计量单次前向解决复杂决策问题。

## 摘要（原文）

> We explore the use of transformers for solving quadratic programs and how this capability benefits decision-making problems that involve covariance matrices. We first show that the linear attention mechanism can provably solve unconstrained QPs by tokenizing the matrix variables (e.g.~$A$ of the objective $\frac{1}{2}x^\top Ax+b^\top x$) row-by-row and emulating gradient descent iterations. Furthermore, by incorporating MLPs, a transformer block can solve (i) $\ell_1$-penalized QPs by emulating iterative soft-thresholding and (ii) $\ell_1$-constrained QPs when equipped with an additional feedback loop. Our theory motivates us to introduce Time2Decide: a generic method that enhances a time series foundation model (TSFM) by explicitly feeding the covariance matrix between the variates. We empirically find that Time2Decide uniformly outperforms the base TSFM model for the classical portfolio optimization problem that admits an $\ell_1$-constrained QP formulation. Remarkably, Time2Decide also outperforms the classical "Predict-then-Optimize (PtO)" procedure, where we first forecast the returns and then explicitly solve a constrained QP, in suitable settings. Our results demonstrate that transformers benefit from explicit use of second-order statistics, and this can enable them to effectively solve complex decision-making problems, like portfolio construction, in one forward pass.

