---
layout: default
title: Stein Variational Ergodic Surface Coverage with SE(3) Constraints
---

# Stein Variational Ergodic Surface Coverage with SE(3) Constraints
**arXiv**：[2603.09458v1](https://arxiv.org/abs/2603.09458) · [PDF](https://arxiv.org/pdf/2603.09458.pdf)  
**作者**：Jiayun Li, Yufeng Jin, Sangli Teng, Dejian Gong, Georgia Chalvatzaki  

**一句话要点**：提出基于SE(3)约束的Stein变分遍历表面覆盖方法，以优化机器人轨迹生成。

**关键词**：机器人轨迹优化, 遍历表面覆盖, SE(3)约束, Stein变分梯度下降, 点云处理, 采样优化

## 3 点简述
- 核心问题：现有遍历轨迹优化方法在处理点云目标时，因非凸优化和SE(3)约束处理不足而受限。
- 方法要点：将点云遍历覆盖重构为流形感知采样问题，推导SE(3)特定SVGD粒子更新，并设计预处理器加速收敛。
- 实验或效果：在3D点云覆盖基准和机器人表面绘制任务中，相比现有方法，实现了更优覆盖质量和可处理计算。

## 摘要（原文）

> Surface manipulation tasks require robots to generate trajectories that comprehensively cover complex 3D surfaces while maintaining precise end-effector poses. Existing ergodic trajectory optimization (TO) methods demonstrate success in coverage tasks, while struggling with point-cloud targets due to the nonconvex optimization landscapes and the inadequate handling of SE(3) constraints in sampling-as-optimization (SAO) techniques. In this work, we introduce a preconditioned SE(3) Stein Variational Gradient Descent (SVGD) approach for SAO ergodic trajectory generation. Our proposed approach comprises multiple innovations. First, we reformulate point-cloud ergodic coverage as a manifold-aware sampling problem. Second, we derive SE(3)-specific SVGD particle updates, and, third, we develop a preconditioner to accelerate TO convergence. Our sampling-based framework consistently identifies superior local optima compared to strong optimization-based and SAO baselines while preserving the SE(3) geometric structure. Experiments on a 3D point-cloud surface coverage benchmark and robotic surface drawing tasks demonstrate that our method achieves superior coverage quality with tractable computation in our setting relative to existing TO and SAO approaches, and is validated in real-world robot experiments.

