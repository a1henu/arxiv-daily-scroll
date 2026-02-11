---
layout: default
title: Learning to Discover Iterative Spectral Algorithms
---

# Learning to Discover Iterative Spectral Algorithms
**arXiv**：[2602.09530v1](https://arxiv.org/abs/2602.09530) · [PDF](https://arxiv.org/pdf/2602.09530.pdf)  
**作者**：Zihang Liu, Oleg Balabanov, Yaoqing Yang, Michael W. Mahoney  

**一句话要点**：提出AutoSpec框架以发现大规模数值线性代数与优化的迭代谱算法

**关键词**：迭代谱算法, 数值线性代数, 自监督学习, 矩阵多项式, 谱滤波, 算法发现

## 3 点简述
- 核心问题：如何自动发现适用于大规模数值线性代数任务的迭代谱算法，以提升计算效率与精度
- 方法要点：基于自监督神经网络，利用粗谱信息预测矩阵多项式系数，实现可执行的数值线性代数递推
- 实验或效果：在真实世界矩阵上，相比基础基线，学习到的算法在精度或迭代次数上实现数量级改进

## 摘要（原文）

> We introduce AutoSpec, a neural network framework for discovering iterative spectral algorithms for large-scale numerical linear algebra and numerical optimization. Our self-supervised models adapt to input operators using coarse spectral information (e.g., eigenvalue estimates and residual norms), and they predict recurrence coefficients for computing or applying a matrix polynomial tailored to a downstream task. The effectiveness of AutoSpec relies on three ingredients: an architecture whose inference pass implements short, executable numerical linear algebra recurrences; efficient training on small synthetic problems with transfer to large-scale real-world operators; and task-defined objectives that enforce the desired approximation or preconditioning behavior across the range of spectral profiles represented in the training set. We apply AutoSpec to discovering algorithms for representative numerical linear algebra tasks: accelerating matrix-function approximation; accelerating sparse linear solvers; and spectral filtering/preconditioning for eigenvalue computations. On real-world matrices, the learned procedures deliver orders-of-magnitude improvements in accuracy and/or reductions in iteration count, relative to basic baselines. We also find clear connections to classical theory: the induced polynomials often exhibit near-equiripple, near-minimax behavior characteristic of Chebyshev polynomials.

