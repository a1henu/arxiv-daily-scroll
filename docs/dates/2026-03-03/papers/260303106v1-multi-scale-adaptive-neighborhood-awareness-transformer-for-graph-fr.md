---
layout: default
title: Multi-Scale Adaptive Neighborhood Awareness Transformer For Graph Fraud Detection
---

# Multi-Scale Adaptive Neighborhood Awareness Transformer For Graph Fraud Detection
**arXiv**：[2603.03106v1](https://arxiv.org/abs/2603.03106) · [PDF](https://arxiv.org/pdf/2603.03106.pdf)  
**作者**：Jiaqi Lv, Qingfeng Du, Yu Zhang, Yongqi Han, Sheng Li  

**一句话要点**：提出多尺度自适应邻域感知Transformer以解决图欺诈检测中的同质性假设和全局建模限制问题。

**关键词**：图欺诈检测, Transformer, 多尺度位置编码, 异质性连接, 全局建模, 图神经网络

## 3 点简述
- 核心问题：图神经网络在同质性假设和全局建模能力上的固有归纳偏差限制了欺诈检测效果。
- 方法要点：设计多尺度位置编码和异质性连接嵌入策略，增强全局建模并缓解分布差异。
- 实验或效果：在三个欺诈检测数据集上验证了MANDATE的优越性能。

## 摘要（原文）

> Graph fraud detection (GFD) is crucial for identifying fraudulent behavior within graphs, benefiting various domains such as financial networks and social media. Existing methods based on graph neural networks (GNNs) have succeeded considerably due to their effective expressive capacity for graph-structured data. However, the inherent inductive bias of GNNs, including the homogeneity assumption and the limited global modeling ability, hinder the effectiveness of these models. To address these challenges, we propose Multi-scale Neighborhood Awareness Transformer (MANDATE), which alleviates the inherent inductive bias of GNNs. Specifically, we design a multi-scale positional encoding strategy to encode the positional information of various distances from the central node. By incorporating it with the self-attention mechanism, the global modeling ability can be enhanced significantly. Meanwhile, we design different embedding strategies for homophilic and heterophilic connections. This mitigates the homophily distribution differences between benign and fraudulent nodes. Moreover, an embedding fusion strategy is designed for multi-relation graphs, which alleviates the distribution bias caused by different relationships. Experiments on three fraud detection datasets demonstrate the superiority of MANDATE.

