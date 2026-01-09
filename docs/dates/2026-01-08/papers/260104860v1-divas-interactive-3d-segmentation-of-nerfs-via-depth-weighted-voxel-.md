---
layout: default
title: DivAS: Interactive 3D Segmentation of NeRFs via Depth-Weighted Voxel Aggregation
---

# DivAS: Interactive 3D Segmentation of NeRFs via Depth-Weighted Voxel Aggregation
**arXiv**：[2601.04860v1](https://arxiv.org/abs/2601.04860) · [PDF](https://arxiv.org/pdf/2601.04860.pdf)  
**作者**：Ayush Pande  

**一句话要点**：提出DivAS框架，通过深度加权体素聚合实现NeRF的免优化交互式3D分割

**关键词**：神经辐射场分割, 交互式3D分割, 深度加权聚合, 免优化框架, 实时视觉反馈, 多视图掩码融合

## 3 点简述
- 现有NeRF分割方法依赖优化训练，牺牲2D基础模型的零样本能力且速度慢
- DivAS利用用户点提示生成2D SAM掩码，结合NeRF深度先验进行精炼，提升几何精度
- 通过定制CUDA内核在200ms内聚合多视图掩码到3D体素网格，实现实时反馈，实验显示分割质量可比优化方法，端到端快2-2.5倍

## 摘要（原文）

> Existing methods for segmenting Neural Radiance Fields (NeRFs) are often optimization-based, requiring slow per-scene training that sacrifices the zero-shot capabilities of 2D foundation models. We introduce DivAS (Depth-interactive Voxel Aggregation Segmentation), an optimization-free, fully interactive framework that addresses these limitations. Our method operates via a fast GUI-based workflow where 2D SAM masks, generated from user point prompts, are refined using NeRF-derived depth priors to improve geometric accuracy and foreground-background separation. The core of our contribution is a custom CUDA kernel that aggregates these refined multi-view masks into a unified 3D voxel grid in under 200ms, enabling real-time visual feedback. This optimization-free design eliminates the need for per-scene training. Experiments on Mip-NeRF 360° and LLFF show that DivAS achieves segmentation quality comparable to optimization-based methods, while being 2-2.5x faster end-to-end, and up to an order of magnitude faster when excluding user prompting time.

