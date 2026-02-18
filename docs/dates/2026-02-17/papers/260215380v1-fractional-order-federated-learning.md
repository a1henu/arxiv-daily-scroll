---
layout: default
title: Fractional-Order Federated Learning
---

# Fractional-Order Federated Learning
**arXiv**：[2602.15380v1](https://arxiv.org/abs/2602.15380) · [PDF](https://arxiv.org/pdf/2602.15380.pdf)  
**作者**：Mohammad Partohaghighi, Roummel Marcia, YangQuan Chen  

**一句话要点**：提出分数阶联邦平均以提升异构数据下的联邦学习效率与稳定性

**关键词**：联邦学习, 分数阶优化, 非独立同分布数据, 收敛加速, 通信效率, 记忆感知更新

## 3 点简述
- 联邦学习存在收敛慢、通信成本高和非独立同分布数据问题
- 引入分数阶随机梯度下降，利用记忆感知更新捕获长期依赖关系
- 在多个基准数据集上验证了性能优势，并提供了理论收敛证明

## 摘要（原文）

> Federated learning (FL) allows remote clients to train a global model collaboratively while protecting client privacy. Despite its privacy-preserving benefits, FL has significant drawbacks, including slow convergence, high communication cost, and non-independent-and-identically-distributed (non-IID) data. In this work, we present a novel FedAvg variation called Fractional-Order Federated Averaging (FOFedAvg), which incorporates Fractional-Order Stochastic Gradient Descent (FOSGD) to capture long-range relationships and deeper historical information. By introducing memory-aware fractional-order updates, FOFedAvg improves communication efficiency and accelerates convergence while mitigating instability caused by heterogeneous, non-IID client data. We compare FOFedAvg against a broad set of established federated optimization algorithms on benchmark datasets including MNIST, FEMNIST, CIFAR-10, CIFAR-100, EMNIST, the Cleveland heart disease dataset, Sent140, PneumoniaMNIST, and Edge-IIoTset. Across a range of non-IID partitioning schemes, FOFedAvg is competitive with, and often outperforms, these baselines in terms of test performance and convergence speed. On the theoretical side, we prove that FOFedAvg converges to a stationary point under standard smoothness and bounded-variance assumptions for fractional order $0<α\le 1$. Together, these results show that fractional-order, memory-aware updates can substantially improve the robustness and effectiveness of federated learning, offering a practical path toward distributed training on heterogeneous data.

