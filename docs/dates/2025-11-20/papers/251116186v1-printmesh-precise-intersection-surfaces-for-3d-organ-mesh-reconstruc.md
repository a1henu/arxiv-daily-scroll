---
layout: default
title: PrIntMesh: Precise Intersection Surfaces for 3D Organ Mesh Reconstruction
---

# PrIntMesh: Precise Intersection Surfaces for 3D Organ Mesh Reconstruction
**arXiv**：[2511.16186v1](https://arxiv.org/abs/2511.16186) · [PDF](https://arxiv.org/pdf/2511.16186.pdf)  
**作者**：Deniz Sayin Mercadier, Hieu Le, Yihong Chen, Jiancheng Yang, Udaranga Wickramasinghe, Pascal Fua  

**一句话要点**：提出PrIntMesh框架以解决器官3D网格重建中的解剖结构不一致问题

**关键词**：3D器官重建, 模板变形, 拓扑保持, 解剖结构约束, 深度学习框架

## 3 点简述
- 核心问题：现有方法独立处理器官子结构，导致解剖学上不合理的重建结果
- 方法要点：基于模板联合变形所有子结构，保持内部边界和光滑表面
- 实验或效果：在心脏、海马体和肺部实现高几何精度和拓扑正确性

## 摘要（原文）

> Human organs are composed of interconnected substructures whose geometry and spatial relationships constrain one another. Yet, most deep-learning approaches treat these parts independently, producing anatomically implausible reconstructions. We introduce PrIntMesh, a template-based, topology-preserving framework that reconstructs organs as unified systems. Starting from a connected template, PrIntMesh jointly deforms all substructures to match patient-specific anatomy, while explicitly preserving internal boundaries and enforcing smooth, artifact-free surfaces. We demonstrate its effectiveness on the heart, hippocampus, and lungs, achieving high geometric accuracy, correct topology, and robust performance even with limited or noisy training data. Compared to voxel- and surface-based methods, PrIntMesh better reconstructs shared interfaces, maintains structural consistency, and provides a data-efficient solution suitable for clinical use.

