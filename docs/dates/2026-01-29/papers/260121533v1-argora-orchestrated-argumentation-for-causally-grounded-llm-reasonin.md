---
layout: default
title: ARGORA: Orchestrated Argumentation for Causally Grounded LLM Reasoning and Decision Making
---

# ARGORA: Orchestrated Argumentation for Causally Grounded LLM Reasoning and Decision Making
**arXiv**：[2601.21533v1](https://arxiv.org/abs/2601.21533) · [PDF](https://arxiv.org/pdf/2601.21533.pdf)  
**作者**：Youngjin Jin, Hanna Kim, Kwanwoo Kim, Chanhee Lee, Seungwon Shin  

**一句话要点**：提出ARGORA框架，通过因果论证图组织多专家讨论以提升LLM推理与决策的透明度和可诊断性。

**关键词**：多专家LLM系统, 论证图, 因果推理, 决策透明度, 校正机制, 可诊断性

## 3 点简述
- 现有多专家LLM系统简单聚合观点，掩盖了驱动决策的关键论证过程。
- ARGORA构建显式论证图，将其建模为因果模型，支持系统性地移除和重算论证以识别必要推理链。
- 在多样基准测试中，ARGORA实现竞争性准确率，并通过校正机制在专家分歧时更常纠正错误，提供因果诊断。

## 摘要（原文）

> Existing multi-expert LLM systems gather diverse perspectives but combine them through simple aggregation, obscuring which arguments drove the final decision. We introduce ARGORA, a framework that organizes multi-expert discussions into explicit argumentation graphs showing which arguments support or attack each other. By casting these graphs as causal models, ARGORA can systematically remove individual arguments and recompute outcomes, identifying which reasoning chains were necessary and whether decisions would change under targeted modifications. We further introduce a correction mechanism that aligns internal reasoning with external judgments when they disagree. Across diverse benchmarks and an open-ended use case, ARGORA achieves competitive accuracy and demonstrates corrective behavior: when experts initially disagree, the framework resolves disputes toward correct answers more often than it introduces new errors, while providing causal diagnostics of decisive arguments.

