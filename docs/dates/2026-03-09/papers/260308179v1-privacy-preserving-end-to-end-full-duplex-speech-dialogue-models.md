---
layout: default
title: Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models
---

# Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models
**arXiv**：[2603.08179v1](https://arxiv.org/abs/2603.08179) · [PDF](https://arxiv.org/pdf/2603.08179.pdf)  
**作者**：Nikita Kuzmin, Tao Zhong, Jiajun Deng, Yingke Zhu, Tristan Tsoi, Tianxiang Cao, Simon Lui, Kong Aik Lee, Eng Siong Chng  

**一句话要点**：提出流式匿名化方法以保护端到端全双工语音对话模型中的说话人隐私

**关键词**：端到端语音对话, 说话人隐私保护, 流式匿名化, 全双工模型, 身份泄露分析

## 3 点简述
- 核心问题：端到端全双工语音模型的隐藏状态泄露说话人身份，隐私风险未受评估
- 方法要点：基于Stream-Voice-Anon设计波形级和特征域流式匿名化方案，降低身份泄露
- 实验或效果：特征域方案将等错误率提升超3.5倍，接近随机水平，波形方案保持高语义相似度

## 摘要（原文）

> End-to-end full-duplex speech models feed user audio through an always-on LLM backbone, yet the speaker privacy implications of their hidden representations remain unexamined. Following the VoicePrivacy 2024 protocol with a lazy-informed attacker, we show that the hidden states of SALM-Duplex and Moshi leak substantial speaker identity across all transformer layers. Layer-wise and turn-wise analyses reveal that leakage persists across all layers, with SALM-Duplex showing stronger leakage in early layers while Moshi leaks uniformly, and that Linkability rises sharply within the first few turns. We propose two streaming anonymization setups using Stream-Voice-Anon: a waveform-level front-end (Anon-W2W) and a feature-domain replacement (Anon-W2F). Anon-W2F raises EER by over 3.5x relative to the discrete encoder baseline (11.2% to 41.0%), approaching the 50% random-chance ceiling, while Anon-W2W retains 78-93% of baseline sBERT across setups with sub-second response latency (FRL under 0.8 s).

