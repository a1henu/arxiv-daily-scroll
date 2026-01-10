---
layout: default
title: WESR: Scaling and Evaluating Word-level Event-Speech Recognition
---

# WESR: Scaling and Evaluating Word-level Event-Speech Recognition
**arXiv**：[2601.04508v1](https://arxiv.org/abs/2601.04508) · [PDF](https://arxiv.org/pdf/2601.04508.pdf)  
**作者**：Chenchen Yang, Kexin Huang, Liwei Fan, Qian Tu, Botian Jiang, Dong Zhang, Linqi Yin, Shimin Li, Zhaoye Fei, Qinyuan Cheng, Xipeng Qiu  

**一句话要点**：提出WESR以解决非语言声音事件识别中的分类与评估挑战

**关键词**：声音事件识别, 评估基准, 语音处理, 非语言事件检测, 多模态学习

## 3 点简述
- 核心问题：现有方法在非语言声音事件识别中分类覆盖不足、时间粒度模糊且缺乏标准化评估框架。
- 方法要点：构建包含21类声音事件的精细分类法，区分离散与连续事件，并开发WESR-Bench评估集以分离ASR错误。
- 实验或效果：基于1700+小时语料训练模型，在事件检测上超越开源模型和商业API，同时保持ASR质量。

## 摘要（原文）

> Speech conveys not only linguistic information but also rich non-verbal vocal events such as laughing and crying. While semantic transcription is well-studied, the precise localization of non-verbal events remains a critical yet under-explored challenge. Current methods suffer from insufficient task definitions with limited category coverage and ambiguous temporal granularity. They also lack standardized evaluation frameworks, hindering the development of downstream applications. To bridge this gap, we first develop a refined taxonomy of 21 vocal events, with a new categorization into discrete (standalone) versus continuous (mixed with speech) types. Based on the refined taxonomy, we introduce WESR-Bench, an expert-annotated evaluation set (900+ utterances) with a novel position-aware protocol that disentangles ASR errors from event detection, enabling precise localization measurement for both discrete and continuous events. We also build a strong baseline by constructing a 1,700+ hour corpus, and train specialized models, surpassing both open-source audio-language models and commercial APIs while preserving ASR quality. We anticipate that WESR will serve as a foundational resource for future research in modeling rich, real-world auditory scenes.

