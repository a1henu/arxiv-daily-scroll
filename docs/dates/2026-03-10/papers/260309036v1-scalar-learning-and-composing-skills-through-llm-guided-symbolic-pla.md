---
layout: default
title: SCALAR: Learning and Composing Skills through LLM Guided Symbolic Planning and Deep RL Grounding
---

# SCALAR: Learning and Composing Skills through LLM Guided Symbolic Planning and Deep RL Grounding
**arXiv**：[2603.09036v1](https://arxiv.org/abs/2603.09036) · [PDF](https://arxiv.org/pdf/2603.09036.pdf)  
**作者**：Renos Zabounidis, Yue Wu, Simon Stepputtis, Woojun Kim, Yuanzhi Li, Tom Mitchell, Katia Sycara  

**一句话要点**：提出SCALAR框架，通过LLM规划与RL双向耦合解决语言到低层控制的落地问题

**关键词**：技能学习, 符号规划, 深度强化学习, 语言模型代理, 双向耦合框架

## 3 点简述
- 核心问题：LLM代理在低层控制中难以落地语言指令，现有方法缺乏反馈修正错误
- 方法要点：LLM规划技能库，RL训练策略并反馈执行结果，迭代优化技能规范
- 实验或效果：在Craftax上实现88.2%钻石收集率，比最佳基线提升1.9倍

## 摘要（原文）

> LM-based agents excel when given high-level action APIs but struggle to ground language into low-level control. Prior work has LLMs generate skills or reward functions for RL, but these one-shot approaches lack feedback to correct specification errors. We introduce SCALAR, a bidirectional framework coupling LLM planning with RL through a learned skill library. The LLM proposes skills with preconditions and effects; RL trains policies for each skill and feeds back execution results to iteratively refine specifications, improving robustness to initial errors. Pivotal Trajectory Analysis corrects LLM priors by analyzing RL trajectories; Frontier Checkpointing optionally saves environment states at skill boundaries to improve sample efficiency. On Craftax, SCALAR achieves 88.2% diamond collection, a 1.9x improvement over the best baseline, and reaches the Gnomish Mines 9.1% of the time where prior methods fail entirely.

