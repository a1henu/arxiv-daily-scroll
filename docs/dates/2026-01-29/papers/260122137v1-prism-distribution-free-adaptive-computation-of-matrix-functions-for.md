---
layout: default
title: PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training
---

# PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training
**arXiv**：[2601.22137v1](https://arxiv.org/abs/2601.22137) · [PDF](https://arxiv.org/pdf/2601.22137.pdf)  
**作者**：Shenghao Yang, Zhichao Wang, Oleg Balabanov, N. Benjamin Erichson, Michael W. Mahoney  

**一句话要点**：提出PRISM框架，通过自适应多项式逼近与随机草图加速矩阵函数计算，以优化神经网络训练。

**关键词**：矩阵函数计算, 自适应多项式逼近, 随机草图, 神经网络训练加速, 优化器集成

## 3 点简述
- 核心问题：矩阵函数计算在神经网络训练中关键但耗时，传统方法依赖显式特征分解或固定谱界。
- 方法要点：PRISM结合自适应多项式拟合与随机草图，迭代中通过草图最小二乘问题适应实例谱，无需先验谱界。
- 实验或效果：应用于矩阵平方根和正交化，集成Shampoo和Muon优化器，实证加速训练过程。

## 摘要（原文）

> Matrix functions such as square root, inverse roots, and orthogonalization play a central role in preconditioned gradient methods for neural network training. This has motivated the development of iterative algorithms that avoid explicit eigendecompositions and rely primarily on matrix multiplications, making them well suited for modern GPU accelerators. We present PRISM (Polynomial-fitting and Randomized Iterative Sketching for Matrix functions computation), a general framework for accelerating iterative algorithms for computing matrix functions. PRISM combines adaptive polynomial approximation with randomized sketching: at each iteration, it fits a polynomial surrogate to the current spectrum via a sketched least-squares problem, adapting to the instance at hand with minimal overhead. We apply PRISM to accelerate Newton-Schulz-like iterations for matrix square roots and orthogonalization, which are core primitives in machine learning. Unlike prior methods, PRISM requires no explicit spectral bounds or singular value estimates; and it adapts automatically to the evolving spectrum. Empirically, PRISM accelerates training when integrated into Shampoo and Muon optimizers.

