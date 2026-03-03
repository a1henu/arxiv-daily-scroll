---
layout: default
title: Training Dynamics of Softmax Self-Attention: Fast Global Convergence via Preconditioning
---

# Training Dynamics of Softmax Self-Attention: Fast Global Convergence via Preconditioning
**arXiv**：[2603.01514v1](https://arxiv.org/abs/2603.01514) · [PDF](https://arxiv.org/pdf/2603.01514.pdf)  
**作者**：Gautam Goel, Mahdi Soltanolkotabi, Peter Bartlett  

**一句话要点**：提出结构感知梯度下降以解决softmax自注意力层训练中的全局收敛问题

**关键词**：自注意力训练, 梯度下降优化, 非凸优化, 矩阵分解, 全局收敛

## 3 点简述
- 研究softmax自注意力层在线性回归任务中的梯度下降训练动态
- 将回归问题等价为非凸矩阵分解，设计带预条件器和正则化的优化算法
- 算法以几何速率收敛至全局最优参数，避免虚假驻点

## 摘要（原文）

> We study the training dynamics of gradient descent in a softmax self-attention layer trained to perform linear regression and show that a simple first-order optimization algorithm can converge to the globally optimal self-attention parameters at a geometric rate. Our analysis proceeds in two steps. First, we show that in the infinite-data limit the regression problem solved by the self-attention layer is equivalent to a nonconvex matrix factorization problem. Second, we exploit this connection to design a novel "structure-aware" variant of gradient descent which efficiently optimizes the original finite-data regression objective. Our optimization algorithm features several innovations over standard gradient descent, including a preconditioner and regularizer which help avoid spurious stationary points, and a data-dependent spectral initialization of parameters which lie near the manifold of global minima with high probability.

