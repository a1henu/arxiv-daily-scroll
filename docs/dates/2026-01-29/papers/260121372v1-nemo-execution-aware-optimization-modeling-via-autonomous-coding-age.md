---
layout: default
title: NEMO: Execution-Aware Optimization Modeling via Autonomous Coding Agents
---

# NEMO: Execution-Aware Optimization Modeling via Autonomous Coding Agents
**arXiv**：[2601.21372v1](https://arxiv.org/abs/2601.21372) · [PDF](https://arxiv.org/pdf/2601.21372.pdf)  
**作者**：Yang Song, Anoushka Vyas, Zirui Wei, Sina Khoshfetrat Pakazad, Henrik Ohlsson, Graham Neubig  

**一句话要点**：提出NEMO系统，通过自主编码代理将自然语言决策问题转化为可执行优化实现。

**关键词**：自主编码代理, 优化建模, 自然语言处理, 可执行代码生成, 代理协调模式

## 3 点简述
- 核心问题：现有方法依赖专用大语言模型或定制代理，常生成无效或不可执行代码，脆弱且复杂。
- 方法要点：以自主编码代理为核心抽象，支持沙盒执行确保代码可执行，引入协调模式如非对称验证循环和外部记忆。
- 实验或效果：在九个优化基准测试中，多数任务达到最先进性能，部分数据集优势显著。

## 摘要（原文）

> In this paper, we present NEMO, a system that translates Natural-language descriptions of decision problems into formal Executable Mathematical Optimization implementations, operating collaboratively with users or autonomously. Existing approaches typically rely on specialized large language models (LLMs) or bespoke, task-specific agents. Such methods are often brittle, complex and frequently generating syntactically invalid or non-executable code.
>   NEMO instead centers on remote interaction with autonomous coding agents (ACAs), treated as a first-class abstraction analogous to API-based interaction with LLMs. This design enables the construction of higher-level systems around ACAs that structure, consolidate, and iteratively refine task specifications. Because ACAs execute within sandboxed environments, code produced by NEMO is executable by construction, allowing automated validation and repair.
>   Building on this, we introduce novel coordination patterns with and across ACAs, including asymmetric validation loops between independently generated optimizer and simulator implementations (serving as a high-level validation mechanism), external memory for experience reuse, and robustness enhancements via minimum Bayes risk (MBR) decoding and self-consistency. We evaluate NEMO on nine established optimization benchmarks. As depicted in Figure 1, it achieves state-of-the-art performance on the majority of tasks, with substantial margins on several datasets, demonstrating the power of execution-aware agentic architectures for automated optimization modeling.

