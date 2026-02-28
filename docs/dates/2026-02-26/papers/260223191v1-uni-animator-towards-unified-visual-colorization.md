---
layout: default
title: Uni-Animator: Towards Unified Visual Colorization
---

# Uni-Animator: Towards Unified Visual Colorization
**arXiv**：[2602.23191v1](https://arxiv.org/abs/2602.23191) · [PDF](https://arxiv.org/pdf/2602.23191.pdf)  
**作者**：Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  

**一句话要点**：提出Uni-Animator框架以统一图像与视频草图着色任务

**关键词**：草图着色, 扩散Transformer, 时序一致性, 物理细节保留, 统一框架

## 3 点简述
- 现有方法难以统一图像与视频着色，存在色彩迁移不精确、细节保留不足和运动场景时序不一致问题
- 通过实例块嵌入增强视觉参考、物理特征强化细节、基于草图的动态RoPE编码来解决上述问题
- 实验表明该方法在图像和视频着色上均取得竞争性性能，具备高细节保真度和强时序一致性

## 摘要（原文）

> We propose Uni-Animator, a novel Diffusion Transformer (DiT)-based framework for unified image and video sketch colorization. Existing sketch colorization methods struggle to unify image and video tasks, suffering from imprecise color transfer with single or multiple references, inadequate preservation of high-frequency physical details, and compromised temporal coherence with motion artifacts in large-motion scenes. To tackle imprecise color transfer, we introduce visual reference enhancement via instance patch embedding, enabling precise alignment and fusion of reference color information. To resolve insufficient physical detail preservation, we design physical detail reinforcement using physical features that effectively capture and retain high-frequency textures. To mitigate motion-induced temporal inconsistency, we propose sketch-based dynamic RoPE encoding that adaptively models motion-aware spatial-temporal dependencies. Extensive experimental results demonstrate that Uni-Animator achieves competitive performance on both image and video sketch colorization, matching that of task-specific methods while unlocking unified cross-domain capabilities with high detail fidelity and robust temporal consistency.

