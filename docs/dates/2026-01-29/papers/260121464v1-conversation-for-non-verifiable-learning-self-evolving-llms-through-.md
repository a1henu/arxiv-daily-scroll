---
layout: default
title: Conversation for Non-verifiable Learning: Self-Evolving LLMs through Meta-Evaluation
---

# Conversation for Non-verifiable Learning: Self-Evolving LLMs through Meta-Evaluation
**arXiv**：[2601.21464v1](https://arxiv.org/abs/2601.21464) · [PDF](https://arxiv.org/pdf/2601.21464.pdf)  
**作者**：Yuan Sui, Bryan Hooi  

**一句话要点**：提出CoNL框架，通过元评估实现LLM在无真值任务中的自我进化

**关键词**：元评估, 多智能体自博弈, 无真值学习, LLM训练, 对话框架

## 3 点简述
- 核心问题：LLM在无真值任务中训练困难，LLM-as-Judge方法受限于评估者质量与偏见。
- 方法要点：引入多智能体自博弈框架，统一生成、评估与元评估，通过诊断奖励优化评估能力。
- 实验或效果：在五个基准测试中，CoNL优于自奖励基线，实现稳定训练与性能提升。

## 摘要（原文）

> Training large language models (LLMs) for non-verifiable tasks, such as creative writing, dialogue, and ethical reasoning, remains challenging due to the absence of ground-truth labels. While LLM-as-Judge approaches offer a scalable alternative to human feedback, they face a fundamental limitation: performance is constrained by the evaluator's own quality. If the judge cannot recognize good solutions, it cannot provide useful training signals, and evaluation biases (e.g., favoring verbosity over quality) remain unaddressed. This motivates meta-evaluation: the ability to evaluate and improve the evaluator itself. We introduce CoNL, a framework that unifies generation, evaluation, and meta-evaluation through multi-agent self-play. Our key insight: critique quality can be measured by whether it helps others improve their solutions. In CoNL, multiple agents sharing the same policy engage in structured conversations to propose, critique, and revise solutions. Critiques that enable solution improvements earn a diagnostic reward, creating explicit supervision for meta-evaluation and enabling joint optimization of generation and judging capabilities through self-play, without external judges or ground truth. Experiments on five benchmarks show that CoNL achieves consistent improvements over self-rewarding baselines while maintaining stable training.

