---
layout: default
title: CLIDD: Cross-Layer Independent Deformable Description for Efficient and Discriminative Local Feature Representation
---

# CLIDD: Cross-Layer Independent Deformable Description for Efficient and Discriminative Local Feature Representation
**arXiv**：[2601.09230v1](https://arxiv.org/abs/2601.09230) · [PDF](https://arxiv.org/pdf/2601.09230.pdf)  
**作者**：Haodi Yao, Fenghua He, Ning Hao, Yao Su  

**一句话要点**：提出CLIDD方法，通过跨层独立可变形描述实现高效且高区分度的局部特征表示，用于实时空间智能任务。

**关键词**：局部特征描述, 跨层采样, 可变形卷积, 硬件优化, 知识蒸馏, 实时匹配

## 3 点简述
- 核心问题：局部特征表示需兼顾高区分度与计算效率，以支持机器人导航等空间智能任务。
- 方法要点：采用跨层独立特征层次采样和可学习偏移，捕获多尺度细节，避免密集表示的计算负担。
- 实验或效果：超紧凑变体参数仅0.004M，匹配SuperPoint精度；高性能配置超越现有方法，在边缘设备上超过200 FPS。

## 摘要（原文）

> Robust local feature representations are essential for spatial intelligence tasks such as robot navigation and augmented reality. Establishing reliable correspondences requires descriptors that provide both high discriminative power and computational efficiency. To address this, we introduce Cross-Layer Independent Deformable Description (CLIDD), a method that achieves superior distinctiveness by sampling directly from independent feature hierarchies. This approach utilizes learnable offsets to capture fine-grained structural details across scales while bypassing the computational burden of unified dense representations. To ensure real-time performance, we implement a hardware-aware kernel fusion strategy that maximizes inference throughput. Furthermore, we develop a scalable framework that integrates lightweight architectures with a training protocol leveraging both metric learning and knowledge distillation. This scheme generates a wide spectrum of model variants optimized for diverse deployment constraints. Extensive evaluations demonstrate that our approach achieves superior matching accuracy and exceptional computational efficiency simultaneously. Specifically, the ultra-compact variant matches the precision of SuperPoint while utilizing only 0.004M parameters, achieving a 99.7% reduction in model size. Furthermore, our high-performance configuration outperforms all current state-of-the-art methods, including high-capacity DINOv2-based frameworks, while exceeding 200 FPS on edge devices. These results demonstrate that CLIDD delivers high-precision local feature matching with minimal computational overhead, providing a robust and scalable solution for real-time spatial intelligence tasks.

