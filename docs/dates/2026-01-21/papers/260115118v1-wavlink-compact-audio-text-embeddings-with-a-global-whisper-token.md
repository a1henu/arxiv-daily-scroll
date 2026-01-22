---
layout: default
title: WavLink: Compact Audio--Text Embeddings with a Global Whisper Token
---

# WavLink: Compact Audio--Text Embeddings with a Global Whisper Token
**arXiv**：[2601.15118v1](https://arxiv.org/abs/2601.15118) · [PDF](https://arxiv.org/pdf/2601.15118.pdf)  
**作者**：Gokul Karthik Kumar, Ludovick Lepauloux, Hakim Hacid  

**一句话要点**：提出WavLink，通过可学习全局令牌增强Whisper编码器，实现紧凑音频-文本嵌入模型。

**关键词**：音频-文本嵌入, Whisper编码器, 全局令牌, 两阶段训练, Matryoshka监督, 检索性能

## 3 点简述
- 核心问题：现有音频-文本嵌入模型未有效利用Whisper编码器，导致特征表示效率不足。
- 方法要点：结合可学习全局令牌与文本编码器，进行两阶段训练和Matryoshka监督，优化设计选择。
- 实验或效果：在检索任务中达到先进性能，嵌入尺寸可缩小8倍且性能下降最小，在AIR-Bench上表现竞争性。

## 摘要（原文）

> Whisper has become the de-facto encoder for extracting general-purpose audio features in large audio-language models, where a 30-second clip is typically represented by 1500 frame features projected into an LLM. In contrast, audio-text embedding models like CLAP-based models have largely relied on alternative audio encoders (e.g., HTS-AT, PaSST), and have not leveraged Whisper effectively. We present WavLink, a compact audio-text embedding model that augments Whisper encoder with a learnable global token, trained jointly with a text encoder. Through a systematic study of design choices, including pretrained text encoders, loss functions, training modes, and data mixtures, we identify configurations that yield state-of-the-art retrieval performance. Our two-stage training recipe across three model sizes, combined with Matryoshka-style supervision, improves scalability, enabling 8x smaller embeddings with minimal performance drop. WavLink also demonstrates competitive performance on AIR-Bench with MCQs and zero-shot classification.

