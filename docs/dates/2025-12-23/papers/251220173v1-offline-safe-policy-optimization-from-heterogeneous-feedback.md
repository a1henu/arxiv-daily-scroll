---
layout: default
title: Offline Safe Policy Optimization From Heterogeneous Feedback
---

# Offline Safe Policy Optimization From Heterogeneous Feedback
**arXiv**：[2512.20173v1](https://arxiv.org/abs/2512.20173) · [PDF](https://arxiv.org/pdf/2512.20173.pdf)  
**作者**：Ze Gong, Pradeep Varakantham, Akshat Kumar  

**一句话要点**：提出PreSa框架，通过偏好与安全对齐直接学习离线安全策略，避免奖励和成本模型误差累积。

**关键词**：离线强化学习, 偏好学习, 安全策略优化, 连续控制, 拉格朗日优化, 人类反馈

## 3 点简述
- 核心问题：离线偏好强化学习中，长时域连续控制任务因奖励和成本模型误差累积导致安全策略性能下降。
- 方法要点：结合偏好学习和安全标签，在拉格朗日优化中直接学习奖励最大化安全策略，无需显式学习奖励和成本模型。
- 实验或效果：在连续控制任务中，使用合成和真实人类反馈评估，PreSa优于现有基线及基于真实奖励和成本的离线安全RL方法。

## 摘要（原文）

> Offline Preference-based Reinforcement Learning (PbRL) learns rewards and policies aligned with human preferences without the need for extensive reward engineering and direct interaction with human annotators. However, ensuring safety remains a critical challenge across many domains and tasks. Previous works on safe RL from human feedback (RLHF) first learn reward and cost models from offline data, then use constrained RL to optimize a safe policy. While such an approach works in the contextual bandits settings (LLMs), in long horizon continuous control tasks, errors in rewards and costs accumulate, leading to impairment in performance when used with constrained RL methods. To address these challenges, (a) instead of indirectly learning policies (from rewards and costs), we introduce a framework that learns a policy directly based on pairwise preferences regarding the agent's behavior in terms of rewards, as well as binary labels indicating the safety of trajectory segments; (b) we propose \textsc{PreSa} (Preference and Safety Alignment), a method that combines preference learning module with safety alignment in a constrained optimization problem. This optimization problem is solved within a Lagrangian paradigm that directly learns reward-maximizing safe policy \textit{without explicitly learning reward and cost models}, avoiding the need for constrained RL; (c) we evaluate our approach on continuous control tasks with both synthetic and real human feedback. Empirically, our method successfully learns safe policies with high rewards, outperforming state-of-the-art baselines, and offline safe RL approaches with ground-truth reward and cost.

