---
layout: default
title: Learning Safe Autonomous Driving Policies Using Predictive Safety Representations
---

# Learning Safe Autonomous Driving Policies Using Predictive Safety Representations
**arXiv**：[2512.17586v1](https://arxiv.org/abs/2512.17586) · [PDF](https://arxiv.org/pdf/2512.17586.pdf)  
**作者**：Mahesh Keswani, Raunak Bhattacharyya  

**一句话要点**：提出SRPL框架，利用预测安全表示提升自动驾驶安全强化学习的奖励-安全权衡

**关键词**：安全强化学习, 自动驾驶策略, 预测安全表示, 奖励-安全权衡, 跨数据集泛化

## 3 点简述
- 核心问题：自动驾驶中安全强化学习存在奖励与安全目标间的根本张力，保守策略降低效率，激进探索危及安全。
- 方法要点：SRPL框架通过预测未来约束违规模型，增强智能体对安全风险的预见能力，以优化策略学习。
- 实验或效果：在Waymo和NuPlan数据集上，SRPL显著提高成功率、降低成本，并增强对观测噪声的鲁棒性和跨数据集泛化能力。

## 摘要（原文）

> Safe reinforcement learning (SafeRL) is a prominent paradigm for autonomous driving, where agents are required to optimize performance under strict safety requirements. This dual objective creates a fundamental tension, as overly conservative policies limit driving efficiency while aggressive exploration risks safety violations. The Safety Representations for Safer Policy Learning (SRPL) framework addresses this challenge by equipping agents with a predictive model of future constraint violations and has shown promise in controlled environments. This paper investigates whether SRPL extends to real-world autonomous driving scenarios. Systematic experiments on the Waymo Open Motion Dataset (WOMD) and NuPlan demonstrate that SRPL can improve the reward-safety tradeoff, achieving statistically significant improvements in success rate (effect sizes r = 0.65-0.86) and cost reduction (effect sizes r = 0.70-0.83), with p < 0.05 for observed improvements. However, its effectiveness depends on the underlying policy optimizer and the dataset distribution. The results further show that predictive safety representations play a critical role in improving robustness to observation noise. Additionally, in zero-shot cross-dataset evaluation, SRPL-augmented agents demonstrate improved generalization compared to non-SRPL methods. These findings collectively demonstrate the potential of predictive safety representations to strengthen SafeRL for autonomous driving.

