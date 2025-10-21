---
layout: default
title: M2H: Multi-Task Learning with Efficient Window-Based Cross-Task Attention for Monocular Spatial Perception
---

# M2H: Multi-Task Learning with Efficient Window-Based Cross-Task Attention for Monocular Spatial Perception
**arXiv**：[2510.17363v1](https://arxiv.org/abs/2510.17363) · [PDF](https://arxiv.org/pdf/2510.17363.pdf)  
**作者**：U. V. B. L Udugama, George Vosselman, Francesco Nex  

**一句话要点**：提出M2H多任务学习框架，通过窗口跨任务注意力提升单目图像空间感知效率

**关键词**：多任务学习, 单目空间感知, 窗口注意力, 轻量级ViT, 实时部署, 3D场景图

## 3 点简述
- 核心问题：边缘设备实时空间感知需高效多任务模型，减少计算开销
- 方法要点：引入窗口跨任务注意力模块，结构化交换特征，保持任务细节
- 实验或效果：在NYUDv2等数据集超越SOTA，保持计算高效，验证实际应用

## 摘要（原文）

> Deploying real-time spatial perception on edge devices requires efficient
> multi-task models that leverage complementary task information while minimizing
> computational overhead. This paper introduces Multi-Mono-Hydra (M2H), a novel
> multi-task learning framework designed for semantic segmentation and depth,
> edge, and surface normal estimation from a single monocular image. Unlike
> conventional approaches that rely on independent single-task models or shared
> encoder-decoder architectures, M2H introduces a Window-Based Cross-Task
> Attention Module that enables structured feature exchange while preserving
> task-specific details, improving prediction consistency across tasks. Built on
> a lightweight ViT-based DINOv2 backbone, M2H is optimized for real-time
> deployment and serves as the foundation for monocular spatial perception
> systems supporting 3D scene graph construction in dynamic environments.
> Comprehensive evaluations show that M2H outperforms state-of-the-art multi-task
> models on NYUDv2, surpasses single-task depth and semantic baselines on
> Hypersim, and achieves superior performance on the Cityscapes dataset, all
> while maintaining computational efficiency on laptop hardware. Beyond
> benchmarks, M2H is validated on real-world data, demonstrating its practicality
> in spatial perception tasks.

