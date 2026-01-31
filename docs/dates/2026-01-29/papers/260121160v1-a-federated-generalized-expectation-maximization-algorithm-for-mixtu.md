---
layout: default
title: A Federated Generalized Expectation-Maximization Algorithm for Mixture Models with an Unknown Number of Components
---

# A Federated Generalized Expectation-Maximization Algorithm for Mixture Models with an Unknown Number of Components
**arXiv**：[2601.21160v1](https://arxiv.org/abs/2601.21160) · [PDF](https://arxiv.org/pdf/2601.21160.pdf)  
**作者**：Michael Ibrahim, Nagi Gebraeel, Weijun Xie  

**一句话要点**：提出FedGEM算法以解决联邦聚类中全局簇数未知和客户端数据异构重叠的问题

**关键词**：联邦学习, 聚类分析, 期望最大化算法, 混合模型, 异构数据

## 3 点简述
- 核心问题：联邦聚类中全局簇数未知，客户端数据具有异构且可能重叠的簇集
- 方法要点：客户端本地执行EM步骤并构建不确定性集，服务器利用这些集推断全局簇数和重叠
- 实验或效果：理论证明收敛性，数值实验显示性能接近集中式EM，优于现有联邦聚类方法

## 摘要（原文）

> We study the problem of federated clustering when the total number of clusters $K$ across clients is unknown, and the clients have heterogeneous but potentially overlapping cluster sets in their local data. To that end, we develop FedGEM: a federated generalized expectation-maximization algorithm for the training of mixture models with an unknown number of components. Our proposed algorithm relies on each of the clients performing EM steps locally, and constructing an uncertainty set around the maximizer associated with each local component. The central server utilizes the uncertainty sets to learn potential cluster overlaps between clients, and infer the global number of clusters via closed-form computations. We perform a thorough theoretical study of our algorithm, presenting probabilistic convergence guarantees under common assumptions. Subsequently, we study the specific setting of isotropic GMMs, providing tractable, low-complexity computations to be performed by each client during each iteration of the algorithm, as well as rigorously verifying assumptions required for algorithm convergence. We perform various numerical experiments, where we empirically demonstrate that our proposed method achieves comparable performance to centralized EM, and that it outperforms various existing federated clustering methods.

