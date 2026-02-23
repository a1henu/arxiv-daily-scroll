---
layout: default
title: Learning Smooth Time-Varying Linear Policies with an Action Jacobian Penalty
---

# Learning Smooth Time-Varying Linear Policies with an Action Jacobian Penalty
**arXiv**：[2602.18312v1](https://arxiv.org/abs/2602.18312) · [PDF](https://arxiv.org/pdf/2602.18312.pdf)  
**作者**：Zhaoming Xie, Kevin Karol, Jessica Hodgins  

**一句话要点**：提出动作雅可比惩罚与线性策略网络以解决强化学习中控制信号不自然问题

**关键词**：强化学习, 控制策略, 动作雅可比惩罚, 线性策略网络, 运动模仿, 物理机器人

## 3 点简述
- 强化学习策略常产生不自然高频控制信号，难以在真实世界实现
- 引入动作雅可比惩罚直接惩罚动作对状态的变化，无需任务特定调参
- 结合线性策略网络降低计算开销，在模拟和物理机器人任务中验证有效性

## 摘要（原文）

> Reinforcement learning provides a framework for learning control policies that can reproduce diverse motions for simulated characters. However, such policies often exploit unnatural high-frequency signals that are unachievable by humans or physical robots, making them poor representations of real-world behaviors. Existing work addresses this issue by adding a reward term that penalizes a large change in actions over time. This term often requires substantial tuning efforts. We propose to use the action Jacobian penalty, which penalizes changes in action with respect to the changes in simulated state directly through auto differentiation. This effectively eliminates unrealistic high-frequency control signals without task specific tuning. While effective, the action Jacobian penalty introduces significant computational overhead when used with traditional fully connected neural network architectures. To mitigate this, we introduce a new architecture called a Linear Policy Net (LPN) that significantly reduces the computational burden for calculating the action Jacobian penalty during training. In addition, a LPN requires no parameter tuning, exhibits faster learning convergence compared to baseline methods, and can be more efficiently queried during inference time compared to a fully connected neural network. We demonstrate that a Linear Policy Net, combined with the action Jacobian penalty, is able to learn policies that generate smooth signals while solving a number of motion imitation tasks with different characteristics, including dynamic motions such as a backflip and various challenging parkour skills. Finally, we apply this approach to create policies for dynamic motions on a physical quadrupedal robot equipped with an arm.

