---
layout: default
title: AgentRx: Diagnosing AI Agent Failures from Execution Trajectories
---

# AgentRx: Diagnosing AI Agent Failures from Execution Trajectories
**arXiv**：[2602.02475v1](https://arxiv.org/abs/2602.02475) · [PDF](https://arxiv.org/pdf/2602.02475.pdf)  
**作者**：Shraddha Barke, Arnav Goyal, Alind Khare, Avaljot Singh, Suman Nath, Chetan Bansal  

**一句话要点**：提出AGENTRX框架，通过约束合成与验证自动诊断AI代理执行轨迹中的关键失败步骤

**关键词**：AI代理诊断, 失败轨迹分析, 约束验证, 多领域基准, 自动化故障定位

## 3 点简述
- AI代理因概率性、长时程、多代理及工具噪声而失败难以定位
- AGENTRX合成约束并逐步评估，生成可审计的违规日志供LLM判断
- 在三个领域基准测试中，框架在步骤定位与失败归因上优于现有基线

## 摘要（原文）

> AI agents often fail in ways that are difficult to localize because executions are probabilistic, long-horizon, multi-agent, and mediated by noisy tool outputs. We address this gap by manually annotating failed agent runs and release a novel benchmark of 115 failed trajectories spanning structured API workflows, incident management, and open-ended web/file tasks. Each trajectory is annotated with a critical failure step and a category from a grounded-theory derived, cross-domain failure taxonomy. To mitigate the human cost of failure attribution, we present AGENTRX, an automated domain-agnostic diagnostic framework that pinpoints the critical failure step in a failed agent trajectory. It synthesizes constraints, evaluates them step-by-step, and produces an auditable validation log of constraint violations with associated evidence; an LLM-based judge uses this log to localize the critical step and category. Our framework improves step localization and failure attribution over existing baselines across three domains.

