---
layout: default
title: Unlocking Multilingual Reasoning Capability of LLMs and LVLMs through Representation Engineering
---

# Unlocking Multilingual Reasoning Capability of LLMs and LVLMs through Representation Engineering
**arXiv**：[2511.23231v1](https://arxiv.org/abs/2511.23231) · [PDF](https://arxiv.org/pdf/2511.23231.pdf)  
**作者**：Qiming Li, Xiaocheng Feng, Yixuan Ma, Zekai Ye, Ruihan Chen, Xiachong Feng, Bing Qin  

**一句话要点**：提出MRRE方法以增强大模型在低资源语言上的推理能力，无需额外训练或翻译工具。

**关键词**：多语言推理, 表示工程, 推理时优化, 低资源语言, 大语言模型, 大视觉语言模型

## 3 点简述
- 核心问题：大模型在英语与低资源语言间推理性能差距大，影响多语言公平性。
- 方法要点：通过推理时注入预计算向量，分步提升跨语言推理和保持语言一致性。
- 实验或效果：在六个模型上平均提升非英语推理5.48%，低资源语言最高达7.54%。

## 摘要（原文）

> Large Language Models (LLMs) and Large Vision-Language Models (LVLMs) demonstrate strong reasoning capabilities, yet their performance in English significantly outperforms that in low-resource languages, raising fairness concerns in multilingual applications. Existing approaches either rely on costly multilingual training or employ prompting with external translation tools, both of which are resource-intensive and sensitive to translation quality. To address these limitations, we propose a training-free inference-time method to enhance Multilingual Reasoning capabilities via Representation Engineering (MRRE) without using any additional training data or tools. MRRE sequentially injects two precomputed vectors at specific layers during inference processing: cross-lingual reasoning enhancement vectors, which steer non-English reasoning representations toward English space to unlock multilingual reasoning, and target-language output anchoring vectors, which restore the distribution of the target language to preserve input-output language consistency. Comprehensive experiments across six advanced LLMs and LVLMs on four reasoning benchmarks demonstrate that MRRE consistently enhances non-English reasoning by an average gain of 5.48% and up to 7.54% in low-resource languages (Thai and Swahili), while improving input-output language consistency by 3.78%.

