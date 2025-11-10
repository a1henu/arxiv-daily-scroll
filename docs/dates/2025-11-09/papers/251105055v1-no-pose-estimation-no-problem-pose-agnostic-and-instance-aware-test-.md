---
layout: default
title: No Pose Estimation? No Problem: Pose-Agnostic and Instance-Aware Test-Time Adaptation for Monocular Depth Estimation
---

# No Pose Estimation? No Problem: Pose-Agnostic and Instance-Aware Test-Time Adaptation for Monocular Depth Estimation
**arXiv**：[2511.05055v1](https://arxiv.org/abs/2511.05055) · [PDF](https://arxiv.org/pdf/2511.05055.pdf)  
**作者**：Mingyu Sung, Hyeonmin Choe, Il-Min Kim, Sangseok Yun, Jae Mo Kang  

**一句话要点**：提出PITTA框架以解决单目深度估计在动态环境中的测试时适应问题

**关键词**：单目深度估计, 测试时适应, 姿态无关, 实例感知掩码, 动态环境适应

## 3 点简述
- 核心问题：单目深度估计模型在训练与测试环境差异时性能下降，现有方法在动态环境中效果不佳
- 方法要点：采用姿态无关测试时适应和实例感知图像掩码，无需相机姿态信息
- 实验或效果：在DrivingStereo和Waymo数据集上超越现有技术，性能显著提升

## 摘要（原文）

> Monocular depth estimation (MDE), inferring pixel-level depths in single RGB
> images from a monocular camera, plays a crucial and pivotal role in a variety
> of AI applications demanding a three-dimensional (3D) topographical scene. In
> the real-world scenarios, MDE models often need to be deployed in environments
> with different conditions from those for training. Test-time (domain)
> adaptation (TTA) is one of the compelling and practical approaches to address
> the issue. Although there have been notable advancements in TTA for MDE,
> particularly in a self-supervised manner, existing methods are still
> ineffective and problematic when applied to diverse and dynamic environments.
> To break through this challenge, we propose a novel and high-performing TTA
> framework for MDE, named PITTA. Our approach incorporates two key innovative
> strategies: (i) pose-agnostic TTA paradigm for MDE and (ii) instance-aware
> image masking. Specifically, PITTA enables highly effective TTA on a pretrained
> MDE network in a pose-agnostic manner without resorting to any camera pose
> information. Besides, our instance-aware masking strategy extracts
> instance-wise masks for dynamic objects (e.g., vehicles, pedestrians, etc.)
> from a segmentation mask produced by a pretrained panoptic segmentation
> network, by removing static objects including background components. To further
> boost performance, we also present a simple yet effective edge extraction
> methodology for the input image (i.e., a single monocular image) and depth map.
> Extensive experimental evaluations on DrivingStereo and Waymo datasets with
> varying environmental conditions demonstrate that our proposed framework,
> PITTA, surpasses the existing state-of-the-art techniques with remarkable
> performance improvements in MDE during TTA.

