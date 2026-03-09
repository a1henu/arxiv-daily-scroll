---
layout: default
title: Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec
---

# Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec
**arXiv**：[2603.05887v1](https://arxiv.org/abs/2603.05887) · [PDF](https://arxiv.org/pdf/2603.05887.pdf)  
**作者**：Junhyeok Lee, Xiluo He, Jihwan Lee, Helin Wang, Shrikanth Narayanan, Thomas Thebaud, Laureano Moro-Velazquez, Jesús Villalba, Najim Dehak  

**一句话要点**：提出自监督表示重建损失以提升流式神经音频编解码器的可懂度和低延迟

**关键词**：神经音频编解码, 自监督学习, 表示重建, 流式处理, 低延迟, 可懂度提升

## 3 点简述
- 问题：基于梅尔谱图重建的神经音频编解码器常导致可懂度下降
- 方法：引入自监督表示重建损失，从编解码器输出重建蒸馏的自监督表示
- 效果：加速训练收敛，实现零前瞻流式架构，在单GPU上达到先进性能

## 摘要（原文）

> Neural audio codecs optimized for mel-spectrogram reconstruction often fail to preserve intelligibility. While semantic encoder distillation improves encoded representations, it does not guarantee content preservation in reconstructed speech. In this work, we demonstrate that self-supervised representation reconstruction (SSRR) loss fundamentally improves codec training and performance. First, SSRR significantly accelerates convergence, enabling competitive results using only a single GPU. Second, it enhances intelligibility by reconstructing distilled self-supervised representations from codec outputs. Third, SSRR enables high intelligibility without additional lookahead in streaming Transformer-based codecs, allowing a zero-lookahead architecture for real-time deployment. As a result, our JHCodec achieves state-of-the-art performance while maintaining minimal latency and reduced training cost. We open-source the full implementation, training pipeline, and demo on Github https://github.com/jhcodec843/jhcodec.

