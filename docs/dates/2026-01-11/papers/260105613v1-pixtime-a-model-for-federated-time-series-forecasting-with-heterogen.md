---
layout: default
title: PiXTime: A Model for Federated Time Series Forecasting with Heterogeneous Data Structures Across Nodes
---

# PiXTime: A Model for Federated Time Series Forecasting with Heterogeneous Data Structures Across Nodes
**arXiv**：[2601.05613v1](https://arxiv.org/abs/2601.05613) · [PDF](https://arxiv.org/pdf/2601.05613.pdf)  
**作者**：Yiming Zhou, Mingyue Cheng, Hao Wang, Enhong Chen  

**一句话要点**：提出PiXTime模型以解决联邦学习中节点间时间序列粒度与变量集异构的预测问题

**关键词**：联邦学习, 时间序列预测, 异构数据, Transformer模型, 跨节点迁移

## 3 点简述
- 核心问题：节点间时间序列因采样标准不同导致粒度与变量集异构，阻碍传统联邦学习
- 方法要点：采用个性化Patch Embedding统一维度，结合全局VE Table对齐变量语义，增强跨节点可迁移性
- 实验或效果：在联邦设置下实现SOTA性能，并在八个真实基准上展示优越预测表现

## 摘要（原文）

> Time series are highly valuable and rarely shareable across nodes, making federated learning a promising paradigm to leverage distributed temporal data. However, different sampling standards lead to diverse time granularities and variable sets across nodes, hindering classical federated learning. We propose PiXTime, a novel time series forecasting model designed for federated learning that enables effective prediction across nodes with multi-granularity and heterogeneous variable sets. PiXTime employs a personalized Patch Embedding to map node-specific granularity time series into token sequences of a unified dimension for processing by a subsequent shared model, and uses a global VE Table to align variable category semantics across nodes, thereby enhancing cross-node transferability. With a transformer-based shared model, PiXTime captures representations of auxiliary series with arbitrary numbers of variables and uses cross-attention to enhance the prediction of the target series. Experiments show PiXTime achieves state-of-the-art performance in federated settings and demonstrates superior performance on eight widely used real-world traditional benchmarks.

