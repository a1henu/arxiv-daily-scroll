---
layout: default
title: Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty
---

# Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty
**arXiv**：[2601.00737v1](https://arxiv.org/abs/2601.00737) · [PDF](https://arxiv.org/pdf/2601.00737.pdf)  
**作者**：Uğurcan Özalp  

**一句话要点**：提出随机演员-评论家算法，通过时域偶然不确定性缓解强化学习中的价值高估问题。

**关键词**：强化学习, 演员-评论家方法, 价值高估缓解, 时域不确定性, 分布评论家, dropout正则化

## 3 点简述
- 核心问题：离策略演员-评论家方法中评论家网络倾向于系统性高估价值估计，影响性能。
- 方法要点：引入时域偶然不确定性（源于随机转移、奖励和策略变化）来缩放悲观偏差，使用单一分布评论家网络建模不确定性。
- 实验或效果：算法在随机环境中实现风险规避行为，通过dropout正则化提升训练稳定性和计算效率。

## 摘要（原文）

> Off-policy actor-critic methods in reinforcement learning train a critic with temporal-difference updates and use it as a learning signal for the policy (actor). This design typically achieves higher sample efficiency than purely on-policy methods. However, critic networks tend to overestimate value estimates systematically. This is often addressed by introducing a pessimistic bias based on uncertainty estimates. Current methods employ ensembling to quantify the critic's epistemic uncertainty-uncertainty due to limited data and model ambiguity-to scale pessimistic updates. In this work, we propose a new algorithm called Stochastic Actor-Critic (STAC) that incorporates temporal (one-step) aleatoric uncertainty-uncertainty arising from stochastic transitions, rewards, and policy-induced variability in Bellman targets-to scale pessimistic bias in temporal-difference updates, rather than relying on epistemic uncertainty. STAC uses a single distributional critic network to model the temporal return uncertainty, and applies dropout to both the critic and actor networks for regularization. Our results show that pessimism based on a distributional critic alone suffices to mitigate overestimation, and naturally leads to risk-averse behavior in stochastic environments. Introducing dropout further improves training stability and performance by means of regularization. With this design, STAC achieves improved computational efficiency using a single distributional critic network.

