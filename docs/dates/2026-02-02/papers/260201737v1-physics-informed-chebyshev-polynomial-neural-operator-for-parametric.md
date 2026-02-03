---
layout: default
title: Physics-Informed Chebyshev Polynomial Neural Operator for Parametric Partial Differential Equations
---

# Physics-Informed Chebyshev Polynomial Neural Operator for Parametric Partial Differential Equations
**arXiv**：[2602.01737v1](https://arxiv.org/abs/2602.01737) · [PDF](https://arxiv.org/pdf/2602.01737.pdf)  
**作者**：Biao Chen, Jing Wang, Hairun Xie, Qineng Wang, Shuai Zhang, Yifan Xia, Jifa Zhang  

**一句话要点**：提出基于切比雪夫多项式的物理信息神经算子以解决参数化偏微分方程求解中的谱偏差和训练不稳定问题。

**关键词**：神经算子, 切比雪夫多项式, 物理信息学习, 参数化偏微分方程, 谱方法, 跨音速流

## 3 点简述
- 核心问题：现有神经算子依赖多层感知机，在物理信息设置下因谱偏差和固定激活函数导致训练不稳定。
- 方法要点：引入切比雪夫谱基替代不稳定单项式展开，通过参数依赖调制机制构建近最优函数空间。
- 实验或效果：在基准参数化偏微分方程上实现更高精度、更快收敛和超参数鲁棒性，并应用于跨音速翼型流问题。

## 摘要（原文）

> Neural operators have emerged as powerful deep learning frameworks for approximating solution operators of parameterized partial differential equations (PDE). However, current methods predominantly rely on multilayer perceptrons (MLPs) for mapping inputs to solutions, which impairs training robustness in physics-informed settings due to inherent spectral biases and fixed activation functions. To overcome the architectural limitations, we introduce the Physics-Informed Chebyshev Polynomial Neural Operator (CPNO), a novel mesh-free framework that leverages a basis transformation to replace unstable monomial expansions with the numerically stable Chebyshev spectral basis. By integrating parameter dependent modulation mechanism to main net, CPNO constructs PDE solutions in a near-optimal functional space, decoupling the model from MLP-specific constraints and enhancing multi-scale representation. Theoretical analysis demonstrates the Chebyshev basis's near-minimax uniform approximation properties and superior conditioning, with Lebesgue constants growing logarithmically with degree, thereby mitigating spectral bias and ensuring stable gradient flow during optimization. Numerical experiments on benchmark parameterized PDEs show that CPNO achieves superior accuracy, faster convergence, and enhanced robustness to hyperparameters. The experiment of transonic airfoil flow has demonstrated the capability of CPNO in characterizing complex geometric problems.

