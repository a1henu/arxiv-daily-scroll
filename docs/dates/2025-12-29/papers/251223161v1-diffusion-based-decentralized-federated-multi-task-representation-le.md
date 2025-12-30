---
layout: default
title: Diffusion-based Decentralized Federated Multi-Task Representation Learning
---

# Diffusion-based Decentralized Federated Multi-Task Representation Learning
**arXiv**：[2512.23161v1](https://arxiv.org/abs/2512.23161) · [PDF](https://arxiv.org/pdf/2512.23161.pdf)  
**作者**：Donghwa Kang, Shana Moothedath  

**一句话要点**：提出基于扩散的去中心化联邦多任务表示学习算法，用于数据稀缺环境下的线性回归任务。

**关键词**：多任务表示学习, 去中心化联邦学习, 扩散算法, 线性回归, 梯度下降, 通信效率

## 3 点简述
- 核心问题：在去中心化设置中，多任务线性回归模型共享低维线性表示，但相关研究较少。
- 方法要点：开发交替投影梯度下降和最小化算法，以扩散方式恢复低秩特征矩阵，提供样本和迭代复杂度保证。
- 实验或效果：通过数值模拟验证算法性能，显示其快速且通信高效，并与基准算法比较。

## 摘要（原文）

> Representation learning is a widely adopted framework for learning in data-scarce environments to obtain a feature extractor or representation from various different yet related tasks. Despite extensive research on representation learning, decentralized approaches remain relatively underexplored. This work develops a decentralized projected gradient descent-based algorithm for multi-task representation learning. We focus on the problem of multi-task linear regression in which multiple linear regression models share a common, low-dimensional linear representation. We present an alternating projected gradient descent and minimization algorithm for recovering a low-rank feature matrix in a diffusion-based decentralized and federated fashion. We obtain constructive, provable guarantees that provide a lower bound on the required sample complexity and an upper bound on the iteration complexity of our proposed algorithm. We analyze the time and communication complexity of our algorithm and show that it is fast and communication-efficient. We performed numerical simulations to validate the performance of our algorithm and compared it with benchmark algorithms.

