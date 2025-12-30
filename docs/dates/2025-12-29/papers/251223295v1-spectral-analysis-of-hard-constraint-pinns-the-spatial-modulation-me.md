---
layout: default
title: Spectral Analysis of Hard-Constraint PINNs: The Spatial Modulation Mechanism of Boundary Functions
---

# Spectral Analysis of Hard-Constraint PINNs: The Spatial Modulation Mechanism of Boundary Functions
**arXiv**：[2512.23295v1](https://arxiv.org/abs/2512.23295) · [PDF](https://arxiv.org/pdf/2512.23295.pdf)  
**作者**：Yuchen Xie, Honghang Chi, Haopeng Quan, Yahui Wang, Wei Wang, Yu Ma  

**一句话要点**：提出硬约束PINNs的谱分析框架，揭示边界函数作为谱滤波器的空间调制机制。

**关键词**：硬约束物理信息神经网络, 神经正切核, 谱分析, 边界条件, 训练收敛, 科学机器学习

## 3 点简述
- 核心问题：硬约束PINNs中边界函数如何影响训练动态，理论机制未知。
- 方法要点：建立神经正切核框架，推导边界函数作为谱滤波器的显式核组合律。
- 实验或效果：验证有效秩预测收敛，指导边界函数从启发式选择转向谱优化设计。

## 摘要（原文）

> Physics-Informed Neural Networks with hard constraints (HC-PINNs) are increasingly favored for their ability to strictly enforce boundary conditions via a trial function ansatz $\tilde{u} = A + B \cdot N$, yet the theoretical mechanisms governing their training dynamics have remained unexplored.
>   Unlike soft-constrained formulations where boundary terms act as additive penalties, this work reveals that the boundary function $B$ introduces a multiplicative spatial modulation that fundamentally alters the learning landscape.
>   A rigorous Neural Tangent Kernel (NTK) framework for HC-PINNs is established, deriving the explicit kernel composition law.
>   This relationship demonstrates that the boundary function $B(\vec{x})$ functions as a spectral filter, reshaping the eigenspectrum of the neural network's native kernel.
>   Through spectral analysis, the effective rank of the residual kernel is identified as a deterministic predictor of training convergence, superior to classical condition numbers.
>   It is shown that widely used boundary functions can inadvertently induce spectral collapse, leading to optimization stagnation despite exact boundary satisfaction.
>   Validated across multi-dimensional benchmarks, this framework transforms the design of boundary functions from a heuristic choice into a principled spectral optimization problem, providing a solid theoretical foundation for geometric hard constraints in scientific machine learning.

