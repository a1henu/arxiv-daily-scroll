---
layout: default
title: SEAFormer: A Spatial Proximity and Edge-Aware Transformer for Real-World Vehicle Routing Problems
---

# SEAFormer: A Spatial Proximity and Edge-Aware Transformer for Real-World Vehicle Routing Problems
**arXiv**：[2601.19395v1](https://arxiv.org/abs/2601.19395) · [PDF](https://arxiv.org/pdf/2601.19395.pdf)  
**作者**：Saeed Nasehi Basharzad, Farhana Choudhury, Egemen Tanin  

**一句话要点**：提出SEAFormer，一种结合空间邻近与边缘感知的Transformer，以解决现实世界车辆路径问题。

**关键词**：车辆路径问题, Transformer模型, 注意力机制, 边缘感知, 大规模优化, 序列依赖

## 3 点简述
- 现实世界车辆路径问题（RWVRPs）具有序列依赖性和边缘信息利用不足的挑战，现有神经方法难以有效处理。
- SEAFormer通过聚类邻近注意力和轻量级边缘感知模块，整合节点与边缘信息，降低计算复杂度并提升性能。
- 实验表明，SEAFormer在多种RWVRP变体上优于现有方法，首次有效解决1000+节点问题，并在经典VRPs上表现优异。

## 摘要（原文）

> Real-world Vehicle Routing Problems (RWVRPs) require solving complex, sequence-dependent challenges at scale with constraints such as delivery time window, replenishment or recharging stops, asymmetric travel cost, etc. While recent neural methods achieve strong results on large-scale classical VRP benchmarks, they struggle to address RWVRPs because their strategies overlook sequence dependencies and underutilize edge-level information, which are precisely the characteristics that define the complexity of RWVRPs. We present SEAFormer, a novel transformer that incorporates both node-level and edge-level information in decision-making through two key innovations. First, our Clustered Proximity Attention (CPA) exploits locality-aware clustering to reduce the complexity of attention from $O(n^2)$ to $O(n)$ while preserving global perspective, allowing SEAFormer to efficiently train on large instances. Second, our lightweight edge-aware module captures pairwise features through residual fusion, enabling effective incorporation of edge-based information and faster convergence. Extensive experiments across four RWVRP variants with various scales demonstrate that SEAFormer achieves superior results over state-of-the-art methods. Notably, SEAFormer is the first neural method to solve 1,000+ node RWVRPs effectively, while also achieving superior performance on classic VRPs, making it a versatile solution for both research benchmarks and real-world applications.

