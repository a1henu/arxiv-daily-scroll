---
layout: default
title: Stragglers Can Contribute More: Uncertainty-Aware Distillation for Asynchronous Federated Learning
---

# Stragglers Can Contribute More: Uncertainty-Aware Distillation for Asynchronous Federated Learning
**arXiv**：[2511.19966v1](https://arxiv.org/abs/2511.19966) · [PDF](https://arxiv.org/pdf/2511.19966.pdf)  
**作者**：Yujia Wang, Fenglong Ma, Jinghui Chen  

**一句话要点**：提出FedEcho框架，通过不确定性感知蒸馏解决异步联邦学习中的过时更新和数据异构问题。

**关键词**：异步联邦学习, 不确定性感知, 知识蒸馏, 数据异构, 模型更新, 客户端可靠性

## 3 点简述
- 异步联邦学习面临过时更新和快速客户端主导导致的性能下降与偏见问题。
- 采用不确定性感知蒸馏，服务器评估预测可靠性并动态调整影响。
- 实验显示FedEcho在异步延迟和数据异构下优于现有基线，无需访问私有数据。

## 摘要（原文）

> Asynchronous federated learning (FL) has recently gained attention for its enhanced efficiency and scalability, enabling local clients to send model updates to the server at their own pace without waiting for slower participants. However, such a design encounters significant challenges, such as the risk of outdated updates from straggler clients degrading the overall model performance and the potential bias introduced by faster clients dominating the learning process, especially under heterogeneous data distributions. Existing methods typically address only one of these issues, creating a conflict where mitigating the impact of outdated updates can exacerbate the bias created by faster clients, and vice versa. To address these challenges, we propose FedEcho, a novel framework that incorporates uncertainty-aware distillation to enhance the asynchronous FL performances under large asynchronous delays and data heterogeneity. Specifically, uncertainty-aware distillation enables the server to assess the reliability of predictions made by straggler clients, dynamically adjusting the influence of these predictions based on their estimated uncertainty. By prioritizing more certain predictions while still leveraging the diverse information from all clients, FedEcho effectively mitigates the negative impacts of outdated updates and data heterogeneity. Through extensive experiments, we demonstrate that FedEcho consistently outperforms existing asynchronous federated learning baselines, achieving robust performance without requiring access to private client data.

