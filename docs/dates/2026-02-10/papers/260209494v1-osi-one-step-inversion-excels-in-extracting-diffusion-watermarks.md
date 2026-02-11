---
layout: default
title: OSI: One-step Inversion Excels in Extracting Diffusion Watermarks
---

# OSI: One-step Inversion Excels in Extracting Diffusion Watermarks
**arXiv**：[2602.09494v1](https://arxiv.org/abs/2602.09494) · [PDF](https://arxiv.org/pdf/2602.09494.pdf)  
**作者**：Yuwei Chen, Zhenliang He, Jia Tang, Meina Kan, Shiguang Shan  

**一句话要点**：提出一步反演方法以高效提取扩散模型水印

**关键词**：扩散模型水印, 一步反演, 符号分类, 高斯阴影, 计算效率, 版权保护

## 3 点简述
- 问题：现有方法需多步反演获取初始噪声，计算成本高且耗时
- 方法：将水印提取重构为可学习的符号分类问题，避免精确回归初始噪声
- 效果：速度提升20倍，准确率更高，水印载荷容量翻倍

## 摘要（原文）

> Watermarking is an important mechanism for provenance and copyright protection of diffusion-generated images. Training-free methods, exemplified by Gaussian Shading, embed watermarks into the initial noise of diffusion models with negligible impact on the quality of generated images. However, extracting this type of watermark typically requires multi-step diffusion inversion to obtain precise initial noise, which is computationally expensive and time-consuming. To address this issue, we propose One-step Inversion (OSI), a significantly faster and more accurate method for extracting Gaussian Shading style watermarks. OSI reformulates watermark extraction as a learnable sign classification problem, which eliminates the need for precise regression of the initial noise. Then, we initialize the OSI model from the diffusion backbone and finetune it on synthesized noise-image pairs with a sign classification objective. In this manner, the OSI model is able to accomplish the watermark extraction efficiently in only one step. Our OSI substantially outperforms the multi-step diffusion inversion method: it is 20x faster, achieves higher extraction accuracy, and doubles the watermark payload capacity. Extensive experiments across diverse schedulers, diffusion backbones, and cryptographic schemes consistently show improvements, demonstrating the generality of our OSI framework.

