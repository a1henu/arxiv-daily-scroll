---
layout: default
title: Learning to Act Robustly with View-Invariant Latent Actions
---

# Learning to Act Robustly with View-Invariant Latent Actions
**arXiv**：[2601.02994v1](https://arxiv.org/abs/2601.02994) · [PDF](https://arxiv.org/pdf/2601.02994.pdf)  
**作者**：Youngjoon Jeong, Junha Chun, Taesup Kim  

**一句话要点**：提出VILA以解决视觉机器人策略在视角变化下的鲁棒性问题

**关键词**：视觉机器人策略, 视角不变表示, 潜在动作建模, 物理动态整合, 鲁棒泛化, 预训练框架

## 3 点简述
- 核心问题：视觉机器人策略易受视角变化影响，现有方法依赖视觉外观，缺乏物理动态整合。
- 方法要点：VILA建模基于轨迹过渡模式的潜在动作，通过动作引导目标对齐视角，学习基于物理动态的视角不变表示。
- 实验或效果：仿真和真实世界实验显示，VILA策略能泛化到未见视角，并良好迁移到新任务，提升鲁棒性和下游学习性能。

## 摘要（原文）

> Vision-based robotic policies often struggle with even minor viewpoint changes, underscoring the need for view-invariant visual representations. This challenge becomes more pronounced in real-world settings, where viewpoint variability is unavoidable and can significantly disrupt policy performance. Existing methods typically learn invariance from multi-view observations at the scene level, but such approaches rely on visual appearance and fail to incorporate the physical dynamics essential for robust generalization. We propose View-Invariant Latent Action (VILA), which models a latent action capturing transition patterns across trajectories to learn view-invariant representations grounded in physical dynamics. VILA aligns these latent actions across viewpoints using an action-guided objective based on ground-truth action sequences. Experiments in both simulation and the real world show that VILA-based policies generalize effectively to unseen viewpoints and transfer well to new tasks, establishing VILA as a strong pretraining framework that improves robustness and downstream learning performance.

