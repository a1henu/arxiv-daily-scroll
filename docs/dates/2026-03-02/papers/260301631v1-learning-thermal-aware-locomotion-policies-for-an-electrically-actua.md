---
layout: default
title: Learning Thermal-Aware Locomotion Policies for an Electrically-Actuated Quadruped Robot
---

# Learning Thermal-Aware Locomotion Policies for an Electrically-Actuated Quadruped Robot
**arXiv**：[2603.01631v1](https://arxiv.org/abs/2603.01631) · [PDF](https://arxiv.org/pdf/2603.01631.pdf)  
**作者**：Letian Qian, Yuhang Wan, Shuhan Wang, Xin Luo  

**一句话要点**：提出热感知强化学习控制方法，以解决电机过热问题，提升四足机器人持续运行能力。

**关键词**：四足机器人控制, 热感知控制, 强化学习策略, 电机过热, 持续运行, 实验验证

## 3 点简述
- 核心问题：电机在高扭矩循环负载下易过热，触发保护机制，限制机器人长时间任务执行。
- 方法要点：将电机温度纳入强化学习策略，引入热约束奖励函数，防止温度超标。
- 实验或效果：在Unitree A1机器人上，基线策略约7分钟触发过热停止，新方法可持续运行超27分钟，保持跟踪性能。

## 摘要（原文）

> Electrically-actuated quadrupedal robots possess high mobility on complex terrains, but their motors tend to accumulate heat under high-torque cyclic loads, potentially triggering overheat protection and limiting long-duration tasks. This work proposes a thermal-aware control method that incorporates motor temperatures into reinforcement learning locomotion policies and introduces thermal-constraint rewards to prevent temperature exceedance. Real-world experiments on the Unitree A1 demonstrate that, under a fixed 3 kg payload, the baseline policy triggers overheat protection and stops within approximately 7 minutes, whereas the proposed method can operate continuously for over 27 minutes without thermal interruptions while maintaining comparable command-tracking performance, thereby enhancing sustainable operational capability.

