---
layout: default
title: HyQuRP: Hybrid quantum-classical neural network with rotational and permutational equivariance for 3D point clouds
---

# HyQuRP: Hybrid quantum-classical neural network with rotational and permutational equivariance for 3D point clouds
**arXiv**：[2602.06381v1](https://arxiv.org/abs/2602.06381) · [PDF](https://arxiv.org/pdf/2602.06381.pdf)  
**作者**：Semin Park, Chae-Yeun Park  

**一句话要点**：提出HyQuRP混合量子-经典神经网络，用于处理具有旋转和置换对称性的3D点云数据。

**关键词**：3D点云处理, 量子机器学习, 等变神经网络, 群表示理论, 混合量子-经典模型

## 3 点简述
- 核心问题：现有等变量子机器学习模型常依赖临时构造，缺乏形式化理论基础。
- 方法要点：基于群表示理论构建，确保对旋转和置换对称性的等变性。
- 实验或效果：在稀疏点云场景下，优于经典和量子基线，如ModelNet基准上达到76.13%准确率。

## 摘要（原文）

> We introduce HyQuRP, a hybrid quantum-classical neural network equivariant to rotational and permutational symmetries. While existing equivariant quantum machine learning models often rely on ad hoc constructions, HyQuRP is built upon the formal foundations of group representation theory. In the sparse-point regime, HyQuRP consistently outperforms strong classical and quantum baselines across multiple benchmarks. For example, when six subsampled points are used, HyQuRP ($\sim$1.5K parameters) achieves 76.13% accuracy on the 5-class ModelNet benchmark, compared to approximately 71% for PointNet, PointMamba, and PointTransformer with similar parameter counts. These results highlight HyQuRP's exceptional data efficiency and suggest the potential of quantum machine learning models for processing 3D point cloud data.

