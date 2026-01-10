---
layout: default
title: Internal Representations as Indicators of Hallucinations in Agent Tool Selection
---

# Internal Representations as Indicators of Hallucinations in Agent Tool Selection
**arXiv**：[2601.05214v1](https://arxiv.org/abs/2601.05214) · [PDF](https://arxiv.org/pdf/2601.05214.pdf)  
**作者**：Kait Healy, Bharathi Srinivasan, Visakh Madathil, Jing Wu  

**一句话要点**：提出基于内部表示的实时检测框架以解决代理工具选择中的幻觉问题

**关键词**：幻觉检测, 工具调用, 内部表示, 实时推理, 代理系统

## 3 点简述
- 核心问题：LLM在工具调用中产生幻觉，如错误工具选择、参数错误和工具绕过，影响可靠性和安全性
- 方法要点：利用LLM生成时的内部表示，在单次前向传播中实时检测幻觉，计算高效
- 实验或效果：在跨领域推理任务中评估，检测准确率高达86.4%，实时推理能力保持，计算开销最小

## 摘要（原文）

> Large Language Models (LLMs) have shown remarkable capabilities in tool calling and tool usage, but suffer from hallucinations where they choose incorrect tools, provide malformed parameters and exhibit 'tool bypass' behavior by performing simulations and generating outputs instead of invoking specialized tools or external systems. This undermines the reliability of LLM based agents in production systems as it leads to inconsistent results, and bypasses security and audit controls. Such hallucinations in agent tool selection require early detection and error handling. Unlike existing hallucination detection methods that require multiple forward passes or external validation, we present a computationally efficient framework that detects tool-calling hallucinations in real-time by leveraging LLMs' internal representations during the same forward pass used for generation. We evaluate this approach on reasoning tasks across multiple domains, demonstrating strong detection performance (up to 86.4\% accuracy) while maintaining real-time inference capabilities with minimal computational overhead, particularly excelling at detecting parameter-level hallucinations and inappropriate tool selections, critical for reliable agent deployment.

