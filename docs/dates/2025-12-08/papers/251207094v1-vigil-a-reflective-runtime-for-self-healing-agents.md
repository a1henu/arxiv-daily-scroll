---
layout: default
title: VIGIL: A Reflective Runtime for Self-Healing Agents
---

# VIGIL: A Reflective Runtime for Self-Healing Agents
**arXiv**：[2512.07094v1](https://arxiv.org/abs/2512.07094) · [PDF](https://arxiv.org/pdf/2512.07094.pdf)  
**作者**：Christopher Cruz  

**一句话要点**：提出VIGIL反射运行时以增强自主代理的自我修复能力

**关键词**：自主代理, 反射运行时, 自我修复, 行为诊断, 提示工程, 代码修复

## 3 点简述
- 问题：现有代理框架缺乏运行时自省，无法诊断失败模式，依赖人工干预。
- 方法：VIGIL通过行为日志分析、情感表示和RBT诊断，生成提示更新和代码修复提案。
- 效果：在案例研究中，VIGIL识别延迟问题，实现元级自我修复，提升系统可靠性。

## 摘要（原文）

> Agentic LLM frameworks promise autonomous behavior via task decomposition, tool use, and iterative planning, but most deployed systems remain brittle. They lack runtime introspection, cannot diagnose their own failure modes, and do not improve over time without human intervention. In practice, many agent stacks degrade into decorated chains of LLM calls with no structural mechanisms for reliability. We present VIGIL (Verifiable Inspection and Guarded Iterative Learning), a reflective runtime that supervises a sibling agent and performs autonomous maintenance rather than task execution. VIGIL ingests behavioral logs, appraises each event into a structured emotional representation, maintains a persistent EmoBank with decay and contextual policies, and derives an RBT diagnosis that sorts recent behavior into strengths, opportunities, and failures. From this analysis, VIGIL generates both guarded prompt updates that preserve core identity semantics and read only code proposals produced by a strategy engine that operates on log evidence and code hotspots. VIGIL functions as a state gated pipeline. Illegal transitions produce explicit errors rather than allowing the LLM to improvise. In a reminder latency case study, VIGIL identified elevated lag, proposed prompt and code repairs, and when its own diagnostic tool failed due to a schema conflict, it surfaced the internal error, produced a fallback diagnosis, and emitted a repair plan. This demonstrates meta level self repair in a deployed agent runtime.

