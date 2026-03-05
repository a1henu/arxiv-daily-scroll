---
layout: default
title: Fermi-Dirac thermal measurements: A framework for quantum hypothesis testing and semidefinite optimization
---

# Fermi-Dirac thermal measurements: A framework for quantum hypothesis testing and semidefinite optimization
**arXiv**：[2603.04061v1](https://arxiv.org/abs/2603.04061) · [PDF](https://arxiv.org/pdf/2603.04061.pdf)  
**作者**：Nana Liu, Mark M. Wilde  

**一句话要点**：提出费米-狄拉克热测量框架，用于量子假设检验与半定优化

**关键词**：量子假设检验, 费米-狄拉克热测量, 半定优化, 量子机器学习, 量子-经典混合算法

## 3 点简述
- 核心问题：量子测量在假设检验中需优化，传统方法计算复杂。
- 方法要点：将测量算子视为有效费米子模式，通过最小化自由能导出费米-狄拉克热测量。
- 实验或效果：低温下性能接近最优测量，可结合量子-经典算法学习参数，拓展至半定优化问题。

## 摘要（原文）

> Quantum measurements are the means by which we recover messages encoded into quantum states. They are at the forefront of quantum hypothesis testing, wherein the goal is to perform an optimal measurement for arriving at a correct conclusion. Mathematically, a measurement operator is Hermitian with eigenvalues in [0,1]. By noticing that this constraint on each eigenvalue is the same as that imposed on fermions by the Pauli exclusion principle, we interpret every eigenmode of a measurement operator as an independent effective fermionic mode. Under this perspective, various objective functions in quantum hypothesis testing can be viewed as the total expected energy associated with these fermionic occupation numbers. By instead fixing a temperature and minimizing the total expected fermionic free energy, we find that optimal measurements for these modified objective functions are Fermi-Dirac thermal measurements, wherein their eigenvalues are specified by Fermi-Dirac distributions. In the low-temperature limit, their performance closely approximates that of optimal measurements for quantum hypothesis testing, and we show that their parameters can be learned by classical or hybrid quantum-classical optimization algorithms. This leads to a new quantum machine-learning model, termed Fermi-Dirac machines, consisting of parameterized Fermi-Dirac thermal measurements-an alternative to quantum Boltzmann machines based on thermal states. Beyond hypothesis testing, we show how general semidefinite optimization problems can be solved using this approach, leading to a novel paradigm for semidefinite optimization on quantum computers, in which the goal is to implement thermal measurements rather than prepare thermal states. Finally, we propose quantum algorithms for implementing Fermi-Dirac thermal measurements, and we also propose second-order hybrid quantum-classical optimization algorithms.

