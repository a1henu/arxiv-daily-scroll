---
layout: default
title: OPBO: Order-Preserving Bayesian Optimization
---

# OPBO: Order-Preserving Bayesian Optimization
**arXiv**：[2512.18980v1](https://arxiv.org/abs/2512.18980) · [PDF](https://arxiv.org/pdf/2512.18980.pdf)  
**作者**：Wei Peng, Jianchen Hu, Kang Liu, Qiaozhu Zhai  

**一句话要点**：提出OPBO方法以解决高维黑盒优化中高斯过程计算复杂度过高的问题。

**关键词**：贝叶斯优化, 高维优化, 黑盒优化, 顺序保持模型, 神经网络代理, 计算效率

## 3 点简述
- 核心问题：高斯过程在高维空间（如维度超过500）中计算复杂度过高，不适合黑盒优化。
- 方法要点：使用保持顺序的代理模型（OP神经网络）替代高斯过程，并选择足够好的解以降低计算成本。
- 实验或效果：在高维黑盒优化问题上，OPBO显著优于基于回归神经网络和高斯过程的传统贝叶斯优化方法。

## 摘要（原文）

> Bayesian optimization is an effective method for solving expensive black-box optimization problems. Most existing methods use Gaussian processes (GP) as the surrogate model for approximating the black-box objective function, it is well-known that it can fail in high-dimensional space (e.g., dimension over 500). We argue that the reliance of GP on precise numerical fitting is fundamentally ill-suited in high-dimensional space, where it leads to prohibitive computational complexity. In order to address this, we propose a simple order-preserving Bayesian optimization (OPBO) method, where the surrogate model preserves the order, instead of the value, of the black-box objective function. Then we can use a simple but effective OP neural network (NN) to replace GP as the surrogate model. Moreover, instead of searching for the best solution from the acquisition model, we select good-enough solutions in the ordinal set to reduce computational cost. The experimental results show that for high-dimensional (over 500) black-box optimization problems, the proposed OPBO significantly outperforms traditional BO methods based on regression NN and GP. The source code is available at https://github.com/pengwei222/OPBO.

