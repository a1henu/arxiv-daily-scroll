---
layout: default
title: SimuFreeMark: A Noise-Simulation-Free Robust Watermarking Against Image Editing
---

# SimuFreeMark: A Noise-Simulation-Free Robust Watermarking Against Image Editing
**arXiv**：[2511.11295v1](https://arxiv.org/abs/2511.11295) · [PDF](https://arxiv.org/pdf/2511.11295.pdf)  
**作者**：Yichao Tang, Mingyang Li, Di Miao, Sheng Li, Zhenxing Qian, Xinpeng Zhang  

**一句话要点**：提出SimuFreeMark框架，利用图像低频稳定性实现免噪声模拟的鲁棒水印。

**关键词**：图像水印, 鲁棒性, 低频组件, 变分自编码器, 免噪声模拟, 语义攻击

## 3 点简述
- 核心问题：现有水印方法依赖噪声模拟训练，泛化性受限，难以应对未知攻击。
- 方法要点：基于图像低频组件鲁棒性，在特征空间嵌入水印，使用预训练VAE绑定稳定表示。
- 实验或效果：在多种攻击下优于现有方法，保持高视觉质量，无需噪声模拟训练。

## 摘要（原文）

> The advancement of artificial intelligence generated content (AIGC) has created a pressing need for robust image watermarking that can withstand both conventional signal processing and novel semantic editing attacks. Current deep learning-based methods rely on training with hand-crafted noise simulation layers, which inherently limit their generalization to unforeseen distortions. In this work, we propose $\textbf{SimuFreeMark}$, a noise-$\underline{\text{simu}}$lation-$\underline{\text{free}}$ water$\underline{\text{mark}}$ing framework that circumvents this limitation by exploiting the inherent stability of image low-frequency components. We first systematically establish that low-frequency components exhibit significant robustness against a wide range of attacks. Building on this foundation, SimuFreeMark embeds watermarks directly into the deep feature space of the low-frequency components, leveraging a pre-trained variational autoencoder (VAE) to bind the watermark with structurally stable image representations. This design completely eliminates the need for noise simulation during training. Extensive experiments demonstrate that SimuFreeMark outperforms state-of-the-art methods across a wide range of conventional and semantic attacks, while maintaining superior visual quality.

