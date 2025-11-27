---
layout: default
title: Hybrid-AIRL: Enhancing Inverse Reinforcement Learning with Supervised Expert Guidance
---

# Hybrid-AIRL: Enhancing Inverse Reinforcement Learning with Supervised Expert Guidance
**arXiv**：[2511.21356v1](https://arxiv.org/abs/2511.21356) · [PDF](https://arxiv.org/pdf/2511.21356.pdf)  
**作者**：Bram Silue, Santiago Amaya-Corredor, Patrick Mannion, Lander Willem, Pieter Libin  

**一句话要点**：提出Hybrid-AIRL以增强逆强化学习在复杂稀疏奖励场景中的性能

**关键词**：逆强化学习, 对抗学习, 稀疏奖励, 专家指导, 策略学习, 奖励函数推断

## 3 点简述
- AIRL在复杂不确定环境中难以推断有效奖励函数，如HULHE扑克
- H-AIRL引入监督损失和随机正则化机制，改进奖励推断和策略学习
- 实验显示H-AIRL在样本效率和稳定性上优于AIRL，适用于现实挑战

## 摘要（原文）

> Adversarial Inverse Reinforcement Learning (AIRL) has shown promise in addressing the sparse reward problem in reinforcement learning (RL) by inferring dense reward functions from expert demonstrations. However, its performance in highly complex, imperfect-information settings remains largely unexplored. To explore this gap, we evaluate AIRL in the context of Heads-Up Limit Hold'em (HULHE) poker, a domain characterized by sparse, delayed rewards and significant uncertainty. In this setting, we find that AIRL struggles to infer a sufficiently informative reward function. To overcome this limitation, we contribute Hybrid-AIRL (H-AIRL), an extension that enhances reward inference and policy learning by incorporating a supervised loss derived from expert data and a stochastic regularization mechanism. We evaluate H-AIRL on a carefully selected set of Gymnasium benchmarks and the HULHE poker setting. Additionally, we analyze the learned reward function through visualization to gain deeper insights into the learning process. Our experimental results show that H-AIRL achieves higher sample efficiency and more stable learning compared to AIRL. This highlights the benefits of incorporating supervised signals into inverse RL and establishes H-AIRL as a promising framework for tackling challenging, real-world settings.

