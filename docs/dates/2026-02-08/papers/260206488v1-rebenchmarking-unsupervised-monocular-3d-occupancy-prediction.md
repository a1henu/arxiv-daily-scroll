---
layout: default
title: Rebenchmarking Unsupervised Monocular 3D Occupancy Prediction
---

# Rebenchmarking Unsupervised Monocular 3D Occupancy Prediction
**arXiv**：[2602.06488v1](https://arxiv.org/abs/2602.06488) · [PDF](https://arxiv.org/pdf/2602.06488.pdf)  
**作者**：Zizhan Guo, Yi Feng, Mengtan Zhang, Haoran Zhang, Wei Ye, Rui Fan  

**一句话要点**：提出无监督单目3D占用预测新基准与遮挡感知机制，以解决训练评估不一致和遮挡区域模糊问题。

**关键词**：无监督学习, 单目3D占用预测, 体积渲染, 遮挡感知, 自动驾驶视觉, 基准评估

## 3 点简述
- 核心问题：现有无监督方法训练与评估协议不一致，且2D真值无法有效约束遮挡区域几何模糊。
- 方法要点：重新定义占用概率表示以对齐评估协议，并引入遮挡感知极化机制利用多视角线索增强遮挡区域判别。
- 实验或效果：实验显示方法显著优于现有无监督方法，性能匹配监督方法，代码与协议将公开。

## 摘要（原文）

> Inferring the 3D structure from a single image, particularly in occluded regions, remains a fundamental yet unsolved challenge in vision-centric autonomous driving. Existing unsupervised approaches typically train a neural radiance field and treat the network outputs as occupancy probabilities during evaluation, overlooking the inconsistency between training and evaluation protocols. Moreover, the prevalent use of 2D ground truth fails to reveal the inherent ambiguity in occluded regions caused by insufficient geometric constraints. To address these issues, this paper presents a reformulated benchmark for unsupervised monocular 3D occupancy prediction. We first interpret the variables involved in the volume rendering process and identify the most physically consistent representation of the occupancy probability. Building on these analyses, we improve existing evaluation protocols by aligning the newly identified representation with voxel-wise 3D occupancy ground truth, thereby enabling unsupervised methods to be evaluated in a manner consistent with that of supervised approaches. Additionally, to impose explicit constraints in occluded regions, we introduce an occlusion-aware polarization mechanism that incorporates multi-view visual cues to enhance discrimination between occupied and free spaces in these regions. Extensive experiments demonstrate that our approach not only significantly outperforms existing unsupervised approaches but also matches the performance of supervised ones. Our source code and evaluation protocol will be made available upon publication.

