---
layout: default
title: Graph Query Networks for Object Detection with Automotive Radar
---

# Graph Query Networks for Object Detection with Automotive Radar
**arXiv**：[2511.15271v1](https://arxiv.org/abs/2511.15271) · [PDF](https://arxiv.org/pdf/2511.15271.pdf)  
**作者**：Loveneet Saini, Hasan Tercan, Tobias Meisen  

**一句话要点**：提出图查询网络以解决汽车雷达稀疏不规则反射下的物体检测问题

**关键词**：物体检测, 雷达感知, 图神经网络, 注意力机制, 鸟瞰图, 关系推理

## 3 点简述
- 核心问题：雷达长波长导致稀疏不规则反射，挑战传统卷积和变换器检测器
- 方法要点：使用图查询动态关注鸟瞰图空间，构建对象特定图进行关系推理和上下文聚合
- 实验或效果：在NuScenes数据集上相对mAP提升高达53%，图构建开销降低80%

## 摘要（原文）

> Object detection with 3D radar is essential for 360-degree automotive perception, but radar's long wavelengths produce sparse and irregular reflections that challenge traditional grid and sequence-based convolutional and transformer detectors. This paper introduces Graph Query Networks (GQN), an attention-based framework that models objects sensed by radar as graphs, to extract individualized relational and contextual features. GQN employs a novel concept of graph queries to dynamically attend over the bird's-eye view (BEV) space, constructing object-specific graphs processed by two novel modules: EdgeFocus for relational reasoning and DeepContext Pooling for contextual aggregation. On the NuScenes dataset, GQN improves relative mAP by up to +53%, including a +8.2% gain over the strongest prior radar method, while reducing peak graph construction overhead by 80% with moderate FLOPs cost.

