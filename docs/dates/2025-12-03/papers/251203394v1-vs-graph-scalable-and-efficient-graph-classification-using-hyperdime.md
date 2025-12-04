---
layout: default
title: VS-Graph: Scalable and Efficient Graph Classification Using Hyperdimensional Computing
---

# VS-Graph: Scalable and Efficient Graph Classification Using Hyperdimensional Computing
**arXiv**：[2512.03394v1](https://arxiv.org/abs/2512.03394) · [PDF](https://arxiv.org/pdf/2512.03394.pdf)  
**作者**：Hamed Poursiami, Shay Snyder, Guojing Cong, Thomas Potok, Maryam Parsa  

**一句话要点**：提出VS-Graph框架，结合超维计算与消息传递，提升图分类效率与性能

**关键词**：图分类, 超维计算, 向量符号架构, 消息传递, 高效训练, 边缘计算

## 3 点简述
- 图分类任务中，图神经网络计算成本高，超维计算性能不足，需平衡效率与表达力
- VS-Graph引入尖峰扩散机制和关联消息传递，在高维向量空间实现拓扑识别与邻域聚合
- 在MUTAG等基准上，准确率接近图神经网络，训练加速达450倍，维度压缩至128仍保持高精度

## 摘要（原文）

> Graph classification is a fundamental task in domains ranging from molecular property prediction to materials design. While graph neural networks (GNNs) achieve strong performance by learning expressive representations via message passing, they incur high computational costs, limiting their scalability and deployment on resource-constrained devices. Hyperdimensional Computing (HDC), also known as Vector Symbolic Architectures (VSA), offers a lightweight, brain-inspired alternative, yet existing HDC-based graph methods typically struggle to match the predictive performance of GNNs. In this work, we propose VS-Graph, a vector-symbolic graph learning framework that narrows the gap between the efficiency of HDC and the expressive power of message passing. VS-Graph introduces a Spike Diffusion mechanism for topology-driven node identification and an Associative Message Passing scheme for multi-hop neighborhood aggregation entirely within the high-dimensional vector space. Without gradient-based optimization or backpropagation, our method achieves competitive accuracy with modern GNNs, outperforming the prior HDC baseline by 4-5% on standard benchmarks such as MUTAG and DD. It also matches or exceeds the performance of the GNN baselines on several datasets while accelerating the training by a factor of up to 450x. Furthermore, VS-Graph maintains high accuracy even with the hypervector dimensionality reduced to D=128, demonstrating robustness under aggressive dimension compression and paving the way for ultra-efficient execution on edge and neuromorphic hardware.

