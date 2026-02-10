---
layout: default
title: Do physics-informed neural networks (PINNs) need to be deep? Shallow PINNs using the Levenberg-Marquardt algorithm
---

# Do physics-informed neural networks (PINNs) need to be deep? Shallow PINNs using the Levenberg-Marquardt algorithm
**arXiv**：[2602.08515v1](https://arxiv.org/abs/2602.08515) · [PDF](https://arxiv.org/pdf/2602.08515.pdf)  
**作者**：Muhammad Luthfi Shahab, Imam Mukhlash, Hadi Susanto  

**一句话要点**：提出浅层物理信息神经网络结合Levenberg-Marquardt算法，高效求解非线性偏微分方程的正反问题。

**关键词**：物理信息神经网络, Levenberg-Marquardt算法, 非线性偏微分方程, 浅层网络, 正反问题求解, 优化方法

## 3 点简述
- 研究浅层PINNs解决非线性PDE正反问题，核心在于网络深度需求未知。
- 将PINNs重构为非线性系统，采用LM算法优化参数，并推导神经网络导数以计算雅可比矩阵。
- 在Burgers等基准问题上测试，LM在收敛速度、精度和损失值上优于BFGS，浅层网络表现良好。

## 摘要（原文）

> This work investigates the use of shallow physics-informed neural networks (PINNs) for solving forward and inverse problems of nonlinear partial differential equations (PDEs). By reformulating PINNs as nonlinear systems, the Levenberg-Marquardt (LM) algorithm is employed to efficiently optimize the network parameters. Analytical expressions for the neural network derivatives with respect to the input variables are derived, enabling accurate and efficient computation of the Jacobian matrix required by LM. The proposed approach is tested on several benchmark problems, including the Burgers, Schrödinger, Allen-Cahn, and three-dimensional Bratu equations. Numerical results demonstrate that LM significantly outperforms BFGS in terms of convergence speed, accuracy, and final loss values, even when using shallow network architectures with only two hidden layers. These findings indicate that, for a wide class of PDEs, shallow PINNs combined with efficient second-order optimization methods can provide accurate and computationally efficient solutions for both forward and inverse problems.

