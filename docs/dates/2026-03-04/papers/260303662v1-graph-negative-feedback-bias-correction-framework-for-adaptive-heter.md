---
layout: default
title: Graph Negative Feedback Bias Correction Framework for Adaptive Heterophily Modeling
---

# Graph Negative Feedback Bias Correction Framework for Adaptive Heterophily Modeling
**arXiv**：[2603.03662v1](https://arxiv.org/abs/2603.03662) · [PDF](https://arxiv.org/pdf/2603.03662.pdf)  
**作者**：Jiaqi Lv, Qingfeng Du, Yu Zhang, Yongqi Han, Sheng Li  

**一句话要点**：提出图负反馈偏置校正框架，以解决异配图上的性能下降问题。

**关键词**：图神经网络, 异配性建模, 偏置校正, 负反馈机制, Dirichlet能量

## 3 点简述
- 核心问题：传统图神经网络受同配性假设限制，在异配图上性能不佳。
- 方法要点：利用负反馈机制校正偏置，引入负反馈损失和独立节点特征反馈。
- 实验或效果：框架可无缝集成现有架构，提升性能且计算开销相近。

## 摘要（原文）

> Graph Neural Networks (GNNs) have emerged as a powerful framework for processing graph-structured data. However, conventional GNNs and their variants are inherently limited by the homophily assumption, leading to degradation in performance on heterophilic graphs. Although substantial efforts have been made to mitigate this issue, they remain constrained by the message-passing paradigm, which is inherently rooted in homophily. In this paper, a detailed analysis of how the underlying label autocorrelation of the homophily assumption introduces bias into GNNs is presented. We innovatively leverage a negative feedback mechanism to correct the bias and propose Graph Negative Feedback Bias Correction (GNFBC), a simple yet effective framework that is independent of any specific aggregation strategy. Specifically, we introduce a negative feedback loss that penalizes the sensitivity of predictions to label autocorrelation. Furthermore, we incorporate the output of graph-agnostic models as a feedback term, leveraging independent node feature information to counteract correlation-induced bias guided by Dirichlet energy. GNFBC can be seamlessly integrated into existing GNN architectures, improving overall performance with comparable computational and memory overhead.

