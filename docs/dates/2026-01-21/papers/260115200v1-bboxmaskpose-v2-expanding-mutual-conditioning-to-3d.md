---
layout: default
title: BBoxMaskPose v2: Expanding Mutual Conditioning to 3D
---

# BBoxMaskPose v2: Expanding Mutual Conditioning to 3D
**arXiv**：[2601.15200v1](https://arxiv.org/abs/2601.15200) · [PDF](https://arxiv.org/pdf/2601.15200.pdf)  
**作者**：Miroslav Purkrabek, Constantin Kolomiiets, Jiri Matas  

**一句话要点**：提出BBoxMaskPose v2，通过互条件机制提升拥挤场景下的2D和3D姿态估计性能。

**关键词**：2D姿态估计, 3D姿态估计, 拥挤场景, 掩码条件, SAM细化, 互条件机制

## 3 点简述
- 核心问题：拥挤场景下2D姿态估计性能不足，影响3D姿态估计。
- 方法要点：集成PMPose概率化掩码条件估计和SAM掩码细化模块。
- 实验或效果：在COCO和OCHuman数据集上超越现有方法，首次在OCHuman上超过50 AP。

## 摘要（原文）

> Most 2D human pose estimation benchmarks are nearly saturated, with the exception of crowded scenes. We introduce PMPose, a top-down 2D pose estimator that incorporates the probabilistic formulation and the mask-conditioning. PMPose improves crowded pose estimation without sacrificing performance on standard scenes. Building on this, we present BBoxMaskPose v2 (BMPv2) integrating PMPose and an enhanced SAM-based mask refinement module. BMPv2 surpasses state-of-the-art by 1.5 average precision (AP) points on COCO and 6 AP points on OCHuman, becoming the first method to exceed 50 AP on OCHuman. We demonstrate that BMP's 2D prompting of 3D model improves 3D pose estimation in crowded scenes and that advances in 2D pose quality directly benefit 3D estimation. Results on the new OCHuman-Pose dataset show that multi-person performance is more affected by pose prediction accuracy than by detection. The code, models, and data are available on https://MiraPurkrabek.github.io/BBox-Mask-Pose/.

