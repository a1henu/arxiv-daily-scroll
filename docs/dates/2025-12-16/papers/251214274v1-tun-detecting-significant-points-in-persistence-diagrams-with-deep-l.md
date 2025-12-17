---
layout: default
title: TUN: Detecting Significant Points in Persistence Diagrams with Deep Learning
---

# TUN: Detecting Significant Points in Persistence Diagrams with Deep Learning
**arXiv**：[2512.14274v1](https://arxiv.org/abs/2512.14274) · [PDF](https://arxiv.org/pdf/2512.14274.pdf)  
**作者**：Yu Chen, Hongwei Lin  

**一句话要点**：提出TUN网络以自动检测一维持久图中的显著点

**关键词**：持久图, 拓扑数据分析, 深度学习, 多模态网络, 显著点检测

## 3 点简述
- 核心问题：持久图中哪些点代表真实拓扑信号难以自动识别，阻碍拓扑数据分析应用。
- 方法要点：结合增强描述符、自注意力、点云编码器、学习融合和逐点分类的多模态网络。
- 实验或效果：在检测显著点方面优于经典方法，展示实际应用有效性。

## 摘要（原文）

> Persistence diagrams (PDs) provide a powerful tool for understanding the topology of the underlying shape of a point cloud. However, identifying which points in PDs encode genuine signals remains challenging. This challenge directly hinders the practical adoption of topological data analysis in many applications, where automated and reliable interpretation of persistence diagrams is essential for downstream decision-making. In this paper, we study automatic significance detection for one-dimensional persistence diagrams. Specifically, we propose Topology Understanding Net (TUN), a multi-modal network that combines enhanced PD descriptors with self-attention, a PointNet-style point cloud encoder, learned fusion, and per-point classification, alongside stable preprocessing and imbalance-aware training. It provides an automated and effective solution for identifying significant points in PDs, which are critical for downstream applications. Experiments show that TUN outperforms classic methods in detecting significant points in PDs, illustrating its effectiveness in real-world applications.

