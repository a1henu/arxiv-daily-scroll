---
layout: default
title: Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos
---

# Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos
**arXiv**：[2511.19936v1](https://arxiv.org/abs/2511.19936) · [PDF](https://arxiv.org/pdf/2511.19936.pdf)  
**作者**：Youngseo Kim, Dohyun Kim, Geohee Han, Paul Hongsuck Seo  

**一句话要点**：提出DRIFT框架，利用图像扩散模型实现视频中零样本对象跟踪

**关键词**：图像扩散模型, 零样本对象跟踪, 语义传播, 视频分割, 自注意力机制

## 3 点简述
- 核心问题：图像扩散模型的自注意力图如何用于视频中的语义传播和对象跟踪
- 方法要点：将自注意力图重新解释为传播核，结合测试时优化策略提升鲁棒性
- 实验或效果：在标准视频对象分割基准上实现零样本最先进性能

## 摘要（原文）

> Image diffusion models, though originally developed for image generation, implicitly capture rich semantic structures that enable various recognition and localization tasks beyond synthesis. In this work, we investigate their self-attention maps can be reinterpreted as semantic label propagation kernels, providing robust pixel-level correspondences between relevant image regions. Extending this mechanism across frames yields a temporal propagation kernel that enables zero-shot object tracking via segmentation in videos. We further demonstrate the effectiveness of test-time optimization strategies-DDIM inversion, textual inversion, and adaptive head weighting-in adapting diffusion features for robust and consistent label propagation. Building on these findings, we introduce DRIFT, a framework for object tracking in videos leveraging a pretrained image diffusion model with SAM-guided mask refinement, achieving state-of-the-art zero-shot performance on standard video object segmentation benchmarks.

