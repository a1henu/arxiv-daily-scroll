---
layout: default
title: PDE-Agent: A toolchain-augmented multi-agent framework for PDE solving
---

# PDE-Agent: A toolchain-augmented multi-agent framework for PDE solving
**arXiv**：[2512.16214v1](https://arxiv.org/abs/2512.16214) · [PDF](https://arxiv.org/pdf/2512.16214.pdf)  
**作者**：Jianming Liu, Ren Zhu, Jian Xu, Kun Ding, Xu-Yao Zhang, Gaofeng Meng, Cheng-Lin Liu  

**一句话要点**：提出PDE-Agent，首个工具链增强的多智能体框架，用于从自然语言描述自动求解偏微分方程。

**关键词**：偏微分方程求解, 多智能体协作, 工具链增强, 自动化科学计算, LLM驱动智能体

## 3 点简述
- 核心问题：传统PDE求解方法依赖专家知识，现有神经网络方法缺乏完全自主性。
- 方法要点：基于LLM驱动智能体，通过Prog-Act框架和Resource-Pool实现多智能体与多工具协作。
- 实验或效果：在PDE-Bench基准测试中，PDE-Agent在复杂多步任务中表现出优越适用性和性能。

## 摘要（原文）

> Solving Partial Differential Equations (PDEs) is a cornerstone of engineering and scientific research. Traditional methods for PDE solving are cumbersome, relying on manual setup and domain expertise. While Physics-Informed Neural Network (PINNs) introduced end-to-end neural network-based solutions, and frameworks like DeepXDE further enhanced automation, these approaches still depend on expert knowledge and lack full autonomy. In this work, we frame PDE solving as tool invocation via LLM-driven agents and introduce PDE-Agent, the first toolchain-augmented multi-agent collaboration framework, inheriting the reasoning capacity of LLMs and the controllability of external tools and enabling automated PDE solving from natural language descriptions. PDE-Agent leverages the strengths of multi-agent and multi-tool collaboration through two key innovations: (1) A Prog-Act framework with graph memory for multi-agent collaboration, which enables effective dynamic planning and error correction via dual-loop mechanisms (localized fixes and global revisions). (2) A Resource-Pool integrated with a tool-parameter separation mechanism for multi-tool collaboration. This centralizes the management of runtime artifacts and resolves inter-tool dependency gaps in existing frameworks. To validate and evaluate this new paradigm for PDE solving , we develop PDE-Bench, a multi-type PDE Benchmark for agent-based tool collaborative solving, and propose multi-level metrics for assessing tool coordination. Evaluations verify that PDE-Agent exhibits superior applicability and performance in complex multi-step, cross-step dependent tasks. This new paradigm of toolchain-augmented multi-agent PDE solving will further advance future developments in automated scientific computing. Our source code and dataset will be made publicly available.

