---
layout: default
title: SOMBRL: Scalable and Optimistic Model-Based RL
---

# SOMBRL: Scalable and Optimistic Model-Based RL
**arXiv**：[2511.20066v1](https://arxiv.org/abs/2511.20066) · [PDF](https://arxiv.org/pdf/2511.20066.pdf)  
**作者**：Bhavya Sukhija, Lenart Treven, Carmelo Sferrazza, Florian Dörfler, Pieter Abbeel, Andreas Krause  

**一句话要点**：提出SOMBRL以解决模型强化学习中高效探索的挑战

**关键词**：模型强化学习, 高效探索, 乐观不确定性, 非线性动态, 在线学习, 硬件验证

## 3 点简述
- 核心问题：模型强化学习中系统动态未知，需在线交互高效探索
- 方法要点：基于乐观不确定性原则，学习不确定性动态模型并优化奖励与不确定性加权和
- 实验或效果：在状态和视觉控制环境中表现优异，硬件测试优于现有方法

## 摘要（原文）

> We address the challenge of efficient exploration in model-based reinforcement learning (MBRL), where the system dynamics are unknown and the RL agent must learn directly from online interactions. We propose Scalable and Optimistic MBRL (SOMBRL), an approach based on the principle of optimism in the face of uncertainty. SOMBRL learns an uncertainty-aware dynamics model and greedily maximizes a weighted sum of the extrinsic reward and the agent's epistemic uncertainty. SOMBRL is compatible with any policy optimizers or planners, and under common regularity assumptions on the system, we show that SOMBRL has sublinear regret for nonlinear dynamics in the (i) finite-horizon, (ii) discounted infinite-horizon, and (iii) non-episodic settings. Additionally, SOMBRL offers a flexible and scalable solution for principled exploration. We evaluate SOMBRL on state-based and visual-control environments, where it displays strong performance across all tasks and baselines. We also evaluate SOMBRL on a dynamic RC car hardware and show SOMBRL outperforms the state-of-the-art, illustrating the benefits of principled exploration for MBRL.

