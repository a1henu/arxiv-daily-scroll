---
layout: default
title: Adaptive Decentralized Federated Learning for Robust Optimization
---

# Adaptive Decentralized Federated Learning for Robust Optimization
**arXiv**：[2512.02852v1](https://arxiv.org/abs/2512.02852) · [PDF](https://arxiv.org/pdf/2512.02852.pdf)  
**作者**：Shuyuan Wu, Feifei Wang, Yuan Gao, Hansheng Wang  

**一句话要点**：提出自适应去中心化联邦学习以解决异常客户端对模型鲁棒性的影响

**关键词**：去中心化联邦学习, 鲁棒优化, 自适应学习率, 异常客户端检测, 收敛分析

## 3 点简述
- 核心问题：去中心化联邦学习中异常客户端（如噪声或中毒数据）会破坏学习过程，降低模型鲁棒性。
- 方法要点：通过自适应调整客户端学习率，对可疑客户端分配较小率、正常客户端分配较大率，无需先验知识或严格邻居条件。
- 实验或效果：理论分析保证收敛性，数值实验显示aDFL方法性能优越。

## 摘要（原文）

> In decentralized federated learning (DFL), the presence of abnormal clients, often caused by noisy or poisoned data, can significantly disrupt the learning process and degrade the overall robustness of the model. Previous methods on this issue often require a sufficiently large number of normal neighboring clients or prior knowledge of reliable clients, which reduces the practical applicability of DFL. To address these limitations, we develop here a novel adaptive DFL (aDFL) approach for robust estimation. The key idea is to adaptively adjust the learning rates of clients. By assigning smaller rates to suspicious clients and larger rates to normal clients, aDFL mitigates the negative impact of abnormal clients on the global model in a fully adaptive way. Our theory does not put any stringent conditions on neighboring nodes and requires no prior knowledge. A rigorous convergence analysis is provided to guarantee the oracle property of aDFL. Extensive numerical experiments demonstrate the superior performance of the aDFL method.

