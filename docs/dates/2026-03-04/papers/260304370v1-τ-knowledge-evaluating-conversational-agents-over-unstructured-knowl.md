---
layout: default
title: $τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge
---

# $τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge
**arXiv**：[2603.04370v1](https://arxiv.org/abs/2603.04370) · [PDF](https://arxiv.org/pdf/2603.04370.pdf)  
**作者**：Quan Shi, Alexandra Zytek, Pedram Razavi, Karthik Narasimhan, Victor Barres  

**一句话要点**：提出τ-Knowledge以评估对话代理在非结构化知识环境中的协调能力

**关键词**：对话代理评估, 非结构化知识整合, 长程交互, 金融科技客服, 检索与工具协调

## 3 点简述
- 核心问题：现有基准独立评估检索或工具使用，缺乏对非结构化知识在长程交互中整合的全面评估
- 方法要点：扩展τ-Bench，引入τ-Banking领域模拟金融科技客服工作流，要求代理协调外部知识与工具输出
- 实验或效果：前沿模型在嵌入检索和终端搜索中仅达约25.5%通过率，可靠性随重复试验急剧下降

## 摘要（原文）

> Conversational agents are increasingly deployed in knowledge-intensive settings, where correct behavior depends on retrieving and applying domain-specific knowledge from large, proprietary, and unstructured corpora during live interactions with users. Yet most existing benchmarks evaluate retrieval or tool use independently of each other, creating a gap in realistic, fully agentic evaluation over unstructured data in long-horizon interactions. We introduce $τ$-Knowledge, an extension of $τ$-Bench for evaluating agents in environments where success depends on coordinating external, natural-language knowledge with tool outputs to produce verifiable, policy-compliant state changes. Our new domain, $τ$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates. Across embedding-based retrieval and terminal-based search, even frontier models with high reasoning budgets achieve only $\sim$25.5% pass^1, with reliability degrading sharply over repeated trials. Agents struggle to retrieve the correct documents from densely interlinked knowledge bases and to reason accurately over complex internal policies. Overall, $τ$-Knowledge provides a realistic testbed for developing agents that integrate unstructured knowledge in human-facing deployments.

