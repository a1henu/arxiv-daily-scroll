---
layout: default
title: CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space
---

# CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space
**arXiv**：[2603.02022v1](https://arxiv.org/abs/2603.02022) · [PDF](https://arxiv.org/pdf/2603.02022.pdf)  
**作者**：Bowen Zhang, Junchuan Zhao, Ian McLoughlin, Ye Wang, A S Madhukumar  

**一句话要点**：提出CodecFlow，通过条件流匹配在神经编解码器潜在空间实现高效语音带宽扩展

**关键词**：语音带宽扩展, 神经音频编解码器, 条件流匹配, 潜在空间重建, 残差向量量化

## 3 点简述
- 核心问题：现有方法计算成本高且高频保真度有限，神经编解码器潜在空间存在表示不匹配挑战。
- 方法要点：采用基于神经编解码器的框架，结合发声感知条件流转换器和结构约束残差向量量化器优化潜在对齐。
- 实验或效果：在8 kHz到16 kHz和44.1 kHz任务中实现强频谱保真度和增强感知质量。

## 摘要（原文）

> Speech Bandwidth Extension improves clarity and intelligibility by restoring/inferring appropriate high-frequency content for low-bandwidth speech. Existing methods often rely on spectrogram or waveform modeling, which can incur higher computational cost and have limited high-frequency fidelity. Neural audio codecs offer compact latent representations that better preserve acoustic detail, yet accurately recovering high-resolution latent information remains challenging due to representation mismatch. We present CodecFlow, a neural codec-based BWE framework that performs efficient speech reconstruction in a compact latent space. CodecFlow employs a voicing-aware conditional flow converter on continuous codec embeddings and a structure-constrained residual vector quantizer to improve latent alignment stability. Optimized end-to-end, CodecFlow achieves strong spectral fidelity and enhanced perceptual quality on 8 kHz to 16 kHz and 44.1 kHz speech BWE tasks.

