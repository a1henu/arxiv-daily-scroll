---
layout: default
title: ChaosBench-Logic: A Benchmark for Logical and Symbolic Reasoning on Chaotic Dynamical Systems
---

# ChaosBench-Logic: A Benchmark for Logical and Symbolic Reasoning on Chaotic Dynamical Systems
**arXiv**：[2601.01982v1](https://arxiv.org/abs/2601.01982) · [PDF](https://arxiv.org/pdf/2601.01982.pdf)  
**作者**：Noel Thomas  

**一句话要点**：提出ChaosBench-Logic基准，以评估大语言模型在混沌动力系统中的逻辑推理能力。

**关键词**：逻辑推理基准, 混沌动力系统, 一阶逻辑本体, 神经符号方法, 大语言模型评估, 科学推理

## 3 点简述
- 核心问题：大语言模型在需要精确逻辑推理的领域表现脆弱，混沌动力系统提供严格测试场景。
- 方法要点：基于统一一阶逻辑本体，涵盖30个系统、11个语义谓词和621个问题，包括多跳推理等七类。
- 实验或效果：前沿模型单题准确率达91-94%，但组合项得0%，对话准确率53.1%-75.5%，揭示推理缺陷。

## 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but remain brittle in domains requiring precise logical and symbolic reasoning. Chaotic dynamical systems provide an especially demanding test because chaos is deterministic yet often misinterpreted as randomness or complexity. We introduce ChaosBench-Logic, a benchmark that evaluates LLM reasoning across 30 diverse dynamical systems using a unified first-order logic (FOL) ontology. Each system is annotated with truth assignments for 11 semantic predicates, and 621 questions are generated across seven reasoning categories, including multi-hop implications, cross-system analogies, counterfactual reasoning, bias probes, and multi-turn dialogues. We define metrics for logical accuracy, implication consistency, dialogue coherence, and contradiction, and we release an open-source evaluation pipeline. Initial experiments show that frontier LLMs such as GPT-4, Claude 3.5 Sonnet, Gemini 2.5 Flash, and the open-source LLaMA-3 70B achieve 91-94% per-item accuracy, yet still score 0% on compositional items and exhibit fragile global coherence. Dialogue-level accuracy ranges from 53.1% (GPT-4 CoT) to 75.5% (LLaMA-3 zero-shot). ChaosBench-Logic provides a rigorous testbed for diagnosing such failures and a foundation for developing neuro-symbolic approaches that improve scientific reasoning in LLMs.

