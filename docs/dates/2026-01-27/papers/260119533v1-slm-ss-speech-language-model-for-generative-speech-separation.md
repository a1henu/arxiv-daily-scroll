---
layout: default
title: SLM-SS: Speech Language Model for Generative Speech Separation
---

# SLM-SS: Speech Language Model for Generative Speech Separation
**arXiv**：[2601.19533v1](https://arxiv.org/abs/2601.19533) · [PDF](https://arxiv.org/pdf/2601.19533.pdf)  
**作者**：Tianhua Li, Chenda Li, Wei Wang, Xin Zhou, Xihui Chen, Jianqing Gao, Yanmin Qian  

**一句话要点**：提出SLM-SS，应用语音语言模型于语音分离以提升分离信号的可懂度与连贯性。

**关键词**：语音分离, 语音语言模型, 序列生成, 可懂度提升, 编码器-解码器模型

## 3 点简述
- 核心问题：传统语音分离方法在信号级指标上表现良好，但分离信号的可懂度不足，影响下游任务性能。
- 方法要点：将语音分离建模为离散多码本序列生成，使用编码器-解码器模型，结合自回归与非自回归策略提升效率。
- 实验或效果：在LibriMix数据集上验证，显著提升语音可懂度，改善下游任务的语言一致性。

## 摘要（原文）

> Speech separation (SS) has advanced significantly with neural network-based methods, showing improved performance on signal-level metrics. However, these methods often struggle to maintain speech intelligibility in the separated signals, which can negatively affect the performance of downstream tasks such as speech recognition. In this work, we propose SLM-SS, a novel approach that applies speech language models to SS, aiming to enhance the intelligibility and coherence of the separated signals. We frame SS as discrete multi-codebook sequence generation, using Encoder-Decoder models to map quantized speech mixtures to target tokens. In addition to the autoregressive modeling strategy, we introduce a non-autoregressive model to improve decoding efficiency for residual tokens. Experimental results on the LibriMix dataset demonstrate that our approach shows significantly better preservation of speech intelligibility, leading to improved linguistic consistency in a variety of downstream tasks compared to existing approaches.

