---
layout: default
title: A Comprehensive Benchmark of Language Models on Unicode and Romanized Sinhala
---

# A Comprehensive Benchmark of Language Models on Unicode and Romanized Sinhala
**arXiv**：[2601.14958v1](https://arxiv.org/abs/2601.14958) · [PDF](https://arxiv.org/pdf/2601.14958.pdf)  
**作者**：Minuri Rajapakse, Ruvan Weerasinghe  

**一句话要点**：提出综合基准评估语言模型在僧伽罗语Unicode和罗马化文本上的性能

**关键词**：语言模型评估, 僧伽罗语处理, 罗马化文本, 困惑度分析, 闭源模型比较

## 3 点简述
- 核心问题：僧伽罗语等低资源、形态丰富语言的语言模型性能研究不足，特别是数字通信中常见的罗马化文本。
- 方法要点：使用困惑度评估开源模型，通过句子补全定性分析领先闭源模型，覆盖Unicode和罗马化僧伽罗语语料。
- 实验或效果：Mistral-Nemo-Base-2407在Unicode文本上表现最佳，Mistral-7B-v0.3在罗马化文本上领先，Llama-3.1-8B整体性能强，闭源模型间存在显著差异。

## 摘要（原文）

> The performance of Language Models (LMs) on lower-resource, morphologically rich languages like Sinhala remains under-explored, particularly for Romanized Sinhala, which is prevalent in digital communication. This paper presents a comprehensive benchmark of modern LMs on a diverse corpus of Unicode and Romanized Sinhala. We evaluate open-source models using perplexity, a measure of how well a model predicts a text, and leading closed-source models via a qualitative analysis of sentence completion. Our findings reveal that the Mistral-Nemo-Base-2407 model achieves the strongest predictive performance on Unicode text and the Mistral-7B-v0.3 model for Romanized text. The results also highlight the strong all-around performance of the Llama-3.1-8B model for both scripts. Furthermore, a significant performance disparity exists among closed-source models: Gemini-1.5-pro and DeepSeek excel at Unicode generation, whereas Claude-3.5-Sonnet is superior at handling Romanized text. These results provide an essential guide for practitioners selecting models for Sinhala-specific applications and highlight the critical role of training data in handling script variations.

