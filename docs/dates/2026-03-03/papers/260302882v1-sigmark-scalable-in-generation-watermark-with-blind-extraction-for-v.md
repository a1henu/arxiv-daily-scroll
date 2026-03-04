---
layout: default
title: SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion
---

# SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion
**arXiv**：[2603.02882v1](https://arxiv.org/abs/2603.02882) · [PDF](https://arxiv.org/pdf/2603.02882.pdf)  
**作者**：Xinjie Zhu, Zijing Zhao, Hui Jin, Qingxiao Guo, Yilong Ma, Yunhao Wang, Xiaobing Guo, Weifeng Zhang  

**一句话要点**：提出SIGMark框架，实现视频扩散模型的无失真盲提取水印，以解决现有方法计算成本高和鲁棒性弱的问题。

**关键词**：视频扩散模型, 盲提取水印, 因果3D VAE, 鲁棒性增强, 无失真水印, 可扩展水印

## 3 点简述
- 核心问题：现有视频扩散模型水印方法非盲提取，存储和计算成本高，且在因果3D VAE下对时间扰动鲁棒性差。
- 方法要点：采用GF-PRC生成水印初始噪声实现盲提取，结合SGO模块增强对时间扰动的鲁棒性。
- 实验或效果：在现代扩散模型上验证，提取时在时空扰动下保持高比特精度，开销小，展现可扩展性和鲁棒性。

## 摘要（原文）

> Artificial Intelligence Generated Content (AIGC), particularly video generation with diffusion models, has been advanced rapidly. Invisible watermarking is a key technology for protecting AI-generated videos and tracing harmful content, and thus plays a crucial role in AI safety. Beyond post-processing watermarks which inevitably degrade video quality, recent studies have proposed distortion-free in-generation watermarking for video diffusion models. However, existing in-generation approaches are non-blind: they require maintaining all the message-key pairs and performing template-based matching during extraction, which incurs prohibitive computational costs at scale. Moreover, when applied to modern video diffusion models with causal 3D Variational Autoencoders (VAEs), their robustness against temporal disturbance becomes extremely weak. To overcome these challenges, we propose SIGMark, a Scalable In-Generation watermarking framework with blind extraction for video diffusion. To achieve blind-extraction, we propose to generate watermarked initial noise using a Global set of Frame-wise PseudoRandom Coding keys (GF-PRC), reducing the cost of storing large-scale information while preserving noise distribution and diversity for distortion-free watermarking. To enhance robustness, we further design a Segment Group-Ordering module (SGO) tailored to causal 3D VAEs, ensuring robust watermark inversion during extraction under temporal disturbance. Comprehensive experiments on modern diffusion models show that SIGMark achieves very high bit-accuracy during extraction under both temporal and spatial disturbances with minimal overhead, demonstrating its scalability and robustness. Our project is available at https://jeremyzhao1998.github.io/SIGMark-release/.

