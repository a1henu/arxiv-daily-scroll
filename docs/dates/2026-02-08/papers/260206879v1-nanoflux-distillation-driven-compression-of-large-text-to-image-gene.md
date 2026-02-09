---
layout: default
title: NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices
---

# NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices
**arXiv**：[2602.06879v1](https://arxiv.org/abs/2602.06879) · [PDF](https://arxiv.org/pdf/2602.06879.pdf)  
**作者**：Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Couto Pimentel Ramos, Luca Morreale, Mehdi Noroozi, Abhinav Mehrotra  

**一句话要点**：提出NanoFLUX蒸馏压缩模型，实现移动设备高质量文本到图像生成

**关键词**：文本到图像生成, 模型压缩, 蒸馏训练, 移动设备部署, 流匹配模型

## 3 点简述
- 核心问题：大规模文本到图像扩散模型规模增大，与移动设备解决方案差距扩大
- 方法要点：采用渐进压缩管道，包括剪枝冗余组件、基于ResNet的令牌下采样和文本编码器蒸馏
- 实验或效果：在移动设备上约2.5秒生成512x512图像，验证高质量设备端生成可行性

## 摘要（原文）

> While large-scale text-to-image diffusion models continue to improve in visual quality, their increasing scale has widened the gap between state-of-the-art models and on-device solutions. To address this gap, we introduce NanoFLUX, a 2.4B text-to-image flow-matching model distilled from 17B FLUX.1-Schnell using a progressive compression pipeline designed to preserve generation quality. Our contributions include: (1) A model compression strategy driven by pruning redundant components in the diffusion transformer, reducing its size from 12B to 2B; (2) A ResNet-based token downsampling mechanism that reduces latency by allowing intermediate blocks to operate on lower-resolution tokens while preserving high-resolution processing elsewhere; (3) A novel text encoder distillation approach that leverages visual signals from early layers of the denoiser during sampling. Empirically, NanoFLUX generates 512 x 512 images in approximately 2.5 seconds on mobile devices, demonstrating the feasibility of high-quality on-device text-to-image generation.

