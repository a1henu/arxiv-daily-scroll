---
layout: default
title: REMAC: Reference-Based Martian Asymmetrical Image Compression
---

# REMAC: Reference-Based Martian Asymmetrical Image Compression
**arXiv**：[2601.18547v1](https://arxiv.org/abs/2601.18547) · [PDF](https://arxiv.org/pdf/2601.18547.pdf)  
**作者**：Qing Ding, Mai Xu, Shengxi Li, Xin Deng, Xin Zou  

**一句话要点**：提出REMAC参考型火星图像压缩方法，以降低编码器复杂度并提升压缩性能

**关键词**：火星图像压缩, 参考图像编码, 非对称计算, 熵模型优化, 多尺度解码器

## 3 点简述
- 针对火星图像压缩中编码器计算资源受限和未利用图像间相似性的问题
- 采用参考图像引导的熵模块和深度多尺度解码器，转移计算负担至解码器
- 实验显示编码器复杂度降低43.51%，BD-PSNR增益达0.2664 dB

## 摘要（原文）

> To expedite space exploration on Mars, it is indispensable to develop an efficient Martian image compression method for transmitting images through the constrained Mars-to-Earth communication channel. Although the existing learned compression methods have achieved promising results for natural images from earth, there remain two critical issues that hinder their effectiveness for Martian image compression: 1) They overlook the highly-limited computational resources on Mars; 2) They do not utilize the strong \textit{inter-image} similarities across Martian images to advance image compression performance. Motivated by our empirical analysis of the strong \textit{intra-} and \textit{inter-image} similarities from the perspective of texture, color, and semantics, we propose a reference-based Martian asymmetrical image compression (REMAC) approach, which shifts computational complexity from the encoder to the resource-rich decoder and simultaneously improves compression performance. To leverage \textit{inter-image} similarities, we propose a reference-guided entropy module and a ref-decoder that utilize useful information from reference images, reducing redundant operations at the encoder and achieving superior compression performance. To exploit \textit{intra-image} similarities, the ref-decoder adopts a deep, multi-scale architecture with enlarged receptive field size to model long-range spatial dependencies. Additionally, we develop a latent feature recycling mechanism to further alleviate the extreme computational constraints on Mars. Experimental results show that REMAC reduces encoder complexity by 43.51\% compared to the state-of-the-art method, while achieving a BD-PSNR gain of 0.2664 dB.

