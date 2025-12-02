---
layout: default
title: Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding
---

# Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding
**arXiv**：[2512.01565v1](https://arxiv.org/abs/2512.01565) · [PDF](https://arxiv.org/pdf/2512.01565.pdf)  
**作者**：Alex Oshin, Rahul Vodeb Ghosh, Augustinos D. Saravanos, Evangelos A. Theodorou  

**一句话要点**：提出Deep FlexQP，通过深度展开加速非线性规划求解，提升优化器性能与泛化能力。

**关键词**：深度展开, 二次规划优化, 非线性规划加速, 泛化性能保证, 数据驱动优化, 预测安全滤波器

## 3 点简述
- 核心问题：传统二次规划（QP）优化器在约束不可行时性能受限，且难以高效处理高维问题。
- 方法要点：基于FlexQP，通过深度展开学习参数反馈策略，实现数据驱动的加速与维度无关的泛化。
- 实验或效果：在投资组合优化、分类和回归等基准测试中，优于现有加速QP方法，提供PAC贝叶斯泛化保证。

## 摘要（原文）

> We propose an always-feasible quadratic programming (QP) optimizer, FlexQP, which is based on an exact relaxation of the QP constraints. If the original constraints are feasible, then the optimizer finds the optimal solution to the original QP. On the other hand, if the constraints are infeasible, the optimizer identifies a solution that minimizes the constraint violation in a sparse manner. FlexQP scales favorably with respect to the problem dimension, is robust to both feasible and infeasible QPs with minimal assumptions on the problem data, and can be effectively warm-started. We subsequently apply deep unfolding to improve our optimizer through data-driven techniques, leading to an accelerated Deep FlexQP. By learning dimension-agnostic feedback policies for the parameters from a small number of training examples, Deep FlexQP generalizes to problems with larger dimensions and can optimize for many more iterations than it was initially trained for. Our approach outperforms two recently proposed state-of-the-art accelerated QP approaches on a suite of benchmark systems including portfolio optimization, classification, and regression problems. We provide guarantees on the expected performance of our deep QP optimizer through probably approximately correct (PAC) Bayes generalization bounds. These certificates are used to design an accelerated sequential quadratic programming solver that solves nonlinear optimal control and predictive safety filter problems faster than traditional approaches. Overall, our approach is very robust and greatly outperforms existing non-learning and learning-based optimizers in terms of both runtime and convergence to the optimal solution across multiple classes of NLPs.

