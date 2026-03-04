---
layout: default
title: Beyond Task Completion: Revealing Corrupt Success in LLM Agents through Procedure-Aware Evaluation
---

# Beyond Task Completion: Revealing Corrupt Success in LLM Agents through Procedure-Aware Evaluation
**arXiv**：[2603.03116v1](https://arxiv.org/abs/2603.03116) · [PDF](https://arxiv.org/pdf/2603.03116.pdf)  
**作者**：Hongliu Cao, Ilias Driouich, Eoin Thomas  

**一句话要点**：提出过程感知评估框架以揭示LLM代理中的腐败成功，超越任务完成度评价

**关键词**：LLM代理评估, 过程感知评估, 腐败成功, 基准设计, 多维度门控, 一致性关系

## 3 点简述
- 当前基准主要评估任务是否完成，忽略执行过程，导致腐败成功被掩盖
- 引入过程感知评估，形式化代理过程为结构化观察，暴露观察、通信与执行间的一致性关系
- 在tau-bench上评估SOTA代理，发现27-78%报告成功为腐败成功，影响模型排名与基准设计

## 摘要（原文）

> Large Language Model (LLM)-based agents are increasingly adopted in high-stakes settings, but current benchmarks evaluate mainly whether a task was completed, not how. We introduce Procedure-Aware Evaluation (PAE), a framework that formalizes agent procedures as structured observations and exposes consistency relationships between what agents observe, communicate, and execute. PAE evaluates agents along complementary axes (Utility, Efficiency, Interaction Quality, Procedural Integrity) and applies multi-dimensional gating that categorically disqualifies corrupt outcomes. Evaluating state-of-the-art LLM agents on tau-bench yields findings at the axis, compliance, and benchmark levels. At the axis level, the dimensions capture non-redundant failure modes: utility masks reliability gaps, speed does not imply precision, and conciseness does not predict intent adherence. At the procedural compliance level, 27-78% of benchmark reported successes are corrupt successes concealing violations across interaction and integrity. Furthermore, gating substantially collapses Pass^4 rate and affects model rankings. The analysis of corrupt success cases reveals distinctive per-model failure signatures: GPT-5 spreads errors across policy, execution, and intent dimensions; Kimi-K2-Thinking concentrates 78% of violations in policy faithfulness and compliance; and Mistral-Large-3 is dominated by faithfulness failures. At the benchmark level, our analysis exposes structural flaws in the benchmark design, including task scope gaps, contradictory reward signals, and simulator artifacts that produce accidental successes.

