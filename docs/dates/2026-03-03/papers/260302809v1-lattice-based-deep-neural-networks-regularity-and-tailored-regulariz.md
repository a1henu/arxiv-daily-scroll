---
layout: default
title: Lattice-based Deep Neural Networks: Regularity and Tailored Regularization
---

# Lattice-based Deep Neural Networks: Regularity and Tailored Regularization
**arXiv**：[2603.02809v1](https://arxiv.org/abs/2603.02809) · [PDF](https://arxiv.org/pdf/2603.02809.pdf)  
**作者**：Alexander Keller, Frances Y. Kuo, Dirk Nuyens, Ian H. Sloan  

**一句话要点**：提出基于格规则的深度神经网络训练方法，以提升高维函数逼近的泛化性能。

**关键词**：格规则, 深度神经网络, 高维积分, 函数逼近, 正则化, 泛化误差

## 3 点简述
- 核心问题：深度神经网络在高维函数逼近中面临泛化误差依赖输入维度的问题。
- 方法要点：使用格规则作为训练点，结合网络参数限制以匹配目标函数正则性。
- 实验或效果：数值实验显示，该方法优于标准ℓ2正则化，理论证明泛化误差界常数独立于维度。

## 摘要（原文）

> This survey article is concerned with the application of lattice rules to Deep Neural Networks (DNNs), lattice rules being a family of quasi-Monte Carlo methods. They have demonstrated effectiveness in various contexts for high-dimensional integration and function approximation. They are extremely easy to implement thanks to their very simple formulation -- all that is required is a good integer generating vector of length matching the dimensionality of the problem. In recent years there has been a burst of research activities on the application and theory of DNNs. We review our recent article on using lattice rules as training points for DNNs with a smooth activation function, where we obtained explicit regularity bounds of the DNNs. By imposing restrictions on the network parameters to match the regularity features of the target function, we prove that DNNs with tailored lattice training points can achieve good theoretical generalization error bounds, with implied constants independent of the input dimension. We also demonstrate numerically that DNNs trained with our tailored regularization perform significantly better than with standard $\ell_2$ regularization.

