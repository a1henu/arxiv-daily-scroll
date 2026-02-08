---
layout: default
title: A Guide to Large Language Models in Modeling and Simulation: From Core Techniques to Critical Challenges
---

# A Guide to Large Language Models in Modeling and Simulation: From Core Techniques to Critical Challenges
**arXiv**：[2602.05883v1](https://arxiv.org/abs/2602.05883) · [PDF](https://arxiv.org/pdf/2602.05883.pdf)  
**作者**：Philippe J. Giabbanelli  

**一句话要点**：提供大语言模型在建模与仿真中的实用指南，强调原则性设计选择与诊断策略。

**关键词**：大语言模型, 建模与仿真, 知识增强, 非确定性, 提示工程, 超参数设置

## 3 点简述
- 核心问题：LLMs在M&S应用中易引入非确定性、数据过载或性能下降等微妙问题。
- 方法要点：讨论提示、温度设置、知识增强（如RAG和LoRA）及数据分解等关键技术。
- 实验或效果：强调通过实证评估帮助模型师做出何时、如何及是否依赖LLMs的明智决策。

## 摘要（原文）

> Large language models (LLMs) have rapidly become familiar tools to researchers and practitioners. Concepts such as prompting, temperature, or few-shot examples are now widely recognized, and LLMs are increasingly used in Modeling & Simulation (M&S) workflows. However, practices that appear straightforward may introduce subtle issues, unnecessary complexity, or may even lead to inferior results. Adding more data can backfire (e.g., deteriorating performance through model collapse or inadvertently wiping out existing guardrails), spending time on fine-tuning a model can be unnecessary without a prior assessment of what it already knows, setting the temperature to 0 is not sufficient to make LLMs deterministic, providing a large volume of M&S data as input can be excessive (LLMs cannot attend to everything) but naive simplifications can lose information. We aim to provide comprehensive and practical guidance on how to use LLMs, with an emphasis on M&S applications. We discuss common sources of confusion, including non-determinism, knowledge augmentation (including RAG and LoRA), decomposition of M&S data, and hyper-parameter settings. We emphasize principled design choices, diagnostic strategies, and empirical evaluation, with the goal of helping modelers make informed decisions about when, how, and whether to rely on LLMs.

