---
layout: default
title: Photonics-Enhanced Graph Convolutional Networks
---

# Photonics-Enhanced Graph Convolutional Networks
**arXiv**：[2512.15549v1](https://arxiv.org/abs/2512.15549) · [PDF](https://arxiv.org/pdf/2512.15549.pdf)  
**作者**：Yuan Wang, Oleksandr Kyriienko  

**一句话要点**：提出光子增强图卷积网络，通过光子位置嵌入提升图机器学习性能并支持光学加速。

**关键词**：光子机器学习, 图卷积网络, 位置嵌入, 光学加速, 混合工作流, 分子数据集

## 3 点简述
- 核心问题：光子机器学习需混合工作流，集成光学处理与传统神经网络架构。
- 方法要点：利用合成频率晶格光传播生成位置嵌入，增强图卷积网络以提供全局结构信息。
- 实验或效果：在长程图基准分子数据集上，回归任务平均绝对误差降低6.3%，分类任务平均精度提升2.3%。

## 摘要（原文）

> Photonics can offer a hardware-native route for machine learning (ML). However, efficient deployment of photonics-enhanced ML requires hybrid workflows that integrate optical processing with conventional CPU/GPU based neural network architectures. Here, we propose such a workflow that combines photonic positional embeddings (PEs) with advanced graph ML models. We introduce a photonics-based method that augments graph convolutional networks (GCNs) with PEs derived from light propagation on synthetic frequency lattices whose couplings match the input graph. We simulate propagation and readout to obtain internode intensity correlation matrices, which are used as PEs in GCNs to provide global structural information. Evaluated on Long Range Graph Benchmark molecular datasets, the method outperforms baseline GCNs with Laplacian based PEs, achieving $6.3\%$ lower mean absolute error for regression and $2.3\%$ higher average precision for classification tasks using a two-layer GCN as a baseline. When implemented in high repetition rate photonic hardware, correlation measurements can enable fast feature generation by bypassing digital simulation of PEs. Our results show that photonic PEs improve GCN performance and support optical acceleration of graph ML.

