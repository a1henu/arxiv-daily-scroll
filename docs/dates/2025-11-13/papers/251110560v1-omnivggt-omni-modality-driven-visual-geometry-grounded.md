---
layout: default
title: OmniVGGT: Omni-Modality Driven Visual Geometry Grounded
---

# OmniVGGT: Omni-Modality Driven Visual Geometry Grounded
**arXiv**：[2511.10560v1](https://arxiv.org/abs/2511.10560) · [PDF](https://arxiv.org/pdf/2511.10560.pdf)  
**作者**：Haosong Peng, Hao Li, Yalun Dai, Yushi Lan, Yihang Luo, Tianyu Qi, Zhengshen Zhang, Yufeng Zhan, Junfei Zhang, Wenchao Xu, Ziwei Liu  

**一句话要点**：提出OmniVGGT框架以利用任意几何模态增强视觉任务性能

**关键词**：多模态融合, 几何编码, 3D视觉, 基础模型, 机器人视觉

## 3 点简述
- 核心问题：现有3D基础模型多依赖RGB输入，忽略几何线索如深度和相机参数。
- 方法要点：通过GeoAdapter和零初始化卷积注入几何信息，保持模型稳定与高效。
- 实验效果：在深度估计和相机姿态估计等任务中优于现有方法，并提升VLA模型性能。

## 摘要（原文）

> General 3D foundation models have started to lead the trend of unifying diverse vision tasks, yet most assume RGB-only inputs and ignore readily available geometric cues (e.g., camera intrinsics, poses, and depth maps). To address this issue, we introduce OmniVGGT, a novel framework that can effectively benefit from an arbitrary number of auxiliary geometric modalities during both training and inference. In our framework, a GeoAdapter is proposed to encode depth and camera intrinsics/extrinsics into a spatial foundation model. It employs zero-initialized convolutions to progressively inject geometric information without disrupting the foundation model's representation space. This design ensures stable optimization with negligible overhead, maintaining inference speed comparable to VGGT even with multiple additional inputs. Additionally, a stochastic multimodal fusion regimen is proposed, which randomly samples modality subsets per instance during training. This enables an arbitrary number of modality inputs during testing and promotes learning robust spatial representations instead of overfitting to auxiliary cues. Comprehensive experiments on monocular/multi-view depth estimation, multi-view stereo, and camera pose estimation demonstrate that OmniVGGT outperforms prior methods with auxiliary inputs and achieves state-of-the-art results even with RGB-only input. To further highlight its practical utility, we integrated OmniVGGT into vision-language-action (VLA) models. The enhanced VLA model by OmniVGGT not only outperforms the vanilla point-cloud-based baseline on mainstream benchmarks, but also effectively leverages accessible auxiliary inputs to achieve consistent gains on robotic tasks.

