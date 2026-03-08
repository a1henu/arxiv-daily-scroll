---
layout: default
title: FedBCD:Communication-Efficient Accelerated Block Coordinate Gradient Descent for Federated Learning
---

# FedBCD:Communication-Efficient Accelerated Block Coordinate Gradient Descent for Federated Learning
**arXiv**：[2603.05116v1](https://arxiv.org/abs/2603.05116) · [PDF](https://arxiv.org/pdf/2603.05116.pdf)  
**作者**：Junkang Liu, Fanhua Shang, Yuanyuan Liu, Hongying Liu, Yuangang Li, YunXiang Gong  

**一句话要点**：提出FedBCGD方法以降低联邦学习中大规模模型的通信开销

**关键词**：联邦学习, 通信效率, 参数分块, 梯度下降, 收敛分析, 大规模模型

## 3 点简述
- 针对联邦学习中大规模模型通信开销高的问题
- 通过参数分块上传和加速算法降低通信复杂度
- 理论分析和实验验证了方法的优越性和收敛性

## 摘要（原文）

> Although Federated Learning has been widely studied in recent years, there are still high overhead expenses in each communication round for large-scale models such as Vision Transformer. To lower the communication complexity, we propose a novel Federated Block Coordinate Gradient Descent (FedBCGD) method for communication efficiency. The proposed method splits model parameters into several blocks, including a shared block and enables uploading a specific parameter block by each client, which can significantly reduce communication overhead. Moreover, we also develop an accelerated FedBCGD algorithm (called FedBCGD+) with client drift control and stochastic variance reduction. To the best of our knowledge, this paper is the first work on parameter block communication for training large-scale deep models. We also provide the convergence analysis for the proposed algorithms. Our theoretical results show that the communication complexities of our algorithms are a factor $1/N$ lower than those of existing methods, where $N$ is the number of parameter blocks, and they enjoy much faster convergence than their counterparts. Empirical results indicate the superiority of the proposed algorithms compared to state-of-the-art algorithms.
>   The code is available at https://github.com/junkangLiu0/FedBCGD.

