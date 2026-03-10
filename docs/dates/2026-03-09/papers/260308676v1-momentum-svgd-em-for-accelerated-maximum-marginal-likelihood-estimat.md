---
layout: default
title: Momentum SVGD-EM for Accelerated Maximum Marginal Likelihood Estimation
---

# Momentum SVGD-EM for Accelerated Maximum Marginal Likelihood Estimation
**arXiv**：[2603.08676v1](https://arxiv.org/abs/2603.08676) · [PDF](https://arxiv.org/pdf/2603.08676.pdf)  
**作者**：Adam Rozzio, Rafael Athanasiades, O. Deniz Akyildiz  

**一句话要点**：提出Momentum SVGD-EM以加速最大边际似然估计，在参数和概率测度空间引入Nesterov加速。

**关键词**：最大边际似然估计, Stein变分梯度下降, Nesterov加速, 交互粒子算法, 概率测度优化

## 3 点简述
- 核心问题：最大边际似然估计（MMLE）作为自由能泛函优化，现有交互粒子算法收敛速度未知。
- 方法要点：基于Stein变分梯度下降（SVGD），在EM框架中引入Nesterov动量加速参数和概率测度更新。
- 实验或效果：在低维和高维任务中，Momentum SVGD-EM一致加速收敛，减少所需迭代次数。

## 摘要（原文）

> Maximum marginal likelihood estimation (MMLE) can be formulated as the optimization of a free energy functional. From this viewpoint, the Expectation-Maximisation (EM) algorithm admits a natural interpretation as a coordinate descent method over the joint space of model parameters and probability measures. Recently, a significant body of work has adopted this perspective, leading to interacting particle algorithms for MMLE. In this paper, we propose an accelerated version of one such procedure, based on Stein variational gradient descent (SVGD), by introducing Nesterov acceleration in both the parameter updates and in the space of probability measures. The resulting method, termed Momentum SVGD-EM, consistently accelerates convergence in terms of required iterations across various tasks of increasing difficulty, demonstrating effectiveness in both low- and high-dimensional settings.

