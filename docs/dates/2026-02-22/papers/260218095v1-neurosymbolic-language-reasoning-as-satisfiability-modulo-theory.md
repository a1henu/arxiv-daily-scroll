---
layout: default
title: Neurosymbolic Language Reasoning as Satisfiability Modulo Theory
---

# Neurosymbolic Language Reasoning as Satisfiability Modulo Theory
**arXiv**：[2602.18095v1](https://arxiv.org/abs/2602.18095) · [PDF](https://arxiv.org/pdf/2602.18095.pdf)  
**作者**：Hyunseok Oh, Sam Stern, Youngki Lee, Matthai Philipose  

**一句话要点**：提出Logitext神经符号语言，将文档表示为自然语言文本约束，结合LLM与SMT求解器提升文本-逻辑推理能力。

**关键词**：神经符号推理, 可满足性模理论, 自然语言理解, 约束求解, 内容审核, 逻辑结构

## 3 点简述
- 核心问题：大语言模型在文本与逻辑交织推理中不可靠，现有神经符号系统局限于完全形式化任务。
- 方法要点：引入Logitext语言，将文档表示为自然语言文本约束，开发算法集成LLM约束评估与SMT求解。
- 实验或效果：在内容审核基准、LegalBench和Super-Natural Instructions上实验，Logitext提高了准确性和覆盖范围。

## 摘要（原文）

> Natural language understanding requires interleaving textual and logical reasoning, yet large language models often fail to perform such reasoning reliably. Existing neurosymbolic systems combine LLMs with solvers but remain limited to fully formalizable tasks such as math or program synthesis, leaving natural documents with only partial logical structure unaddressed. We introduce Logitext, a neurosymbolic language that represents documents as natural language text constraints (NLTCs), making partial logical structure explicit. We develop an algorithm that integrates LLM-based constraint evaluation with satisfiability modulo theory (SMT) solving, enabling joint textual-logical reasoning. Experiments on a new content moderation benchmark, together with LegalBench and Super-Natural Instructions, show that Logitext improves both accuracy and coverage. This work is the first that treats LLM-based reasoning as an SMT theory, extending neurosymbolic methods beyond fully formalizable domains.

