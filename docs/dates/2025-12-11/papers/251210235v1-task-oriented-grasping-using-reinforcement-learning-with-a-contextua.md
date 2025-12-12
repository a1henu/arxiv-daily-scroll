---
layout: default
title: Task-Oriented Grasping Using Reinforcement Learning with a Contextual Reward Machine
---

# Task-Oriented Grasping Using Reinforcement Learning with a Contextual Reward Machine
**arXiv**：[2512.10235v1](https://arxiv.org/abs/2512.10235) · [PDF](https://arxiv.org/pdf/2512.10235.pdf)  
**作者**：Hui Li, Akhlak Uz Zaman, Fujian Yan, Hongsheng He  

**一句话要点**：提出结合上下文奖励机器的强化学习框架以解决任务导向抓取问题

**关键词**：任务导向抓取, 强化学习, 上下文奖励机器, 状态抽象, 转移奖励, 机器人抓取

## 3 点简述
- 核心问题：任务导向抓取任务复杂，状态-动作空间大，学习效率低。
- 方法要点：使用上下文奖励机器分解任务为子任务，每个子任务关联特定上下文，包括奖励函数、动作空间和状态抽象函数，并引入转移奖励引导阶段序列。
- 实验或效果：在模拟任务中达到95%成功率，优于现有方法；在真实机器人上实现83.3%成功率，展示高准确性和学习效率。

## 摘要（原文）

> This paper presents a reinforcement learning framework that incorporates a Contextual Reward Machine for task-oriented grasping. The Contextual Reward Machine reduces task complexity by decomposing grasping tasks into manageable sub-tasks. Each sub-task is associated with a stage-specific context, including a reward function, an action space, and a state abstraction function. This contextual information enables efficient intra-stage guidance and improves learning efficiency by reducing the state-action space and guiding exploration within clearly defined boundaries. In addition, transition rewards are introduced to encourage or penalize transitions between stages which guides the model toward desirable stage sequences and further accelerates convergence. When integrated with the Proximal Policy Optimization algorithm, the proposed method achieved a 95% success rate across 1,000 simulated grasping tasks encompassing diverse objects, affordances, and grasp topologies. It outperformed the state-of-the-art methods in both learning speed and success rate. The approach was transferred to a real robot, where it achieved a success rate of 83.3% in 60 grasping tasks over six affordances. These experimental results demonstrate superior accuracy, data efficiency, and learning efficiency. They underscore the model's potential to advance task-oriented grasping in both simulated and real-world settings.

