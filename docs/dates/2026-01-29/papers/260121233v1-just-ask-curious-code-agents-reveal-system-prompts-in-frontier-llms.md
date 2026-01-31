---
layout: default
title: Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs
---

# Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs
**arXiv**：[2601.21233v1](https://arxiv.org/abs/2601.21233) · [PDF](https://arxiv.org/pdf/2601.21233.pdf)  
**作者**：Xiang Zheng, Yutao Wu, Hanxun Huang, Yige Li, Xingjun Ma, Bo Li, Yu-Gang Jiang, Cong Wang  

**一句话要点**：提出JustAsk框架，通过自主探索揭示代码代理中系统提示的安全漏洞

**关键词**：代码代理安全, 系统提示提取, 自主探索框架, LLM攻击面, 黑盒评估

## 3 点简述
- 核心问题：代码代理的自主性扩展了LLM攻击面，导致系统提示提取成为新兴安全风险
- 方法要点：JustAsk无需人工提示或监督，通过在线探索和分层技能空间自主发现提取策略
- 实验或效果：在41个黑盒商业模型上评估，实现近乎完整的系统提示恢复，暴露设计级漏洞

## 摘要（原文）

> Autonomous code agents built on large language models are reshaping software and AI development through tool use, long-horizon reasoning, and self-directed interaction. However, this autonomy introduces a previously unrecognized security risk: agentic interaction fundamentally expands the LLM attack surface, enabling systematic probing and recovery of hidden system prompts that guide model behavior. We identify system prompt extraction as an emergent vulnerability intrinsic to code agents and present \textbf{\textsc{JustAsk}}, a self-evolving framework that autonomously discovers effective extraction strategies through interaction alone. Unlike prior prompt-engineering or dataset-based attacks, \textsc{JustAsk} requires no handcrafted prompts, labeled supervision, or privileged access beyond standard user interaction. It formulates extraction as an online exploration problem, using Upper Confidence Bound-based strategy selection and a hierarchical skill space spanning atomic probes and high-level orchestration. These skills exploit imperfect system-instruction generalization and inherent tensions between helpfulness and safety. Evaluated on \textbf{41} black-box commercial models across multiple providers, \textsc{JustAsk} consistently achieves full or near-complete system prompt recovery, revealing recurring design- and architecture-level vulnerabilities. Our results expose system prompts as a critical yet largely unprotected attack surface in modern agent systems.

