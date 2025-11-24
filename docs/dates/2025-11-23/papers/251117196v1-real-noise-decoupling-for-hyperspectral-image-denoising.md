---
layout: default
title: Real Noise Decoupling for Hyperspectral Image Denoising
---

# Real Noise Decoupling for Hyperspectral Image Denoising
**arXiv**：[2511.17196v1](https://arxiv.org/abs/2511.17196) · [PDF](https://arxiv.org/pdf/2511.17196.pdf)  
**作者**：Yingkai Zhang, Tao Zhang, Jing Nie, Ying Fu  

**一句话要点**：提出多阶段噪声解耦框架以解决高光谱图像去噪中复杂噪声建模难题

**关键词**：高光谱图像去噪, 噪声解耦, 多阶段学习, 小波引导网络, 预训练策略

## 3 点简述
- 核心问题：真实高光谱图像噪声复杂，难以准确建模，限制去噪方法效果。
- 方法要点：将噪声分解为显式和隐式分量，利用预训练网络和高频小波引导网络分别处理。
- 实验或效果：在公开和自采集数据集上优于现有方法，显著提升图像质量。

## 摘要（原文）

> Hyperspectral image (HSI) denoising is a crucial step in enhancing the quality of HSIs. Noise modeling methods can fit noise distributions to generate synthetic HSIs to train denoising networks. However, the noise in captured HSIs is usually complex and difficult to model accurately, which significantly limits the effectiveness of these approaches. In this paper, we propose a multi-stage noise-decoupling framework that decomposes complex noise into explicitly modeled and implicitly modeled components. This decoupling reduces the complexity of noise and enhances the learnability of HSI denoising methods when applied to real paired data. Specifically, for explicitly modeled noise, we utilize an existing noise model to generate paired data for pre-training a denoising network, equipping it with prior knowledge to handle the explicitly modeled noise effectively. For implicitly modeled noise, we introduce a high-frequency wavelet guided network. Leveraging the prior knowledge from the pre-trained module, this network adaptively extracts high-frequency features to target and remove the implicitly modeled noise from real paired HSIs. Furthermore, to effectively eliminate all noise components and mitigate error accumulation across stages, a multi-stage learning strategy, comprising separate pre-training and joint fine-tuning, is employed to optimize the entire framework. Extensive experiments on public and our captured datasets demonstrate that our proposed framework outperforms state-of-the-art methods, effectively handling complex real-world noise and significantly enhancing HSI quality.

