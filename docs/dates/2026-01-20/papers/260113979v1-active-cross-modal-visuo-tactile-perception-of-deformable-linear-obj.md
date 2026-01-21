---
layout: default
title: Active Cross-Modal Visuo-Tactile Perception of Deformable Linear Objects
---

# Active Cross-Modal Visuo-Tactile Perception of Deformable Linear Objects
**arXiv**：[2601.13979v1](https://arxiv.org/abs/2601.13979) · [PDF](https://arxiv.org/pdf/2601.13979.pdf)  
**作者**：Raffaele Mazza, Ciro Natale, Pietro Falco  

**一句话要点**：提出主动跨模态视觉-触觉感知框架，以解决严重视觉遮挡下可变形线性物体的3D形状重建问题。

**关键词**：跨模态感知, 可变形物体重建, 视觉-触觉融合, 基础模型应用, 机器人操作

## 3 点简述
- 核心问题：现有视觉方法在光照变化、背景杂乱或部分可见时性能下降，难以处理严重视觉遮挡的可变形线性物体。
- 方法要点：集成基础模型视觉感知与自适应触觉探索，通过SAM和Florence处理视觉数据，触觉传感器探索遮挡段，融合点云并插值重建。
- 实验或效果：使用机器人验证，能准确重建简单和高度弯曲的单或多电缆配置，即使大部分被遮挡。

## 摘要（原文）

> This paper presents a novel cross-modal visuo-tactile perception framework for the 3D shape reconstruction of deformable linear objects (DLOs), with a specific focus on cables subject to severe visual occlusions. Unlike existing methods relying predominantly on vision, whose performance degrades under varying illumination, background clutter, or partial visibility, the proposed approach integrates foundation-model-based visual perception with adaptive tactile exploration. The visual pipeline exploits SAM for instance segmentation and Florence for semantic refinement, followed by skeletonization, endpoint detection, and point-cloud extraction. Occluded cable segments are autonomously identified and explored with a tactile sensor, which provides local point clouds that are merged with the visual data through Euclidean clustering and topology-preserving fusion. A B-spline interpolation driven by endpoint-guided point sorting yields a smooth and complete reconstruction of the cable shape. Experimental validation using a robotic manipulator equipped with an RGB-D camera and a tactile pad demonstrates that the proposed framework accurately reconstructs both simple and highly curved single or multiple cable configurations, even when large portions are occluded. These results highlight the potential of foundation-model-enhanced cross-modal perception for advancing robotic manipulation of deformable objects.

