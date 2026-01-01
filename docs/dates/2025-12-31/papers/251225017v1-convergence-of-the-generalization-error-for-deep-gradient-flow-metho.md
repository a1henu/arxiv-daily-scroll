---
layout: default
title: Convergence of the generalization error for deep gradient flow methods for PDEs
---

# Convergence of the generalization error for deep gradient flow methods for PDEs
**arXiv**：[2512.25017v1](https://arxiv.org/abs/2512.25017) · [PDF](https://arxiv.org/pdf/2512.25017.pdf)  
**作者**：Chenguang Liu, Antonis Papapantoleon, Jasper Rou  

**一句话要点**：分析深度梯度流方法求解偏微分方程的泛化误差收敛性

**关键词**：深度梯度流方法, 偏微分方程求解, 泛化误差分析, 神经网络近似, 梯度流极限, 数学理论

## 3 点简述
- 核心问题：为深度梯度流方法求解高维偏微分方程提供数学基础，分析泛化误差收敛性。
- 方法要点：将泛化误差分解为近似误差和训练误差，分别证明在神经元数无限和训练时间无限时趋于零。
- 实验或效果：未知具体实验，但理论推导表明在宽网络极限下，梯度流随训练时间趋于稳定，误差收敛。

## 摘要（原文）

> The aim of this article is to provide a firm mathematical foundation for the application of deep gradient flow methods (DGFMs) for the solution of (high-dimensional) partial differential equations (PDEs). We decompose the generalization error of DGFMs into an approximation and a training error. We first show that the solution of PDEs that satisfy reasonable and verifiable assumptions can be approximated by neural networks, thus the approximation error tends to zero as the number of neurons tends to infinity. Then, we derive the gradient flow that the training process follows in the ``wide network limit'' and analyze the limit of this flow as the training time tends to infinity. These results combined show that the generalization error of DGFMs tends to zero as the number of neurons and the training time tend to infinity.

