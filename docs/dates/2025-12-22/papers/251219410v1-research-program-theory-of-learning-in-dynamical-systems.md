---
layout: default
title: Research Program: Theory of Learning in Dynamical Systems
---

# Research Program: Theory of Learning in Dynamical Systems
**arXiv**：[2512.19410v1](https://arxiv.org/abs/2512.19410) · [PDF](https://arxiv.org/pdf/2512.19410.pdf)  
**作者**：Elad Hazan, Shai Shalev Shwartz, Nathan Srebro  

**一句话要点**：提出动态可学习性理论框架，基于下一令牌预测研究动态系统的有限样本学习问题。

**关键词**：动态系统学习, 有限样本理论, 下一令牌预测, 谱滤波, 可学习性框架

## 3 点简述
- 核心问题：动态系统仅从观测中何时可学习，关注有限样本和系统结构属性。
- 方法要点：定义动态可学习性，强调稳定性、混合性等结构对观测需求的影响。
- 实验或效果：在线性动态系统中，通过谱滤波实现有限观测后的准确预测，无需系统辨识。

## 摘要（原文）

> Modern learning systems increasingly interact with data that evolve over time and depend on hidden internal state. We ask a basic question: when is such a dynamical system learnable from observations alone? This paper proposes a research program for understanding learnability in dynamical systems through the lens of next-token prediction. We argue that learnability in dynamical systems should be studied as a finite-sample question, and be based on the properties of the underlying dynamics rather than the statistical properties of the resulting sequence. To this end, we give a formulation of learnability for stochastic processes induced by dynamical systems, focusing on guarantees that hold uniformly at every time step after a finite burn-in period. This leads to a notion of dynamic learnability which captures how the structure of a system, such as stability, mixing, observability, and spectral properties, governs the number of observations required before reliable prediction becomes possible. We illustrate the framework in the case of linear dynamical systems, showing that accurate prediction can be achieved after finite observation without system identification, by leveraging improper methods based on spectral filtering. We survey the relationship between learning in dynamical systems and classical PAC, online, and universal prediction theories, and suggest directions for studying nonlinear and controlled systems.

