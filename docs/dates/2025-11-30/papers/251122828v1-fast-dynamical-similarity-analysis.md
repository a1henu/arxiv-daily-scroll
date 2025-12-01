---
layout: default
title: Fast dynamical similarity analysis
---

# Fast dynamical similarity analysis
**arXiv**：[2511.22828v1](https://arxiv.org/abs/2511.22828) · [PDF](https://arxiv.org/pdf/2511.22828.pdf)  
**作者**：Arman Behrad, Mitchell Ostrow, Mohammad Taha Fakharian, Ila Fiete, Christian Beste, Shervin Safavi  

**一句话要点**：提出fastDSA以高效计算神经系统的动态相似性，提升计算速度至少一个数量级。

**关键词**：动态相似性分析, Hankel嵌入, 计算效率优化, 神经系统比较, 数据驱动建模

## 3 点简述
- 核心问题：传统相似性度量忽略神经表示的动态过程，现有动态相似性方法计算缓慢。
- 方法要点：通过数据驱动选择Hankel嵌入有效阶次，并采用轻量优化替代正交约束，降低计算成本。
- 实验或效果：fastDSA在保持准确性和鲁棒性的同时，计算效率显著高于先前方法。

## 摘要（原文）

> To understand how neural systems process information, it is often essential to compare one circuit with another, one brain with another, or data with a model. Traditional similarity measures ignore the dynamical processes underlying neural representations. Dynamical similarity methods offer a framework to compare the temporal structure of dynamical systems by embedding their (possibly) nonlinear dynamics into a globally linear space and there computing conjugacy metrics. However, identifying the best embedding and computing these metrics can be computationally slow. Here we introduce fast Dynamical Similarity Analysis (fastDSA), which is computationally far more efficient than previous methods while maintaining their accuracy and robustness. FastDSA introduces two key components that boost efficiency: (1) automatic selection of the effective model order of the Hankel (delay) embedding from the data via a data-driven singular-value threshold that identifies the informative subspace and discards noise to lower computational cost without sacrificing signal, and (2) a novel optimization procedure and objective, which replaces the slow exact orthogonality constraint in finding a minimal distance between dynamics matrices with a lightweight process to keep the search close to the space of orthogonal transformations. We demonstrate that fastDSA is at least an order of magnitude faster than the previous methods. Furthermore, we demonstrate that fastDSA has the properties of its ancestor, including its invariances and sensitivities to system dynamics. FastDSA, therefore, provides a computationally efficient and accurate method for dynamical similarity analysis.

