---
layout: default
title: Soliton profiles: Classical Numerical Schemes vs. Neural Network - Based Solvers
---

# Soliton profiles: Classical Numerical Schemes vs. Neural Network - Based Solvers
**arXiv**：[2512.24634v1](https://arxiv.org/abs/2512.24634) · [PDF](https://arxiv.org/pdf/2512.24634.pdf)  
**作者**：Chandler Haight, Svetlana Roudenko, Zhongming Wang  

**一句话要点**：比较经典数值方法与神经网络求解器在一维色散PDE孤子剖面计算中的性能

**关键词**：孤子剖面计算, 经典数值方法, 物理信息神经网络, 算子学习, 一维色散PDE, 性能比较

## 3 点简述
- 研究一维非线性薛定谔、Klein-Gordon和广义KdV方程的孤子剖面计算问题
- 对比经典方法（如Petviashvili法）与神经网络方法（PINNs和算子学习）的精度和效率
- 经典方法在单实例计算中精度和效率更高，算子学习方法适合多参数实例的快速推理

## 摘要（原文）

> We present a comparative study of classical numerical solvers, such as Petviashvili's method or finite difference with Newton iterations, and neural network-based methods for computing ground states or profiles of solitary-wave solutions to the one-dimensional dispersive PDEs that include the nonlinear Schrödinger, the nonlinear Klein-Gordon and the generalized KdV equations. We confirm that classical approaches retain high-order accuracy and strong computational efficiency for single-instance problems in the one-dimensional setting. Physics-informed neural networks (PINNs) are also able to reproduce qualitative solutions but are generally less accurate and less efficient in low dimensions than classical solvers due to expensive training and slow convergence. We also investigate the operator-learning methods, which, although computationally intensive during training, can be reused across many parameter instances, providing rapid inference after pretraining, making them attractive for applications involving repeated simulations or real-time predictions. For single-instance computations, however, the accuracy of operator-learning methods remains lower than that of classical methods or PINNs, in general.

