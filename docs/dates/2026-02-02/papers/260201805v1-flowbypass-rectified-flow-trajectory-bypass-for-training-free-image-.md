---
layout: default
title: FlowBypass: Rectified Flow Trajectory Bypass for Training-Free Image Editing
---

# FlowBypass: Rectified Flow Trajectory Bypass for Training-Free Image Editing
**arXiv**：[2602.01805v1](https://arxiv.org/abs/2602.01805) · [PDF](https://arxiv.org/pdf/2602.01805.pdf)  
**作者**：Menglin Han, Zhangkai Ni  

**一句话要点**：提出FlowBypass框架，通过构建旁路轨迹解决免训练图像编辑中的误差累积与提示对齐权衡问题。

**关键词**：免训练图像编辑, Rectified Flow, 轨迹旁路, 误差累积, 提示对齐, 高保真编辑

## 3 点简述
- 核心问题：现有免训练图像编辑方法依赖反转-重建轨迹，存在误差累积与提示对齐的固有权衡。
- 方法要点：基于Rectified Flow，分析推导并构建连接反转与重建轨迹的旁路，避免特征操作，实现无缝过渡。
- 实验或效果：实验显示FlowBypass在保持高保真细节的同时，优于现有方法，实现更强的提示对齐。

## 摘要（原文）

> Training-free image editing has attracted increasing attention for its efficiency and independence from training data. However, existing approaches predominantly rely on inversion-reconstruction trajectories, which impose an inherent trade-off: longer trajectories accumulate errors and compromise fidelity, while shorter ones fail to ensure sufficient alignment with the edit prompt. Previous attempts to address this issue typically employ backbone-specific feature manipulations, limiting general applicability. To address these challenges, we propose FlowBypass, a novel and analytical framework grounded in Rectified Flow that constructs a bypass directly connecting inversion and reconstruction trajectories, thereby mitigating error accumulation without relying on feature manipulations. We provide a formal derivation of two trajectories, from which we obtain an approximate bypass formulation and its numerical solution, enabling seamless trajectory transitions. Extensive experiments demonstrate that FlowBypass consistently outperforms state-of-the-art image editing methods, achieving stronger prompt alignment while preserving high-fidelity details in irrelevant regions.

