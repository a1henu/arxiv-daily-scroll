---
layout: default
title: BumpNet: A Sparse Neural Network Framework for Learning PDE Solutions
---

# BumpNet: A Sparse Neural Network Framework for Learning PDE Solutions
**arXiv**：[2512.17198v1](https://arxiv.org/abs/2512.17198) · [PDF](https://arxiv.org/pdf/2512.17198.pdf)  
**作者**：Shao-Ting Chiu, Ioannis G. Kevrekidis, Ulisses Braga-Neto  

**一句话要点**：提出BumpNet稀疏神经网络框架，用于学习偏微分方程解和算子学习。

**关键词**：稀疏神经网络, 偏微分方程求解, 算子学习, 自适应剪枝, 基函数扩展

## 3 点简述
- 核心问题：基于径向基函数网络等传统方法，在偏微分方程数值解和算子学习中，如何高效利用现代训练技术并实现模型简约性。
- 方法要点：构建基于sigmoid激活函数的基函数，参数全可训练，通过动态剪枝实现自适应稀疏化。
- 实验或效果：结合PINNs、EDNNs和DeepONet等架构，在数值实验中展示高效性和准确性。

## 摘要（原文）

> We introduce BumpNet, a sparse neural network framework for PDE numerical solution and operator learning. BumpNet is based on meshless basis function expansion, in a similar fashion to radial-basis function (RBF) networks. Unlike RBF networks, the basis functions in BumpNet are constructed from ordinary sigmoid activation functions. This enables the efficient use of modern training techniques optimized for such networks. All parameters of the basis functions, including shape, location, and amplitude, are fully trainable. Model parsimony and h-adaptivity are effectively achieved through dynamically pruning basis functions during training. BumpNet is a general framework that can be combined with existing neural architectures for learning PDE solutions: here, we propose Bump-PINNs (BumpNet with physics-informed neural networks) for solving general PDEs; Bump-EDNN (BumpNet with evolutionary deep neural networks) to solve time-evolution PDEs; and Bump-DeepONet (BumpNet with deep operator networks) for PDE operator learning. Bump-PINNs are trained using the same collocation-based approach used by PINNs, Bump-EDNN uses a BumpNet only in the spatial domain and uses EDNNs to advance the solution in time, while Bump-DeepONets employ a BumpNet regression network as the trunk network of a DeepONet. Extensive numerical experiments demonstrate the efficiency and accuracy of the proposed architecture.

