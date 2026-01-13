---
layout: default
title: Layerwise goal-oriented adaptivity for neural ODEs: an optimal control perspective
---

# Layerwise goal-oriented adaptivity for neural ODEs: an optimal control perspective
**arXiv**：[2601.07397v1](https://arxiv.org/abs/2601.07397) · [PDF](https://arxiv.org/pdf/2601.07397.pdf)  
**作者**：Michael Hintermüller, Michael Hinze, Denis Korolev  

**一句话要点**：提出基于最优控制视角的层间目标导向自适应方法，用于神经ODE网络架构构建。

**关键词**：神经ODE, 最优控制, 自适应网络, 分类任务, 双加权残差

## 3 点简述
- 核心问题：神经ODE网络架构的自适应构建，以提升模型效率和性能。
- 方法要点：采用目标导向双加权残差技术，将问题转化为ODE约束优化，使用DG(0)离散化和最速下降法。
- 实验或效果：应用于数据集分类任务，在多个经典示例中展示结果。

## 摘要（原文）

> In this work, we propose a novel layerwise adaptive construction method for neural network architectures. Our approach is based on a goal--oriented dual-weighted residual technique for the optimal control of neural differential equations. This leads to an ordinary differential equation constrained optimization problem with controls acting as coefficients and a specific loss function. We implement our approach on the basis of a DG(0) Galerkin discretization of the neural ODE, leading to an explicit Euler time marching scheme. For the optimization we use steepest descent. Finally, we apply our method to the construction of neural networks for the classification of data sets, where we present results for a selection of well known examples from the literature.

