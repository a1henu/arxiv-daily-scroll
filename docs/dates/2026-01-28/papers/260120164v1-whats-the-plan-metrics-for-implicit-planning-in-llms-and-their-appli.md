---
layout: default
title: What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering
---

# What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering
**arXiv**：[2601.20164v1](https://arxiv.org/abs/2601.20164) · [PDF](https://arxiv.org/pdf/2601.20164.pdf)  
**作者**：Jim Maar, Denis Paperno, Callum Stuart McDougall, Neel Nanda  

**一句话要点**：提出简单方法评估大语言模型中的隐式规划能力，应用于押韵生成和问答场景。

**关键词**：隐式规划评估, 大语言模型分析, 押韵生成, 问答系统, 向量引导技术

## 3 点简述
- 核心问题：大语言模型在训练中是否表现出隐式规划行为，如为未来押韵词或答案做准备。
- 方法要点：使用向量引导技术，在生成前一行末尾进行操控，影响中间令牌生成。
- 实验或效果：方法可扩展至多个模型，发现隐式规划普遍存在，从10亿参数模型开始。

## 摘要（原文）

> Prior work suggests that language models, while trained on next token prediction, show implicit planning behavior: they may select the next token in preparation to a predicted future token, such as a likely rhyming word, as supported by a prior qualitative study of Claude 3.5 Haiku using a cross-layer transcoder. We propose much simpler techniques for assessing implicit planning in language models. With case studies on rhyme poetry generation and question answering, we demonstrate that our methodology easily scales to many models. Across models, we find that the generated rhyme (e.g. "-ight") or answer to a question ("whale") can be manipulated by steering at the end of the preceding line with a vector, affecting the generation of intermediate tokens leading up to the rhyme or answer word. We show that implicit planning is a universal mechanism, present in smaller models than previously thought, starting from 1B parameters. Our methodology offers a widely applicable direct way to study implicit planning abilities of LLMs. More broadly, understanding planning abilities of language models can inform decisions in AI safety and control.

