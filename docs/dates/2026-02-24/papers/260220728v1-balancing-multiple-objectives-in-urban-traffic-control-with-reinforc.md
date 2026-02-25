---
layout: default
title: Balancing Multiple Objectives in Urban Traffic Control with Reinforcement Learning from AI Feedback
---

# Balancing Multiple Objectives in Urban Traffic Control with Reinforcement Learning from AI Feedback
**arXiv**：[2602.20728v1](https://arxiv.org/abs/2602.20728) · [PDF](https://arxiv.org/pdf/2602.20728.pdf)  
**作者**：Chenyang Zhao, Vinny Cahill, Ivana Dusparic  

**一句话要点**：提出多目标RLAIF方法以解决城市交通控制中多目标平衡问题

**关键词**：多目标强化学习, AI反馈强化学习, 城市交通控制, 偏好学习, 奖励设计

## 3 点简述
- 核心问题：多目标强化学习中奖励设计困难，易导致策略偏向主导目标
- 方法要点：扩展RLAIF至多目标系统，利用LLM生成偏好标签替代人工标注
- 实验或效果：未知具体实验细节，但声称能生成反映不同用户优先级的平衡策略

## 摘要（原文）

> Reward design has been one of the central challenges for real world reinforcement learning (RL) deployment, especially in settings with multiple objectives. Preference-based RL offers an appealing alternative by learning from human preferences over pairs of behavioural outcomes. More recently, RL from AI feedback (RLAIF) has demonstrated that large language models (LLMs) can generate preference labels at scale, mitigating the reliance on human annotators. However, existing RLAIF work typically focuses only on single-objective tasks, leaving the open question of how RLAIF handles systems that involve multiple objectives. In such systems trade-offs among conflicting objectives are difficult to specify, and policies risk collapsing into optimizing for a dominant goal. In this paper, we explore the extension of the RLAIF paradigm to multi-objective self-adaptive systems. We show that multi-objective RLAIF can produce policies that yield balanced trade-offs reflecting different user priorities without laborious reward engineering. We argue that integrating RLAIF into multi-objective RL offers a scalable path toward user-aligned policy learning in domains with inherently conflicting objectives.

