---
layout: default
title: RAPTR: Radar-based 3D Pose Estimation using Transformer
---

# RAPTR: Radar-based 3D Pose Estimation using Transformer
**arXiv**：[2511.08387v1](https://arxiv.org/abs/2511.08387) · [PDF](https://arxiv.org/pdf/2511.08387.pdf)  
**作者**：Sorachi Kato, Ryoma Yataka, Pu Perry Wang, Pedro Miraldo, Takuya Fujihashi, Petros Boufounos  

**一句话要点**：提出RAPTR以在弱监督下使用雷达进行室内3D人体姿态估计

**关键词**：雷达姿态估计, 弱监督学习, 3D人体姿态, Transformer架构, 室内场景

## 3 点简述
- 核心问题：雷达室内3D姿态估计依赖昂贵3D关键点标注，难以在复杂场景中扩展
- 方法要点：采用两阶段解码器，结合伪3D可变形注意力，利用3D边界框和2D关键点标签
- 实验或效果：在两个数据集上优于现有方法，关节位置误差显著降低

## 摘要（原文）

> Radar-based indoor 3D human pose estimation typically relied on fine-grained 3D keypoint labels, which are costly to obtain especially in complex indoor settings involving clutter, occlusions, or multiple people. In this paper, we propose \textbf{RAPTR} (RAdar Pose esTimation using tRansformer) under weak supervision, using only 3D BBox and 2D keypoint labels which are considerably easier and more scalable to collect. Our RAPTR is characterized by a two-stage pose decoder architecture with a pseudo-3D deformable attention to enhance (pose/joint) queries with multi-view radar features: a pose decoder estimates initial 3D poses with a 3D template loss designed to utilize the 3D BBox labels and mitigate depth ambiguities; and a joint decoder refines the initial poses with 2D keypoint labels and a 3D gravity loss. Evaluated on two indoor radar datasets, RAPTR outperforms existing methods, reducing joint position error by $34.3\%$ on HIBER and $76.9\%$ on MMVR. Our implementation is available at https://github.com/merlresearch/radar-pose-transformer.

