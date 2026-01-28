---
layout: default
title: GraphDLG: Exploring Deep Leakage from Gradients in Federated Graph Learning
---

# GraphDLG: Exploring Deep Leakage from Gradients in Federated Graph Learning
**arXiv**：[2601.19745v1](https://arxiv.org/abs/2601.19745) · [PDF](https://arxiv.org/pdf/2601.19745.pdf)  
**作者**：Shuyue Wei, Wantong Chen, Tongyu Wei, Chen Gong, Yongxin Tong, Lizhen Cui  

**一句话要点**：提出GraphDLG以解决联邦图学习中梯度泄露导致的原始图数据恢复问题

**关键词**：联邦图学习, 梯度泄露, 图神经网络, 隐私保护, 数据恢复

## 3 点简述
- 核心问题：联邦图学习中梯度泄露能否有效恢复图结构和节点特征，现有研究多聚焦图像或文本数据
- 方法要点：理论分析FGL组件，提出GraphDLG利用随机图或客户端训练图辅助恢复，通过递归规则解耦图结构与节点特征
- 实验或效果：实验显示GraphDLG优于现有方案，节点特征重建MSE提升超5.46%，图结构重建AUC提升超25.04%

## 摘要（原文）

> Federated graph learning (FGL) has recently emerged as a promising privacy-preserving paradigm that enables distributed graph learning across multiple data owners. A critical privacy concern in federated learning is whether an adversary can recover raw data from shared gradients, a vulnerability known as deep leakage from gradients (DLG). However, most prior studies on the DLG problem focused on image or text data, and it remains an open question whether graphs can be effectively recovered, particularly when the graph structure and node features are uniquely entangled in GNNs. In this work, we first theoretically analyze the components in FGL and derive a crucial insight: once the graph structure is recovered, node features can be obtained through a closed-form recursive rule. Building on this analysis, we propose GraphDLG, a novel approach to recover raw training graphs from shared gradients in FGL, which can utilize randomly generated graphs or client-side training graphs as auxiliaries to enhance recovery. Extensive experiments demonstrate that GraphDLG outperforms existing solutions by successfully decoupling the graph structure and node features, achieving improvements of over 5.46% (by MSE) for node feature reconstruction and over 25.04% (by AUC) for graph structure reconstruction.

