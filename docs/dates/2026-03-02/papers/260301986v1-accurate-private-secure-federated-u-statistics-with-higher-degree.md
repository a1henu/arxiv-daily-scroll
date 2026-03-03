---
layout: default
title: Accurate, private, secure, federated U-statistics with higher degree
---

# Accurate, private, secure, federated U-statistics with higher degree
**arXiv**：[2603.01986v1](https://arxiv.org/abs/2603.01986) · [PDF](https://arxiv.org/pdf/2603.01986.pdf)  
**作者**：Quentin Sinh, Jan Ramon  

**一句话要点**：提出基于多方计算的协议，在联邦学习中安全计算高阶U统计量并提升准确性。

**关键词**：联邦学习, U统计量, 多方计算, 差分隐私, 统计推断, 安全计算

## 3 点简述
- 研究联邦学习下计算高阶U统计量的问题，涉及Kendall's τ等统计量。
- 利用多方计算实现中心差分隐私，改进现有方法的准确性和可扩展性。
- 理论分析显示误差显著降低，实验验证如Kendall's τ的均方误差减少达四个数量级。

## 摘要（原文）

> We study the problem of computing a U-statistic with a kernel function f of degree k $\ge$ 2, i.e., the average of some function f over all k-tuples of instances, in a federated learning setting. Ustatistics of degree 2 include several useful statistics such as Kendall's $τ$ coefficient, the Area under the Receiver-Operator Curve and the Gini mean difference. Existing methods provide solutions only under the lower-utility local differential privacy model and/or scale poorly in the size of the domain discretization. In this work, we propose a protocol that securely computes U-statistics of degree k $\ge$ 2 under central differential privacy by leveraging Multi Party Computation (MPC). Our method substantially improves accuracy when compared to prior solutions. We provide a detailed theoretical analysis of its accuracy, communication and computational properties. We evaluate its performance empirically, obtaining favorable results, e.g., for Kendall's $τ$ coefficient, our approach reduces the Mean Squared Error by up to four orders of magnitude over existing baselines.

