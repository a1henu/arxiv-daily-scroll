---
layout: default
title: WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning
---

# WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning
**arXiv**：[2602.17025v1](https://arxiv.org/abs/2602.17025) · [PDF](https://arxiv.org/pdf/2602.17025.pdf)  
**作者**：Gagan Mundada, Zihan Huang, Rohan Surana, Sheldon Yu, Jennifer Yuntong Zhang, Xintong Li, Tong Yu, Lina Yao, Jingbo Shang, Julian McAuley, Junda Wu  

**一句话要点**：提出WS-GRPO以解决GRPO在推理任务中因过度思考导致的低效问题

**关键词**：弱监督学习, 策略优化, 推理效率, 语言模型训练, 偏好模型

## 3 点简述
- 核心问题：GRPO在复杂推理中因相对目标导致过度思考，降低推理效率
- 方法要点：利用弱监督从终端奖励生成前缀级信号，指导继续或停止推理
- 实验或效果：在推理基准上显著减少推理长度，同时保持与基线相当的准确性

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) is effective for training language models on complex reasoning. However, since the objective is defined relative to a group of sampled trajectories, extended deliberation can create more chances to realize relative gains, leading to inefficient reasoning and overthinking, and complicating the trade-off between correctness and rollout efficiency. Controlling this behavior is difficult in practice, considering (i) Length penalties are hard to calibrate because longer rollouts may reflect harder problems that require longer reasoning, penalizing tokens risks truncating useful reasoning along with redundant continuation; and (ii) supervision that directly indicates when to continue or stop is typically unavailable beyond final answer correctness. We propose Weakly Supervised GRPO (WS-GRPO), which improves rollout efficiency by converting terminal rewards into correctness-aware guidance over partial trajectories. Unlike global length penalties that are hard to calibrate, WS-GRPO trains a preference model from outcome-only correctness to produce prefix-level signals that indicate when additional continuation is beneficial. Thus, WS-GRPO supplies outcome-derived continue/stop guidance, reducing redundant deliberation while maintaining accuracy. We provide theoretical results and empirically show on reasoning benchmarks that WS-GRPO substantially reduces rollout length while remaining competitive with GRPO baselines.

