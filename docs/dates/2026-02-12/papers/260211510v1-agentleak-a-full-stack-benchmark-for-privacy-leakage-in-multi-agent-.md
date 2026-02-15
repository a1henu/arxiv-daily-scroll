---
layout: default
title: AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems
---

# AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems
**arXiv**：[2602.11510v1](https://arxiv.org/abs/2602.11510) · [PDF](https://arxiv.org/pdf/2602.11510.pdf)  
**作者**：Faouzi El Yagoubi, Ranwa Al Mallah, Godwin Badu-Marfo  

**一句话要点**：提出AgentLeak基准以评估多智能体LLM系统中的隐私泄露风险

**关键词**：多智能体系统, 隐私泄露基准, 内部通道审计, LLM安全, 智能体通信

## 3 点简述
- 核心问题：多智能体LLM系统存在内部通道隐私泄露风险，现有基准无法测量
- 方法要点：构建首个全栈基准，覆盖内部通道，包含1000场景和攻击分类
- 实验或效果：测试5个模型，发现内部通道泄露率高，输出审计遗漏41.7%违规

## 摘要（原文）

> Multi-agent Large Language Model (LLM) systems create privacy risks that current benchmarks cannot measure. When agents coordinate on tasks, sensitive data passes through inter-agent messages, shared memory, and tool arguments; pathways that output-only audits never inspect. We introduce AgentLeak, to the best of our knowledge the first full-stack benchmark for privacy leakage covering internal channels, spanning 1,000 scenarios across healthcare, finance, legal, and corporate domains, paired with a 32-class attack taxonomy and three-tier detection pipeline. Testing GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, and Llama 3.3 70B across 4,979 traces reveals that multi-agent configurations reduce per-channel output leakage (C1: 27.2% vs 43.2% in single-agent) but introduce unmonitored internal channels that raise total system exposure to 68.9% (OR-aggregated across C1, C2, C5). Internal channels account for most of this gap: inter-agent messages (C2) leak at 68.8%, compared to 27.2% on C1 (output channel). This means that output-only audits miss 41.7% of violations. Claude 3.5 Sonnet, which emphasizes safety alignment in its design, achieves the lowest leakage rates on both external (3.3%) and internal (28.1%) channels, suggesting that model-level safety training may transfer to internal channel protection. Across all five models and four domains, the pattern C2 > C1 holds consistently, confirming that inter-agent communication is the primary vulnerability. These findings underscore the need for coordination frameworks that incorporate internal-channel privacy protections and enforce privacy controls on inter-agent communication.

