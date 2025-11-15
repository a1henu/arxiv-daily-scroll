---
layout: default
title: Harnessing Bounded-Support Evolution Strategies for Policy Refinement
---

# Harnessing Bounded-Support Evolution Strategies for Policy Refinement
**arXiv**：[2511.09923v1](https://arxiv.org/abs/2511.09923) · [PDF](https://arxiv.org/pdf/2511.09923.pdf)  
**作者**：Ethan Hirschowitz, Fabio Ramos  

**一句话要点**：提出三角分布进化策略以解决机器人策略精炼中的梯度噪声问题

**关键词**：进化策略, 策略精炼, 机器人操作, 无梯度优化, 强化学习

## 3 点简述
- 核心问题：在线策略强化学习在机器人策略精炼中面临梯度噪声大、信号弱的问题
- 方法要点：使用有界三角噪声和中心秩有限差分估计器实现稳定、可并行、无梯度更新
- 实验或效果：在机器人操作任务中，相比PPO提升成功率26.5%，显著降低方差

## 摘要（原文）

> Improving competent robot policies with on-policy RL is often hampered by noisy, low-signal gradients. We revisit Evolution Strategies (ES) as a policy-gradient proxy and localize exploration with bounded, antithetic triangular perturbations, suitable for policy refinement. We propose Triangular-Distribution ES (TD-ES) which pairs bounded triangular noise with a centered-rank finite-difference estimator to deliver stable, parallelizable, gradient-free updates. In a two-stage pipeline -- PPO pretraining followed by TD-ES refinement -- this preserves early sample efficiency while enabling robust late-stage gains. Across a suite of robotic manipulation tasks, TD-ES raises success rates by 26.5% relative to PPO and greatly reduces variance, offering a simple, compute-light path to reliable refinement.

