---
layout: default
title: Affostruction: 3D Affordance Grounding with Generative Reconstruction
---

# Affostruction: 3D Affordance Grounding with Generative Reconstruction
**arXiv**：[2601.09211v1](https://arxiv.org/abs/2601.09211) · [PDF](https://arxiv.org/pdf/2601.09211.pdf)  
**作者**：Chunghyun Park, Seunghyeon Lee, Minsu Cho  

**一句话要点**：提出Affostruction框架，通过生成式重建解决RGBD图像中物体功能区域定位问题

**关键词**：功能区域定位, 3D重建, 生成式模型, RGBD图像, 主动视角选择

## 3 点简述
- 核心问题：从RGBD图像定位物体表面功能区域，现有方法仅预测可见区域，忽略未观测部分。
- 方法要点：结合生成式多视角重建、基于流的定位和主动视角选择，实现完整形状上的功能区域预测。
- 实验或效果：在功能区域定位上提升40.4%，3D重建提升67.7%，支持完整形状的准确预测。

## 摘要（原文）

> This paper addresses the problem of affordance grounding from RGBD images of an object, which aims to localize surface regions corresponding to a text query that describes an action on the object. While existing methods predict affordance regions only on visible surfaces, we propose Affostruction, a generative framework that reconstructs complete geometry from partial observations and grounds affordances on the full shape including unobserved regions. We make three core contributions: generative multi-view reconstruction via sparse voxel fusion that extrapolates unseen geometry while maintaining constant token complexity, flow-based affordance grounding that captures inherent ambiguity in affordance distributions, and affordance-driven active view selection that leverages predicted affordances for intelligent viewpoint sampling. Affostruction achieves 19.1 aIoU on affordance grounding (40.4\% improvement) and 32.67 IoU for 3D reconstruction (67.7\% improvement), enabling accurate affordance prediction on complete shapes.

