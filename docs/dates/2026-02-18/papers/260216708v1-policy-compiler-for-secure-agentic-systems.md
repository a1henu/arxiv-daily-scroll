---
layout: default
title: Policy Compiler for Secure Agentic Systems
---

# Policy Compiler for Secure Agentic Systems
**arXiv**：[2602.16708v1](https://arxiv.org/abs/2602.16708) · [PDF](https://arxiv.org/pdf/2602.16708.pdf)  
**作者**：Nils Palumbo, Sarthak Choudhary, Jihye Choi, Prasad Chalasani, Mihai Christodorescu, Somesh Jha  

**一句话要点**：提出PCAS策略编译器，为基于LLM的智能体系统提供确定性策略强制执行。

**关键词**：策略强制执行, 智能体系统, 依赖图建模, Datalog语言, 参考监控器, 信息流控制

## 3 点简述
- LLM智能体在复杂授权场景中缺乏策略强制执行保证，嵌入提示无法确保合规。
- PCAS将系统状态建模为依赖图，使用Datalog衍生语言表达策略，通过参考监控器拦截违规。
- 在客户服务任务中，PCAS将策略合规率从48%提升至93%，且无策略违规。

## 摘要（原文）

> LLM-based agents are increasingly being deployed in contexts requiring complex authorization policies: customer service protocols, approval workflows, data access restrictions, and regulatory compliance. Embedding these policies in prompts provides no enforcement guarantees. We present PCAS, a Policy Compiler for Agentic Systems that provides deterministic policy enforcement.
>   Enforcing such policies requires tracking information flow across agents, which linear message histories cannot capture. Instead, PCAS models the agentic system state as a dependency graph capturing causal relationships among events such as tool calls, tool results, and messages. Policies are expressed in a Datalog-derived language, as declarative rules that account for transitive information flow and cross-agent provenance. A reference monitor intercepts all actions and blocks violations before execution, providing deterministic enforcement independent of model reasoning.
>   PCAS takes an existing agent implementation and a policy specification, and compiles them into an instrumented system that is policy-compliant by construction, with no security-specific restructuring required. We evaluate PCAS on three case studies: information flow policies for prompt injection defense, approval workflows in a multi-agent pharmacovigilance system, and organizational policies for customer service. On customer service tasks, PCAS improves policy compliance from 48% to 93% across frontier models, with zero policy violations in instrumented runs.

