---
layout: default
title: Regularized Random Fourier Features and Finite Element Reconstruction for Operator Learning in Sobolev Space
---

# Regularized Random Fourier Features and Finite Element Reconstruction for Operator Learning in Sobolev Space
**arXiv**：[2512.17884v1](https://arxiv.org/abs/2512.17884) · [PDF](https://arxiv.org/pdf/2512.17884.pdf)  
**作者**：Xinyue Yu, Hayden Schaeffer  

**一句话要点**：提出正则化随机傅里叶特征与有限元重构方法，用于从噪声数据中学习算子。

**关键词**：算子学习, 随机傅里叶特征, 正则化方法, 有限元重构, 偏微分方程, 噪声鲁棒性

## 3 点简述
- 核心问题：基于核的算子学习在大训练集下计算成本高且对噪声敏感。
- 方法要点：使用多元学生t分布随机特征和频率加权Tikhonov正则化抑制高频噪声。
- 实验或效果：在多个PDE基准问题中验证了方法的鲁棒性和性能提升，训练时间减少。

## 摘要（原文）

> Operator learning is a data-driven approximation of mappings between infinite-dimensional function spaces, such as the solution operators of partial differential equations. Kernel-based operator learning can offer accurate, theoretically justified approximations that require less training than standard methods. However, they can become computationally prohibitive for large training sets and can be sensitive to noise. We propose a regularized random Fourier feature (RRFF) approach, coupled with a finite element reconstruction map (RRFF-FEM), for learning operators from noisy data. The method uses random features drawn from multivariate Student's $t$ distributions, together with frequency-weighted Tikhonov regularization that suppresses high-frequency noise. We establish high-probability bounds on the extreme singular values of the associated random feature matrix and show that when the number of features $N$ scales like $m \log m$ with the number of training samples $m$, the system is well-conditioned, which yields estimation and generalization guarantees. Detailed numerical experiments on benchmark PDE problems, including advection, Burgers', Darcy flow, Helmholtz, Navier-Stokes, and structural mechanics, demonstrate that RRFF and RRFF-FEM are robust to noise and achieve improved performance with reduced training time compared to the unregularized random feature model, while maintaining competitive accuracy relative to kernel and neural operator tests.

