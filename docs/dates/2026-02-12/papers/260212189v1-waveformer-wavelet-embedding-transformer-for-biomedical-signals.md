---
layout: default
title: WaveFormer: Wavelet Embedding Transformer for Biomedical Signals
---

# WaveFormer: Wavelet Embedding Transformer for Biomedical Signals
**arXiv**：[2602.12189v1](https://arxiv.org/abs/2602.12189) · [PDF](https://arxiv.org/pdf/2602.12189.pdf)  
**作者**：Habib Irani, Bikram De, Vangelis Metsis  

**一句话要点**：提出WaveFormer，通过小波嵌入和动态位置编码解决生物医学信号分类中长序列和多尺度频率模式捕获问题。

**关键词**：生物医学信号分类, 小波变换, Transformer架构, 动态位置编码, 多尺度频率模式, 时间序列分析

## 3 点简述
- 生物医学信号分类面临长序列、复杂时域动态和多尺度频率模式挑战，标准Transformer难以有效处理。
- WaveFormer在嵌入构建和位置编码阶段集成离散小波变换，提取频率特征并适应信号特定时域结构。
- 在八个数据集上评估，涵盖人类活动识别和脑信号分析，WaveFormer通过频率感知处理实现竞争性能。

## 摘要（原文）

> Biomedical signal classification presents unique challenges due to long sequences, complex temporal dynamics, and multi-scale frequency patterns that are poorly captured by standard transformer architectures. We propose WaveFormer, a transformer architecture that integrates wavelet decomposition at two critical stages: embedding construction, where multi-channel Discrete Wavelet Transform (DWT) extracts frequency features to create tokens containing both time-domain and frequency-domain information, and positional encoding, where Dynamic Wavelet Positional Encoding (DyWPE) adapts position embeddings to signal-specific temporal structure through mono-channel DWT analysis. We evaluate WaveFormer on eight diverse datasets spanning human activity recognition and brain signal analysis, with sequence lengths ranging from 50 to 3000 timesteps and channel counts from 1 to 144. Experimental results demonstrate that WaveFormer achieves competitive performance through comprehensive frequency-aware processing. Our approach provides a principled framework for incorporating frequency-domain knowledge into transformer-based time series classification.

