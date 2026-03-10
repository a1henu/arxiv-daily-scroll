---
layout: default
title: ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting
---

# ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting
**arXiv**：[2603.08661v1](https://arxiv.org/abs/2603.08661) · [PDF](https://arxiv.org/pdf/2603.08661.pdf)  
**作者**：Jordi Muñoz Vicente  

**一句话要点**：提出ImprovedGS+以在3D高斯泼溅中实现高性能重建，通过C++/CUDA重实现提升效率与质量。

**关键词**：3D高斯泼溅, C++/CUDA实现, 高性能计算, 场景重建, LichtFeld-Studio框架, 自适应调度

## 3 点简述
- 核心问题：3D高斯泼溅在重建保真度与计算效率间需平衡，现有方法存在主机-设备同步和训练延迟问题。
- 方法要点：采用C++/CUDA原生实现，引入长轴分割CUDA核、基于拉普拉斯的重要性核与自适应指数尺度调度器。
- 实验效果：在Mip-NeRF360数据集上，1M预算变体训练时间减少26.8%，高斯数减少13.3%，全变体PSNR提升1.28 dB，参数复杂度降低38.4%。

## 摘要（原文）

> Recent advancements in 3D Gaussian Splatting (3DGS) have shifted the focus toward balancing reconstruction fidelity with computational efficiency. In this work, we propose ImprovedGS+, a high-performance, low-level reinvention of the ImprovedGS strategy, implemented natively within the LichtFeld-Studio framework. By transitioning from high-level Python logic to hardware-optimized C++/CUDA kernels, we achieve a significant reduction in host-device synchronization and training latency. Our implementation introduces a Long-Axis-Split (LAS) CUDA kernel, custom Laplacian-based importance kernels with Non-Maximum Suppression (NMS) for edge scores, and an adaptive Exponential Scale Scheduler. Experimental results on the Mip-NeRF360 dataset demonstrate that ImprovedGS+ establishes a new Pareto-optimal front for scene reconstruction. Our 1M-budget variant outperforms the state-of-the-art MCMC baseline by achieving a 26.8% reduction in training time (saving 17 minutes per session) and utilizing 13.3% fewer Gaussians while maintaining superior visual quality. Furthermore, our full variant demonstrates a 1.28 dB PSNR increase over the ADC baseline with a 38.4% reduction in parametric complexity. These results validate ImprovedGS+ as a scalable, high-speed solution that upholds the core pillars of Speed, Quality, and Usability within the LichtFeld-Studio ecosystem.

