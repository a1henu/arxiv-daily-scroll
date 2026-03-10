---
layout: default
title: Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio
---

# Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio
**arXiv**：[2603.08683v1](https://arxiv.org/abs/2603.08683) · [PDF](https://arxiv.org/pdf/2603.08683.pdf)  
**作者**：Phillip Long, Zachary Novack, Chris Donahue  

**一句话要点**：提出Trilobyte字节级标记化方法，实现首个可处理的24位无损音频压缩基准测试。

**关键词**：无损音频压缩, 语言模型基准测试, 字节级标记化, 高比特深度音频, 自回归模型

## 3 点简述
- 核心问题：自回归语言模型用于无损音频压缩时，高比特深度（如16/24位）因词汇量过大而难以处理。
- 方法要点：引入Trilobyte字节级标记化，将词汇量从O(2^b)降至O(1)，支持全分辨率音频压缩。
- 实验或效果：在8/16位音频上超越FLAC，但24位压缩增益相对有限，提供多领域基准数据。

## 摘要（原文）

> Autoregressive "language" models (LMs) trained on raw waveforms can be repurposed for lossless audio compression, but prior work is limited to 8-bit audio, leaving open whether such approaches work for practical settings (16/24-bit) and can compete with existing codecs. We benchmark LM-based compression on full-fidelity audio across diverse domains (music, speech, bioacoustics), sampling rates (16kHz-48kHz), and bit depths (8, 16, 24-bit). Standard sample-level tokenization becomes intractable at higher bit depths due to vocabulary size (65K for 16-bit; 16.7M for 24-bit). We propose Trilobyte, a byte-level tokenization schema for full resolution audio, improving vocabulary scaling from $O(2^{b})$ to $O(1)$ and enabling the first tractable 24-bit LM-based lossless compression. While LMs consistently outperform FLAC and yield state-of-the-art compression at 8-bit and 16-bit, we observe that compression gains become more modest as bit depth increases beyond 8-bit.

