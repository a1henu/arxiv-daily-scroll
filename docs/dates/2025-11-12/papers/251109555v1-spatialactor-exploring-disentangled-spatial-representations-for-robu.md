---
layout: default
title: SpatialActor: Exploring Disentangled Spatial Representations for Robust Robotic Manipulation
---

# SpatialActor: Exploring Disentangled Spatial Representations for Robust Robotic Manipulation
**arXiv**：[2511.09555v1](https://arxiv.org/abs/2511.09555) · [PDF](https://arxiv.org/pdf/2511.09555.pdf)  
**作者**：Hao Shi, Bin Xie, Yingfei Liu, Yang Yue, Tiancai Wang, Haoqiang Fan, Xiangyu Zhang, Gao Huang  

**一句话要点**：提出SpatialActor框架以解决机器人操作中语义与几何纠缠问题

**关键词**：机器人操作, 解耦表示, 空间变换器, 语义几何融合, 鲁棒性增强

## 3 点简述
- 核心问题：基于点或图像的方法因语义与几何纠缠，对深度噪声敏感，且忽略低层空间线索。
- 方法要点：通过解耦语义与几何，融合噪声深度与语义先验，并利用空间变换器增强2D-3D映射。
- 实验或效果：在RLBench上达87.4%成功率，噪声条件下提升13.9%-19.4%，增强泛化与鲁棒性。

## 摘要（原文）

> Robotic manipulation requires precise spatial understanding to interact with objects in the real world. Point-based methods suffer from sparse sampling, leading to the loss of fine-grained semantics. Image-based methods typically feed RGB and depth into 2D backbones pre-trained on 3D auxiliary tasks, but their entangled semantics and geometry are sensitive to inherent depth noise in real-world that disrupts semantic understanding. Moreover, these methods focus on high-level geometry while overlooking low-level spatial cues essential for precise interaction. We propose SpatialActor, a disentangled framework for robust robotic manipulation that explicitly decouples semantics and geometry. The Semantic-guided Geometric Module adaptively fuses two complementary geometry from noisy depth and semantic-guided expert priors. Also, a Spatial Transformer leverages low-level spatial cues for accurate 2D-3D mapping and enables interaction among spatial features. We evaluate SpatialActor on multiple simulation and real-world scenarios across 50+ tasks. It achieves state-of-the-art performance with 87.4% on RLBench and improves by 13.9% to 19.4% under varying noisy conditions, showing strong robustness. Moreover, it significantly enhances few-shot generalization to new tasks and maintains robustness under various spatial perturbations. Project Page: https://shihao1895.github.io/SpatialActor

