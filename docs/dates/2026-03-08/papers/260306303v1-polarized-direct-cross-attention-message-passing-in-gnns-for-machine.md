---
layout: default
title: Polarized Direct Cross-Attention Message Passing in GNNs for Machinery Fault Diagnosis
---

# Polarized Direct Cross-Attention Message Passing in GNNs for Machinery Fault Diagnosis
**arXiv**：[2603.06303v1](https://arxiv.org/abs/2603.06303) · [PDF](https://arxiv.org/pdf/2603.06303.pdf)  
**作者**：Zongyu Shi, Laibin Zhang, Maoyin Chen  

**一句话要点**：提出极化直接交叉注意力消息传递框架，以解决旋转机械故障诊断中图神经网络建模动态交互的局限性。

**关键词**：图神经网络, 故障诊断, 注意力机制, 消息传递, 噪声鲁棒性, 工业应用

## 3 点简述
- 核心问题：传统图神经网络依赖预定义静态图结构和同质聚合，难以建模复杂动态交互。
- 方法要点：引入极化直接交叉注意力机制，基于数据驱动图构建，从三种语义节点特征动态推断注意力权重。
- 实验或效果：在工业数据集上实现最优诊断精度和噪声鲁棒性，超越七种基线方法。

## 摘要（原文）

> The reliability of safety-critical industrial systems hinges on accurate and robust fault diagnosis in rotating machinery. Conventional graph neural networks (GNNs) for machinery fault diagnosis face limitations in modeling complex dynamic interactions due to their reliance on predefined static graph structures and homogeneous aggregation schemes. To overcome these challenges, this paper introduces polarized direct cross-attention (PolaDCA), a novel relational learning framework that enables adaptive message passing through data-driven graph construction. Our approach builds upon a direct cross-attention (DCA) mechanism that dynamically infers attention weights from three semantically distinct node features (such as individual characteristics, neighborhood consensus, and neighborhood diversity) without requiring fixed adjacency matrices. Theoretical analysis establishes PolaDCA's superior noise robustness over conventional GNNs. Extensive experiments on industrial datasets (i.e., XJTUSuprgear, CWRUBearing and Three-Phase Flow Facility datasets) demonstrate state-of-the-art diagnostic accuracy and enhanced generalization under varying noise conditions, outperforming seven competitive baseline methods. The proposed framework provides an effective solution for safety-critical industrial applications.

