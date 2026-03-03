---
layout: default
title: CA-AFP: Cluster-Aware Adaptive Federated Pruning
---

# CA-AFP: Cluster-Aware Adaptive Federated Pruning
**arXiv**：[2603.01739v1](https://arxiv.org/abs/2603.01739) · [PDF](https://arxiv.org/pdf/2603.01739.pdf)  
**作者**：Om Govind Jha, Harsh Shukla, Haroon R. Lone  

**一句话要点**：提出CA-AFP框架，通过集群感知自适应剪枝联合解决联邦学习中的统计与系统异构性问题。

**关键词**：联邦学习, 模型剪枝, 聚类方法, 异构性处理, 自适应优化, 通信效率

## 3 点简述
- 核心问题：联邦学习面临统计异构性和资源受限设备导致的系统异构性挑战。
- 方法要点：基于聚类进行集群特定模型剪枝，结合权重幅度、集群内一致性和梯度一致性评分机制。
- 实验或效果：在人类活动识别基准上验证，平衡预测准确性、客户端间公平性和通信效率，优于基线方法。

## 摘要（原文）

> Federated Learning (FL) faces major challenges in real-world deployments due to statistical heterogeneity across clients and system heterogeneity arising from resource-constrained devices. While clustering-based approaches mitigate statistical heterogeneity and pruning techniques improve memory and communication efficiency, these strategies are typically studied in isolation.
>   We propose CA-AFP, a unified framework that jointly addresses both challenges by performing cluster-specific model pruning. In CA-AFP, clients are first grouped into clusters, and a separate model for each cluster is adaptively pruned during training. The framework introduces two key innovations: (1) a cluster-aware importance scoring mechanism that combines weight magnitude, intra-cluster coherence, and gradient consistency to identify parameters for pruning, and (2) an iterative pruning schedule that progressively removes parameters while enabling model self-healing through weight regrowth.
>   We evaluate CA-AFP on two widely used human activity recognition benchmarks, UCI HAR and WISDM, under natural user-based federated partitions. Experimental results demonstrate that CA-AFP achieves a favorable balance between predictive accuracy, inter-client fairness, and communication efficiency. Compared to pruning-based baselines, CA-AFP consistently improves accuracy and lower performance disparity across clients with limited fine-tuning, while requiring substantially less communication than dense clustering-based methods. It also shows robustness to different Non-IID levels of data. Finally, ablation studies analyze the impact of clustering, pruning schedules and scoring mechanism offering practical insights into the design of efficient and adaptive FL systems.

