---
layout: default
title: The Art of Efficient Reasoning: Data, Reward, and Optimization
---

# The Art of Efficient Reasoning: Data, Reward, and Optimization
**arXiv**：[2602.20945v1](https://arxiv.org/abs/2602.20945) · [PDF](https://arxiv.org/pdf/2602.20945.pdf)  
**作者**：Taiqiang Wu, Zenan Zu, Bo Zhou, Ngai Wong  

**一句话要点**：系统研究大语言模型高效推理机制，提出训练策略以避免长度崩溃并提升泛化能力。

**关键词**：大语言模型, 高效推理, 强化学习, 奖励塑造, 长度适应, 泛化能力

## 3 点简述
- 核心问题：大语言模型链式思维推理计算开销大，需激励短而准确的思考轨迹。
- 方法要点：通过强化学习奖励塑造，揭示两阶段训练范式（长度适应与推理精炼），并训练于相对简单提示以确保正奖励信号密度。
- 实验或效果：在统一协议下进行大规模实验（约20万GPU小时），验证策略在Qwen3系列模型（0.6B至30B）中的鲁棒性和泛化性。

## 摘要（原文）

> Large Language Models (LLMs) consistently benefit from scaled Chain-of-Thought (CoT) reasoning, but also suffer from heavy computational overhead. To address this issue, efficient reasoning aims to incentivize short yet accurate thinking trajectories, typically through reward shaping with Reinforcement Learning (RL). In this paper, we systematically investigate the mechanics of efficient reasoning for LLMs. For comprehensive evaluation, we advocate for more fine-grained metrics, including length distribution conditioned on correctness and performance across a wide spectrum of token budgets ranging from 2k to 32k. First, we reveal that the training process follows a two-stage paradigm: length adaptation and reasoning refinement. After that, we conduct extensive experiments (about 0.2 million GPU hours) in a unified protocol, deconstructing training prompts and rollouts, reward shaping, and optimization strategies. In particular, a key finding is to train on relatively easier prompts, ensuring the density of positive reward signals and thus avoiding the length collapse. Meanwhile, the learned length bias can be generalized across domains. We distill all findings into valuable insights and practical guidelines, and further validate them across the Qwen3 series, ranging from 0.6B to 30B, demonstrating the robustness and generalization.

