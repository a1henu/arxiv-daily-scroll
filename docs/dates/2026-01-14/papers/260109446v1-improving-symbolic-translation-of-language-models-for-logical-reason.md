---
layout: default
title: Improving Symbolic Translation of Language Models for Logical Reasoning
---

# Improving Symbolic Translation of Language Models for Logical Reasoning
**arXiv**：[2601.09446v1](https://arxiv.org/abs/2601.09446) · [PDF](https://arxiv.org/pdf/2601.09446.pdf)  
**作者**：Ramya Keerthy Thatikonda, Jiuzhou Han, Wray Buntine, Ehsan Shareghi  

**一句话要点**：提出增量推理与验证模块以提升小语言模型的逻辑推理符号翻译性能

**关键词**：逻辑推理, 符号翻译, 语言模型微调, 增量推理, 验证模块, 一阶逻辑

## 3 点简述
- 核心问题：小语言模型在自然语言到一阶逻辑翻译中易产生格式和翻译错误，影响推理可靠性。
- 方法要点：通过错误分类、大模型合成数据微调、增量推理（分谓词生成和FOL翻译两阶段）及验证模块改进翻译质量。
- 实验或效果：在四个逻辑推理数据集上评估，降低错误率、提高谓词覆盖和推理性能，增强小模型可靠性。

## 摘要（原文）

> The use of formal language for deductive logical reasoning aligns well with language models (LMs), where translating natural language (NL) into first-order logic (FOL) and employing an external solver results in a verifiable and therefore reliable reasoning system. However, smaller LMs often struggle with this translation task, frequently producing incorrect symbolic outputs due to formatting and translation errors. Existing approaches typically rely on self-iteration to correct these errors, but such methods depend heavily on the capabilities of the underlying model. To address this, we first categorize common errors and fine-tune smaller LMs using data synthesized by large language models. The evaluation is performed using the defined error categories. We introduce incremental inference, which divides inference into two stages, predicate generation and FOL translation, providing greater control over model behavior and enhancing generation quality as measured by predicate metrics. This decomposition framework also enables the use of a verification module that targets predicate-arity errors to further improve performance. Our study evaluates three families of models across four logical-reasoning datasets. The comprehensive fine-tuning, incremental inference, and verification modules reduce error rates, increase predicate coverage, and improve reasoning performance for smaller LMs, moving us closer to developing reliable and accessible symbolic-reasoning systems.

