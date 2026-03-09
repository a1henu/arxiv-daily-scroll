---
layout: default
title: Architectural Unification for Polarimetric Imaging Across Multiple Degradations
---

# Architectural Unification for Polarimetric Imaging Across Multiple Degradations
**arXiv**：[2603.05834v1](https://arxiv.org/abs/2603.05834) · [PDF](https://arxiv.org/pdf/2603.05834.pdf)  
**作者**：Chu Zhou, Yufei Han, Junda Liao, Linrui Dai, Wangze Xu, Art Subpa-Asa, Heng Guo, Boxin Shi, Imari Sato  

**一句话要点**：提出统一架构框架以解决多退化场景下的偏振成像问题

**关键词**：偏振成像, 统一架构, 图像-Stokes处理, 物理一致性, 多退化恢复

## 3 点简述
- 核心问题：偏振参数从退化测量中恢复困难，现有方法缺乏跨场景适应性和物理一致性
- 方法要点：采用结构共享的统一架构，单阶段联合图像-Stokes处理，保持物理一致性
- 实验或效果：在低光去噪、运动去模糊和去马赛克任务中实现最先进性能

## 摘要（原文）

> Polarimetric imaging aims to recover polarimetric parameters, including Total Intensity (TI), Degree of Polarization (DoP), and Angle of Polarization (AoP), from captured polarized measurements. In real-world scenarios, these measurements are frequently affected by diverse degradations such as low-light noise, motion blur, and mosaicing artifacts. Due to the nonlinear dependency of DoP and AoP on the measured intensities, accurately retrieving physically consistent polarimetric parameters from degraded observations remains highly challenging. Existing approaches typically adopt task-specific network architectures tailored to individual degradation types, limiting their adaptability across different restoration scenarios. Moreover, many methods rely on multi-stage processing pipelines that suffer from error accumulation, or operate solely in a single domain (either image or Stokes domain), failing to fully exploit the intrinsic physical relationships between them. In this work, we propose a unified architectural framework for polarimetric imaging that is structurally shared across multiple degradation scenarios. Rather than redesigning network structures for each task, our framework maintains a consistent architectural design while being trained separately for different degradations. The model performs single-stage joint image-Stokes processing, avoiding error accumulation and explicitly preserving physical consistency. Extensive experiments show that this unified architectural design, when trained for specific degradation types, consistently achieves state-of-the-art performance across low-light denoising, motion deblurring, and demosaicing tasks, establishing a versatile and physically grounded solution for degraded polarimetric imaging.

