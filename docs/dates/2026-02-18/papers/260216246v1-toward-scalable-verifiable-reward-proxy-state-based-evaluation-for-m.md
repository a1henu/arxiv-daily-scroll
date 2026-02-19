---
layout: default
title: Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents
---

# Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents
**arXiv**：[2602.16246v1](https://arxiv.org/abs/2602.16246) · [PDF](https://arxiv.org/pdf/2602.16246.pdf)  
**作者**：Yun-Shiuan Chuang, Chaitanya Kulkarni, Alec Chiu, Avinash Thangali, Zijie Pan, Shivani Shekhar, Yirou Ge, Yixi Li, Uma Kona, Linsey Pang, Prakhar Mehrotra  

**一句话要点**：提出基于代理状态的评估框架，以可扩展方式验证多轮工具调用LLM代理的奖励。

**关键词**：LLM代理评估, 代理状态跟踪, 多轮工具调用, 可扩展基准, 幻觉检测, 模拟框架

## 3 点简述
- 核心问题：现有确定性后端基准成本高且迭代困难，难以可靠评估多轮工具调用LLM代理。
- 方法要点：使用LLM驱动的模拟框架，通过代理状态跟踪和LLM判断来验证目标完成和检测幻觉，无需确定性数据库。
- 实验或效果：基准产生稳定模型排名，支持策略内/外数据生成，人类-LLM判断一致性超过90%，实现可扩展评估。

## 摘要（原文）

> Interactive large language model (LLM) agents operating via multi-turn dialogue and multi-step tool calling are increasingly used in production. Benchmarks for these agents must both reliably compare models and yield on-policy training data. Prior agentic benchmarks (e.g., tau-bench, tau2-bench, AppWorld) rely on fully deterministic backends, which are costly to build and iterate. We propose Proxy State-Based Evaluation, an LLM-driven simulation framework that preserves final state-based evaluation without a deterministic database. Specifically, a scenario specifies the user goal, user/system facts, expected final state, and expected agent behavior, and an LLM state tracker infers a structured proxy state from the full interaction trace. LLM judges then verify goal completion and detect tool/user hallucinations against scenario constraints. Empirically, our benchmark produces stable, model-differentiating rankings across families and inference-time reasoning efforts, and its on-/off-policy rollouts provide supervision that transfers to unseen scenarios. Careful scenario specification yields near-zero simulator hallucination rates as supported by ablation studies. The framework also supports sensitivity analyses over user personas. Human-LLM judge agreement exceeds 90%, indicating reliable automated evaluation. Overall, proxy state-based evaluation offers a practical, scalable alternative to deterministic agentic benchmarks for industrial LLM agents.

