---
layout: default
title: InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents
---

# InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents
**arXiv**：[2601.03204v1](https://arxiv.org/abs/2601.03204) · [PDF](https://arxiv.org/pdf/2601.03204.pdf)  
**作者**：Chenglin Yu, Yuchen Wang, Songmiao Wang, Hongxia Yang, Ming Li  

**一句话要点**：提出InfiAgent框架，通过外部化状态解决LLM智能体在长时任务中的上下文增长和错误累积问题。

**关键词**：长时任务智能体, 状态外部化, 上下文管理, 通用智能体框架, 文件中心抽象

## 3 点简述
- 核心问题：LLM智能体在长时任务中因上下文无限增长和错误累积而失效。
- 方法要点：采用文件中心状态抽象，将持久状态外部化，保持推理上下文严格有界。
- 实验或效果：在DeepResearch和80篇文献综述任务中，无需任务特定微调，性能媲美大型专有系统，长时覆盖率高。

## 摘要（原文）

> LLM agents can reason and use tools, but they often break down on long-horizon tasks due to unbounded context growth and accumulated errors. Common remedies such as context compression or retrieval-augmented prompting introduce trade-offs between information fidelity and reasoning stability. We present InfiAgent, a general-purpose framework that keeps the agent's reasoning context strictly bounded regardless of task duration by externalizing persistent state into a file-centric state abstraction. At each step, the agent reconstructs context from a workspace state snapshot plus a fixed window of recent actions. Experiments on DeepResearch and an 80-paper literature review task show that, without task-specific fine-tuning, InfiAgent with a 20B open-source model is competitive with larger proprietary systems and maintains substantially higher long-horizon coverage than context-centric baselines. These results support explicit state externalization as a practical foundation for stable long-horizon agents. Github Repo:https://github.com/ChenglinPoly/infiAgent

