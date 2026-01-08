---
layout: default
title: Kantorovich-Type Stochastic Neural Network Operators for the Mean-Square Approximation of Certain Second-Order Stochastic Processes
---

# Kantorovich-Type Stochastic Neural Network Operators for the Mean-Square Approximation of Certain Second-Order Stochastic Processes
**arXiv**：[2601.03634v1](https://arxiv.org/abs/2601.03634) · [PDF](https://arxiv.org/pdf/2601.03634.pdf)  
**作者**：Sachin Saini, Uaday Singh  

**一句话要点**：提出Kantorovich型随机神经网络算子，用于二阶随机过程的均方逼近。

**关键词**：随机神经网络算子, 均方逼近, 随机过程, Kantorovich型, 随机神经元, 数值模拟

## 3 点简述
- 问题：随机动态的神经网络逼近研究较少，现有方法多限于确定性函数。
- 方法：构建基于随机神经元的算子，通过随机积分器引入随机性，继承过程概率结构。
- 效果：理论证明均方收敛，数值模拟显示样本路径准确重构和均方误差快速衰减。

## 摘要（原文）

> Artificial neural network operators (ANNOs) have been widely used for approximating deterministic input-output functions; however, their extension to random dynamics remains comparatively unexplored. In this paper, we construct a new class of \textbf{Kantorovich-type Stochastic Neural Network Operators (K-SNNOs)} in which randomness is incorporated not at the coefficient level, but through \textbf{stochastic neurons} driven by stochastic integrators. This framework enables the operator to inherit the probabilistic structure of the underlying process, making it suitable for modeling and approximating stochastic signals. We establish mean-square convergence of K-SNNOs to the target stochastic process and derive quantitative error estimates expressing the rate of approximation in terms of the modulus of continuity. Numerical simulations further validate the theoretical results by demonstrating accurate reconstruction of sample paths and rapid decay of the mean square error (MSE). Graphical results, including sample-wise approximations and empirical MSE behaviour, illustrate the robustness and effectiveness of the proposed stochastic-neuron-based operator.

