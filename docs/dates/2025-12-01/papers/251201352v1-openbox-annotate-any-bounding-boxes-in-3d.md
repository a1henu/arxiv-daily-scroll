---
layout: default
title: OpenBox: Annotate Any Bounding Boxes in 3D
---

# OpenBox: Annotate Any Bounding Boxes in 3D
**arXiv**：[2512.01352v1](https://arxiv.org/abs/2512.01352) · [PDF](https://arxiv.org/pdf/2512.01352.pdf)  
**作者**：In-Jae Lee, Mungyeom Kim, Kwonyoung Ryu, Pierre Musacchio, Jaesik Park  

**一句话要点**：提出OpenBox两阶段自动标注管道，利用2D视觉基础模型高效生成高质量3D边界框标注。

**关键词**：3D目标检测, 自动标注, 跨模态对齐, 开放词汇检测, 自适应边界框, 点云处理

## 3 点简述
- 核心问题：现有3D目标检测方法标注成本高、忽略物体物理状态、依赖自训练导致质量低和计算开销大。
- 方法要点：通过跨模态实例对齐关联2D图像与3D点云，基于刚性和运动状态分类生成自适应边界框。
- 实验或效果：在Waymo、Lyft、nuScenes数据集上验证，相比基线提升准确性和效率，无需自训练。

## 摘要（原文）

> Unsupervised and open-vocabulary 3D object detection has recently gained attention, particularly in autonomous driving, where reducing annotation costs and recognizing unseen objects are critical for both safety and scalability. However, most existing approaches uniformly annotate 3D bounding boxes, ignore objects' physical states, and require multiple self-training iterations for annotation refinement, resulting in suboptimal quality and substantial computational overhead. To address these challenges, we propose OpenBox, a two-stage automatic annotation pipeline that leverages a 2D vision foundation model. In the first stage, OpenBox associates instance-level cues from 2D images processed by a vision foundation model with the corresponding 3D point clouds via cross-modal instance alignment. In the second stage, it categorizes instances by rigidity and motion state, then generates adaptive bounding boxes with class-specific size statistics. As a result, OpenBox produces high-quality 3D bounding box annotations without requiring self-training. Experiments on the Waymo Open Dataset, the Lyft Level 5 Perception dataset, and the nuScenes dataset demonstrate improved accuracy and efficiency over baselines.

