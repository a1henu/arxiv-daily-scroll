---
layout: default
title: AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows
---

# AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows
**arXiv**：[2603.02601v1](https://arxiv.org/abs/2603.02601) · [PDF](https://arxiv.org/pdf/2603.02601.pdf)  
**作者**：Varun Pratap Bhardwaj  

**一句话要点**：提出AgentAssay框架以解决非确定性AI代理工作流回归测试的token效率问题。

**关键词**：AI代理测试, 回归测试, 非确定性工作流, 行为指纹, 成本优化, 统计保证

## 3 点简述
- 核心问题：缺乏验证AI代理在提示、工具、模型或编排逻辑变更后是否退化的原则性方法。
- 方法要点：引入基于假设检验的随机三值判定、行为指纹映射和多变量回归检测等技术。
- 实验或效果：在多个模型和场景中实现78-100%成本节省，行为指纹检测能力达86%。

## 摘要（原文）

> Autonomous AI agents are deployed at unprecedented scale, yet no principled methodology exists for
>   verifying that an agent has not regressed after changes to its prompts, tools, models, or
>   orchestration logic. We present AgentAssay, the first token-efficient framework for regression
>   testing non-deterministic AI agent workflows, achieving 78-100% cost reduction while maintaining
>   rigorous statistical guarantees. Our contributions include: (1) stochastic three-valued verdicts
>   (PASS/FAIL/INCONCLUSIVE) grounded in hypothesis testing; (2) five-dimensional agent coverage metrics;
>   (3) agent-specific mutation testing operators; (4) metamorphic relations for agent workflows; (5)
>   CI/CD deployment gates as statistical decision procedures; (6) behavioral fingerprinting that maps
>   execution traces to compact vectors, enabling multivariate regression detection; (7) adaptive budget
>   optimization calibrating trial counts to behavioral variance; and (8) trace-first offline analysis
>   enabling zero-cost testing on production traces. Experiments across 5 models (GPT-5.2, Claude Sonnet
>   4.6, Mistral-Large-3, Llama-4-Maverick, Phi-4), 3 scenarios, and 7,605 trials demonstrate that
>   behavioral fingerprinting achieves 86% detection power where binary testing has 0%, SPRT reduces
>   trials by 78%, and the full pipeline achieves 100% cost savings through trace-first analysis.
>   Implementation: 20,000+ lines of Python, 751 tests, 10 framework adapters.

