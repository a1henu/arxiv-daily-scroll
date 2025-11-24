---
layout: default
title: Human Imitated Bipedal Locomotion with Frequency Based Gait Generator Network
---

# Human Imitated Bipedal Locomotion with Frequency Based Gait Generator Network
**arXiv**：[2511.17387v1](https://arxiv.org/abs/2511.17387) · [PDF](https://arxiv.org/pdf/2511.17387.pdf)  
**作者**：Yusuf Baran Ates, Omer Morgul  

**一句话要点**：提出基于频率的步态生成器网络与PPO控制器，实现仿人双足行走

**关键词**：双足行走, 步态生成, 深度强化学习, PPO控制器, 运动模仿

## 3 点简述
- 核心问题：混合动力学和地形变化使仿人双足行走学习困难
- 方法要点：结合人类运动学习的步态生成器与PPO进行扭矩控制
- 实验或效果：在平坦或缓坡训练，泛化到陡坡和粗糙地面

## 摘要（原文）

> Learning human-like, robust bipedal walking remains difficult due to hybrid dynamics and terrain variability. We propose a lightweight framework that combines a gait generator network learned from human motion with Proximal Policy Optimization (PPO) controller for torque control. Despite being trained only on flat or mildly sloped ground, the learned policies generalize to steeper ramps and rough surfaces. Results suggest that pairing spectral motion priors with Deep Reinforcement Learning (DRL) offers a practical path toward natural and robust bipedal locomotion with modest training cost.

