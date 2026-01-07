---
layout: default
title: Logical Phase Transitions: Understanding Collapse in LLM Logical Reasoning
---

# Logical Phase Transitions: Understanding Collapse in LLM Logical Reasoning
**arXiv**：[2601.02902v1](https://arxiv.org/abs/2601.02902) · [PDF](https://arxiv.org/pdf/2601.02902.pdf)  
**作者**：Xinglang Zhang, Yunyao Zhang, ZeLiang Chen, Junqing Yu, Wei Yang, Zikai Song  

**一句话要点**：提出神经符号课程调优以缓解大语言模型在逻辑推理中的崩溃现象

**关键词**：逻辑推理, 大语言模型, 神经符号学习, 课程学习, 性能崩溃

## 3 点简述
- 核心问题：大语言模型在逻辑复杂度增加时，推理性能会突然崩溃，而非平滑下降。
- 方法要点：通过神经符号课程调优，自适应对齐自然语言与逻辑符号，并围绕相变边界重塑训练动态。
- 实验或效果：在五个基准测试中，有效缓解高复杂度下的推理崩溃，提升准确率并改善泛化能力。

## 摘要（原文）

> Symbolic logical reasoning is a critical yet underexplored capability of large language models (LLMs), providing reliable and verifiable decision-making in high-stakes domains such as mathematical reasoning and legal judgment. In this study, we present a systematic analysis of logical reasoning under controlled increases in logical complexity, and reveal a previously unrecognized phenomenon, which we term Logical Phase Transitions: rather than degrading smoothly, logical reasoning performance remains stable within a regime but collapses abruptly beyond a critical logical depth, mirroring physical phase transitions such as water freezing beyond a critical temperature threshold. Building on this insight, we propose Neuro-Symbolic Curriculum Tuning, a principled framework that adaptively aligns natural language with logical symbols to establish a shared representation, and reshapes training dynamics around phase-transition boundaries to progressively strengthen reasoning at increasing logical depths. Experiments on five benchmarks show that our approach effectively mitigates logical reasoning collapse at high complexity, yielding average accuracy gains of +1.26 in naive prompting and +3.95 in CoT, while improving generalization to unseen logical compositions. Code and data are available at https://github.com/AI4SS/Logical-Phase-Transitions.

