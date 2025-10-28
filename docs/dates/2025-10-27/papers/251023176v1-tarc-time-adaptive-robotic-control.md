---
layout: default
title: TARC: Time-Adaptive Robotic Control
---

# TARC: Time-Adaptive Robotic Control
**arXiv**：[2510.23176v1](https://arxiv.org/abs/2510.23176) · [PDF](https://arxiv.org/pdf/2510.23176.pdf)  
**作者**：Arnav Sukhija, Lenart Treven, Jin Cheng, Florian Dörfler, Stelian Coros, Andreas Krause  

**一句话要点**：提出时间自适应机器人控制方法，通过强化学习联合选择控制动作与持续时间，解决固定频率控制的效率与鲁棒性权衡问题。

**关键词**：机器人控制, 强化学习, 自适应频率, 仿真到真实迁移, 零样本学习

## 3 点简述
- 固定频率控制导致效率与鲁棒性权衡，限制机器人适应动态环境。
- 采用强化学习策略，联合优化控制动作及其应用时长，实现频率自适应。
- 零样本仿真到真实实验验证，在高速RC车和四足机器人上优于固定频率基线。

## 摘要（原文）

> Fixed-frequency control in robotics imposes a trade-off between the
> efficiency of low-frequency control and the robustness of high-frequency
> control, a limitation not seen in adaptable biological systems. We address this
> with a reinforcement learning approach in which policies jointly select control
> actions and their application durations, enabling robots to autonomously
> modulate their control frequency in response to situational demands. We
> validate our method with zero-shot sim-to-real experiments on two distinct
> hardware platforms: a high-speed RC car and a quadrupedal robot. Our method
> matches or outperforms fixed-frequency baselines in terms of rewards while
> significantly reducing the control frequency and exhibiting adaptive frequency
> control under real-world conditions.

