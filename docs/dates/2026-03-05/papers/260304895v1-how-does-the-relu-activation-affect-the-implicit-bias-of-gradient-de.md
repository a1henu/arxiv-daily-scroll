---
layout: default
title: How Does the ReLU Activation Affect the Implicit Bias of Gradient Descent on High-dimensional Neural Network Regression?
---

# How Does the ReLU Activation Affect the Implicit Bias of Gradient Descent on High-dimensional Neural Network Regression?
**arXiv**：[2603.04895v1](https://arxiv.org/abs/2603.04895) · [PDF](https://arxiv.org/pdf/2603.04895.pdf)  
**作者**：Kuo-Wei Lai, Guanghui Wang, Molei Tao, Vidya Muthukumar  

**一句话要点**：分析高维随机特征下ReLU浅层网络梯度下降的隐式偏差，近似最小L2范数解。

**关键词**：隐式偏差, 梯度下降, ReLU激活, 高维数据, 随机特征, 浅层神经网络

## 3 点简述
- 研究过参数化ReLU浅层网络在平方损失下梯度下降的隐式偏差问题。
- 采用原始-对偶分析，追踪预测和系数演化，证明ReLU激活模式快速稳定。
- 高维随机数据下，隐式偏差以高概率近似最小L2范数解，间隙为Θ(√(n/d))。

## 摘要（原文）

> Overparameterized ML models, including neural networks, typically induce underdetermined training objectives with multiple global minima. The implicit bias refers to the limiting global minimum that is attained by a common optimization algorithm, such as gradient descent (GD). In this paper, we characterize the implicit bias of GD for training a shallow ReLU model with the squared loss on high-dimensional random features. Prior work showed that the implicit bias does not exist in the worst-case (Vardi and Shamir, 2021), or corresponds exactly to the minimum-l2-norm solution among all global minima under exactly orthogonal data (Boursier et al., 2022). Our work interpolates between these two extremes and shows that, for sufficiently high-dimensional random data, the implicit bias approximates the minimum-l2-norm solution with high probability with a gap on the order $Θ(\sqrt{n/d})$, where n is the number of training examples and d is the feature dimension. Our results are obtained through a novel primal-dual analysis, which carefully tracks the evolution of predictions, data-span coefficients, as well as their interactions, and shows that the ReLU activation pattern quickly stabilizes with high probability over the random data.

