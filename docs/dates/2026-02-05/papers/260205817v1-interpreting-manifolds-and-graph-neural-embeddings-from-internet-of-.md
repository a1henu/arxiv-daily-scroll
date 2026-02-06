---
layout: default
title: Interpreting Manifolds and Graph Neural Embeddings from Internet of Things Traffic Flows
---

# Interpreting Manifolds and Graph Neural Embeddings from Internet of Things Traffic Flows
**arXiv**：[2602.05817v1](https://arxiv.org/abs/2602.05817) · [PDF](https://arxiv.org/pdf/2602.05817.pdf)  
**作者**：Enrique Feito-Casares, Francisco M. Melgarejo-Meseguer, Elena Casiraghi, Giorgio Valentini, José-Luis Rojo-Álvarez  

**一句话要点**：提出可解释管道以解决物联网流量中图神经网络嵌入的可视化与监控问题

**关键词**：物联网流量分析, 图神经网络嵌入, 可解释人工智能, 流形学习, 入侵检测

## 3 点简述
- 物联网网络拓扑复杂，传统监控工具难以捕捉设备间动态关系
- 通过将高维嵌入映射到潜在流形，生成可直接可视化的低维表示
- 在入侵检测中达到0.830的F1分数，并揭示概念漂移等现象

## 摘要（原文）

> The rapid expansion of Internet of Things (IoT) ecosystems has led to increasingly complex and heterogeneous network topologies. Traditional network monitoring and visualization tools rely on aggregated metrics or static representations, which fail to capture the evolving relationships and structural dependencies between devices. Although Graph Neural Networks (GNNs) offer a powerful way to learn from relational data, their internal representations often remain opaque and difficult to interpret for security-critical operations. Consequently, this work introduces an interpretable pipeline that generates directly visualizable low-dimensional representations by mapping high-dimensional embeddings onto a latent manifold. This projection enables the interpretable monitoring and interoperability of evolving network states, while integrated feature attribution techniques decode the specific characteristics shaping the manifold structure. The framework achieves a classification F1-score of 0.830 for intrusion detection while also highlighting phenomena such as concept drift. Ultimately, the presented approach bridges the gap between high-dimensional GNN embeddings and human-understandable network behavior, offering new insights for network administrators and security analysts.

