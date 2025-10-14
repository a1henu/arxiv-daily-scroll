---
layout: default
title: DKPMV: Dense Keypoints Fusion from Multi-View RGB Frames for 6D Pose Estimation of Textureless Objects
---

# DKPMV: Dense Keypoints Fusion from Multi-View RGB Frames for 6D Pose Estimation of Textureless Objects
**arXiv**：[2510.10933v1](https://arxiv.org/abs/2510.10933) · [PDF](https://arxiv.org/pdf/2510.10933.pdf)  
**作者**：Jiahong Chen, Jinghao Wang, Zi Wang, Ziwen Wang, Banglei Guan, Qifeng Yu  

**一句话要点**：提出DKPMV以解决无纹理物体6D姿态估计中多视角RGB图像融合不足的问题

**关键词**：6D姿态估计, 多视角融合, 密集关键点, 无纹理物体, 注意力机制, 对称感知训练

## 3 点简述
- 核心问题：无纹理物体6D姿态估计常因深度信息缺失而困难，现有多视角方法依赖深度数据或几何线索利用不足。
- 方法要点：设计三阶段渐进姿态优化策略，通过注意力聚合和对称感知训练增强关键点网络，实现密集关键点融合。
- 实验或效果：在ROBI数据集上优于多视角RGB方法，多数情况下超越RGB-D方法，代码即将发布。

## 摘要（原文）

> 6D pose estimation of textureless objects is valuable for industrial robotic
> applications, yet remains challenging due to the frequent loss of depth
> information. Current multi-view methods either rely on depth data or
> insufficiently exploit multi-view geometric cues, limiting their performance.
> In this paper, we propose DKPMV, a pipeline that achieves dense keypoint-level
> fusion using only multi-view RGB images as input. We design a three-stage
> progressive pose optimization strategy that leverages dense multi-view keypoint
> geometry information. To enable effective dense keypoint fusion, we enhance the
> keypoint network with attentional aggregation and symmetry-aware training,
> improving prediction accuracy and resolving ambiguities on symmetric objects.
> Extensive experiments on the ROBI dataset demonstrate that DKPMV outperforms
> state-of-the-art multi-view RGB approaches and even surpasses the RGB-D methods
> in the majority of cases. The code will be available soon.

