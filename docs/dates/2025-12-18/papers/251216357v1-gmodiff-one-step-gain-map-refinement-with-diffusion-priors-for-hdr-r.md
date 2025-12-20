---
layout: default
title: GMODiff: One-Step Gain Map Refinement with Diffusion Priors for HDR Reconstruction
---

# GMODiff: One-Step Gain Map Refinement with Diffusion Priors for HDR Reconstruction
**arXiv**：[2512.16357v1](https://arxiv.org/abs/2512.16357) · [PDF](https://arxiv.org/pdf/2512.16357.pdf)  
**作者**：Tao Hu, Weiyu Zhou, Yanjie Tu, Peng Wu, Wei Dong, Qingsen Yan, Yanning Zhang  

**一句话要点**：提出GMODiff，通过增益图一步扩散框架解决多曝光HDR重建问题

**关键词**：高动态范围重建, 扩散模型, 增益图估计, 一步去噪, 多曝光图像处理, 感知质量优化

## 3 点简述
- 核心问题：预训练潜在扩散模型直接用于HDR重建存在动态范围受限、推理成本高和内容幻觉挑战
- 方法要点：将HDR重建重构为条件引导的增益图估计任务，从回归估计初始化实现一步去噪
- 实验或效果：在实验中表现优于多种先进方法，推理速度比基于LDM的方法快100倍

## 摘要（原文）

> Pre-trained Latent Diffusion Models (LDMs) have recently shown strong perceptual priors for low-level vision tasks, making them a promising direction for multi-exposure High Dynamic Range (HDR) reconstruction. However, directly applying LDMs to HDR remains challenging due to: (1) limited dynamic-range representation caused by 8-bit latent compression, (2) high inference cost from multi-step denoising, and (3) content hallucination inherent to generative nature. To address these challenges, we introduce GMODiff, a gain map-driven one-step diffusion framework for multi-exposure HDR reconstruction. Instead of reconstructing full HDR content, we reformulate HDR reconstruction as a conditionally guided Gain Map (GM) estimation task, where the GM encodes the extended dynamic range while retaining the same bit depth as LDR images. We initialize the denoising process from an informative regression-based estimate rather than pure noise, enabling the model to generate high-quality GMs in a single denoising step. Furthermore, recognizing that regression-based models excel in content fidelity while LDMs favor perceptual quality, we leverage regression priors to guide both the denoising process and latent decoding of the LDM, suppressing hallucinations while preserving structural accuracy. Extensive experiments demonstrate that our GMODiff performs favorably against several state-of-the-art methods and is 100 faster than previous LDM-based methods.

