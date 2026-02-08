---
layout: default
title: Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
---

# Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
**arXiv**：[2602.05887v1](https://arxiv.org/abs/2602.05887) · [PDF](https://arxiv.org/pdf/2602.05887.pdf)  
**作者**：Tianqi Shen, Jinji Yang, Junze He, Kunhan Gao, Ziye Ma  

**一句话要点**：提出模拟提升框架以确定性逃离矩阵感知中的虚假局部极小值

**关键词**：非凸优化, 矩阵感知, 局部极小值逃离, 过参数化, 确定性框架

## 3 点简述
- 低秩矩阵感知存在大量虚假局部极小值，梯度优化易陷入其中
- 通过模拟过参数化空间的逃离方向，无需实际提升计算复杂度
- 数值实验表明能可靠逃离局部极小值并收敛至全局最优

## 摘要（原文）

> Low-rank matrix sensing is a fundamental yet challenging nonconvex problem whose optimization landscape typically contains numerous spurious local minima, making it difficult for gradient-based optimizers to converge to the global optimum. Recent work has shown that over-parameterization via tensor lifting can convert such local minima into strict saddle points, an insight that also partially explains why massive scaling can improve generalization and performance in modern machine learning. Motivated by this observation, we propose a Simulated Oracle Direction (SOD) escape mechanism that simulates the landscape and escape direction of the over-parametrized space, without resorting to actually lifting the problem, since that would be computationally intractable. In essence, we designed a mathematical framework to project over-parametrized escape directions onto the original parameter space to guarantee a strict decrease of objective value from existing local minima. To the best of the our knowledge, this represents the first deterministic framework that could escape spurious local minima with guarantee, especially without using random perturbations or heuristic estimates. Numerical experiments demonstrate that our framework reliably escapes local minima and facilitates convergence to global optima, while incurring minimal computational cost when compared to explicit tensor over-parameterization. We believe this framework has non-trivial implications for nonconvex optimization beyond matrix sensing, by showcasing how simulated over-parameterization can be leveraged to tame challenging optimization landscapes.

