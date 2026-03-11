---
layout: default
title: Spectral-Structured Diffusion for Single-Image Rain Removal
---

# Spectral-Structured Diffusion for Single-Image Rain Removal
**arXiv**：[2603.09054v1](https://arxiv.org/abs/2603.09054) · [PDF](https://arxiv.org/pdf/2603.09054.pdf)  
**作者**：Yucheng Xing, Xin Wang  

**一句话要点**：提出SpectralDiff框架，通过谱结构扩散解决单幅图像去雨问题。

**关键词**：单幅图像去雨, 谱结构扩散, 全乘积U-Net, 卷积定理, 渐进去噪, 计算效率

## 3 点简述
- 雨纹具有方向性和频域集中性，传统空间域扩散模型未显式处理这些谱结构特征。
- SpectralDiff引入结构化谱扰动，引导渐进抑制多方向雨成分，并设计全乘积U-Net提升效率。
- 在合成和真实基准测试中，SpectralDiff在去雨性能、模型紧凑性和推理效率上表现优异。

## 摘要（原文）

> Rain streaks manifest as directional and frequency-concentrated structures that overlap across multiple scales, making single-image rain removal particularly challenging. While diffusion-based restoration models provide a powerful framework for progressive denoising, standard spatial-domain diffusion does not explicitly account for such structured spectral characteristics. We introduce SpectralDiff, a spectral-structured diffusion-based framework tailored for single-image rain removal. Rather than redefining the diffusion formulation, our method incorporates structured spectral perturbations to guide the progressive suppression of multi-directional rain components. To support this design, we further propose a full-product U-Net architecture that leverages the convolution theorem to replace convolution operations with element-wise product layers, improving computational efficiency while preserving modeling capacity. Extensive experiments on synthetic and real-world benchmarks demonstrate that SpectralDiff achieves competitive rain removal performance with improved model compactness and favorable inference efficiency compared to existing diffusion-based approaches.

