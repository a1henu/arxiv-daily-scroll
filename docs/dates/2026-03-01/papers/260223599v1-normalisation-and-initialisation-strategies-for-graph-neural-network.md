---
layout: default
title: Normalisation and Initialisation Strategies for Graph Neural Networks in Blockchain Anomaly Detection
---

# Normalisation and Initialisation Strategies for Graph Neural Networks in Blockchain Anomaly Detection
**arXiv**：[2602.23599v1](https://arxiv.org/abs/2602.23599) · [PDF](https://arxiv.org/pdf/2602.23599.pdf)  
**作者**：Dang Sy Duy, Nguyen Duy Chien, Kapil Dev, Jeff Nijsse  

**一句话要点**：系统评估图神经网络在区块链异常检测中的归一化与初始化策略

**关键词**：图神经网络, 区块链异常检测, 初始化策略, 归一化策略, 反洗钱, 类不平衡

## 3 点简述
- 核心问题：图神经网络在反洗钱应用中，初始化与归一化策略的影响未充分探索。
- 方法要点：在Elliptic比特币数据集上，对GCN、GAT和GraphSAGE进行系统消融实验。
- 实验或效果：发现策略效果与架构相关，为类不平衡数据集提供实用部署指导。

## 摘要（原文）

> Graph neural networks (GNNs) offer a principled approach to financial fraud detection by jointly learning from node features and transaction graph topology. However, their effectiveness on real-world anti-money laundering (AML) benchmarks depends critically on training practices such as specifically weight initialisation and normalisation that remain underexplored. We present a systematic ablation of initialisation and normalisation strategies across three GNN architectures (GCN, GAT, and GraphSAGE) on the Elliptic Bitcoin dataset. Our experiments reveal that initialisation and normalisation are architecture-dependent: GraphSAGE achieves the strongest performance with Xavier initialisation alone, GAT benefits most from combining GraphNorm with Xavier initialisation, while GCN shows limited sensitivity to these modifications. These findings offer practical, architecture-specific guidance for deploying GNNs in AML pipelines for datasets with severe class imbalance. We release a reproducible experimental framework with temporal data splits, seeded runs, and full ablation results.

