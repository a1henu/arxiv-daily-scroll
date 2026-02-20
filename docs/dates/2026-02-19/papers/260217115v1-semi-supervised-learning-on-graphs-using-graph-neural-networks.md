---
layout: default
title: Semi-Supervised Learning on Graphs using Graph Neural Networks
---

# Semi-Supervised Learning on Graphs using Graph Neural Networks
**arXiv**：[2602.17115v1](https://arxiv.org/abs/2602.17115) · [PDF](https://arxiv.org/pdf/2602.17115.pdf)  
**作者**：Juntong Chen, Claire Donnat, Olga Klopp, Johannes Schmidt-Hieber  

**一句话要点**：提出图神经网络半监督节点回归的严格风险界理论，以解释其成功条件与性能缩放。

**关键词**：图神经网络, 半监督学习, 节点回归, 风险界理论, 图卷积, 非参数估计

## 3 点简述
- 核心问题：图神经网络在半监督节点回归中表现优异，但缺乏严谨理论解释其成功机制与局限性。
- 方法要点：研究聚合-读出模型，针对线性图卷积和深度ReLU读出，推导非渐近风险界，分离近似、随机和优化误差。
- 实验或效果：数值实验验证理论，提供理解图神经网络性能与局限的系统框架，并推导全监督下的经典非参数收敛率。

## 摘要（原文）

> Graph neural networks (GNNs) work remarkably well in semi-supervised node regression, yet a rigorous theory explaining when and why they succeed remains lacking. To address this gap, we study an aggregate-and-readout model that encompasses several common message passing architectures: node features are first propagated over the graph then mapped to responses via a nonlinear function. For least-squares estimation over GNNs with linear graph convolutions and a deep ReLU readout, we prove a sharp non-asymptotic risk bound that separates approximation, stochastic, and optimization errors. The bound makes explicit how performance scales with the fraction of labeled nodes and graph-induced dependence. Approximation guarantees are further derived for graph-smoothing followed by smooth nonlinear readouts, yielding convergence rates that recover classical nonparametric behavior under full supervision while characterizing performance when labels are scarce. Numerical experiments validate our theory, providing a systematic framework for understanding GNN performance and limitations.

