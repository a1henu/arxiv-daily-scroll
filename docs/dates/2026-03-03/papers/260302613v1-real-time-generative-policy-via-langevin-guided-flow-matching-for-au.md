---
layout: default
title: Real-Time Generative Policy via Langevin-Guided Flow Matching for Autonomous Driving
---

# Real-Time Generative Policy via Langevin-Guided Flow Matching for Autonomous Driving
**arXiv**：[2603.02613v1](https://arxiv.org/abs/2603.02613) · [PDF](https://arxiv.org/pdf/2603.02613.pdf)  
**作者**：Tianze Zhu, Yinuo Wang, Wenjun Zou, Tianyi Zhang, Likun Wang, Letian Tao, Feihong Zhang, Yao Lyu, Shengbo Eben Li  

**一句话要点**：提出DACER-F算法，通过流匹配实现自动驾驶中实时生成策略，降低推理延迟。

**关键词**：自动驾驶, 强化学习, 流匹配, 朗之万动力学, 实时决策, 生成策略

## 3 点简述
- 问题：生成策略在自动驾驶中推理延迟高，阻碍实时决策部署。
- 方法：引入流匹配和朗之万动力学，单步推理生成动作，平衡Q值与探索。
- 效果：在复杂模拟和标准基准上超越基线，保持超低延迟和高性能。

## 摘要（原文）

> Reinforcement learning (RL) is a fundamental methodology in autonomous driving systems, where generative policies exhibit considerable potential by leveraging their ability to model complex distributions to enhance exploration. However, their inherent high inference latency severely impedes their deployment in real-time decision-making and control. To address this issue, we propose diffusion actor-critic with entropy regulator via flow matching (DACER-F) by introducing flow matching into online RL, enabling the generation of competitive actions in a single inference step. By leveraging Langevin dynamics and gradients of the Q-function, DACER-F dynamically optimizes actions from experience replay toward a target distribution that balances high Q-value information with exploratory behavior. The flow policy is then trained to efficiently learn a mapping from a simple prior distribution to this dynamic target. In complex multi-lane and intersection simulations, DACER-F outperforms baselines diffusion actor-critic with entropy regulator (DACER) and distributional soft actor-critic (DSAC), while maintaining an ultra-low inference latency. DACER-F further demonstrates its scalability on standard RL benchmark DeepMind Control Suite (DMC), achieving a score of 775.8 in the humanoid-stand task and surpassing prior methods. Collectively, these results establish DACER-F as a high-performance and computationally efficient RL algorithm.

