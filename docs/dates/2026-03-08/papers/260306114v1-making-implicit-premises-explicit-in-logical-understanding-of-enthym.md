---
layout: default
title: Making Implicit Premises Explicit in Logical Understanding of Enthymemes
---

# Making Implicit Premises Explicit in Logical Understanding of Enthymemes
**arXiv**：[2603.06114v1](https://arxiv.org/abs/2603.06114) · [PDF](https://arxiv.org/pdf/2603.06114.pdf)  
**作者**：Xuyao Feng, Anthony Hunter  

**一句话要点**：提出集成LLM与神经符号推理的流水线，以解决省略三段论逻辑解码问题。

**关键词**：省略三段论, 逻辑解码, 大语言模型, 神经符号推理, 蕴含验证

## 3 点简述
- 核心问题：现实文本中的省略三段论缺乏系统方法进行逻辑解码与蕴含验证。
- 方法要点：结合LLM生成隐含前提、翻译逻辑公式，并使用SAT求解器进行神经符号推理。
- 实验或效果：在两个数据集上评估，在精确度、召回率等指标上表现出色。

## 摘要（原文）

> Real-world arguments in text and dialogues are normally enthymemes (i.e. some of their premises and/or claims are implicit). Natural language processing (NLP) methods for handling enthymemes can potentially identify enthymemes in text but they do not decode their underlying logic, whereas logic-based approaches for handling them assume a knowledgebase with sufficient formulae that can be used to decode them via abduction. There is therefore a lack of a systematic method for translating textual components of an enthymeme into a logical argument and generating the logical formulae required for their decoding, and thereby showing logical entailment. To address this, we propose a pipeline that integrates: (1) a large language model (LLM) to generate intermediate implicit premises based on the explicit premise and claim; (2) another LLM to translate the natural language into logical formulas; and (3) a neuro-symbolic reasoner based on a SAT solver to determine entailment. We evaluate our pipeline on two enthymeme datasets, demonstrating promising performance in selecting the correct implicit premise, as measured by precision, recall, F1-score, and accuracy.

