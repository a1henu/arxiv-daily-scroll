---
layout: default
title: Mapper-GIN: Lightweight Structural Graph Abstraction for Corrupted 3D Point Cloud Classification
---

# Mapper-GIN: Lightweight Structural Graph Abstraction for Corrupted 3D Point Cloud Classification
**arXiv**：[2602.05522v1](https://arxiv.org/abs/2602.05522) · [PDF](https://arxiv.org/pdf/2602.05522.pdf)  
**作者**：Jeongbin You, Donggun Kim, Sejun Park, Seungsang Oh  

**一句话要点**：提出Mapper-GIN，通过结构图抽象提升损坏3D点云分类的鲁棒性

**关键词**：3D点云分类, 结构图抽象, Mapper算法, 图同构网络, 鲁棒性, 轻量级模型

## 3 点简述
- 核心问题：现有方法依赖大模型或数据增强实现鲁棒性，探索结构抽象是否有效
- 方法要点：使用Mapper算法分区点云为重叠区域，构建区域图，用图同构网络进行分类
- 实验或效果：在ModelNet40-C基准上，仅0.5M参数，在噪声和变换损坏下达到竞争性准确率

## 摘要（原文）

> Robust 3D point cloud classification is often pursued by scaling up backbones or relying on specialized data augmentation. We instead ask whether structural abstraction alone can improve robustness, and study a simple topology-inspired decomposition based on the Mapper algorithm. We propose Mapper-GIN, a lightweight pipeline that partitions a point cloud into overlapping regions using Mapper (PCA lens, cubical cover, and followed by density-based clustering), constructs a region graph from their overlaps, and performs graph classification with a Graph Isomorphism Network. On the corruption benchmark ModelNet40-C, Mapper-GIN achieves competitive and stable accuracy under Noise and Transformation corruptions with only 0.5M parameters. In contrast to prior approaches that require heavier architectures or additional mechanisms to gain robustness, Mapper-GIN attains strong corruption robustness through simple region-level graph abstraction and GIN message passing. Overall, our results suggest that region-graph structure offers an efficient and interpretable source of robustness for 3D visual recognition.

