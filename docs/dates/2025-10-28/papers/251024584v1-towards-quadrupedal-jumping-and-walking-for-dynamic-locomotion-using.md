---
layout: default
title: Towards Quadrupedal Jumping and Walking for Dynamic Locomotion using Reinforcement Learning
---

# Towards Quadrupedal Jumping and Walking for Dynamic Locomotion using Reinforcement Learning
**arXiv**：[2510.24584v1](https://arxiv.org/abs/2510.24584) · [PDF](https://arxiv.org/pdf/2510.24584.pdf)  
**作者**：Jørgen Anker Olsen, Lars Rønhaug Pettersen, Kostas Alexis  

**一句话要点**：提出基于课程强化学习的框架，实现机器人动态跳跃与行走

**关键词**：强化学习, 机器人跳跃, 动态运动, 课程学习, Sim2Real

## 3 点简述
- 核心问题：机器人动态跳跃奖励稀疏，难以高效学习精确跳跃行为。
- 方法要点：利用弹道定律稠密化奖励，采用参考状态初始化加速探索。
- 实验效果：水平跳跃达1.25米，垂直跳跃达1.0米，验证Sim2Real迁移。

## 摘要（原文）

> This paper presents a curriculum-based reinforcement learning framework for
> training precise and high-performance jumping policies for the robot `Olympus'.
> Separate policies are developed for vertical and horizontal jumps, leveraging a
> simple yet effective strategy. First, we densify the inherently sparse jumping
> reward using the laws of projectile motion. Next, a reference state
> initialization scheme is employed to accelerate the exploration of dynamic
> jumping behaviors without reliance on reference trajectories. We also present a
> walking policy that, when combined with the jumping policies, unlocks versatile
> and dynamic locomotion capabilities. Comprehensive testing validates walking on
> varied terrain surfaces and jumping performance that exceeds previous works,
> effectively crossing the Sim2Real gap. Experimental validation demonstrates
> horizontal jumps up to 1.25 m with centimeter accuracy and vertical jumps up to
> 1.0 m. Additionally, we show that with only minor modifications, the proposed
> method can be used to learn omnidirectional jumping.

