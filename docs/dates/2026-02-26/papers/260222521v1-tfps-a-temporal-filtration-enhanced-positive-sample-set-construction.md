---
layout: default
title: TFPS: A Temporal Filtration-enhanced Positive Sample Set Construction Method for Implicit Collaborative Filtering
---

# TFPS: A Temporal Filtration-enhanced Positive Sample Set Construction Method for Implicit Collaborative Filtering
**arXiv**：[2602.22521v1](https://arxiv.org/abs/2602.22521) · [PDF](https://arxiv.org/pdf/2602.22521.pdf)  
**作者**：Jiayi Wu, Zhengyu Wu, Xunkai Li, Rong-Hua Li, Guoren Wang  

**一句话要点**：提出TFPS方法，通过时间过滤增强正样本集构建，以解决隐式协同过滤中忽视时间信息的问题。

**关键词**：隐式协同过滤, 正样本构建, 时间过滤, 推荐系统, 图分层

## 3 点简述
- 核心问题：现有隐式协同过滤方法忽视时间间隔信息，难以准确捕捉用户当前偏好。
- 方法要点：基于时间间隔设计衰减模型，将原始图分层，并采用层增强策略构建高质量正样本集。
- 实验或效果：在三个真实数据集上验证有效性，可提升Recall@k和NDCG@k指标。

## 摘要（原文）

> The negative sampling strategy can effectively train collaborative filtering (CF) recommendation models based on implicit feedback by constructing positive and negative samples. However, existing methods primarily optimize the negative sampling process while neglecting the exploration of positive samples. Some denoising recommendation methods can be applied to denoise positive samples within negative sampling strategies, but they ignore temporal information. Existing work integrates sequential information during model aggregation but neglects time interval information, hindering accurate capture of users' current preferences. To address this problem, from a data perspective, we propose a novel temporal filtration-enhanced approach to construct a high-quality positive sample set. First, we design a time decay model based on interaction time intervals, transforming the original graph into a weighted user-item bipartite graph. Then, based on predefined filtering operations, the weighted user-item bipartite graph is layered. Finally, we design a layer-enhancement strategy to construct a high-quality positive sample set for the layered subgraphs. We provide theoretical insights into why TFPS can improve Recall@k and NDCG@k, and extensive experiments on three real-world datasets demonstrate the effectiveness of the proposed method. Additionally, TFPS can be integrated with various implicit CF recommenders or negative sampling methods to enhance its performance.

