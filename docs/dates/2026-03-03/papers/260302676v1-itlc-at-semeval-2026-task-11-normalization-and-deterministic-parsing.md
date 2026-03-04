---
layout: default
title: ITLC at SemEval-2026 Task 11: Normalization and Deterministic Parsing for Formal Reasoning in LLMs
---

# ITLC at SemEval-2026 Task 11: Normalization and Deterministic Parsing for Formal Reasoning in LLMs
**arXiv**：[2603.02676v1](https://arxiv.org/abs/2603.02676) · [PDF](https://arxiv.org/pdf/2603.02676.pdf)  
**作者**：Wicaksono Leksono Muhamad, Joanito Agili Lopo, Tack Hwa Wong, Muhammad Ravi Shulthan Habibi, Samuel Cahyawijaya  

**一句话要点**：提出基于结构抽象和确定性解析的方法，以减少大语言模型在多语言推理任务中的内容效应。

**关键词**：大语言模型, 多语言推理, 内容效应, 结构抽象, 确定性解析, 逻辑表示

## 3 点简述
- 核心问题：大语言模型在多语言推理任务中受内容效应影响，导致性能偏差。
- 方法要点：通过显式结构抽象将三段论转换为规范逻辑表示，并应用确定性解析判断有效性。
- 实验或效果：在SemEval-2026 Task 11多语言基准测试中，方法在所有子任务中排名前五，显著减少内容效应。

## 摘要（原文）

> Large language models suffer from content effects in reasoning tasks, particularly in multi-lingual contexts. We introduce a novel method that reduces these biases through explicit structural abstraction that transforms syllogisms into canonical logical representations and applies deterministic parsing to determine validity. Evaluated on the SemEval-2026 Task 11 multilingual benchmark, our approach achieves top-5 rankings across all subtasks while substantially reducing content effects and offering a competitive alternative to complex fine-tuning or activation-level interventions.

