---
layout: default
title: Mobile-O: Unified Multimodal Understanding and Generation on Mobile Device
---

# Mobile-O: Unified Multimodal Understanding and Generation on Mobile Device
**arXiv**：[2602.20161v1](https://arxiv.org/abs/2602.20161) · [PDF](https://arxiv.org/pdf/2602.20161.pdf)  
**作者**：Abdelrahman Shaker, Ahmed Heakl, Jaseel Muhammad, Ritesh Thawkar, Omkar Thawakar, Senmao Li, Hisham Cholakkal, Ian Reid, Eric P. Xing, Salman Khan, Fahad Shahbaz Khan  

**一句话要点**：提出Mobile-O以在移动设备上实现高效统一的多模态理解与生成

**关键词**：移动设备部署, 统一多模态模型, 视觉语言融合, 扩散生成, 边缘计算, 实时处理

## 3 点简述
- 现有统一多模态模型数据需求大且计算重，难以部署于边缘设备
- 核心模块Mobile Conditioning Projector通过深度可分离卷积和层级对齐，高效融合视觉语言特征与扩散生成器
- 在少量数据训练下，Mobile-O在生成和理解任务上性能优越，在iPhone上每512x512图像仅需约3秒

## 摘要（原文）

> Unified multimodal models can both understand and generate visual content within a single architecture. Existing models, however, remain data-hungry and too heavy for deployment on edge devices. We present Mobile-O, a compact vision-language-diffusion model that brings unified multimodal intelligence to a mobile device. Its core module, the Mobile Conditioning Projector (MCP), fuses vision-language features with a diffusion generator using depthwise-separable convolutions and layerwise alignment. This design enables efficient cross-modal conditioning with minimal computational cost. Trained on only a few million samples and post-trained in a novel quadruplet format (generation prompt, image, question, answer), Mobile-O jointly enhances both visual understanding and generation capabilities. Despite its efficiency, Mobile-O attains competitive or superior performance compared to other unified models, achieving 74% on GenEval and outperforming Show-O and JanusFlow by 5% and 11%, while running 6x and 11x faster, respectively. For visual understanding, Mobile-O surpasses them by 15.3% and 5.1% averaged across seven benchmarks. Running in only ~3s per 512x512 image on an iPhone, Mobile-O establishes the first practical framework for real-time unified multimodal understanding and generation on edge devices. We hope Mobile-O will ease future research in real-time unified multimodal intelligence running entirely on-device with no cloud dependency. Our code, models, datasets, and mobile application are publicly available at https://amshaker.github.io/Mobile-O/

