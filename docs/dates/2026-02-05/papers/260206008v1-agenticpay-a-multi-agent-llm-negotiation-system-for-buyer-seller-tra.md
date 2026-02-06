---
layout: default
title: AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions
---

# AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions
**arXiv**：[2602.06008v1](https://arxiv.org/abs/2602.06008) · [PDF](https://arxiv.org/pdf/2602.06008.pdf)  
**作者**：Xianyang Liu, Shangding Gu, Dawn Song  

**一句话要点**：提出AgenticPay基准与仿真框架，用于评估多智能体买家-卖家语言谈判系统。

**关键词**：多智能体谈判, 语言经济交互, 基准测试, 仿真框架, 战略推理

## 3 点简述
- 核心问题：现有基准缺乏评估多智能体语言经济交互的原则性设置。
- 方法要点：建模私有约束和产品估值，支持多轮语言谈判和110+任务。
- 实验或效果：基准测试显示先进LLM在谈判性能和战略推理上存在显著差距。

## 摘要（原文）

> Large language model (LLM)-based agents are increasingly expected to negotiate, coordinate, and transact autonomously, yet existing benchmarks lack principled settings for evaluating language-mediated economic interaction among multiple agents. We introduce AgenticPay, a benchmark and simulation framework for multi-agent buyer-seller negotiation driven by natural language. AgenticPay models markets in which buyers and sellers possess private constraints and product-dependent valuations, and must reach agreements through multi-round linguistic negotiation rather than numeric bidding alone. The framework supports a diverse suite of over 110 tasks ranging from bilateral bargaining to many-to-many markets, with structured action extraction and metrics for feasibility, efficiency, and welfare. Benchmarking state-of-the-art proprietary and open-weight LLMs reveals substantial gaps in negotiation performance and highlights challenges in long-horizon strategic reasoning, establishing AgenticPay as a foundation for studying agentic commerce and language-based market interaction. Code and dataset are available at the link: https://github.com/SafeRL-Lab/AgenticPay.

