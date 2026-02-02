---
layout: default
title: VisionTrim: Unified Vision Token Compression for Training-Free MLLM Acceleration
---

# VisionTrim: Unified Vision Token Compression for Training-Free MLLM Acceleration
**arXiv**：[2601.22674v1](https://arxiv.org/abs/2601.22674) · [PDF](https://arxiv.org/pdf/2601.22674.pdf)  
**作者**：Hanxun Yu, Wentong Li, Xuan Qu, Song Wang, Junbo Chen, Jianke Zhu  

**一句话要点**：提出VisionTrim框架，通过训练无关的视觉令牌压缩解决多模态大模型高计算成本问题。

**关键词**：多模态大模型, 视觉令牌压缩, 训练无关加速, 文本引导合并, 高分辨率图像, 视频理解

## 3 点简述
- 核心问题：多模态大模型因视觉令牌过多导致高计算成本，尤其在视频和高分辨率场景中。
- 方法要点：集成两个即插即用模块：DVTS保留关键视觉令牌，TGVC基于文本引导合并令牌。
- 实验或效果：在多种图像和视频基准测试中表现优越，促进实际部署。

## 摘要（原文）

> Multimodal large language models (MLLMs) suffer from high computational costs due to excessive visual tokens, particularly in high-resolution and video-based scenarios. Existing token reduction methods typically focus on isolated pipeline components and often neglect textual alignment, leading to performance degradation. In this paper, we propose VisionTrim, a unified framework for training-free MLLM acceleration, integrating two effective plug-and-play modules: 1) the Dominant Vision Token Selection (DVTS) module, which preserves essential visual tokens via a global-local view, and 2) the Text-Guided Vision Complement (TGVC) module, which facilitates context-aware token merging guided by textual cues. Extensive experiments across diverse image and video multimodal benchmarks demonstrate the performance superiority of our VisionTrim, advancing practical MLLM deployment in real-world applications. The code is available at: https://github.com/hanxunyu/VisionTrim.

