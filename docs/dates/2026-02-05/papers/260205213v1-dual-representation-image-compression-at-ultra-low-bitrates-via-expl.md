---
layout: default
title: Dual-Representation Image Compression at Ultra-Low Bitrates via Explicit Semantics and Implicit Textures
---

# Dual-Representation Image Compression at Ultra-Low Bitrates via Explicit Semantics and Implicit Textures
**arXiv**：[2602.05213v1](https://arxiv.org/abs/2602.05213) · [PDF](https://arxiv.org/pdf/2602.05213.pdf)  
**作者**：Chuqin Zhou, Xiaoyue Ling, Yunuo Chen, Jincheng Dai, Guo Lu, Wenjun Zhang  

**一句话要点**：提出双表示图像压缩框架，在超低码率下通过显式语义与隐式纹理提升感知质量。

**关键词**：图像压缩, 超低码率, 生成压缩, 显式语义, 隐式纹理, 扩散模型

## 3 点简述
- 核心问题：现有生成压缩方法在超低码率下存在语义保真度与感知真实性的权衡限制。
- 方法要点：训练无关地整合显式高层语义与隐式细粒度纹理，利用扩散模型和反向信道编码。
- 实验或效果：在多个数据集上实现最优率-感知性能，DISTS BD-Rate显著超越DiffC等现有方法。

## 摘要（原文）

> While recent neural codecs achieve strong performance at low bitrates when optimized for perceptual quality, their effectiveness deteriorates significantly under ultra-low bitrate conditions. To mitigate this, generative compression methods leveraging semantic priors from pretrained models have emerged as a promising paradigm. However, existing approaches are fundamentally constrained by a tradeoff between semantic faithfulness and perceptual realism. Methods based on explicit representations preserve content structure but often lack fine-grained textures, whereas implicit methods can synthesize visually plausible details at the cost of semantic drift. In this work, we propose a unified framework that bridges this gap by coherently integrating explicit and implicit representations in a training-free manner. Specifically, We condition a diffusion model on explicit high-level semantics while employing reverse-channel coding to implicitly convey fine-grained details. Moreover, we introduce a plug-in encoder that enables flexible control of the distortion-perception tradeoff by modulating the implicit information. Extensive experiments demonstrate that the proposed framework achieves state-of-the-art rate-perception performance, outperforming existing methods and surpassing DiffC by 29.92%, 19.33%, and 20.89% in DISTS BD-Rate on the Kodak, DIV2K, and CLIC2020 datasets, respectively.

