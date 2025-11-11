---
layout: default
title: PointCubeNet: 3D Part-level Reasoning with 3x3x3 Point Cloud Blocks
---

# PointCubeNet: 3D Part-level Reasoning with 3x3x3 Point Cloud Blocks
**arXiv**：[2511.06744v1](https://arxiv.org/abs/2511.06744) · [PDF](https://arxiv.org/pdf/2511.06744.pdf)  
**作者**：Da-Yeong Kim, Yeong-Jun Cho  

**一句话要点**：提出PointCubeNet以实现无监督3D部件级推理，通过3x3x3点云块分析

**关键词**：3D点云理解, 无监督学习, 部件级推理, 多模态框架, 伪标签方法

## 3 点简述
- 核心问题：3D对象部件级推理通常依赖部件标注，缺乏无监督方法。
- 方法要点：使用全局和局部分支，局部分支以3x3x3块分析点云子区域。
- 实验或效果：无监督训练增强整体3D对象理解，实现可靠部件级推理。

## 摘要（原文）

> In this paper, we propose PointCubeNet, a novel multi-modal 3D understanding
> framework that achieves part-level reasoning without requiring any part
> annotations. PointCubeNet comprises global and local branches. The proposed
> local branch, structured into 3x3x3 local blocks, enables part-level analysis
> of point cloud sub-regions with the corresponding local text labels. Leveraging
> the proposed pseudo-labeling method and local loss function, PointCubeNet is
> effectively trained in an unsupervised manner. The experimental results
> demonstrate that understanding 3D object parts enhances the understanding of
> the overall 3D object. In addition, this is the first attempt to perform
> unsupervised 3D part-level reasoning and achieves reliable and meaningful
> results.

