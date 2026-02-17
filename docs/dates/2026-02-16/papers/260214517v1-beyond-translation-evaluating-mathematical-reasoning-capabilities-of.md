---
layout: default
title: Beyond Translation: Evaluating Mathematical Reasoning Capabilities of LLMs in Sinhala and Tamil
---

# Beyond Translation: Evaluating Mathematical Reasoning Capabilities of LLMs in Sinhala and Tamil
**arXiv**：[2602.14517v1](https://arxiv.org/abs/2602.14517) · [PDF](https://arxiv.org/pdf/2602.14517.pdf)  
**作者**：Sukumar Kishanthan, Kumar Thushalika, Buddhi Jayasekara, Asela Hevapathige  

**一句话要点**：评估LLMs在僧伽罗语和泰米尔语中的数学推理能力，揭示跨语言推理的非均匀性

**关键词**：多语言数学推理, 低资源语言评估, 翻译伪影, 平行数据集, 复杂推理退化

## 3 点简述
- 核心问题：LLMs在低资源语言中的数学推理是否依赖翻译而非真实多语言能力
- 方法要点：构建平行数据集，避免翻译伪影，评估六类数学问题
- 实验或效果：基础算术推理跨语言稳健，复杂推理在僧伽罗语和泰米尔语中显著退化

## 摘要（原文）

> Large language models (LLMs) demonstrate strong mathematical reasoning in English, but whether these capabilities reflect genuine multilingual reasoning or reliance on translation-based processing in low-resource languages like Sinhala and Tamil remains unclear. We examine this fundamental question by evaluating whether LLMs genuinely reason mathematically in these languages or depend on implicit translation to English-like representations. Using a taxonomy of six math problem types, from basic arithmetic to complex unit conflict and optimization problems, we evaluate four prominent large language models. To avoid translation artifacts that confound language ability with translation quality, we construct a parallel dataset where each problem is natively authored by fluent speakers with mathematical training in all three languages. Our analysis demonstrates that while basic arithmetic reasoning transfers robustly across languages, complex reasoning tasks show significant degradation in Tamil and Sinhala. The pattern of failures varies by model and problem type, suggesting that apparent multilingual competence may not reflect uniform reasoning capabilities across languages. These findings challenge the common assumption that models exhibiting strong multilingual performance can reason equally effectively across languages, and highlight the need for fine-grained, type-aware evaluation in multilingual settings.

