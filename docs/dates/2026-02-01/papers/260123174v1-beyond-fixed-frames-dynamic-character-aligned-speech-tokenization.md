---
layout: default
title: Beyond Fixed Frames: Dynamic Character-Aligned Speech Tokenization
---

# Beyond Fixed Frames: Dynamic Character-Aligned Speech Tokenization
**arXiv**：[2601.23174v1](https://arxiv.org/abs/2601.23174) · [PDF](https://arxiv.org/pdf/2601.23174.pdf)  
**作者**：Luca Della Libera, Cem Subakan, Mirco Ravanelli  

**一句话要点**：提出DyCAST动态字符对齐语音分词器，以解决固定帧率音频编解码器生成过长序列的问题。

**关键词**：动态语音分词, 字符对齐, 可变帧率编解码, 检索增强解码, 语音重合成

## 3 点简述
- 核心问题：现有神经音频编解码器使用固定帧率，导致语音序列过长且效率低下。
- 方法要点：通过软字符级对齐和显式时长建模，实现可变帧率分词，支持对齐无关推理。
- 实验或效果：在低帧率下保持竞争性语音重合成质量，显著减少令牌使用量。

## 摘要（原文）

> Neural audio codecs are at the core of modern conversational speech technologies, converting continuous speech into sequences of discrete tokens that can be processed by LLMs. However, existing codecs typically operate at fixed frame rates, allocating tokens uniformly in time and producing unnecessarily long sequences. In this work, we introduce DyCAST, a Dynamic Character-Aligned Speech Tokenizer that enables variable-frame-rate tokenization through soft character-level alignment and explicit duration modeling. DyCAST learns to associate tokens with character-level linguistic units during training and supports alignment-free inference with direct control over token durations at decoding time. To improve speech resynthesis quality at low frame rates, we further introduce a retrieval-augmented decoding mechanism that enhances reconstruction fidelity without increasing bitrate. Experiments show that DyCAST achieves competitive speech resynthesis quality and downstream performance while using significantly fewer tokens than fixed-frame-rate codecs.

