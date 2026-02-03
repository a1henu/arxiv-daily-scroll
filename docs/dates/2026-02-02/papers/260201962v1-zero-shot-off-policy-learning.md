---
layout: default
title: Zero-Shot Off-Policy Learning
---

# Zero-Shot Off-Policy Learning
**arXiv**：[2602.01962v1](https://arxiv.org/abs/2602.01962) · [PDF](https://arxiv.org/pdf/2602.01962.pdf)  
**作者**：Arip Asadulaev, Maksim Bobrin, Salem Lahlou, Dmitry Dylov, Fakhri Karray, Martin Takac  

**一句话要点**：提出基于后继测度与平稳密度比连接的零样本离策略学习算法，实现无训练快速适应新任务。

**关键词**：零样本强化学习, 离策略学习, 平稳分布校正, 后继测度, 重要性采样, 快速适应

## 3 点简述
- 核心问题：零样本强化学习中，离策略学习面临分布偏移和价值函数高估偏差，需从无奖励数据适应新任务。
- 方法要点：通过理论连接后继测度与平稳密度比，在线推断最优重要性采样比率，执行平稳分布校正。
- 实验或效果：在SMPL Humanoid运动跟踪、ExoRL连续控制和OGBench长时程任务中基准测试，集成前向后向表示框架实现快速适应。

## 摘要（原文）

> Off-policy learning methods seek to derive an optimal policy directly from a fixed dataset of prior interactions. This objective presents significant challenges, primarily due to the inherent distributional shift and value function overestimation bias. These issues become even more noticeable in zero-shot reinforcement learning, where an agent trained on reward-free data must adapt to new tasks at test time without additional training. In this work, we address the off-policy problem in a zero-shot setting by discovering a theoretical connection of successor measures to stationary density ratios. Using this insight, our algorithm can infer optimal importance sampling ratios, effectively performing a stationary distribution correction with an optimal policy for any task on the fly. We benchmark our method in motion tracking tasks on SMPL Humanoid, continuous control on ExoRL, and for the long-horizon OGBench tasks. Our technique seamlessly integrates into forward-backward representation frameworks and enables fast-adaptation to new tasks in a training-free regime. More broadly, this work bridges off-policy learning and zero-shot adaptation, offering benefits to both research areas.

