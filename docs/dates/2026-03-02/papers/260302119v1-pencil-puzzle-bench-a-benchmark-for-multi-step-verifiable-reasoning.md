---
layout: default
title: Pencil Puzzle Bench: A Benchmark for Multi-Step Verifiable Reasoning
---

# Pencil Puzzle Bench: A Benchmark for Multi-Step Verifiable Reasoning
**arXiv**：[2603.02119v1](https://arxiv.org/abs/2603.02119) · [PDF](https://arxiv.org/pdf/2603.02119.pdf)  
**作者**：Justin Waugh  

**一句话要点**：提出Pencil Puzzle Bench基准，通过铅笔谜题评估大语言模型的多步可验证推理能力。

**关键词**：大语言模型评估, 多步推理基准, 约束满足问题, 过程监督, 代理模式, 长上下文利用

## 3 点简述
- 核心问题：评估大语言模型在约束满足问题上的推理能力，需支持确定性、步骤级验证。
- 方法要点：基于62,231个谜题数据库，构建300个谜题的基准，支持直接询问和代理模式，可检查中间状态。
- 实验或效果：评估51个模型，揭示推理努力扩展和代理迭代两个能力轴，如GPT-5.2和Claude Opus 4.6性能显著提升。

## 摘要（原文）

> We introduce Pencil Puzzle Bench, a framework for evaluating large language model reasoning through pencil puzzles, a family of constraint-satisfaction problems closely related to NP-complete problems, with deterministic, step-level verification. From a database of 62,231 puzzles across 94 varieties with verified unique solutions, we select a benchmark of 300 puzzles spanning 20 varieties and evaluate 51 models from 11 providers in two modes: direct ask (single-shot) and agentic (multi-turn with iterative verification). A key differentiator of our benchmark is that every intermediate board state can be checked against variety-specific constraints, localizing errors to the exact rule violated, providing the infrastructure for dense, per-move reward signals for process supervision and reinforcement learning.
>   Our evaluation reveals two distinct axes of capability: (1) reasoning effort scaling, where GPT-5.2 improves 81x from no reasoning to maximum effort; and (2) agentic iteration, where Claude Opus 4.6 rises from 0.3% to 30.0% through iterative checking, while GPT-5.2@xhigh improves from 20.2% to 56.0%. Agentic attempts span a median of 29 turns over 17 minutes, with the longest exceeding 1,221 turns and 14.3 hours - a demanding test of long-context utilization, not just reasoning.

