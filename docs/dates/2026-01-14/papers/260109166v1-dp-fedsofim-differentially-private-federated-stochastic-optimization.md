---
layout: default
title: DP-FEDSOFIM: Differentially Private Federated Stochastic Optimization using Regularized Fisher Information Matrix
---

# DP-FEDSOFIM: Differentially Private Federated Stochastic Optimization using Regularized Fisher Information Matrix
**arXiv**：[2601.09166v1](https://arxiv.org/abs/2601.09166) · [PDF](https://arxiv.org/pdf/2601.09166.pdf)  
**作者**：Sidhant R. Nair, Tanmay Sen, Mrinmay Sen  

**一句话要点**：提出DP-FedSOFIM以解决差分隐私联邦学习中二阶方法内存开销高的问题

**关键词**：差分隐私联邦学习, 二阶优化, Fisher信息矩阵, 内存效率, 服务器端预处理

## 3 点简述
- 差分隐私联邦学习在严格隐私预算下收敛慢，二阶方法内存开销大
- 利用Fisher信息矩阵作为预处理器，客户端仅需O(d)内存，通过Sherman-Morrison公式高效计算
- 实验在CIFAR-10上显示优于一阶基线，服务器端预处理保持差分隐私

## 摘要（原文）

> Differentially private federated learning (DP-FL) suffers from slow convergence under tight privacy budgets due to the overwhelming noise introduced to preserve privacy. While adaptive optimizers can accelerate convergence, existing second-order methods such as DP-FedNew require O(d^2) memory at each client to maintain local feature covariance matrices, making them impractical for high-dimensional models. We propose DP-FedSOFIM, a server-side second-order optimization framework that leverages the Fisher Information Matrix (FIM) as a natural gradient preconditioner while requiring only O(d) memory per client. By employing the Sherman-Morrison formula for efficient matrix inversion, DP-FedSOFIM achieves O(d) computational complexity per round while maintaining the convergence benefits of second-order methods. Our analysis proves that the server-side preconditioning preserves (epsilon, delta)-differential privacy through the post-processing theorem. Empirical evaluation on CIFAR-10 demonstrates that DP-FedSOFIM achieves superior test accuracy compared to first-order baselines across multiple privacy regimes.

