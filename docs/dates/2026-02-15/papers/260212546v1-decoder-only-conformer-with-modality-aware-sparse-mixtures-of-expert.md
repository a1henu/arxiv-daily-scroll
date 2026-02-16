---
layout: default
title: Decoder-only Conformer with Modality-aware Sparse Mixtures of Experts for ASR
---

# Decoder-only Conformer with Modality-aware Sparse Mixtures of Experts for ASR
**arXiv**：[2602.12546v1](https://arxiv.org/abs/2602.12546) · [PDF](https://arxiv.org/pdf/2602.12546.pdf)  
**作者**：Jaeyoung Lee, Masato Mimura  

**一句话要点**：提出仅解码器Conformer结合模态感知稀疏专家混合，用于自动语音识别，无需外部编码器或大语言模型。

**关键词**：自动语音识别, 仅解码器架构, 稀疏专家混合, 模态感知路由, 混合因果注意力

## 3 点简述
- 核心问题：传统ASR模型依赖外部语音编码器或预训练大语言模型，增加复杂性和计算成本。
- 方法要点：使用模态感知稀疏专家混合，为语音和文本分配独立专家池，结合混合因果Conformer块进行单栈处理。
- 实验或效果：在Librispeech和Common Voice数据集上，以更少参数超越强基线，提升识别准确率。

## 摘要（原文）

> We present a decoder-only Conformer for automatic speech recognition (ASR) that processes speech and text in a single stack without external speech encoders or pretrained large language models (LLM). The model uses a modality-aware sparse mixture of experts (MoE): disjoint expert pools for speech and text with hard routing and top-1 selection, embedded in hybrid-causality Conformer blocks (bidirectional for speech, causal for text). Training combines CTC on speech positions with label-smoothed cross-entropy for text generation. Our 113M-parameter model consistently improves WER over a 139M AED baseline on Librispeech (2.8% vs. 3.2% test-clean; 5.6% vs. 6.0% test-other). On Common Voice 16.1 with a single multilingual model across five languages, our approach reduces average WER from 12.2% to 10.6%. To our knowledge, this is the first randomly initialized decoder-only ASR that surpasses strong AED baselines via modality-aware routing and sparse MoE, achieving better accuracy with fewer active parameters and without alignment/adaptation modules.

