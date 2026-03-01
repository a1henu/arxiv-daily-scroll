---
layout: default
title: ProjFlow: Projection Sampling with Flow Matching for Zero-Shot Exact Spatial Motion Control
---

# ProjFlow: Projection Sampling with Flow Matching for Zero-Shot Exact Spatial Motion Control
**arXiv**：[2602.22742v1](https://arxiv.org/abs/2602.22742) · [PDF](https://arxiv.org/pdf/2602.22742.pdf)  
**作者**：Akihisa Watanabe, Qing Yu, Edgar Simo-Serra, Kent Fujiwara  

**一句话要点**：提出ProjFlow，通过投影采样与流匹配实现零样本精确空间运动控制

**关键词**：运动生成, 零样本控制, 投影采样, 流匹配, 线性约束, 骨骼拓扑

## 3 点简述
- 核心问题：现有方法需任务特定训练或优化慢，硬约束常破坏运动自然性。
- 方法要点：基于线性逆问题观察，引入训练无关采样器，使用骨骼拓扑感知度量实现硬约束。
- 实验或效果：在运动修复和2D到3D提升中，精确满足约束，保持或提升真实感。

## 摘要（原文）

> Generating human motion with precise spatial control is a challenging problem. Existing approaches often require task-specific training or slow optimization, and enforcing hard constraints frequently disrupts motion naturalness. Building on the observation that many animation tasks can be formulated as a linear inverse problem, we introduce ProjFlow, a training-free sampler that achieves zero-shot, exact satisfaction of linear spatial constraints while preserving motion realism. Our key advance is a novel kinematics-aware metric that encodes skeletal topology. This metric allows the sampler to enforce hard constraints by distributing corrections coherently across the entire skeleton, avoiding the unnatural artifacts of naive projection. Furthermore, for sparse inputs, such as filling in long gaps between a few keyframes, we introduce a time-varying formulation using pseudo-observations that fade during sampling. Extensive experiments on representative applications, motion inpainting, and 2D-to-3D lifting, demonstrate that ProjFlow achieves exact constraint satisfaction and matches or improves realism over zero-shot baselines, while remaining competitive with training-based controllers.

