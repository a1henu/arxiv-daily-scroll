---
layout: default
title: DeMark: A Query-Free Black-Box Attack on Deepfake Watermarking Defenses
---

# DeMark: A Query-Free Black-Box Attack on Deepfake Watermarking Defenses
**arXiv**：[2601.16473v1](https://arxiv.org/abs/2601.16473) · [PDF](https://arxiv.org/pdf/2601.16473.pdf)  
**作者**：Wei Song, Zhenchang Xing, Liming Zhu, Yulei Sui, Jingling Xue  

**一句话要点**：提出DeMark，一种无需查询的黑盒攻击框架，针对深度伪造防御水印方案进行攻击。

**关键词**：深度伪造防御, 黑盒攻击, 水印移除, 潜在空间漏洞, 压缩感知

## 3 点简述
- 核心问题：防御水印在深度伪造图像中易被移除，挑战其固有抗性假设。
- 方法要点：基于压缩感知的稀疏化过程，利用编码器-解码器水印模型的潜在空间漏洞。
- 实验或效果：在八种先进水印方案上，平均将检测准确率从100%降至32.9%，保持视觉质量。

## 摘要（原文）

> The rapid proliferation of realistic deepfakes has raised urgent concerns over their misuse, motivating the use of defensive watermarks in synthetic images for reliable detection and provenance tracking. However, this defense paradigm assumes such watermarks are inherently resistant to removal. We challenge this assumption with DeMark, a query-free black-box attack framework that targets defensive image watermarking schemes for deepfakes. DeMark exploits latent-space vulnerabilities in encoder-decoder watermarking models through a compressive sensing based sparsification process, suppressing watermark signals while preserving perceptual and structural realism appropriate for deepfakes. Across eight state-of-the-art watermarking schemes, DeMark reduces watermark detection accuracy from 100% to 32.9% on average while maintaining natural visual quality, outperforming existing attacks. We further evaluate three defense strategies, including image super resolution, sparse watermarking, and adversarial training, and find them largely ineffective. These results demonstrate that current encoder decoder watermarking schemes remain vulnerable to latent-space manipulations, underscoring the need for more robust watermarking methods to safeguard against deepfakes.

