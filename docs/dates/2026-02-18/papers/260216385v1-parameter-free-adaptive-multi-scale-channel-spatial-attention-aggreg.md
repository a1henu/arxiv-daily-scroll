---
layout: default
title: Parameter-Free Adaptive Multi-Scale Channel-Spatial Attention Aggregation framework for 3D Indoor Semantic Scene Completion Toward Assisting Visually Impaired
---

# Parameter-Free Adaptive Multi-Scale Channel-Spatial Attention Aggregation framework for 3D Indoor Semantic Scene Completion Toward Assisting Visually Impaired
**arXiv**：[2602.16385v1](https://arxiv.org/abs/2602.16385) · [PDF](https://arxiv.org/pdf/2602.16385.pdf)  
**作者**：Qi He, XiangXiang Wang, Jingtao Zhang, Yongbin Yu, Hongxiang Chu, Manping Fan, JingYe Cai, Zhenglin Yang  

**一句话要点**：提出自适应多尺度通道-空间注意力聚合框架，以提升单目3D室内语义场景补全的可靠性和结构稳定性，辅助视障用户。

**关键词**：语义场景补全, 单目视觉, 注意力机制, 多尺度融合, 辅助感知, 嵌入式部署

## 3 点简述
- 核心问题：现有单目SSC方法在2D-3D投影和多尺度融合中缺乏体素特征可靠性和跨尺度信息传播的显式建模，导致投影扩散和特征纠缠。
- 方法要点：基于MonoScene，通过并行通道-空间注意力聚合校准体素特征，并采用分层自适应特征门控策略稳定多尺度融合。
- 实验或效果：在NYUv2基准上，SSC mIoU提升至27.25%（+0.31），SC IoU提升至43.10%（+0.59），并在嵌入式硬件上验证了部署可行性。

## 摘要（原文）

> In indoor assistive perception for visually impaired users, 3D Semantic Scene Completion (SSC) is expected to provide structurally coherent and semantically consistent occupancy under strictly monocular vision for safety-critical scene understanding. However, existing monocular SSC approaches often lack explicit modeling of voxel-feature reliability and regulated cross-scale information propagation during 2D-3D projection and multi-scale fusion, making them vulnerable to projection diffusion and feature entanglement and thus limiting structural stability.To address these challenges, this paper presents an Adaptive Multi-scale Attention Aggregation (AMAA) framework built upon the MonoScene pipeline. Rather than introducing a heavier backbone, AMAA focuses on reliability-oriented feature regulation within a monocular SSC framework. Specifically, lifted voxel features are jointly calibrated in semantic and spatial dimensions through parallel channel-spatial attention aggregation, while multi-scale encoder-decoder fusion is stabilized via a hierarchical adaptive feature-gating strategy that regulates information injection across scales.Experiments on the NYUv2 benchmark demonstrate consistent improvements over MonoScene without significantly increasing system complexity: AMAA achieves 27.25% SSC mIoU (+0.31) and 43.10% SC IoU (+0.59). In addition, system-level deployment on an NVIDIA Jetson platform verifies that the complete AMAA framework can be executed stably on embedded hardware. Overall, AMAA improves monocular SSC quality and provides a reliable and deployable perception framework for indoor assistive systems targeting visually impaired users.

