---
layout: default
title: Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks
---

# Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks
**arXiv**：[2602.22817v1](https://arxiv.org/abs/2602.22817) · [PDF](https://arxiv.org/pdf/2602.22817.pdf)  
**作者**：Shuo He, Lang Feng, Qi Wei, Xin Cheng, Lei Feng, Bo An  

**一句话要点**：提出层次化组策略优化以解决长视野智能任务中的上下文不一致问题

**关键词**：强化学习, 长视野任务, 策略优化, 上下文一致性, 优势估计, 智能体学习

## 3 点简述
- 核心问题：基于组的强化学习在逐步策略优化中，因组内步骤历史上下文不一致导致优势估计偏差。
- 方法要点：通过将步骤分配到多个层次化组，计算组内优势并自适应加权聚合，优化偏差-方差权衡。
- 实验或效果：在ALFWorld和WebShop任务上，使用Qwen2.5模型，显著优于现有方法，无需额外模型或轨迹。

## 摘要（原文）

> Group-based reinforcement learning (RL), such as GRPO, has advanced the capabilities of large language models on long-horizon agentic tasks. To enable more fine-grained policy updates, recent research has increasingly shifted toward stepwise group-based policy optimization, which treats each step in a rollout trajectory independently while using a memory module to retain historical context. However, we find a key issue in estimating stepwise relative advantages, namely context inconsistency, where steps within the same group may differ in their historical contexts. Empirically, we reveal that this issue can lead to severely biased advantage estimation, thereby degrading policy optimization significantly. To address the issue, in this paper, we propose Hierarchy-of-Groups Policy Optimization (HGPO) for long-horizon agentic tasks. Specifically, within a group of rollout trajectories, HGPO assigns each step to multiple hierarchical groups according to the consistency of historical contexts. Then, for each step, HGPO computes distinct advantages within each group and aggregates them with an adaptive weighting scheme. In this way, HGPO can achieve a favorable bias-variance trade-off in stepwise advantage estimation, without extra models or rollouts. Evaluations on two challenging agentic tasks, ALFWorld and WebShop with Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct, show that HGPO significantly outperforms existing agentic RL methods under the same computational constraints. Code is available at https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo.

