---
layout: default
title: FairGFL: Privacy-Preserving Fairness-Aware Federated Learning with Overlapping Subgraphs
---

# FairGFL: Privacy-Preserving Fairness-Aware Federated Learning with Overlapping Subgraphs
**arXiv**：[2512.23235v1](https://arxiv.org/abs/2512.23235) · [PDF](https://arxiv.org/pdf/2512.23235.pdf)  
**作者**：Zihao Zhou, Shusen Yang, Fangyuan Zhao, Xuebin Ren  

**一句话要点**：提出FairGFL算法以解决图联邦学习中不平衡重叠子图导致的公平性问题

**关键词**：图联邦学习, 隐私保护, 公平性优化, 重叠子图, 加权聚合

## 3 点简述
- 核心问题：图数据中不平衡重叠子图引发跨客户端不公平，影响模型效用
- 方法要点：采用隐私保护的重叠比估计和加权聚合，结合正则化优化公平与效用权衡
- 实验或效果：在四个基准数据集上优于基线算法，提升模型效用和公平性

## 摘要（原文）

> Graph federated learning enables the collaborative extraction of high-order information from distributed subgraphs while preserving the privacy of raw data. However, graph data often exhibits overlap among different clients. Previous research has demonstrated certain benefits of overlapping data in mitigating data heterogeneity. However, the negative effects have not been explored, particularly in cases where the overlaps are imbalanced across clients. In this paper, we uncover the unfairness issue arising from imbalanced overlapping subgraphs through both empirical observations and theoretical reasoning. To address this issue, we propose FairGFL (FAIRness-aware subGraph Federated Learning), a novel algorithm that enhances cross-client fairness while maintaining model utility in a privacy-preserving manner. Specifically, FairGFL incorporates an interpretable weighted aggregation approach to enhance fairness across clients, leveraging privacy-preserving estimation of their overlapping ratios. Furthermore, FairGFL improves the tradeoff between model utility and fairness by integrating a carefully crafted regularizer into the federated composite loss function. Through extensive experiments on four benchmark graph datasets, we demonstrate that FairGFL outperforms four representative baseline algorithms in terms of both model utility and fairness.

