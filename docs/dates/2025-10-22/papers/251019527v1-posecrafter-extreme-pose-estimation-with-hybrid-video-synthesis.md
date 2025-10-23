---
layout: default
title: PoseCrafter: Extreme Pose Estimation with Hybrid Video Synthesis
---

# PoseCrafter: Extreme Pose Estimation with Hybrid Video Synthesis
**arXiv**：[2510.19527v1](https://arxiv.org/abs/2510.19527) · [PDF](https://arxiv.org/pdf/2510.19527.pdf)  
**作者**：Qing Mao, Tianxin Huang, Yu Zhu, Jinqiu Sun, Yanning Zhang, Gim Hee Lee  

**一句话要点**：提出PoseCrafter通过混合视频生成解决稀疏重叠图像对的姿态估计问题

**关键词**：姿态估计, 视频合成, 特征匹配, 3D视觉, 稀疏重叠

## 3 点简述
- 核心问题：稀疏重叠图像对的相机姿态估计困难，现有方法在小或无重叠时性能差
- 方法要点：结合视频插值和姿态条件新视图合成，生成清晰中间帧并基于特征匹配选择
- 实验或效果：在多个数据集上显著提升姿态估计性能，尤其小或无重叠场景

## 摘要（原文）

> Pairwise camera pose estimation from sparsely overlapping image pairs remains
> a critical and unsolved challenge in 3D vision. Most existing methods struggle
> with image pairs that have small or no overlap. Recent approaches attempt to
> address this by synthesizing intermediate frames using video interpolation and
> selecting key frames via a self-consistency score. However, the generated
> frames are often blurry due to small overlap inputs, and the selection
> strategies are slow and not explicitly aligned with pose estimation. To solve
> these cases, we propose Hybrid Video Generation (HVG) to synthesize clearer
> intermediate frames by coupling a video interpolation model with a
> pose-conditioned novel view synthesis model, where we also propose a Feature
> Matching Selector (FMS) based on feature correspondence to select intermediate
> frames appropriate for pose estimation from the synthesized results. Extensive
> experiments on Cambridge Landmarks, ScanNet, DL3DV-10K, and NAVI demonstrate
> that, compared to existing SOTA methods, PoseCrafter can obviously enhance the
> pose estimation performances, especially on examples with small or no overlap.

