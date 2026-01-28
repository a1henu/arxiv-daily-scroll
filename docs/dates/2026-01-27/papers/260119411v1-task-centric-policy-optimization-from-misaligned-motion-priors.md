---
layout: default
title: Task-Centric Policy Optimization from Misaligned Motion Priors
---

# Task-Centric Policy Optimization from Misaligned Motion Priors
**arXiv**：[2601.19411v1](https://arxiv.org/abs/2601.19411) · [PDF](https://arxiv.org/pdf/2601.19411.pdf)  
**作者**：Ziang Zheng, Kai Feng, Yi Nie, Shentao Qin  

**一句话要点**：提出任务中心运动先验以解决人形机器人控制中演示与任务错配问题

**关键词**：人形机器人控制, 对抗模仿学习, 任务优先框架, 运动先验, 梯度冲突分析

## 3 点简述
- 核心问题：人类演示常因体现差异和任务无关变化而与机器人任务错配，导致模仿损害性能
- 方法要点：将模仿作为条件正则化器，仅在兼容任务进展时纳入信号，实现自适应几何感知更新
- 实验或效果：在人形控制实验中验证了稳健任务性能和一致运动风格，支持噪声演示

## 摘要（原文）

> Humanoid control often leverages motion priors from human demonstrations to encourage natural behaviors. However, such demonstrations are frequently suboptimal or misaligned with robotic tasks due to embodiment differences, retargeting errors, and task-irrelevant variations, causing naïve imitation to degrade task performance. Conversely, task-only reinforcement learning admits many task-optimal solutions, often resulting in unnatural or unstable motions. This exposes a fundamental limitation of linear reward mixing in adversarial imitation learning. We propose \emph{Task-Centric Motion Priors} (TCMP), a task-priority adversarial imitation framework that treats imitation as a conditional regularizer rather than a co-equal objective. TCMP maximizes task improvement while incorporating imitation signals only when they are compatible with task progress, yielding an adaptive, geometry-aware update that preserves task-feasible descent and suppresses harmful imitation under misalignment. We provide theoretical analysis of gradient conflict and task-priority stationary points, and validate our claims through humanoid control experiments demonstrating robust task performance with consistent motion style under noisy demonstrations.

