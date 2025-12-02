---
layout: default
title: StyleYourSmile: Cross-Domain Face Retargeting Without Paired Multi-Style Data
---

# StyleYourSmile: Cross-Domain Face Retargeting Without Paired Multi-Style Data
**arXiv**：[2512.01895v1](https://arxiv.org/abs/2512.01895) · [PDF](https://arxiv.org/pdf/2512.01895.pdf)  
**作者**：Avirup Dey, Vinay Namboodiri  

**一句话要点**：提出StyleYourSmile方法，无需配对多风格数据实现跨域人脸表情重定向

**关键词**：跨域人脸重定向, 风格解耦, 扩散模型, 无配对数据, 身份保持

## 3 点简述
- 核心问题：跨域人脸重定向需解耦控制身份、表情和风格，现有方法泛化差或依赖多风格配对数据。
- 方法要点：采用双编码器框架提取域不变身份特征和域特定风格变化，结合扩散模型进行重定向。
- 实验或效果：在广泛视觉域中实现优越的身份保持和重定向保真度，无需测试时优化或微调。

## 摘要（原文）

> Cross-domain face retargeting requires disentangled control over identity, expressions, and domain-specific stylistic attributes. Existing methods, typically trained on real-world faces, either fail to generalize across domains, need test-time optimizations, or require fine-tuning with carefully curated multi-style datasets to achieve domain-invariant identity representations. In this work, we introduce \textit{StyleYourSmile}, a novel one-shot cross-domain face retargeting method that eliminates the need for curated multi-style paired data. We propose an efficient data augmentation strategy alongside a dual-encoder framework, for extracting domain-invariant identity cues and capturing domain-specific stylistic variations. Leveraging these disentangled control signals, we condition a diffusion model to retarget facial expressions across domains. Extensive experiments demonstrate that \textit{StyleYourSmile} achieves superior identity preservation and retargeting fidelity across a wide range of visual domains.

