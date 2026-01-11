---
layout: default
title: DivAS: Interactive 3D Segmentation of NeRFs via Depth-Weighted Voxel Aggregation
---

# DivAS: Interactive 3D Segmentation of NeRFs via Depth-Weighted Voxel Aggregation
**arXiv**：[2601.04860v1](https://arxiv.org/abs/2601.04860) · [PDF](https://arxiv.org/pdf/2601.04860.pdf)  
**作者**：Ayush Pande  

**一句话要点**：提出DivAS框架，通过深度加权体素聚合实现NeRF的交互式3D分割，无需逐场景训练。

**关键词**：NeRF分割, 交互式3D分割, 深度加权聚合, 无优化框架, 实时视觉反馈, 多视角掩码融合

## 3 点简述
- 现有NeRF分割方法依赖优化，逐场景训练慢且牺牲2D基础模型的零样本能力。
- DivAS采用无优化设计，结合2D SAM掩码和NeRF深度先验，通过CUDA内核快速聚合多视角掩码到3D体素网格。
- 实验显示，在Mip-NeRF 360°和LLFF上，DivAS分割质量可比优化方法，端到端快2-2.5倍，排除用户提示时间时快一个数量级。

## 摘要（原文）

> Existing methods for segmenting Neural Radiance Fields (NeRFs) are often optimization-based, requiring slow per-scene training that sacrifices the zero-shot capabilities of 2D foundation models. We introduce DivAS (Depth-interactive Voxel Aggregation Segmentation), an optimization-free, fully interactive framework that addresses these limitations. Our method operates via a fast GUI-based workflow where 2D SAM masks, generated from user point prompts, are refined using NeRF-derived depth priors to improve geometric accuracy and foreground-background separation. The core of our contribution is a custom CUDA kernel that aggregates these refined multi-view masks into a unified 3D voxel grid in under 200ms, enabling real-time visual feedback. This optimization-free design eliminates the need for per-scene training. Experiments on Mip-NeRF 360° and LLFF show that DivAS achieves segmentation quality comparable to optimization-based methods, while being 2-2.5x faster end-to-end, and up to an order of magnitude faster when excluding user prompting time.

