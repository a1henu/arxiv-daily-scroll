---
layout: default
title: SaferPath: Hierarchical Visual Navigation with Learned Guidance and Safety-Constrained Control
---

# SaferPath: Hierarchical Visual Navigation with Learned Guidance and Safety-Constrained Control
**arXiv**：[2603.01898v1](https://arxiv.org/abs/2603.01898) · [PDF](https://arxiv.org/pdf/2603.01898.pdf)  
**作者**：Lingjie Zhang, Zeyu Jiang, Changhao Chen  

**一句话要点**：提出SaferPath分层视觉导航框架，结合学习引导与安全约束控制，以提升移动机器人在密集室内环境中的安全性和泛化能力。

**关键词**：视觉导航, 分层框架, 安全约束控制, 轨迹优化, 模型预测控制, 室内机器人

## 3 点简述
- 核心问题：端到端学习视觉导航方法在未知、杂乱或狭窄环境中泛化性差且易碰撞，尤其在密集室内场景中表现不佳。
- 方法要点：采用分层框架，先通过端到端模型生成引导轨迹，再使用MP-SVES优化控制模块进行安全约束轨迹优化，并由MPC控制器跟踪执行。
- 实验或效果：在未见障碍物、密集非结构化空间和狭窄走廊等场景中，SaferPath显著提高成功率、减少碰撞，优于ViNT和NoMaD等基线方法。

## 摘要（原文）

> Visual navigation is a core capability for mobile robots, yet end-to-end learning-based methods often struggle with generalization and safety in unseen, cluttered, or narrow environments. These limitations are especially pronounced in dense indoor settings, where collisions are likely and end-to-end models frequently fail. To address this, we propose SaferPath, a hierarchical visual navigation framework that leverages learned guidance from existing end-to-end models and refines it through a safety-constrained optimization-control module. SaferPath transforms visual observations into a traversable-area map and refines guidance trajectories using Model Predictive Stein Variational Evolution Strategy (MP-SVES), efficiently generating safe trajectories in only a few iterations. The refined trajectories are tracked by an MPC controller, ensuring robust navigation in complex environments. Extensive experiments in scenarios with unseen obstacles, dense unstructured spaces, and narrow corridors demonstrate that SaferPath consistently improves success rates and reduces collisions, outperforming representative baselines such as ViNT and NoMaD, and enabling safe navigation in challenging real-world settings.

