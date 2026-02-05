---
layout: default
title: X2HDR: HDR Image Generation in a Perceptually Uniform Space
---

# X2HDR: HDR Image Generation in a Perceptually Uniform Space
**arXiv**：[2602.04814v1](https://arxiv.org/abs/2602.04814) · [PDF](https://arxiv.org/pdf/2602.04814.pdf)  
**作者**：Ronghuan Wu, Wanchao Su, Kede Ma, Jing Liao, Rafał K. Mantiuk  

**一句话要点**：提出在感知均匀空间中适配扩散模型以生成HDR图像，无需从头训练。

**关键词**：高动态范围图像生成, 感知均匀编码, 扩散模型适配, 文本到HDR合成, RAW到HDR重建

## 3 点简述
- 核心问题：现有扩散模型因缺乏大规模HDR训练数据，输出限于LDR，HDR与LDR图像统计差异大。
- 方法要点：将HDR输入转换为感知均匀编码（如PU21），冻结VAE，仅微调去噪器，适配扩散模型。
- 实验或效果：适配方法提升感知保真度、文本-图像对齐和有效动态范围，支持文本到HDR和RAW到HDR任务。

## 摘要（原文）

> High-dynamic-range (HDR) formats and displays are becoming increasingly prevalent, yet state-of-the-art image generators (e.g., Stable Diffusion and FLUX) typically remain limited to low-dynamic-range (LDR) output due to the lack of large-scale HDR training data. In this work, we show that existing pretrained diffusion models can be easily adapted to HDR generation without retraining from scratch. A key challenge is that HDR images are natively represented in linear RGB, whose intensity and color statistics differ substantially from those of sRGB-encoded LDR images. This gap, however, can be effectively bridged by converting HDR inputs into perceptually uniform encodings (e.g., using PU21 or PQ). Empirically, we find that LDR-pretrained variational autoencoders (VAEs) reconstruct PU21-encoded HDR inputs with fidelity comparable to LDR data, whereas linear RGB inputs cause severe degradations. Motivated by this finding, we describe an efficient adaptation strategy that freezes the VAE and finetunes only the denoiser via low-rank adaptation in a perceptually uniform space. This results in a unified computational method that supports both text-to-HDR synthesis and single-image RAW-to-HDR reconstruction. Experiments demonstrate that our perceptually encoded adaptation consistently improves perceptual fidelity, text-image alignment, and effective dynamic range, relative to previous techniques.

