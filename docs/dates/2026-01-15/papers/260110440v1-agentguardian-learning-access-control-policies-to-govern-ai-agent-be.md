---
layout: default
title: AgentGuardian: Learning Access Control Policies to Govern AI Agent Behavior
---

# AgentGuardian: Learning Access Control Policies to Govern AI Agent Behavior
**arXiv**：[2601.10440v1](https://arxiv.org/abs/2601.10440) · [PDF](https://arxiv.org/pdf/2601.10440.pdf)  
**作者**：Nadya Abaev, Denis Klimov, Gerard Levinov, David Mimran, Yuval Elovici, Asaf Shabtai  

**一句话要点**：提出AgentGuardian框架，通过上下文感知访问控制策略保护AI代理行为安全

**关键词**：AI代理安全, 访问控制策略, 上下文感知, 控制流治理, 恶意输入检测

## 3 点简述
- 核心问题：AI代理在自动化任务中可能执行未授权操作或处理不当输入，威胁系统完整性
- 方法要点：在受控阶段监控执行轨迹，学习合法行为并生成自适应策略，基于实时输入上下文和控制流依赖
- 实验或效果：在两个真实AI代理应用中有效检测恶意输入，保持正常功能，减轻幻觉驱动错误

## 摘要（原文）

> Artificial intelligence (AI) agents are increasingly used in a variety of domains to automate tasks, interact with users, and make decisions based on data inputs. Ensuring that AI agents perform only authorized actions and handle inputs appropriately is essential for maintaining system integrity and preventing misuse. In this study, we introduce the AgentGuardian, a novel security framework that governs and protects AI agent operations by enforcing context-aware access-control policies. During a controlled staging phase, the framework monitors execution traces to learn legitimate agent behaviors and input patterns. From this phase, it derives adaptive policies that regulate tool calls made by the agent, guided by both real-time input context and the control flow dependencies of multi-step agent actions. Evaluation across two real-world AI agent applications demonstrates that AgentGuardian effectively detects malicious or misleading inputs while preserving normal agent functionality. Moreover, its control-flow-based governance mechanism mitigates hallucination-driven errors and other orchestration-level malfunctions.

