---
layout: default
title: Geometry of Drifting MDPs with Path-Integral Stability Certificates
---

# Geometry of Drifting MDPs with Path-Integral Stability Certificates
**arXiv**：[2601.21991v1](https://arxiv.org/abs/2601.21991) · [PDF](https://arxiv.org/pdf/2601.21991.pdf)  
**作者**：Zuyuan Zhang, Mahdi Imani, Tian Lan  

**一句话要点**：提出基于微分同伦路径的几何框架，以解决非平稳强化学习中环境漂移的跟踪问题。

**关键词**：非平稳强化学习, 几何建模, 路径积分稳定性, 同伦跟踪, 动态MDP, 在线适应

## 3 点简述
- 核心问题：现有非平稳强化学习理论缺乏对局部环境变化（如加速度和动作间隙）的建模，导致跟踪误差和策略抖动。
- 方法要点：将非平稳MDP建模为微分同伦路径，分析最优贝尔曼不动点的运动，推导路径积分稳定性界和间隙安全可行区域。
- 实验或效果：提出HT-RL和HT-MCTS轻量级包装器，在振荡和切换场景中提升跟踪性能和动态遗憾。

## 摘要（原文）

> Real-world reinforcement learning is often \emph{nonstationary}: rewards and dynamics drift, accelerate, oscillate, and trigger abrupt switches in the optimal action. Existing theory often represents nonstationarity with coarse-scale models that measure \emph{how much} the environment changes, not \emph{how} it changes locally -- even though acceleration and near-ties drive tracking error and policy chattering. We take a geometric view of nonstationary discounted Markov Decision Processes (MDPs) by modeling the environment as a differentiable homotopy path and tracking the induced motion of the optimal Bellman fixed point. This yields a length--curvature--kink signature of intrinsic complexity: cumulative drift, acceleration/oscillation, and action-gap-induced nonsmoothness. We prove a solver-agnostic path-integral stability bound and derive gap-safe feasible regions that certify local stability away from switch regimes. Building on these results, we introduce \textit{Homotopy-Tracking RL (HT-RL)} and \textit{HT-MCTS}, lightweight wrappers that estimate replay-based proxies of length, curvature, and near-tie proximity online and adapt learning or planning intensity accordingly. Experiments show improved tracking and dynamic regret over matched static baselines, with the largest gains in oscillatory and switch-prone regimes.

