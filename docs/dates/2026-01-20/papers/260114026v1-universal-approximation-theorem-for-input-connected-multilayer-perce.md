---
layout: default
title: Universal Approximation Theorem for Input-Connected Multilayer Perceptrons
---

# Universal Approximation Theorem for Input-Connected Multilayer Perceptrons
**arXiv**：[2601.14026v1](https://arxiv.org/abs/2601.14026) · [PDF](https://arxiv.org/pdf/2601.14026.pdf)  
**作者**：Vugar Ismailov  

**一句话要点**：提出输入连接多层感知机，证明其在非线性激活下能通用逼近连续函数。

**关键词**：输入连接多层感知机, 通用逼近定理, 神经网络架构, 连续函数逼近, 非线性激活函数

## 3 点简述
- 研究输入连接多层感知机架构，隐藏神经元接收前层输出和原始输入的仿射连接。
- 在单变量设置中，给出网络函数的迭代公式，并证明通用逼近定理。
- 扩展到向量值输入，建立紧凑子集上连续函数的通用逼近定理。

## 摘要（原文）

> We introduce the Input-Connected Multilayer Perceptron (IC-MLP), a feedforward neural network architecture in which each hidden neuron receives, in addition to the outputs of the preceding layer, a direct affine connection from the raw input. We first study this architecture in the univariate setting and give an explicit and systematic description of IC-MLPs with an arbitrary finite number of hidden layers, including iterated formulas for the network functions. In this setting, we prove a universal approximation theorem showing that deep IC-MLPs can approximate any continuous function on a closed interval of the real line if and only if the activation function is nonlinear. We then extend the analysis to vector-valued inputs and establish a corresponding universal approximation theorem for continuous functions on compact subsets of $\mathbb{R}^n$.

