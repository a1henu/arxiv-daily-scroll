---
layout: default
title: Semi-Supervised Learning on Graphs using Graph Neural Networks
---

# Semi-Supervised Learning on Graphs using Graph Neural Networks
**arXiv**：[2602.17115v1](https://arxiv.org/abs/2602.17115) · [PDF](https://arxiv.org/pdf/2602.17115.pdf)  
**作者**：Juntong Chen, Claire Donnat, Olga Klopp, Johannes Schmidt-Hieber  

**一句话要点**：提出聚合-读出模型以分析图神经网络在半监督节点回归中的理论性能

**关键词**：图神经网络, 半监督学习, 节点回归, 理论分析, 风险界, 图卷积

## 3 点简述
- 核心问题：图神经网络在半监督节点回归中缺乏严格理论解释其成功条件
- 方法要点：使用线性图卷积和深度ReLU读出，推导非渐近风险界分离误差成分
- 实验或效果：数值实验验证理论，提供理解性能与局限的系统框架

## 摘要（原文）

> Graph neural networks (GNNs) work remarkably well in semi-supervised node regression, yet a rigorous theory explaining when and why they succeed remains lacking. To address this gap, we study an aggregate-and-readout model that encompasses several common message passing architectures: node features are first propagated over the graph then mapped to responses via a nonlinear function. For least-squares estimation over GNNs with linear graph convolutions and a deep ReLU readout, we prove a sharp non-asymptotic risk bound that separates approximation, stochastic, and optimization errors. The bound makes explicit how performance scales with the fraction of labeled nodes and graph-induced dependence. Approximation guarantees are further derived for graph-smoothing followed by smooth nonlinear readouts, yielding convergence rates that recover classical nonparametric behavior under full supervision while characterizing performance when labels are scarce. Numerical experiments validate our theory, providing a systematic framework for understanding GNN performance and limitations.

