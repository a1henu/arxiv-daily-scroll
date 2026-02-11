---
layout: default
title: Look-Ahead and Look-Back Flows: Training-Free Image Generation with Trajectory Smoothing
---

# Look-Ahead and Look-Back Flows: Training-Free Image Generation with Trajectory Smoothing
**arXiv**：[2602.09449v1](https://arxiv.org/abs/2602.09449) · [PDF](https://arxiv.org/pdf/2602.09449.pdf)  
**作者**：Yan Luo, Henry Huang, Todd Y. Zhou, Mengyu Wang  

**一句话要点**：提出前瞻与回溯流，通过轨迹平滑实现免训练图像生成

**关键词**：免训练生成, 流匹配, 轨迹平滑, 图像生成, 潜空间优化

## 3 点简述
- 核心问题：调整流匹配中的速度场会引入误差累积，影响生成质量
- 方法要点：基于未来和过去信息，在潜空间直接平滑轨迹以减少误差
- 实验或效果：在COCO17等数据集上，性能优于多种先进模型

## 摘要（原文）

> Recent advances have reformulated diffusion models as deterministic ordinary differential equations (ODEs) through the framework of flow matching, providing a unified formulation for the noise-to-data generative process. Various training-free flow matching approaches have been developed to improve image generation through flow velocity field adjustment, eliminating the need for costly retraining. However, Modifying the velocity field $v$ introduces errors that propagate through the full generation path, whereas adjustments to the latent trajectory $z$ are naturally corrected by the pretrained velocity network, reducing error accumulation. In this paper, we propose two complementary training-free latent-trajectory adjustment approaches based on future and past velocity $v$ and latent trajectory $z$ information that refine the generative path directly in latent space. We propose two training-free trajectory smoothing schemes: \emph{Look-Ahead}, which averages the current and next-step latents using a curvature-gated weight, and \emph{Look-Back}, which smoothes latents using an exponential moving average with decay. We demonstrate through extensive experiments and comprehensive evaluation metrics that the proposed training-free trajectory smoothing models substantially outperform various state-of-the-art models across multiple datasets including COCO17, CUB-200, and Flickr30K.

