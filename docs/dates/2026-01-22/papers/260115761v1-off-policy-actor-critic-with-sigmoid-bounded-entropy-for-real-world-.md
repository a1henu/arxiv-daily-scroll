---
layout: default
title: Off-Policy Actor-Critic with Sigmoid-Bounded Entropy for Real-World Robot Learning
---

# Off-Policy Actor-Critic with Sigmoid-Bounded Entropy for Real-World Robot Learning
**arXiv**：[2601.15761v1](https://arxiv.org/abs/2601.15761) · [PDF](https://arxiv.org/pdf/2601.15761.pdf)  
**作者**：Xiefeng Wu, Mingyu Hu, Shu Zhang  

**一句话要点**：提出SigEnt-SAC方法，通过sigmoid有界熵项解决真实世界机器人学习中的样本效率与稳定性问题。

**关键词**：离策略演员-评论家, sigmoid有界熵, 真实世界机器人学习, 样本效率, Q函数振荡, 稀疏奖励

## 3 点简述
- 核心问题：真实世界强化学习面临样本效率低、稀疏奖励和视觉噪声挑战，现有方法成本高或稳定性差。
- 方法要点：设计sigmoid有界熵项，防止负熵驱动优化导致分布外动作，减少Q函数振荡，支持从单条专家轨迹学习。
- 实验或效果：在D4RL基准上显著缓解Q函数振荡，更快达到100%成功率；真实机器人任务中，仅需少量交互即可学习成功策略。

## 摘要（原文）

> Deploying reinforcement learning in the real world remains challenging due to sample inefficiency, sparse rewards, and noisy visual observations. Prior work leverages demonstrations and human feedback to improve learning efficiency and robustness. However, offline-to-online methods need large datasets and can be unstable, while VLA-assisted RL relies on large-scale pretraining and fine-tuning. As a result, a low-cost real-world RL method with minimal data requirements has yet to emerge. We introduce \textbf{SigEnt-SAC}, an off-policy actor-critic method that learns from scratch using a single expert trajectory. Our key design is a sigmoid-bounded entropy term that prevents negative-entropy-driven optimization toward out-of-distribution actions and reduces Q-function oscillations. We benchmark SigEnt-SAC on D4RL tasks against representative baselines. Experiments show that SigEnt-SAC substantially alleviates Q-function oscillations and reaches a 100\% success rate faster than prior methods. Finally, we validate SigEnt-SAC on four real-world robotic tasks across multiple embodiments, where agents learn from raw images and sparse rewards; results demonstrate that SigEnt-SAC can learn successful policies with only a small number of real-world interactions, suggesting a low-cost and practical pathway for real-world RL deployment.

