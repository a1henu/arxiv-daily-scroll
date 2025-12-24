---
layout: default
title: FedPOD: the deployable units of training for federated learning
---

# FedPOD: the deployable units of training for federated learning
**arXiv**：[2512.20610v1](https://arxiv.org/abs/2512.20610) · [PDF](https://arxiv.org/pdf/2512.20610.pdf)  
**作者**：Daewoon Kim, Si Young Yie, Jae Sung Lee  

**一句话要点**：提出FedPOD以优化联邦学习中的训练效率和通信成本，并兼容Kubernetes自动扩展。

**关键词**：联邦学习, 训练效率优化, 通信成本降低, Kubernetes兼容, 数据分布建模

## 3 点简述
- 核心问题：FedPIDAvg因排除异常参与者和依赖历史信息，限制了数据利用和灵活性。
- 方法要点：FedPOD通过纳入异常参与者、消除历史依赖和每轮计算验证损失来改进。
- 实验或效果：在Dice分数和收敛分数上表现与FedPIDAvg相当，平均分数分别为0.78、0.71、0.72和0.74。

## 摘要（原文）

> This paper proposes FedPOD (Proportionally Orchestrated Derivative) for optimizing learning efficiency and communication cost in federated learning among multiple clients. Inspired by FedPIDAvg, we define a round-wise task for FedPOD to enhance training efficiency. FedPIDAvg achieved performance improvement by incorporating the training loss reduction for prediction entropy as weights using differential terms. Furthermore, by modeling data distribution with a Poisson distribution and using a PID controller, it reduced communication costs even in skewed data distribution. However, excluding participants classified as outliers based on the Poisson distribution can limit data utilization. Additionally, PID controller requires the same participants to be maintained throughout the federated learning process as it uses previous rounds' learning information in the current round. In our approach, FedPOD addresses these issues by including participants excluded as outliers, eliminating dependency on previous rounds' learning information, and applying a method for calculating validation loss at each round. In this challenge, FedPOD presents comparable performance to FedPIDAvg in metrics of Dice score, 0.78, 0.71 and 0.72 for WT, ET and TC in average, and projected convergence score, 0.74 in average. Furthermore, the concept of FedPOD draws inspiration from Kubernetes' smallest computing unit, POD, designed to be compatible with Kubernetes auto-scaling. Extending round-wise tasks of FedPOD to POD units allows flexible design by applying scale-out similar to Kubernetes' auto-scaling. This work demonstrated the potentials of FedPOD to enhance federated learning by improving efficiency, flexibility, and performance in metrics.

