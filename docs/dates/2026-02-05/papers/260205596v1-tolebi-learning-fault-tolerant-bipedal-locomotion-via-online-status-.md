---
layout: default
title: TOLEBI: Learning Fault-Tolerant Bipedal Locomotion via Online Status Estimation and Fallibility Rewards
---

# TOLEBI: Learning Fault-Tolerant Bipedal Locomotion via Online Status Estimation and Fallibility Rewards
**arXiv**：[2602.05596v1](https://arxiv.org/abs/2602.05596) · [PDF](https://arxiv.org/pdf/2602.05596.pdf)  
**作者**：Hokyun Lee, Woo-Jeong Baek, Junhyeok Cha, Jaeheung Park  

**一句话要点**：提出TOLEBI框架以解决双足机器人运动中的硬件故障容错问题

**关键词**：双足机器人运动, 故障容错学习, 强化学习, 在线状态估计, 仿真到真实迁移

## 3 点简述
- 核心问题：现有强化学习方法在双足机器人运动中缺乏处理硬件故障的能力，可能导致严重后果
- 方法要点：通过模拟注入关节锁定、电源丢失和外部扰动，结合在线关节状态模块实时分类关节条件
- 实验或效果：在仿真和真实人形机器人TOCABI上验证了方法的适用性，实现了故障容错运动策略

## 摘要（原文）

> With the growing employment of learning algorithms in robotic applications, research on reinforcement learning for bipedal locomotion has become a central topic for humanoid robotics. While recently published contributions achieve high success rates in locomotion tasks, scarce attention has been devoted to the development of methods that enable to handle hardware faults that may occur during the locomotion process. However, in real-world settings, environmental disturbances or sudden occurrences of hardware faults might yield severe consequences. To address these issues, this paper presents TOLEBI (A faulT-tOlerant Learning framEwork for Bipedal locomotIon) that handles faults on the robot during operation. Specifically, joint locking, power loss and external disturbances are injected in simulation to learn fault-tolerant locomotion strategies. In addition to transferring the learned policy to the real robot via sim-to-real transfer, an online joint status module incorporated. This module enables to classify joint conditions by referring to the actual observations at runtime under real-world conditions. The validation experiments conducted both in real-world and simulation with the humanoid robot TOCABI highlight the applicability of the proposed approach. To our knowledge, this manuscript provides the first learning-based fault-tolerant framework for bipedal locomotion, thereby fostering the development of efficient learning methods in this field.

