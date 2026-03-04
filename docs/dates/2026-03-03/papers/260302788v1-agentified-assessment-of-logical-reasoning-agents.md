---
layout: default
title: Agentified Assessment of Logical Reasoning Agents
---

# Agentified Assessment of Logical Reasoning Agents
**arXiv**：[2603.02788v1](https://arxiv.org/abs/2603.02788) · [PDF](https://arxiv.org/pdf/2603.02788.pdf)  
**作者**：Zhiyu Ni, Yifeng Xiao, Zheng Liang  

**一句话要点**：提出基于评估者代理的框架，以可复现、可审计的方式评估逻辑推理代理。

**关键词**：逻辑推理评估, 代理化评估, 自动形式化, 一阶逻辑, SMT求解, 基准测试

## 3 点简述
- 核心问题：评估逻辑推理代理时需确保评估过程可复现、可审计且对执行失败鲁棒。
- 方法要点：使用评估者代理发布任务、执行预算、解析输出并记录结构化失败类型，被测代理仅需暴露标准化接口。
- 实验或效果：在一阶逻辑推理案例中，自动形式化代理在清理后的FOLIO验证集上达到86.70%准确率，优于思维链基线。

## 摘要（原文）

> We present a framework for evaluating and benchmarking logical reasoning agents when assessment itself must be reproducible, auditable, and robust to execution failures. Building on agentified assessment, we use an assessor agent to issue tasks, enforce execution budgets, parse outputs, and record structured failure types, while the agent under test only needs to expose a standardized agent-to-agent interface. As a case study, we benchmark an auto-formalization agent for first-order logic (FOL) reasoning on a solver-verified and repaired split of FOLIO. The agent translates natural language premises and conclusions into executable Z3Py programs and employs satisfiability modulo theories (SMT) solving to determine logical entailment. On the cleaned FOLIO validation set, the auto-formalization agent achieves 86.70% accuracy under the assessor protocol, outperforming a chain-of-thought baseline (73.89%).

