---
layout: default
title: Multi-Modal Decentralized Reinforcement Learning for Modular Reconfigurable Lunar Robots
---

# Multi-Modal Decentralized Reinforcement Learning for Modular Reconfigurable Lunar Robots
**arXiv**：[2510.20347v1](https://arxiv.org/abs/2510.20347) · [PDF](https://arxiv.org/pdf/2510.20347.pdf)  
**作者**：Ashutosh Mishra, Shreya Santra, Elian Neppel, Edoardo M. Rossi Lombardi, Shamistan Karimov, Kentaro Uno, Kazuya Yoshida  

**一句话要点**：提出去中心化强化学习方案以解决模块化月球机器人形态组合爆炸的控制问题

**关键词**：模块化机器人, 去中心化强化学习, 零样本泛化, 月球机器人, 策略学习

## 3 点简述
- 核心问题：模块化可重构机器人的形态组合爆炸阻碍统一控制
- 方法要点：各模块学习独立策略，轮模块用SAC，7自由度肢体用PPO
- 实验效果：仿真中实现零样本泛化，现场测试验证自主运动与重构

## 摘要（原文）

> Modular reconfigurable robots suit task-specific space operations, but the
> combinatorial growth of morphologies hinders unified control. We propose a
> decentralized reinforcement learning (Dec-RL) scheme where each module learns
> its own policy: wheel modules use Soft Actor-Critic (SAC) for locomotion and
> 7-DoF limbs use Proximal Policy Optimization (PPO) for steering and
> manipulation, enabling zero-shot generalization to unseen configurations. In
> simulation, the steering policy achieved a mean absolute error of 3.63{\deg}
> between desired and induced angles; the manipulation policy plateaued at 84.6 %
> success on a target-offset criterion; and the wheel policy cut average motor
> torque by 95.4 % relative to baseline while maintaining 99.6 % success.
> Lunar-analogue field tests validated zero-shot integration for autonomous
> locomotion, steering, and preliminary alignment for reconfiguration. The system
> transitioned smoothly among synchronous, parallel, and sequential modes for
> Policy Execution, without idle states or control conflicts, indicating a
> scalable, reusable, and robust approach for modular lunar robots.

