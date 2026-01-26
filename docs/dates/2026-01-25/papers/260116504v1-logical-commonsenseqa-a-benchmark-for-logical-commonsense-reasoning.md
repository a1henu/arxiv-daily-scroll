---
layout: default
title: LOGICAL-COMMONSENSEQA: A Benchmark for Logical Commonsense Reasoning
---

# LOGICAL-COMMONSENSEQA: A Benchmark for Logical Commonsense Reasoning
**arXiv**：[2601.16504v1](https://arxiv.org/abs/2601.16504) · [PDF](https://arxiv.org/pdf/2601.16504.pdf)  
**作者**：Obed Junias, Maria Leonor Pacheco  

**一句话要点**：提出LOGICAL-COMMONSENSEQA基准，以逻辑组合方式评估常识推理能力。

**关键词**：常识推理, 逻辑组合, 基准评估, 零样本学习, 链式思维提示

## 3 点简述
- 核心问题：现有基准依赖单标签评估，无法区分语句间的联合、互斥或联合不可信关系。
- 方法要点：使用逻辑运算符（AND、OR、NEITHER/NOR）对原子语句对进行组合，构建新基准。
- 实验或效果：模型在合取推理表现尚可，析取推理中等，但基于否定的问题性能显著下降。

## 摘要（原文）

> Commonsense reasoning often involves evaluating multiple plausible interpretations rather than selecting a single atomic answer, yet most benchmarks rely on single-label evaluation, obscuring whether statements are jointly plausible, mutually exclusive, or jointly implausible. We introduce LOGICAL-COMMONSENSEQA, a benchmark that re-frames commonsense reasoning as logical composition over pairs of atomic statements using plausibility-level operators (AND, OR, NEITHER/NOR). Evaluating instruction-tuned, reasoning-specialized, and fine-tuned models under zero-shot, few-shot, and chain-of-thought prompting, we find that while models perform reasonably on conjunctive and moderately on disjunctive reasoning, performance degrades sharply on negation-based questions. LOGICAL-COMMONSENSEQA exposes fundamental reasoning limitations and provides a controlled framework for advancing compositional commonsense reasoning.

