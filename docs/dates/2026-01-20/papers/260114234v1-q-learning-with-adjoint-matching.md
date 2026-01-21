---
layout: default
title: Q-learning with Adjoint Matching
---

# Q-learning with Adjoint Matching
**arXiv**：[2601.14234v1](https://arxiv.org/abs/2601.14234) · [PDF](https://arxiv.org/pdf/2601.14234.pdf)  
**作者**：Qiyang Li, Sergey Levine  

**一句话要点**：提出QAM算法，通过伴随匹配解决连续动作强化学习中扩散策略的梯度优化难题

**关键词**：强化学习, 连续动作控制, 扩散策略, 伴随匹配, 时序差分学习

## 3 点简述
- 核心问题：连续动作RL中，扩散/流匹配策略的多步去噪过程导致基于梯度的优化数值不稳定
- 方法要点：利用伴随匹配技术转换评论家的动作梯度，构建无需反向传播的逐步目标函数
- 实验效果：在离线及离线到在线RL的稀疏奖励任务中，性能优于现有方法

## 摘要（原文）

> We propose Q-learning with Adjoint Matching (QAM), a novel TD-based reinforcement learning (RL) algorithm that tackles a long-standing challenge in continuous-action RL: efficient optimization of an expressive diffusion or flow-matching policy with respect to a parameterized Q-function. Effective optimization requires exploiting the first-order information of the critic, but it is challenging to do so for flow or diffusion policies because direct gradient-based optimization via backpropagation through their multi-step denoising process is numerically unstable. Existing methods work around this either by only using the value and discarding the gradient information, or by relying on approximations that sacrifice policy expressivity or bias the learned policy. QAM sidesteps both of these challenges by leveraging adjoint matching, a recently proposed technique in generative modeling, which transforms the critic's action gradient to form a step-wise objective function that is free from unstable backpropagation, while providing an unbiased, expressive policy at the optimum. Combined with temporal-difference backup for critic learning, QAM consistently outperforms prior approaches on hard, sparse reward tasks in both offline and offline-to-online RL.

