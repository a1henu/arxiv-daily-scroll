---
layout: default
title: Device Association and Resource Allocation for Hierarchical Split Federated Learning in Space-Air-Ground Integrated Network
---

# Device Association and Resource Allocation for Hierarchical Split Federated Learning in Space-Air-Ground Integrated Network
**arXiv**：[2601.13817v1](https://arxiv.org/abs/2601.13817) · [PDF](https://arxiv.org/pdf/2601.13817.pdf)  
**作者**：Haitao Zhao, Xiaoyu Tang, Bo Xu, Jinlong Sun, Linghao Zhang  

**一句话要点**：提出分层分割联邦学习框架，优化设备关联与资源分配以解决SAGIN中联邦学习的资源受限和数据不平衡问题。

**关键词**：分层分割联邦学习, 空间-空-地一体化网络, 设备关联, 资源分配, 联合优化, 训练效率

## 3 点简述
- 核心问题：6G SAGIN中联邦学习面临资源受限和数据分布不平衡的挑战。
- 方法要点：设计HSFL框架，通过联合优化设备关联、模型分割层选择和资源分配来最小化训练损失和延迟。
- 实验或效果：仿真结果表明算法能有效平衡SAGIN中联邦学习的训练效率和模型准确性。

## 摘要（原文）

> 6G facilitates deployment of Federated Learning (FL) in the Space-Air-Ground Integrated Network (SAGIN), yet FL confronts challenges such as resource constrained and unbalanced data distribution. To address these issues, this paper proposes a Hierarchical Split Federated Learning (HSFL) framework and derives its upper bound of loss function. To minimize the weighted sum of training loss and latency, we formulate a joint optimization problem that integrates device association, model split layer selection, and resource allocation. We decompose the original problem into several subproblems, where an iterative optimization algorithm for device association and resource allocation based on brute-force split point search is proposed. Simulation results demonstrate that the proposed algorithm can effectively balance training efficiency and model accuracy for FL in SAGIN.

