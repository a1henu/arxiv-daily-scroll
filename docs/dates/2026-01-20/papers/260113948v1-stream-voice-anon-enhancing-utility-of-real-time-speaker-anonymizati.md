---
layout: default
title: Stream-Voice-Anon: Enhancing Utility of Real-Time Speaker Anonymization via Neural Audio Codec and Language Models
---

# Stream-Voice-Anon: Enhancing Utility of Real-Time Speaker Anonymization via Neural Audio Codec and Language Models
**arXiv**：[2601.13948v1](https://arxiv.org/abs/2601.13948) · [PDF](https://arxiv.org/pdf/2601.13948.pdf)  
**作者**：Nikita Kuzmin, Songting Liu, Kong Aik Lee, Eng Siong Chng  

**一句话要点**：提出Stream-Voice-Anon，通过神经音频编解码器和因果语言模型增强实时说话人匿名化的实用性

**关键词**：实时说话人匿名化, 神经音频编解码器, 因果语言模型, 隐私保护, 语音处理

## 3 点简述
- 核心问题：在线语音应用中实时说话人匿名化研究不足，现有方法缺乏隐私保护技术
- 方法要点：基于因果语言模型的神经音频编解码器架构，集成伪说话人表示采样和说话人嵌入混合策略
- 实验或效果：在VoicePrivacy 2024协议下，相比DarkStream显著提升可懂度和情感保留，延迟相近

## 摘要（原文）

> Protecting speaker identity is crucial for online voice applications, yet streaming speaker anonymization (SA) remains underexplored. Recent research has demonstrated that neural audio codec (NAC) provides superior speaker feature disentanglement and linguistic fidelity. NAC can also be used with causal language models (LM) to enhance linguistic fidelity and prompt control for streaming tasks. However, existing NAC-based online LM systems are designed for voice conversion (VC) rather than anonymization, lacking the techniques required for privacy protection. Building on these advances, we present Stream-Voice-Anon, which adapts modern causal LM-based NAC architectures specifically for streaming SA by integrating anonymization techniques. Our anonymization approach incorporates pseudo-speaker representation sampling, a speaker embedding mixing and diverse prompt selection strategies for LM conditioning that leverage the disentanglement properties of quantized content codes to prevent speaker information leakage. Additionally, we compare dynamic and fixed delay configurations to explore latency-privacy trade-offs in real-time scenarios. Under the VoicePrivacy 2024 Challenge protocol, Stream-Voice-Anon achieves substantial improvements in intelligibility (up to 46% relative WER reduction) and emotion preservation (up to 28% UAR relative) compared to the previous state-of-the-art streaming method DarkStream while maintaining comparable latency (180ms vs 200ms) and privacy protection against lazy-informed attackers, though showing 15% relative degradation against semi-informed attackers.

