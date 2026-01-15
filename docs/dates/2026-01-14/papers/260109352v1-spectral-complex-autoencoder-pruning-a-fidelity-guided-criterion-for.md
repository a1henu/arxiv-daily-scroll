---
layout: default
title: Spectral Complex Autoencoder Pruning: A Fidelity-Guided Criterion for Extreme Structured Channel Compression
---

# Spectral Complex Autoencoder Pruning: A Fidelity-Guided Criterion for Extreme Structured Channel Compression
**arXiv**：[2601.09352v1](https://arxiv.org/abs/2601.09352) · [PDF](https://arxiv.org/pdf/2601.09352.pdf)  
**作者**：Wei Liu, Xing Deng, Haijian Shao, Yingtao Jiang  

**一句话要点**：提出谱复自编码器剪枝，通过复交互场谱重构保真度指导极端结构化通道压缩。

**关键词**：通道剪枝, 谱重构, 复交互场, 结构化压缩, 自编码器, 神经网络压缩

## 3 点简述
- 核心问题：在卷积层中，如何有效衡量单个输出通道的功能冗余以实现极端压缩。
- 方法要点：构建复交互场，训练低容量自编码器重构归一化谱，以保真度评估通道可压缩性。
- 实验或效果：在VGG16/CIFAR-10上，实现90.11% FLOP和96.30%参数减少，精度下降1.67%。

## 摘要（原文）

> We propose Spectral Complex Autoencoder Pruning (SCAP), a reconstruction-based criterion that measures functional redundancy at the level of individual output channels. For each convolutional layer, we construct a complex interaction field by pairing the full multi-channel input activation as the real part with a single output-channel activation (spatially aligned and broadcast across input channels) as the imaginary part. We transform this complex field to the frequency domain and train a low-capacity autoencoder to reconstruct normalized spectra. Channels whose spectra are reconstructed with high fidelity are interpreted as lying close to a low-dimensional manifold captured by the autoencoder and are therefore more compressible; conversely, channels with low fidelity are retained as they encode information that cannot be compactly represented by the learned manifold. This yields an importance score (optionally fused with the filter L1 norm) that supports simple threshold-based pruning and produces a structurally consistent pruned network. On VGG16 trained on CIFAR-10, at a fixed threshold of 0.6, we obtain 90.11% FLOP reduction and 96.30% parameter reduction with an absolute Top-1 accuracy drop of 1.67% from a 93.44% baseline after fine-tuning, demonstrating that spectral reconstruction fidelity of complex interaction fields is an effective proxy for channel-level redundancy under aggressive compression.

