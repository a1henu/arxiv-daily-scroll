---
layout: default
title: Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic
---

# Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic
**arXiv**：[2601.22970v1](https://arxiv.org/abs/2601.22970) · [PDF](https://arxiv.org/pdf/2601.22970.pdf)  
**作者**：Jeong Woon Lee, Kyoleen Kwak, Daeho Kim, Hyoseok Hwang  

**一句话要点**：提出PAVE框架以稳定Q梯度场，解决连续行动者-评论者方法中策略振荡问题

**关键词**：连续行动者-评论者方法, 策略平滑性, Q梯度场稳定, 评论者正则化, 微分几何分析, 强化学习部署

## 3 点简述
- 核心问题：连续行动者-评论者方法学到的策略常出现高频振荡，不适合物理部署。
- 方法要点：通过理论分析，证明策略平滑性受评论者微分几何控制，引入PAVE框架正则化评论者以稳定Q梯度场。
- 实验或效果：PAVE在保持任务性能的同时，实现与策略侧正则化方法相当的平滑性和鲁棒性，无需修改行动者。

## 摘要（原文）

> Policies learned via continuous actor-critic methods often exhibit erratic, high-frequency oscillations, making them unsuitable for physical deployment. Current approaches attempt to enforce smoothness by directly regularizing the policy's output. We argue that this approach treats the symptom rather than the cause. In this work, we theoretically establish that policy non-smoothness is fundamentally governed by the differential geometry of the critic. By applying implicit differentiation to the actor-critic objective, we prove that the sensitivity of the optimal policy is bounded by the ratio of the Q-function's mixed-partial derivative (noise sensitivity) to its action-space curvature (signal distinctness). To empirically validate this theoretical insight, we introduce PAVE (Policy-Aware Value-field Equalization), a critic-centric regularization framework that treats the critic as a scalar field and stabilizes its induced action-gradient field. PAVE rectifies the learning signal by minimizing the Q-gradient volatility while preserving local curvature. Experimental results demonstrate that PAVE achieves smoothness and robustness comparable to policy-side smoothness regularization methods, while maintaining competitive task performance, without modifying the actor.

