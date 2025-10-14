---
layout: default
title: Guiding Energy-Efficient Locomotion through Impact Mitigation Rewards
---

# Guiding Energy-Efficient Locomotion through Impact Mitigation Rewards
**arXiv**：[2510.09543v1](https://arxiv.org/abs/2510.09543) · [PDF](https://arxiv.org/pdf/2510.09543.pdf)  
**作者**：Chenghao Wang, Arjun Viswanathan, Eric Sihite, Alireza Ramezani  

**一句话要点**：提出基于冲击缓解因子的奖励项，以提升机器人能量效率。

**关键词**：能量效率优化, 强化学习, 冲击缓解因子, 被动动态, 机器人运动控制

## 3 点简述
- 模仿学习忽略被动动态，导致机器人运动能量效率不足。
- 结合冲击缓解因子与对抗运动先验，学习显式轨迹与隐式动态。
- 实验显示成本运输降低达32%，验证能量效率提升。

## 摘要（原文）

> Animals achieve energy-efficient locomotion by their implicit passive
> dynamics, a marvel that has captivated roboticists for decades.Recently,
> methods incorporated Adversarial Motion Prior (AMP) and Reinforcement learning
> (RL) shows promising progress to replicate Animals' naturalistic motion.
> However, such imitation learning approaches predominantly capture explicit
> kinematic patterns, so-called gaits, while overlooking the implicit passive
> dynamics. This work bridges this gap by incorporating a reward term guided by
> Impact Mitigation Factor (IMF), a physics-informed metric that quantifies a
> robot's ability to passively mitigate impacts. By integrating IMF with AMP, our
> approach enables RL policies to learn both explicit motion trajectories from
> animal reference motion and the implicit passive dynamic. We demonstrate energy
> efficiency improvements of up to 32%, as measured by the Cost of Transport
> (CoT), across both AMP and handcrafted reward structure.

