---
layout: default
title: Understanding Frechet Speech Distance for Synthetic Speech Quality Evaluation
---

# Understanding Frechet Speech Distance for Synthetic Speech Quality Evaluation
**arXiv**：[2601.21386v1](https://arxiv.org/abs/2601.21386) · [PDF](https://arxiv.org/pdf/2601.21386.pdf)  
**作者**：June-Woo Kim, Dhruv Agarwal, Federica Cerina  

**一句话要点**：评估Fréchet语音距离在合成语音质量评估中的可靠性，提出WavLM Base+特征作为稳定指标

**关键词**：合成语音评估, Fréchet距离, WavLM特征, 客观指标, 人类听力测试, 语音质量

## 3 点简述
- 核心问题：合成语音质量客观评估困难，依赖昂贵的人类听力测试，Fréchet距离可靠性受嵌入和设置影响
- 方法要点：全面评估Fréchet语音距离及其变体SMMD，结合人类听力测试、TTS可懂度和ASR WER验证感知相关性
- 实验或效果：WavLM Base+特征与人类评分最稳定对齐，FSD和SMMD可作为补充性、成本效益高的评估指标

## 摘要（原文）

> Objective evaluation of synthetic speech quality remains a critical challenge. Human listening tests are the gold standard, but costly and impractical at scale. Fréchet Distance has emerged as a promising alternative, yet its reliability depends heavily on the choice of embeddings and experimental settings. In this work, we comprehensively evaluate Fréchet Speech Distance (FSD) and its variant Speech Maximum Mean Discrepancy (SMMD) under varied embeddings and conditions. We further incorporate human listening evaluations alongside TTS intelligibility and synthetic-trained ASR WER to validate the perceptual relevance of these metrics. Our findings show that WavLM Base+ features yield the most stable alignment with human ratings. While FSD and SMMD cannot fully replace subjective evaluation, we show that they can serve as complementary, cost-efficient, and reproducible measures, particularly useful when large-scale or direct listening assessments are infeasible. Code is available at https://github.com/kaen2891/FrechetSpeechDistance.

