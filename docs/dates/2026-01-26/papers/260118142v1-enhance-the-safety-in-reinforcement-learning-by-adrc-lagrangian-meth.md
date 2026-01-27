---
layout: default
title: Enhance the Safety in Reinforcement Learning by ADRC Lagrangian Methods
---

# Enhance the Safety in Reinforcement Learning by ADRC Lagrangian Methods
**arXiv**：[2601.18142v1](https://arxiv.org/abs/2601.18142) · [PDF](https://arxiv.org/pdf/2601.18142.pdf)  
**作者**：Mingxu Zhang, Huicheng Zhang, Jiaming Ji, Yaodong Yang, Ying Sun  

**一句话要点**：提出ADRC-Lagrangian方法以增强强化学习中的安全性

**关键词**：安全强化学习, Lagrangian方法, 主动抗扰控制, 鲁棒性优化, 安全约束, 实验验证

## 3 点简述
- 核心问题：现有Lagrangian方法因参数敏感和相位滞后导致振荡和频繁安全违规
- 方法要点：利用主动抗扰控制提升鲁棒性，统一框架涵盖经典和PID方法
- 实验或效果：实验显示安全违规减少74%，违规幅度降89%，平均成本降67%

## 摘要（原文）

> Safe reinforcement learning (Safe RL) seeks to maximize rewards while satisfying safety constraints, typically addressed through Lagrangian-based methods. However, existing approaches, including PID and classical Lagrangian methods, suffer from oscillations and frequent safety violations due to parameter sensitivity and inherent phase lag. To address these limitations, we propose ADRC-Lagrangian methods that leverage Active Disturbance Rejection Control (ADRC) for enhanced robustness and reduced oscillations. Our unified framework encompasses classical and PID Lagrangian methods as special cases while significantly improving safety performance. Extensive experiments demonstrate that our approach reduces safety violations by up to 74%, constraint violation magnitudes by 89%, and average costs by 67\%, establishing superior effectiveness for Safe RL in complex environments.

