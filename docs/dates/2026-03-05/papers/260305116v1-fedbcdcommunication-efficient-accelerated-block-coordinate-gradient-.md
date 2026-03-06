---
layout: default
title: FedBCD:Communication-Efficient Accelerated Block Coordinate Gradient Descent for Federated Learning
---

# FedBCD:Communication-Efficient Accelerated Block Coordinate Gradient Descent for Federated Learning
**arXiv**：[2603.05116v1](https://arxiv.org/abs/2603.05116) · [PDF](https://arxiv.org/pdf/2603.05116.pdf)  
**作者**：Junkang Liu, Fanhua Shang, Yuanyuan Liu, Hongying Liu, Yuangang Li, YunXiang Gong  

**一句话要点**：提出FedBCGD方法以降低联邦学习中大规模模型的通信开销

**关键词**：联邦学习, 通信效率, 参数分块, 梯度下降, 大规模模型, 收敛分析

## 3 点简述
- 核心问题：联邦学习在大规模模型（如Vision Transformer）训练中通信开销高
- 方法要点：将模型参数分块，客户端仅上传特定块，结合加速算法控制客户端漂移
- 实验或效果：理论分析显示通信复杂度降低至1/N，实证结果优于现有方法

## 摘要（原文）

> Although Federated Learning has been widely studied in recent years, there are still high overhead expenses in each communication round for large-scale models such as Vision Transformer. To lower the communication complexity, we propose a novel Federated Block Coordinate Gradient Descent (FedBCGD) method for communication efficiency. The proposed method splits model parameters into several blocks, including a shared block and enables uploading a specific parameter block by each client, which can significantly reduce communication overhead. Moreover, we also develop an accelerated FedBCGD algorithm (called FedBCGD+) with client drift control and stochastic variance reduction. To the best of our knowledge, this paper is the first work on parameter block communication for training large-scale deep models. We also provide the convergence analysis for the proposed algorithms. Our theoretical results show that the communication complexities of our algorithms are a factor $1/N$ lower than those of existing methods, where $N$ is the number of parameter blocks, and they enjoy much faster convergence than their counterparts. Empirical results indicate the superiority of the proposed algorithms compared to state-of-the-art algorithms.
>   The code is available at https://github.com/junkangLiu0/FedBCGD.

