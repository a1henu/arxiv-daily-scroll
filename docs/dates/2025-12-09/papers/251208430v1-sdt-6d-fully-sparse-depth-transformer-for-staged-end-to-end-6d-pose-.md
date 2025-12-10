---
layout: default
title: SDT-6D: Fully Sparse Depth-Transformer for Staged End-to-End 6D Pose Estimation in Industrial Multi-View Bin Picking
---

# SDT-6D: Fully Sparse Depth-Transformer for Staged End-to-End 6D Pose Estimation in Industrial Multi-View Bin Picking
**arXiv**：[2512.08430v1](https://arxiv.org/abs/2512.08430) · [PDF](https://arxiv.org/pdf/2512.08430.pdf)  
**作者**：Nico Leuze, Maximilian Hoh, Samed Doğan, Nicolas R. -Peña, Alfred Schoettl  

**一句话要点**：提出全稀疏深度Transformer，用于工业多视角箱拣中分阶段端到端6D姿态估计

**关键词**：6D姿态估计, 稀疏Transformer, 多视角深度融合, 工业箱拣, 端到端学习, 点云处理

## 3 点简述
- 核心问题：工业箱拣中密集遮挡、反射和无纹理部件导致6D姿态估计困难
- 方法要点：融合多视角深度图，采用分阶段热图机制和密度感知稀疏Transformer块
- 实验或效果：在IPD和MV-YCB数据集上验证，在杂乱场景中表现竞争性

## 摘要（原文）

> Accurately recovering 6D poses in densely packed industrial bin-picking environments remain a serious challenge, owing to occlusions, reflections, and textureless parts. We introduce a holistic depth-only 6D pose estimation approach that fuses multi-view depth maps into either a fine-grained 3D point cloud in its vanilla version, or a sparse Truncated Signed Distance Field (TSDF). At the core of our framework lies a staged heatmap mechanism that yields scene-adaptive attention priors across different resolutions, steering computation toward foreground regions, thus keeping memory requirements at high resolutions feasible. Along, we propose a density-aware sparse transformer block that dynamically attends to (self-) occlusions and the non-uniform distribution of 3D data. While sparse 3D approaches has proven effective for long-range perception, its potential in close-range robotic applications remains underexplored. Our framework operates fully sparse, enabling high-resolution volumetric representations to capture fine geometric details crucial for accurate pose estimation in clutter. Our method processes the entire scene integrally, predicting the 6D pose via a novel per-voxel voting strategy, allowing simultaneous pose predictions for an arbitrary number of target objects. We validate our method on the recently published IPD and MV-YCB multi-view datasets, demonstrating competitive performance in heavily cluttered industrial and household bin picking scenarios.

