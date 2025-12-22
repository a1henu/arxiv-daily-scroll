---
layout: default
title: Beyond Semantic Features: Pixel-level Mapping for Generalized AI-Generated Image Detection
---

# Beyond Semantic Features: Pixel-level Mapping for Generalized AI-Generated Image Detection
**arXiv**：[2512.17350v1](https://arxiv.org/abs/2512.17350) · [PDF](https://arxiv.org/pdf/2512.17350.pdf)  
**作者**：Chenming Zhou, Jiaan Wang, Yu Li, Lei Li, Juan Cao, Sheng Tang  

**一句话要点**：提出像素级映射预处理以提升AI生成图像检测的跨生成器泛化能力

**关键词**：AI生成图像检测, 泛化能力, 像素级映射, 语义线索破坏, 高频痕迹, 跨生成器评估

## 3 点简述
- 当前检测器因过度依赖特定语义线索而难以泛化至未见生成模型
- 通过像素级映射破坏图像像素值分布，迫使检测器关注生成过程的高频痕迹
- 在GAN和扩散模型实验中显著提升先进检测器的跨生成器性能

## 摘要（原文）

> The rapid evolution of generative technologies necessitates reliable methods for detecting AI-generated images. A critical limitation of current detectors is their failure to generalize to images from unseen generative models, as they often overfit to source-specific semantic cues rather than learning universal generative artifacts. To overcome this, we introduce a simple yet remarkably effective pixel-level mapping pre-processing step to disrupt the pixel value distribution of images and break the fragile, non-essential semantic patterns that detectors commonly exploit as shortcuts. This forces the detector to focus on more fundamental and generalizable high-frequency traces inherent to the image generation process. Through comprehensive experiments on GAN and diffusion-based generators, we show that our approach significantly boosts the cross-generator performance of state-of-the-art detectors. Extensive analysis further verifies our hypothesis that the disruption of semantic cues is the key to generalization.

