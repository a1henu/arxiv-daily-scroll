---
layout: default
title: Synthetic Pattern Generation and Detection of Financial Activities using Graph Autoencoders
---

# Synthetic Pattern Generation and Detection of Financial Activities using Graph Autoencoders
**arXiv**：[2601.21446v1](https://arxiv.org/abs/2601.21446) · [PDF](https://arxiv.org/pdf/2601.21446.pdf)  
**作者**：Francesco Zola, Lucia Muñoz, Andrea Venturi, Amaia Gil  

**一句话要点**：提出基于图自编码器的合成数据方法，用于检测金融活动中的非法模式

**关键词**：图自编码器, 金融活动检测, 合成数据生成, 拓扑模式学习, 图卷积网络

## 3 点简述
- 核心问题：非法金融活动检测因真实数据稀缺和隐私限制而困难
- 方法要点：使用参数化生成器创建合成数据，训练图自编码器学习拓扑模式
- 实验或效果：GAE-GCN在多种模式中表现最一致，GAE-SAGE和GAE-GAT仅在少数模式中竞争

## 摘要（原文）

> Illicit financial activities such as money laundering often manifest through recurrent topological patterns in transaction networks. Detecting these patterns automatically remains challenging due to the scarcity of labeled real-world data and strict privacy constraints. To address this, we investigate whether Graph Autoencoders (GAEs) can effectively learn and distinguish topological patterns that mimic money laundering operations when trained on synthetic data. The analysis consists of two phases: (i) data generation, where synthetic samples are created for seven well-known illicit activity patterns using parametrized generators that preserve structural consistency while introducing realistic variability; and (ii) model training and validation, where separate GAEs are trained on each pattern without explicit labels, relying solely on reconstruction error as an indicator of learned structure. We compare three GAE implementations based on three distinct convolutional layers: Graph Convolutional (GAE-GCN), GraphSAGE (GAE-SAGE), and Graph Attention Network (GAE-GAT). Experimental results show that GAE-GCN achieves the most consistent reconstruction performance across patterns, while GAE-SAGE and GAE-GAT exhibit competitive results only in few specific patterns. These findings suggest that graph-based representation learning on synthetic data provides a viable path toward developing AI-driven tools for detecting illicit behaviors, overcoming the limitations of financial datasets.

