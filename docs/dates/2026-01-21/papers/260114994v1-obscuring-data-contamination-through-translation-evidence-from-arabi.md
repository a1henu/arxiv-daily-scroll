---
layout: default
title: Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora
---

# Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora
**arXiv**：[2601.14994v1](https://arxiv.org/abs/2601.14994) · [PDF](https://arxiv.org/pdf/2601.14994.pdf)  
**作者**：Chaymaa Abbas, Nour Shamaa, Mariette Awad  

**一句话要点**：提出翻译感知污染检测方法，以解决多语言大语言模型评估中的数据污染问题。

**关键词**：数据污染检测, 多语言评估, 翻译感知方法, 大语言模型, 阿拉伯语数据集

## 3 点简述
- 核心问题：数据污染在多语言环境中被翻译掩盖，影响大语言模型评估的有效性。
- 方法要点：扩展测试槽猜测方法，结合Min-K%概率分析，开发翻译感知污染检测。
- 实验或效果：在阿拉伯语数据集上微调模型，显示翻译能抑制污染指标，但模型仍受益于污染数据。

## 摘要（原文）

> Data contamination undermines the validity of Large Language Model evaluation by enabling models to rely on memorized benchmark content rather than true generalization. While prior work has proposed contamination detection methods, these approaches are largely limited to English benchmarks, leaving multilingual contamination poorly understood. In this work, we investigate contamination dynamics in multilingual settings by fine-tuning several open-weight LLMs on varying proportions of Arabic datasets and evaluating them on original English benchmarks. To detect memorization, we extend the Tested Slot Guessing method with a choice-reordering strategy and incorporate Min-K% probability analysis, capturing both behavioral and distributional contamination signals.
>   Our results show that translation into Arabic suppresses conventional contamination indicators, yet models still benefit from exposure to contaminated data, particularly those with stronger Arabic capabilities. This effect is consistently reflected in rising Mink% scores and increased cross-lingual answer consistency as contamination levels grow. To address this blind spot, we propose Translation-Aware Contamination Detection, which identifies contamination by comparing signals across multiple translated benchmark variants rather than English alone. The Translation-Aware Contamination Detection reliably exposes contamination even when English-only methods fail. Together, our findings highlight the need for multilingual, translation-aware evaluation pipelines to ensure fair, transparent, and reproducible assessment of LLMs.

