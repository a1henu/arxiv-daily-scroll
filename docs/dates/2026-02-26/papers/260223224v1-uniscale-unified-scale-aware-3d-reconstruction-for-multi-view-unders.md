---
layout: default
title: UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception
---

# UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception
**arXiv**：[2602.23224v1](https://arxiv.org/abs/2602.23224) · [PDF](https://arxiv.org/pdf/2602.23224.pdf)  
**作者**：Mohammad Mahdavian, Gordon Tan, Binbin Xu, Yuan Ren, Dongfeng Bai, Bingbing Liu  

**一句话要点**：提出UniScale统一框架，通过先验注入实现机器人感知中的多视图尺度感知三维重建。

**关键词**：多视图三维重建, 尺度感知, 机器人感知, 几何先验, 统一框架, 度量尺度恢复

## 3 点简述
- 核心问题：机器人视觉导航中，从多视图图像准确提取环境结构并恢复度量尺度是关键挑战。
- 方法要点：使用单一前馈网络联合估计相机参数、尺度不变深度和点图，并可选整合几何先验以恢复场景度量尺度。
- 实验或效果：在多个基准测试中评估，展示强泛化能力和跨环境一致性能，无需从头训练，适合资源受限机器人团队。

## 摘要（原文）

> We present UniScale, a unified, scale-aware multi-view 3D reconstruction framework for robotic applications that flexibly integrates geometric priors through a modular, semantically informed design. In vision-based robotic navigation, the accurate extraction of environmental structure from raw image sequences is critical for downstream tasks. UniScale addresses this challenge with a single feed-forward network that jointly estimates camera intrinsics and extrinsics, scale-invariant depth and point maps, and the metric scale of a scene from multi-view images, while optionally incorporating auxiliary geometric priors when available. By combining global contextual reasoning with camera-aware feature representations, UniScale is able to recover the metric-scale of the scene. In robotic settings where camera intrinsics are known, they can be easily incorporated to improve performance, with additional gains obtained when camera poses are also available. This co-design enables robust, metric-aware 3D reconstruction within a single unified model. Importantly, UniScale does not require training from scratch, and leverages world priors exhibited in pre-existing models without geometric encoding strategies, making it particularly suitable for resource-constrained robotic teams. We evaluate UniScale on multiple benchmarks, demonstrating strong generalization and consistent performance across diverse environments. We will release our implementation upon acceptance.

