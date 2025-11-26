---
layout: default
title: On the Limits of Momentum in Decentralized and Federated Optimization
---

# On the Limits of Momentum in Decentralized and Federated Optimization
**arXiv**：[2511.20168v1](https://arxiv.org/abs/2511.20168) · [PDF](https://arxiv.org/pdf/2511.20168.pdf)  
**作者**：Riccardo Zaccone, Sai Praneeth Karimireddy, Carlo Masone  

**一句话要点**：分析动量在去中心化和联邦优化中的局限性，证明其受统计异质性影响

**关键词**：联邦学习, 去中心化优化, 动量方法, 统计异质性, 收敛分析

## 3 点简述
- 核心问题：动量在去中心化和联邦学习中是否能克服统计异质性保证收敛
- 方法要点：理论分析动量在循环客户端参与下的行为，证明其收敛受限
- 实验或效果：数值和深度学习实验验证理论，确认在现实场景中的相关性

## 摘要（原文）

> Recent works have explored the use of momentum in local methods to enhance distributed SGD. This is particularly appealing in Federated Learning (FL), where momentum intuitively appears as a solution to mitigate the effects of statistical heterogeneity. Despite recent progress in this direction, it is still unclear if momentum can guarantee convergence under unbounded heterogeneity in decentralized scenarios, where only some workers participate at each round. In this work we analyze momentum under cyclic client participation, and theoretically prove that it remains inevitably affected by statistical heterogeneity. Similarly to SGD, we prove that decreasing step-sizes do not help either: in fact, any schedule decreasing faster than $Θ\left(1/t\right)$ leads to convergence to a constant value that depends on the initialization and the heterogeneity bound. Numerical results corroborate the theory, and deep learning experiments confirm its relevance for realistic settings.

