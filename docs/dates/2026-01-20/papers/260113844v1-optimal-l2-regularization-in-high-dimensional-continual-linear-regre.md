---
layout: default
title: Optimal L2 Regularization in High-dimensional Continual Linear Regression
---

# Optimal L2 Regularization in High-dimensional Continual Linear Regression
**arXiv**：[2601.13844v1](https://arxiv.org/abs/2601.13844) · [PDF](https://arxiv.org/pdf/2601.13844.pdf)  
**作者**：Gilad Karpel, Edward Moroshko, Ran Levinstein, Ron Meir, Daniel Soudry, Itay Evron  

**一句话要点**：推导高维持续线性回归中L2正则化的最优强度，证明其随任务数近线性缩放

**关键词**：持续学习, 线性回归, L2正则化, 高维统计, 泛化理论, 标签噪声

## 3 点简述
- 研究过参数化持续线性回归中L2正则化对泛化的影响，推导任意线性教师下的闭式解
- 证明各向同性正则化在单教师和多教师设置下缓解标签噪声，最优正则强度随任务数T近似为T/ln T
- 通过线性回归和神经网络实验验证理论，为持续学习系统设计提供实用方案

## 摘要（原文）

> We study generalization in an overparameterized continual linear regression setting, where a model is trained with L2 (isotropic) regularization across a sequence of tasks. We derive a closed-form expression for the expected generalization loss in the high-dimensional regime that holds for arbitrary linear teachers. We demonstrate that isotropic regularization mitigates label noise under both single-teacher and multiple i.i.d. teacher settings, whereas prior work accommodating multiple teachers either did not employ regularization or used memory-demanding methods. Furthermore, we prove that the optimal fixed regularization strength scales nearly linearly with the number of tasks $T$, specifically as $T/\ln T$. To our knowledge, this is the first such result in theoretical continual learning. Finally, we validate our theoretical findings through experiments on linear regression and neural networks, illustrating how this scaling law affects generalization and offering a practical recipe for the design of continual learning systems.

