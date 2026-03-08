---
layout: default
title: SCoUT: Scalable Communication via Utility-Guided Temporal Grouping in Multi-Agent Reinforcement Learning
---

# SCoUT: Scalable Communication via Utility-Guided Temporal Grouping in Multi-Agent Reinforcement Learning
**arXiv**：[2603.04833v1](https://arxiv.org/abs/2603.04833) · [PDF](https://arxiv.org/pdf/2603.04833.pdf)  
**作者**：Manav Vora, Gokul Puthumanaillam, Hiroyasu Tsukamoto, Melkior Ornik  

**一句话要点**：提出SCoUT方法，通过效用引导的时序分组解决多智能体强化学习中的可扩展通信问题

**关键词**：多智能体强化学习, 可扩展通信, 时序分组, 反事实学习, 去中心化执行

## 3 点简述
- 核心问题：部分可观测MARL中通信时机与对象选择困难，单消息对奖励影响难以隔离
- 方法要点：使用Gumbel-Softmax进行软分组，结合组感知评论家与反事实通信优势实现精确信用分配
- 实验或效果：训练时集中化，执行时去中心化，降低评论家复杂度与方差，提升协调效率

## 摘要（原文）

> Communication can improve coordination in partially observed multi-agent reinforcement learning (MARL), but learning \emph{when} and \emph{who} to communicate with requires choosing among many possible sender-recipient pairs, and the effect of any single message on future reward is hard to isolate. We introduce \textbf{SCoUT} (\textbf{S}calable \textbf{Co}mmunication via \textbf{U}tility-guided \textbf{T}emporal grouping), which addresses both these challenges via temporal and agent abstraction within traditional MARL. During training, SCoUT resamples \textit{soft} agent groups every \(K\) environment steps (macro-steps) via Gumbel-Softmax; these groups are latent clusters that induce an affinity used as a differentiable prior over recipients. Using the same assignments, a group-aware critic predicts values for each agent group and maps them to per-agent baselines through the same soft assignments, reducing critic complexity and variance. Each agent is trained with a three-headed policy: environment action, send decision, and recipient selection. To obtain precise communication learning signals, we derive counterfactual communication advantages by analytically removing each sender's contribution from the recipient's aggregated messages. This counterfactual computation enables precise credit assignment for both send and recipient-selection decisions. At execution time, all centralized training components are discarded and only the per-agent policy is run, preserving decentralized execution. Project website, videos and code: \hyperlink{https://scout-comm.github.io/}{https://scout-comm.github.io/}

