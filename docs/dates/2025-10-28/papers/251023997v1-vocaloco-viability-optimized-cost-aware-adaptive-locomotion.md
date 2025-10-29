---
layout: default
title: VOCALoco: Viability-Optimized Cost-aware Adaptive Locomotion
---

# VOCALoco: Viability-Optimized Cost-aware Adaptive Locomotion
**arXiv**：[2510.23997v1](https://arxiv.org/abs/2510.23997) · [PDF](https://arxiv.org/pdf/2510.23997.pdf)  
**作者**：Stanley Wu, Mohamad H. Danesh, Simon Li, Hanna Yurchyk, Amin Abyaneh, Anas El Houssaini, David Meger, Hsiu-Chin Lin  

**一句话要点**：提出VOCALoco框架以优化腿式机器人在复杂地形中的安全与能效自适应运动

**关键词**：腿式机器人运动, 自适应策略选择, 能效优化, 安全评估, 深度强化学习, 楼梯导航

## 3 点简述
- 问题：端到端深度强化学习在腿式机器人运动中存在安全性和可解释性不足的问题
- 方法：基于感知输入动态评估预训练策略的可行性和能耗，选择安全高效策略
- 效果：在楼梯任务中，相比传统方法，提升了机器人的鲁棒性和安全性

## 摘要（原文）

> Recent advancements in legged robot locomotion have facilitated traversal
> over increasingly complex terrains. Despite this progress, many existing
> approaches rely on end-to-end deep reinforcement learning (DRL), which poses
> limitations in terms of safety and interpretability, especially when
> generalizing to novel terrains. To overcome these challenges, we introduce
> VOCALoco, a modular skill-selection framework that dynamically adapts
> locomotion strategies based on perceptual input. Given a set of pre-trained
> locomotion policies, VOCALoco evaluates their viability and energy-consumption
> by predicting both the safety of execution and the anticipated cost of
> transport over a fixed planning horizon. This joint assessment enables the
> selection of policies that are both safe and energy-efficient, given the
> observed local terrain. We evaluate our approach on staircase locomotion tasks,
> demonstrating its performance in both simulated and real-world scenarios using
> a quadrupedal robot. Empirical results show that VOCALoco achieves improved
> robustness and safety during stair ascent and descent compared to a
> conventional end-to-end DRL policy

