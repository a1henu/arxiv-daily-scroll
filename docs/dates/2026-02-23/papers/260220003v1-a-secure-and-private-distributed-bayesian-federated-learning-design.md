---
layout: default
title: A Secure and Private Distributed Bayesian Federated Learning Design
---

# A Secure and Private Distributed Bayesian Federated Learning Design
**arXiv**：[2602.20003v1](https://arxiv.org/abs/2602.20003) · [PDF](https://arxiv.org/pdf/2602.20003.pdf)  
**作者**：Nuocheng Yang, Sihua Wang, Zhaohui Yang, Mingzhe Chen, Changchuan Yin, Kaibin Huang  

**一句话要点**：提出基于贝叶斯联邦学习的分布式框架，以解决隐私泄露、拜占庭攻击和收敛慢问题。

**关键词**：分布式联邦学习, 贝叶斯学习, 隐私保护, 拜占庭鲁棒性, 图神经网络, 强化学习

## 3 点简述
- 核心问题：分布式联邦学习面临隐私泄露、拜占庭攻击和收敛速度慢的挑战。
- 方法要点：采用贝叶斯方法训练本地模型，通过图神经网络强化学习优化邻居选择。
- 实验或效果：仿真显示方法在鲁棒性和效率上优于传统方案，且开销更低。

## 摘要（原文）

> Distributed Federated Learning (DFL) enables decentralized model training across large-scale systems without a central parameter server. However, DFL faces three critical challenges: privacy leakage from honest-but-curious neighbors, slow convergence due to the lack of central coordination, and vulnerability to Byzantine adversaries aiming to degrade model accuracy. To address these issues, we propose a novel DFL framework that integrates Byzantine robustness, privacy preservation, and convergence acceleration. Within this framework, each device trains a local model using a Bayesian approach and independently selects an optimal subset of neighbors for posterior exchange. We formulate this neighbor selection as an optimization problem to minimize the global loss function under security and privacy constraints. Solving this problem is challenging because devices only possess partial network information, and the complex coupling between topology, security, and convergence remains unclear. To bridge this gap, we first analytically characterize the trade-offs between dynamic connectivity, Byzantine detection, privacy levels, and convergence speed. Leveraging these insights, we develop a fully distributed Graph Neural Network (GNN)-based Reinforcement Learning (RL) algorithm. This approach enables devices to make autonomous connection decisions based on local observations. Simulation results demonstrate that our method achieves superior robustness and efficiency with significantly lower overhead compared to traditional security and privacy schemes.

