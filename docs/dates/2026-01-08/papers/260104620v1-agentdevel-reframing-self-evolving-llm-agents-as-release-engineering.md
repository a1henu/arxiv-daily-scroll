---
layout: default
title: AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering
---

# AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering
**arXiv**：[2601.04620v1](https://arxiv.org/abs/2601.04620) · [PDF](https://arxiv.org/pdf/2601.04620.pdf)  
**作者**：Di Zhang  

**一句话要点**：提出AgentDevel，将LLM代理改进重构为发布工程，以解决不稳定和难以审计的问题。

**关键词**：LLM代理, 发布工程, 非回归保证, 可执行诊断, 翻转中心门控, 代理改进

## 3 点简述
- 核心问题：现有LLM代理自改进方法导致不稳定、难以审计的改进轨迹，难以保证非回归或跨版本故障推理。
- 方法要点：引入发布工程管道，包括实现无关的LLM批评器、基于脚本的可执行诊断和翻转中心门控，强调非回归为主要目标。
- 实验或效果：在重执行基准测试中，AgentDevel实现稳定改进，显著减少回归，并产生可复现、可审计的工件。

## 摘要（原文）

> Recent progress in large language model (LLM) agents has largely focused on embedding self-improvement mechanisms inside the agent or searching over many concurrent variants. While these approaches can raise aggregate scores, they often yield unstable and hard-to-audit improvement trajectories, making it difficult to guarantee non-regression or to reason about failures across versions. We reframe agent improvement as \textbf{release engineering}: agents are treated as shippable artifacts, and improvement is externalized into a regression-aware release pipeline. We introduce \textbf{AgentDevel}, a release engineering pipeline that iteratively runs the current agent, produces implementation-blind, symptom-level quality signals from execution traces, synthesizes a single release candidate (RC) via executable diagnosis, and promotes it under flip-centered gating. AgentDevel features three core designs: (i) an implementation-blind LLM critic that characterizes failure appearances without accessing agent internals, (ii) script-based executable diagnosis that aggregates dominant symptom patterns and produces auditable engineering specifications, and (iii) flip-centered gating that prioritizes pass to fail regressions and fail to pass fixes as first-class evidence. Unlike population-based search or in-agent self-refinement, AgentDevel maintains a single canonical version line and emphasizes non-regression as a primary objective. Experiments on execution-heavy benchmarks demonstrate that AgentDevel yields stable improvements with significantly fewer regressions while producing reproducible, auditable artifacts. Overall, AgentDevel provides a practical development discipline for building, debugging, and releasing LLM agents as software development.

