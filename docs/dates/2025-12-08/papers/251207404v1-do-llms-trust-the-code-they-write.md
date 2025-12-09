---
layout: default
title: Do LLMs Trust the Code They Write?
---

# Do LLMs Trust the Code They Write?
**arXiv**：[2512.07404v1](https://arxiv.org/abs/2512.07404) · [PDF](https://arxiv.org/pdf/2512.07404.pdf)  
**作者**：Francisco Ribeiro, Claudio Spiess, Prem Devanbu, Sarah Nadi  

**一句话要点**：提出利用LLM内部正确性表示以提升代码生成质量，无需测试执行。

**关键词**：大语言模型, 代码生成, 内部表示, 正确性检测, 隐藏状态分析

## 3 点简述
- 核心问题：LLM生成代码时输出概率与正确性关联弱，导致错误代码频发。
- 方法要点：通过对比正确与错误代码的隐藏状态，提取LLM内部编码的正确性表示。
- 实验或效果：在四个LLM上实验，该表示优于标准对数似然排序和模型口头置信度，能选择更高质量代码。

## 摘要（原文）

> Despite the effectiveness of large language models (LLMs) for code generation, they often output incorrect code. One reason is that model output probabilities are often not well-correlated with correctness, and reflect only the final output of the generation process. Inspired by findings that LLMs internally encode concepts like truthfulness, this paper explores if LLMs similarly represent code correctness. Specifically, we identify a correctness representation inside LLMs by contrasting the hidden states between pairs of correct and incorrect code for the same programming tasks. By experimenting on four LLMs, we show that exploiting this extracted correctness representation outperforms standard log-likelihood ranking, as well as verbalized model confidence. Furthermore, we explore how this internal correctness signal can be used to select higher-quality code samples, without requiring test execution. Ultimately, this work demonstrates how leveraging internal representations can enhance code generation systems and make LLMs more reliable, thus improving confidence in automatically generated code.

