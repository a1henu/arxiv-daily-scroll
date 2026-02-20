---
layout: default
title: IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents
---

# IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents
**arXiv**：[2602.17049v1](https://arxiv.org/abs/2602.17049) · [PDF](https://arxiv.org/pdf/2602.17049.pdf)  
**作者**：Seoyoung Lee, Seobin Yoon, Seongbeen Lee, Yoojung Chun, Dayoung Park, Doyeon Kim, Joo Yong Sim  

**一句话要点**：提出IntentCUA框架，通过意图级表示和共享记忆提升计算机使用代理的长时程执行稳定性与效率

**关键词**：计算机使用代理, 意图抽象, 多智能体规划, 共享记忆, 长时程任务, 桌面自动化

## 3 点简述
- 核心问题：现有方法在长时程任务中易偏离用户意图，重复解决常规子问题，导致错误累积和效率低下
- 方法要点：采用多智能体框架，抽象交互轨迹为多视图意图表示和可重用技能，通过共享记忆协调规划与优化
- 实验或效果：在端到端评估中，任务成功率74.83%，步骤效率比0.91，优于基于强化学习和轨迹检索的基线

## 摘要（原文）

> Computer-use agents operate over long horizons under noisy perception, multi-window contexts, evolving environment states. Existing approaches, from RL-based planners to trajectory retrieval, often drift from user intent and repeatedly solve routine subproblems, leading to error accumulation and inefficiency. We present IntentCUA, a multi-agent computer-use framework designed to stabilize long-horizon execution through intent-aligned plan memory. A Planner, Plan-Optimizer, and Critic coordinate over shared memory that abstracts raw interaction traces into multi-view intent representations and reusable skills. At runtime, intent prototypes retrieve subgroup-aligned skills and inject them into partial plans, reducing redundant re-planning and mitigating error propagation across desktop applications. In end-to-end evaluations, IntentCUA achieved a 74.83% task success rate with a Step Efficiency Ratio of 0.91, outperforming RL-based and trajectory-centric baselines. Ablations show that multi-view intent abstraction and shared plan memory jointly improve execution stability, with the cooperative multi-agent loop providing the largest gains on long-horizon tasks. These results highlight that system-level intent abstraction and memory-grounded coordination are key to reliable and efficient desktop automation in large, dynamic environments.

