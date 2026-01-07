---
layout: default
title: StableDPT: Temporal Stable Monocular Video Depth Estimation
---

# StableDPT: Temporal Stable Monocular Video Depth Estimation
**arXiv**：[2601.02793v1](https://arxiv.org/abs/2601.02793) · [PDF](https://arxiv.org/pdf/2601.02793.pdf)  
**作者**：Ivan Sobko, Hayko Riemenschneider, Markus Gross, Christopher Schroers  

**一句话要点**：提出StableDPT以解决单目视频深度估计中的时间不稳定问题

**关键词**：单目视频深度估计, 时间稳定性, 跨注意力机制, 关键帧采样, 长视频处理

## 3 点简述
- 核心问题：单图像深度估计模型应用于视频时产生时间不稳定和闪烁伪影
- 方法要点：在DPT头部集成高效跨注意力时间层，从关键帧捕获全局上下文
- 实验或效果：在多个基准数据集上展示改进的时间一致性和2倍以上处理速度

## 摘要（原文）

> Applying single image Monocular Depth Estimation (MDE) models to video sequences introduces significant temporal instability and flickering artifacts. We propose a novel approach that adapts any state-of-the-art image-based (depth) estimation model for video processing by integrating a new temporal module - trainable on a single GPU in a few days. Our architecture StableDPT builds upon an off-the-shelf Vision Transformer (ViT) encoder and enhances the Dense Prediction Transformer (DPT) head. The core of our contribution lies in the temporal layers within the head, which use an efficient cross-attention mechanism to integrate information from keyframes sampled across the entire video sequence. This allows the model to capture global context and inter-frame relationships leading to more accurate and temporally stable depth predictions. Furthermore, we propose a novel inference strategy for processing videos of arbitrary length avoiding the scale misalignment and redundant computations associated with overlapping windows used in other methods. Evaluations on multiple benchmark datasets demonstrate improved temporal consistency, competitive state-of-the-art performance and on top 2x faster processing in real-world scenarios.

