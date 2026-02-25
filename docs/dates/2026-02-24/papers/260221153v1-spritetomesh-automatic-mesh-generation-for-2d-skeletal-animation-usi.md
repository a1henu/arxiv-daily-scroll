---
layout: default
title: SPRITETOMESH: Automatic Mesh Generation for 2D Skeletal Animation Using Learned Segmentation and Contour-Aware Vertex Placement
---

# SPRITETOMESH: Automatic Mesh Generation for 2D Skeletal Animation Using Learned Segmentation and Contour-Aware Vertex Placement
**arXiv**：[2602.21153v1](https://arxiv.org/abs/2602.21153) · [PDF](https://arxiv.org/pdf/2602.21153.pdf)  
**作者**：Bastien Gimbert  

**一句话要点**：提出SPRITETOMESH，通过混合学习-算法方法自动将2D游戏精灵图像转换为骨骼动画兼容的三角形网格。

**关键词**：2D骨骼动画, 自动网格生成, 图像分割, 轮廓检测, Delaunay三角剖分, 游戏开发工具

## 3 点简述
- 核心问题：传统手动创建动画就绪网格耗时，每精灵需15-60分钟，需艺术家沿视觉边界放置顶点。
- 方法要点：使用分割网络生成准确掩码，结合算法提取轮廓顶点和内部顶点，通过Delaunay三角剖分生成最终网格。
- 实验或效果：管道处理精灵时间少于3秒，比手动创建快300x-1200x，分割网络IoU达0.87，验证混合设计优于纯神经网络预测。

## 摘要（原文）

> We present SPRITETOMESH, a fully automatic pipeline for converting 2D game sprite images into triangle meshes compatible with skeletal animation frameworks such as Spine2D. Creating animation-ready meshes is traditionally a tedious manual process requiring artists to carefully place vertices along visual boundaries, a task that typically takes 15-60 minutes per sprite. Our method addresses this through a hybrid learned-algorithmic approach. A segmentation network (EfficientNet-B0 encoder with U-Net decoder) trained on over 100,000 sprite-mask pairs from 172 games achieves an IoU of 0.87, providing accurate binary masks from arbitrary input images. From these masks, we extract exterior contour vertices using Douglas-Peucker simplification with adaptive arc subdivision, and interior vertices along visual boundaries detected via bilateral-filtered multi-channel Canny edge detection with contour-following placement. Delaunay triangulation with mask-based centroid filtering produces the final mesh. Through controlled experiments, we demonstrate that direct vertex position prediction via neural network heatmap regression is fundamentally not viable for this task: the heatmap decoder consistently fails to converge (loss plateau at 0.061) while the segmentation decoder trains normally under identical conditions. We attribute this to the inherently artistic nature of vertex placement - the same sprite can be meshed validly in many different ways. This negative result validates our hybrid design: learned segmentation where ground truth is unambiguous, algorithmic placement where domain heuristics are appropriate. The complete pipeline processes a sprite in under 3 seconds, representing a speedup of 300x-1200x over manual creation. We release our trained model to the game development community.

