---
layout: default
title: Autonomous Agents on Blockchains: Standards, Execution Models, and Trust Boundaries
---

# Autonomous Agents on Blockchains: Standards, Execution Models, and Trust Boundaries
**arXiv**：[2601.04583v1](https://arxiv.org/abs/2601.04583) · [PDF](https://arxiv.org/pdf/2601.04583.pdf)  
**作者**：Saad Alqithami  

**一句话要点**：提出代理-区块链互操作性分类与威胁模型，以解决安全接口设计挑战

**关键词**：代理-区块链互操作性, 威胁模型, 集成模式, 交易意图, 策略执行, 系统评估

## 3 点简述
- 核心问题：代理与区块链集成需标准、安全接口，避免安全、治理和经济风险
- 方法要点：通过文献综述构建五类集成模式、威胁模型和系统能力矩阵
- 实验或效果：分析20多个系统，提出交易意图模式和策略决策记录作为研究路线图

## 摘要（原文）

> Advances in large language models have enabled agentic AI systems that can reason, plan, and interact with external tools to execute multi-step workflows, while public blockchains have evolved into a programmable substrate for value transfer, access control, and verifiable state transitions. Their convergence introduces a high-stakes systems challenge: designing standard, interoperable, and secure interfaces that allow agents to observe on-chain state, formulate transaction intents, and authorize execution without exposing users, protocols, or organizations to unacceptable security, governance, or economic risks. This survey systematizes the emerging landscape of agent-blockchain interoperability through a systematic literature review, identifying 317 relevant works from an initial pool of over 3000 records. We contribute a five-part taxonomy of integration patterns spanning read-only analytics, simulation and intent generation, delegated execution, autonomous signing, and multi-agent workflows; a threat model tailored to agent-driven transaction pipelines that captures risks ranging from prompt injection and policy misuse to key compromise, adversarial execution dynamics, and multi-agent collusion; and a comparative capability matrix analyzing more than 20 representative systems across 13 dimensions, including custody models, permissioning, policy enforcement, observability, and recovery. Building on the gaps revealed by this analysis, we outline a research roadmap centered on two interface abstractions: a Transaction Intent Schema for portable and unambiguous goal specification, and a Policy Decision Record for auditable, verifiable policy enforcement across execution environments. We conclude by proposing a reproducible evaluation suite and benchmarks for assessing the safety, reliability, and economic robustness of agent-mediated on-chain execution.

