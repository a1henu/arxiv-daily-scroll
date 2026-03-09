---
layout: default
title: ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code
---

# ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code
**arXiv**：[2603.06365v1](https://arxiv.org/abs/2603.06365) · [PDF](https://arxiv.org/pdf/2603.06365.pdf)  
**作者**：Elzo Brito dos Santos Filho  

**一句话要点**：提出ESAA-Security架构，以解决AI生成代码安全审计中的不可复现和不可追溯问题。

**关键词**：事件溯源架构, AI生成代码审计, 安全审计框架, 可验证审计, 代理辅助安全, 风险分类

## 3 点简述
- 核心问题：AI辅助代码生成导致安全审计覆盖不均、结果不可复现且缺乏审计轨迹。
- 方法要点：采用事件溯源架构，通过约束输出和重放验证实现可追溯、可复现的审计流程。
- 实验或效果：框架定义26任务、16安全域和95检查，生成结构化报告和风险矩阵。

## 摘要（原文）

> AI-assisted software generation has increased development speed, but it has also amplified a persistent engineering problem: systems that are functionally correct may still be structurally insecure. In practice, prompt-based security review with large language models often suffers from uneven coverage, weak reproducibility, unsupported findings, and the absence of an immutable audit trail. The ESAA architecture addresses a related governance problem in agentic software engineering by separating heuristic agent cognition from deterministic state mutation through append-only events, constrained outputs, and replay-based verification. This paper presents ESAA-Security, a domain-specific specialization of ESAA for agent-assisted security auditing of software repositories, with particular emphasis on AI-generated or AI-modified code. ESAA-Security structures auditing as a governed execution pipeline with four phases reconnaissance, domain audit execution, risk classification, and final reporting and operationalizes the workflow into 26 tasks, 16 security domains, and 95 executable checks. The framework produces structured check results, vulnerability inventories, severity classifications, risk matrices, remediation guidance, executive summaries, and a final markdown/JSON audit report. The central idea is that security review should not be modeled as a free-form conversation with an LLM, but as an evidence-oriented audit process governed by contracts and events. In ESAA-Security, agents emit structured intentions under constrained protocols; the orchestrator validates them, persists accepted outputs to an append-only log, reprojects derived views, and verifies consistency through replay and hashing. The result is a traceable, reproducible, and risk-oriented audit architecture whose final report is auditable by construction.

