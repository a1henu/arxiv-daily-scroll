---
layout: default
title: CTC-TTS: LLM-based dual-streaming text-to-speech with CTC alignment
---

# CTC-TTS: LLM-based dual-streaming text-to-speech with CTC alignment
**arXiv**：[2602.19574v1](https://arxiv.org/abs/2602.19574) · [PDF](https://arxiv.org/pdf/2602.19574.pdf)  
**作者**：Hanwen Liu, Saierdaer Yusuyin, Hao Huang, Zhijian Ou  

**一句话要点**：提出CTC-TTS，基于CTC对齐和双词交织策略，实现低延迟双流语音合成。

**关键词**：语音合成, CTC对齐, 双流合成, 低延迟, LLM-TTS, 零样本学习

## 3 点简述
- 问题：现有LLM-TTS系统在低延迟双流合成中，依赖传统对齐工具和固定比例交织，导致灵活性差和性能受限。
- 方法：采用CTC对齐器替代MFA，引入双词交织策略，设计CTC-TTS-L和CTC-TTS-F变体以平衡质量与延迟。
- 效果：实验表明，CTC-TTS在流式合成和零样本任务上优于基线，提供高质量和低延迟选项。

## 摘要（原文）

> Large-language-model (LLM)-based text-to-speech (TTS) systems can generate natural speech, but most are not designed for low-latency dual-streaming synthesis. High-quality dual-streaming TTS depends on accurate text--speech alignment and well-designed training sequences that balance synthesis quality and latency. Prior work often relies on GMM-HMM based forced-alignment toolkits (e.g., MFA), which are pipeline-heavy and less flexible than neural aligners; fixed-ratio interleaving of text and speech tokens struggles to capture text--speech alignment regularities. We propose CTC-TTS, which replaces MFA with a CTC based aligner and introduces a bi-word based interleaving strategy. Two variants are designed: CTC-TTS-L (token concatenation along the sequence length) for higher quality and CTC-TTS-F (embedding stacking along the feature dimension) for lower latency. Experiments show that CTC-TTS outperforms fixed-ratio interleaving and MFA-based baselines on streaming synthesis and zero-shot tasks. Speech samples are available at https://ctctts.github.io/.

