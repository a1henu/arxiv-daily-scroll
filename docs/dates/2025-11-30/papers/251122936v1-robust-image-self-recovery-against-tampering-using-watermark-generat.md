---
layout: default
title: Robust Image Self-Recovery against Tampering using Watermark Generation with Pixel Shuffling
---

# Robust Image Self-Recovery against Tampering using Watermark Generation with Pixel Shuffling
**arXiv**：[2511.22936v1](https://arxiv.org/abs/2511.22936) · [PDF](https://arxiv.org/pdf/2511.22936.pdf)  
**作者**：Minyoung Kim, Paul Hongsuck Seo  

**一句话要点**：提出ReImage框架，通过像素重排水印实现鲁棒图像自恢复以应对篡改

**关键词**：图像自恢复, 神经水印, 像素重排, 篡改检测, AIGC安全

## 3 点简述
- 针对AIGC时代数字媒体真实性担忧，现有方法在篡改区域恢复上不准确
- 采用神经水印嵌入重排图像作为水印，结合生成器和图像增强模块优化恢复
- 在多种篡改场景下实现最先进性能，代码和模型将发布

## 摘要（原文）

> The rapid growth of Artificial Intelligence-Generated Content (AIGC) raises concerns about the authenticity of digital media. In this context, image self-recovery, reconstructing original content from its manipulated version, offers a practical solution for understanding the attacker's intent and restoring trustworthy data. However, existing methods often fail to accurately recover tampered regions, falling short of the primary goal of self-recovery. To address this challenge, we propose ReImage, a neural watermarking-based self-recovery framework that embeds a shuffled version of the target image into itself as a watermark. We design a generator that produces watermarks optimized for neural watermarking and introduce an image enhancement module to refine the recovered image. We further analyze and resolve key limitations of shuffled watermarking, enabling its effective use in self-recovery. We demonstrate that ReImage achieves state-of-the-art performance across diverse tampering scenarios, consistently producing high-quality recovered images. The code and pretrained models will be released upon publication.

