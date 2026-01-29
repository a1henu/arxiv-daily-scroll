---
layout: default
title: GPO: Growing Policy Optimization for Legged Robot Locomotion and Whole-Body Control
---

# GPO: Growing Policy Optimization for Legged Robot Locomotion and Whole-Body Control
**arXiv**：[2601.20668v1](https://arxiv.org/abs/2601.20668) · [PDF](https://arxiv.org/pdf/2601.20668.pdf)  
**作者**：Shuhao Liao, Peizhuo Li, Xinrong Yang, Linnan Chang, Zhaoxin Fan, Qing Wang, Lei Shi, Yuhong Cao, Wenjun Wu, Guillaume Sartoretti  

**一句话要点**：提出Growing Policy Optimization以解决足式机器人扭矩控制中探索困难的问题

**关键词**：强化学习, 足式机器人控制, 扭矩控制, 策略优化, 动作空间变换, 零样本部署

## 3 点简述
- 核心问题：足式机器人扭矩控制因高维连续动作空间和探索不足导致训练困难
- 方法要点：采用时变动作变换限制早期动作空间，逐步扩展以促进有效探索
- 实验或效果：在四足和六足机器人上验证，实现零样本硬件部署，性能优于现有方法

## 摘要（原文）

> Training reinforcement learning (RL) policies for legged robots remains challenging due to high-dimensional continuous actions, hardware constraints, and limited exploration. Existing methods for locomotion and whole-body control work well for position-based control with environment-specific heuristics (e.g., reward shaping, curriculum design, and manual initialization), but are less effective for torque-based control, where sufficiently exploring the action space and obtaining informative gradient signals for training is significantly more difficult. We introduce Growing Policy Optimization (GPO), a training framework that applies a time-varying action transformation to restrict the effective action space in the early stage, thereby encouraging more effective data collection and policy learning, and then progressively expands it to enhance exploration and achieve higher expected return. We prove that this transformation preserves the PPO update rule and introduces only bounded, vanishing gradient distortion, thereby ensuring stable training. We evaluate GPO on both quadruped and hexapod robots, including zero-shot deployment of simulation-trained policies on hardware. Policies trained with GPO consistently achieve better performance. These results suggest that GPO provides a general, environment-agnostic optimization framework for learning legged locomotion.

