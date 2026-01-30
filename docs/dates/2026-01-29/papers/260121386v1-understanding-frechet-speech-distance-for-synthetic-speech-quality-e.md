---
layout: default
title: Understanding Frechet Speech Distance for Synthetic Speech Quality Evaluation
---

# Understanding Frechet Speech Distance for Synthetic Speech Quality Evaluation
**arXiv**：[2601.21386v1](https://arxiv.org/abs/2601.21386) · [PDF](https://arxiv.org/pdf/2601.21386.pdf)  
**作者**：June-Woo Kim, Dhruv Agarwal, Federica Cerina  

**一句话要点**：评估Fréchet语音距离在合成语音质量评估中的可靠性，提出基于WavLM特征的稳定度量方法。

**关键词**：合成语音评估, Fréchet距离, 客观度量, 语音质量, WavLM特征, 人类听测验证

## 3 点简述
- 核心问题：合成语音质量客观评估困难，依赖昂贵的人工听测，需可靠替代指标。
- 方法要点：全面评估Fréchet语音距离及其变体在不同嵌入和条件下的表现，结合人类听测验证。
- 实验或效果：WavLM Base+特征与人类评分最稳定对齐，指标可作为成本效益高的补充评估工具。

## 摘要（原文）

> Objective evaluation of synthetic speech quality remains a critical challenge. Human listening tests are the gold standard, but costly and impractical at scale. Fréchet Distance has emerged as a promising alternative, yet its reliability depends heavily on the choice of embeddings and experimental settings. In this work, we comprehensively evaluate Fréchet Speech Distance (FSD) and its variant Speech Maximum Mean Discrepancy (SMMD) under varied embeddings and conditions. We further incorporate human listening evaluations alongside TTS intelligibility and synthetic-trained ASR WER to validate the perceptual relevance of these metrics. Our findings show that WavLM Base+ features yield the most stable alignment with human ratings. While FSD and SMMD cannot fully replace subjective evaluation, we show that they can serve as complementary, cost-efficient, and reproducible measures, particularly useful when large-scale or direct listening assessments are infeasible. Code is available at https://github.com/kaen2891/FrechetSpeechDistance.

