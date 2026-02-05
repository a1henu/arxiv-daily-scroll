---
layout: default
title: Cross-Attention Transformer for Joint Multi-Receiver Uplink Neural Decoding
---

# Cross-Attention Transformer for Joint Multi-Receiver Uplink Neural Decoding
**arXiv**：[2602.04728v1](https://arxiv.org/abs/2602.04728) · [PDF](https://arxiv.org/pdf/2602.04728.pdf)  
**作者**：Xavier Tardy, Grégoire Lefebvre, Apostolos Kountouris, Haïfa Fares, Amor Nafkha  

**一句话要点**：提出跨注意力Transformer以联合解码多接收器上行OFDM信号，无需显式信道估计。

**关键词**：跨注意力Transformer, 多接收器联合解码, 上行OFDM信号, 神经网络解码, Wi-Fi接收器, 信道估计免依赖

## 3 点简述
- 核心问题：多接收器上行OFDM信号联合解码，传统方法依赖显式信道估计，在稀疏导频或链路退化时性能受限。
- 方法要点：使用共享编码器学习各接收器时频结构，跨注意力模块融合接收器信息，输出软对数似然比供标准信道解码器使用。
- 实验或效果：在真实Wi-Fi信道中，模型优于经典流程和卷积基线，匹配或超越完美信道知识基线，计算成本低、延迟小。

## 摘要（原文）

> We propose a cross-attention Transformer for joint decoding of uplink OFDM signals received by multiple coordinated access points. A shared per-receiver encoder learns time-frequency structure within each received grid, and a token-wise cross-attention module fuses the receivers to produce soft log-likelihood ratios for a standard channel decoder, without requiring explicit per-receiver channel estimates. Trained with a bit-metric objective, the model adapts its fusion to per-receiver reliability, tolerates missing or degraded links, and remains robust when pilots are sparse. Across realistic Wi-Fi channels, it consistently outperforms classical pipelines and strong convolutional baselines, frequently matching (and in some cases surpassing) a powerful baseline that assumes perfect channel knowledge per access point. Despite its expressiveness, the architecture is compact, has low computational cost (low GFLOPs), and achieves low latency on GPUs, making it a practical building block for next-generation Wi-Fi receivers.

