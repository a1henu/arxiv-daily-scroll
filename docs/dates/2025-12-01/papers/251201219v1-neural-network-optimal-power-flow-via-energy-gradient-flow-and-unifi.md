---
layout: default
title: Neural Network Optimal Power Flow via Energy Gradient Flow and Unified Dynamics
---

# Neural Network Optimal Power Flow via Energy Gradient Flow and Unified Dynamics
**arXiv**：[2512.01219v1](https://arxiv.org/abs/2512.01219) · [PDF](https://arxiv.org/pdf/2512.01219.pdf)  
**作者**：Xuezhi Liu  

**一句话要点**：提出基于神经网络动力学和能量梯度流的OPF求解方法，实现无监督物理约束学习。

**关键词**：最优潮流, 神经网络动力学, 能量梯度流, 无监督学习, 物理约束优化

## 3 点简述
- 核心问题：传统OPF方法计算效率低、依赖初始值，现有深度学习OPF方法需大量标注数据且难保证物理一致性。
- 方法要点：将OPF转化为能量最小化问题，通过能量函数和梯度流引导网络学习满足约束的最优解，无需标注数据。
- 实验或效果：未知，但方法声称实现无监督端到端学习，可能提升计算效率和物理一致性。

## 摘要（原文）

> Optimal Power Flow (OPF) is a core optimization problem in power system operation and planning, aiming to minimize generation costs while satisfying physical constraints such as power flow equations, generator limits, and voltage limits. Traditional OPF solving methods typically employ iterative optimization algorithms (such as interior point methods, sequential quadratic programming, etc.), with limitations including low computational efficiency, initial value sensitivity, and low batch computation efficiency. Most existing deep learning-based OPF methods rely on supervised learning, requiring pre-solving large numbers of cases, and have difficulty guaranteeing physical consistency. This paper proposes an Optimal Power Flow solving method based on neural network dynamics and energy gradient flow, transforming OPF problems into energy minimization problems. By constructing an energy function to measure the degree of deviation from the constraint manifold, and guiding networks to learn optimal solutions that simultaneously satisfy power flow constraints and minimize costs through gradient flow. Neural networks are trained unsupervised by directly minimizing physical residuals, requiring no labeled data, achieving true "end-to-end" physics-constrained learning.

