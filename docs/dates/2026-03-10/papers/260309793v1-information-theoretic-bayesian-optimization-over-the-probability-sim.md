---
layout: default
title: Information Theoretic Bayesian Optimization over the Probability Simplex
---

# Information Theoretic Bayesian Optimization over the Probability Simplex
**arXiv**：[2603.09793v1](https://arxiv.org/abs/2603.09793) · [PDF](https://arxiv.org/pdf/2603.09793.pdf)  
**作者**：Federico Pavesi, Antonio Candelieri, Noémie Jaquier  

**一句话要点**：提出α-GaBO算法，基于信息几何在概率单纯形上优化概率和混合模型。

**关键词**：贝叶斯优化, 信息几何, 概率单纯形, Riemannian度量, Matérn核, 混合模型优化

## 3 点简述
- 核心问题：贝叶斯优化在概率单纯形等非欧约束域中效率低。
- 方法要点：利用信息几何构造Riemannian度量和Matérn核，设计几何优化器。
- 实验或效果：在基准函数和真实应用（如分类器混合）中优于约束欧几里得方法。

## 摘要（原文）

> Bayesian optimization is a data-efficient technique that has been shown to be extremely powerful to optimize expensive, black-box, and possibly noisy objective functions. Many applications involve optimizing probabilities and mixtures which naturally belong to the probability simplex, a constrained non-Euclidean domain defined by non-negative entries summing to one. This paper introduces $α$-GaBO, a novel family of Bayesian optimization algorithms over the probability simplex. Our approach is grounded in information geometry, a branch of Riemannian geometry which endows the simplex with a Riemannian metric and a class of connections. Based on information geometry theory, we construct Matérn kernels that reflect the geometry of the probability simplex, as well as a one-parameter family of geometric optimizers for the acquisition function. We validate our method on benchmark functions and on a variety of real-world applications including mixtures of components, mixtures of classifiers, and a robotic control task, showing its increased performance compared to constrained Euclidean approaches.

