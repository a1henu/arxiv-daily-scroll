---
layout: default
title: NFCDS: A Plug-and-Play Noise Frequency-Controlled Diffusion Sampling Strategy for Image Restoration
---

# NFCDS: A Plug-and-Play Noise Frequency-Controlled Diffusion Sampling Strategy for Image Restoration
**arXiv**：[2601.21248v1](https://arxiv.org/abs/2601.21248) · [PDF](https://arxiv.org/pdf/2601.21248.pdf)  
**作者**：Zhen Wang, Hongyi Liu, Jianing Li, Zhihui Wei  

**一句话要点**：提出噪声频率控制扩散采样策略，以提升基于扩散的零样本图像恢复的保真度与感知质量平衡。

**关键词**：图像恢复, 扩散模型, 噪声控制, 傅里叶分析, 即插即用方法, 零样本学习

## 3 点简述
- 核心问题：扩散采样中的噪声引入导致图像保真度下降，与感知质量存在冲突。
- 方法要点：通过傅里叶域滤波器渐进抑制低频噪声并保留高频噪声，直接注入数据一致性先验。
- 实验或效果：作为即插即用模块，在多种零样本任务中改善保真度-感知平衡，无需额外训练。

## 摘要（原文）

> Diffusion sampling-based Plug-and-Play (PnP) methods produce images with high perceptual quality but often suffer from reduced data fidelity, primarily due to the noise introduced during reverse diffusion. To address this trade-off, we propose Noise Frequency-Controlled Diffusion Sampling (NFCDS), a spectral modulation mechanism for reverse diffusion noise. We show that the fidelity-perception conflict can be fundamentally understood through noise frequency: low-frequency components induce blur and degrade fidelity, while high-frequency components drive detail generation. Based on this insight, we design a Fourier-domain filter that progressively suppresses low-frequency noise and preserves high-frequency content. This controlled refinement injects a data-consistency prior directly into sampling, enabling fast convergence to results that are both high-fidelity and perceptually convincing--without additional training. As a PnP module, NFCDS seamlessly integrates into existing diffusion-based restoration frameworks and improves the fidelity-perception balance across diverse zero-shot tasks.

