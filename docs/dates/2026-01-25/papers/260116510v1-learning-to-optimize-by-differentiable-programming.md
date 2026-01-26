---
layout: default
title: Learning to Optimize by Differentiable Programming
---

# Learning to Optimize by Differentiable Programming
**arXiv**：[2601.16510v1](https://arxiv.org/abs/2601.16510) · [PDF](https://arxiv.org/pdf/2601.16510.pdf)  
**作者**：Liping Tao, Xindi Tong, Chee Wei Tan  

**一句话要点**：提出可微分编程学习优化方法，以提升大规模优化问题的收敛性与解质量。

**关键词**：可微分编程, 优化算法学习, 自动微分, 大规模优化, 对偶方法

## 3 点简述
- 核心问题：大规模优化问题需低迭代成本的一阶方法，传统设计依赖人工经验。
- 方法要点：利用PyTorch等框架的可微分编程，通过自动微分端到端学习优化算法设计。
- 实验或效果：基于Fenchel-Rockafellar对偶指导，在LP、OPF等案例中展示学习ADMM、PDHG等方法的性能提升。

## 摘要（原文）

> Solving massive-scale optimization problems requires scalable first-order methods with low per-iteration cost. This tutorial highlights a shift in optimization: using differentiable programming not only to execute algorithms but to learn how to design them. Modern frameworks such as PyTorch, TensorFlow, and JAX enable this paradigm through efficient automatic differentiation. Embedding first-order methods within these systems allows end-to-end training that improves convergence and solution quality. Guided by Fenchel-Rockafellar duality, the tutorial demonstrates how duality-informed iterative schemes such as ADMM and PDHG can be learned and adapted. Case studies across LP, OPF, Laplacian regularization, and neural network verification illustrate these gains.

