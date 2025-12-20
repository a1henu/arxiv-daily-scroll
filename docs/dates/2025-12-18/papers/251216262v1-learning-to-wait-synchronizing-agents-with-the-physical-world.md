---
layout: default
title: Learning to Wait: Synchronizing Agents with the Physical World
---

# Learning to Wait: Synchronizing Agents with the Physical World
**arXiv**：[2512.16262v1](https://arxiv.org/abs/2512.16262) · [PDF](https://arxiv.org/pdf/2512.16262.pdf)  
**作者**：Yifei She, Ping Zhang, He Liu, Yanmin Jia, Yang Jing, Zijun Liu, Peng Sun, Xiangbin Li, Xiaohe Hu  

**一句话要点**：提出基于LLM的智能体侧方法，通过预测等待时间同步物理世界异步任务

**关键词**：智能体同步, 异步环境, 时间预测, 代码即行动, 上下文学习, Kubernetes模拟

## 3 点简述
- 核心问题：真实世界智能体任务存在动作延迟，导致时间差，传统环境侧方案限制可扩展性或增加冗余观察
- 方法要点：扩展代码即行动范式，利用语义先验和上下文学习预测精确等待时间，主动对齐认知时间线与物理世界
- 实验或效果：在模拟Kubernetes集群中验证，智能体能精确校准内部时钟，减少查询开销和执行延迟

## 摘要（原文）

> Real-world agentic tasks, unlike synchronous Markov Decision Processes (MDPs), often involve non-blocking actions with variable latencies, creating a fundamental \textit{Temporal Gap} between action initiation and completion. Existing environment-side solutions, such as blocking wrappers or frequent polling, either limit scalability or dilute the agent's context window with redundant observations. In this work, we propose an \textbf{Agent-side Approach} that empowers Large Language Models (LLMs) to actively align their \textit{Cognitive Timeline} with the physical world. By extending the Code-as-Action paradigm to the temporal domain, agents utilize semantic priors and In-Context Learning (ICL) to predict precise waiting durations (\texttt{time.sleep(t)}), effectively synchronizing with asynchronous environment without exhaustive checking. Experiments in a simulated Kubernetes cluster demonstrate that agents can precisely calibrate their internal clocks to minimize both query overhead and execution latency, validating that temporal awareness is a learnable capability essential for autonomous evolution in open-ended environments.

