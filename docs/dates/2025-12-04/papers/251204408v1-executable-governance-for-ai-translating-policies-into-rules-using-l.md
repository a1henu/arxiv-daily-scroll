---
layout: default
title: Executable Governance for AI: Translating Policies into Rules Using LLMs
---

# Executable Governance for AI: Translating Policies into Rules Using LLMs
**arXiv**：[2512.04408v1](https://arxiv.org/abs/2512.04408) · [PDF](https://arxiv.org/pdf/2512.04408.pdf)  
**作者**：Gautam Varma Datla, Anudeep Vurity, Tejaswani Dash, Tazeem Ahmad, Mohd Adnan, Saima Rafi  

**一句话要点**：提出Policy-to-Tests框架，利用LLMs将自然语言AI政策转换为可执行规则以解决手动转换的低效问题。

**关键词**：AI政策执行, 自然语言处理, 可执行规则生成, 领域特定语言, LLM应用, 安全评估

## 3 点简述
- 核心问题：AI政策指南多为文本，手动转换为可执行规则缓慢、易错且难以扩展。
- 方法要点：开发P2T框架，通过管道和领域特定语言将政策文档标准化为机器可读规则。
- 实验或效果：在多种政策上应用，AI生成规则接近人类基准，并验证了在生成代理中的安全影响。

## 摘要（原文）

> AI policy guidance is predominantly written as prose, which practitioners must first convert into executable rules before frameworks can evaluate or enforce them. This manual step is slow, error-prone, difficult to scale, and often delays the use of safeguards in real-world deployments. To address this gap, we present Policy-to-Tests (P2T), a framework that converts natural-language policy documents into normalized, machine-readable rules. The framework comprises a pipeline and a compact domain-specific language (DSL) that encodes hazards, scope, conditions, exceptions, and required evidence, yielding a canonical representation of extracted rules. To test the framework beyond a single policy, we apply it across general frameworks, sector guidance, and enterprise standards, extracting obligation-bearing clauses and converting them into executable rules. These AI-generated rules closely match strong human baselines on span-level and rule-level metrics, with robust inter-annotator agreement on the gold set. To evaluate downstream behavioral and safety impact, we add HIPAA-derived safeguards to a generative agent and compare it with an otherwise identical agent without guardrails. An LLM-based judge, aligned with gold-standard criteria, measures violation rates and robustness to obfuscated and compositional prompts. Detailed results are provided in the appendix. We release the codebase, DSL, prompts, and rule sets as open-source resources to enable reproducible evaluation.

