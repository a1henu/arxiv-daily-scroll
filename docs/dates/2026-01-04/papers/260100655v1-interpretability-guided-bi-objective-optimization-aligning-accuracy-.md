---
layout: default
title: Interpretability-Guided Bi-objective Optimization: Aligning Accuracy and Explainability
---

# Interpretability-Guided Bi-objective Optimization: Aligning Accuracy and Explainability
**arXiv**：[2601.00655v1](https://arxiv.org/abs/2601.00655) · [PDF](https://arxiv.org/pdf/2601.00655.pdf)  
**作者**：Kasra Fouladi, Hamta Rahmani  

**一句话要点**：提出可解释性引导的双目标优化框架，以在时间序列数据中平衡准确性与可解释性。

**关键词**：可解释性优化, 双目标优化, 时间序列分析, 特征重要性, 有向无环图, 分布外问题

## 3 点简述
- 核心问题：在训练可解释模型时，如何结合领域知识并处理特征重要性计算中的分布外问题。
- 方法要点：使用有向无环图编码特征重要性层次，并引入最优路径预言机改进时间积分梯度。
- 实验或效果：理论分析证明收敛性和鲁棒性，实证显示在时间序列数据上能有效实施约束且精度损失最小。

## 摘要（原文）

> This paper introduces Interpretability-Guided Bi-objective Optimization (IGBO), a framework that trains interpretable models by incorporating structured domain knowledge via a bi-objective formulation. IGBO encodes feature importance hierarchies as a Directed Acyclic Graph (DAG) and uses Temporal Integrated Gradients (TIG) to measure feature importance. To address the Out-of-Distribution (OOD) problem in TIG computation, we propose an Optimal Path Oracle that learns data-manifold-aware integration paths. Theoretical analysis proves convergence properties and robustness to mini-batch noise, while empirical results on time-series data demonstrate IGBO's effectiveness in enforcing DAG constraints with minimal accuracy loss, outperforming standard regularization baselines.

