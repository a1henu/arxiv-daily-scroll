---
layout: default
title: Geometry of Drifting MDPs with Path-Integral Stability Certificates
---

# Geometry of Drifting MDPs with Path-Integral Stability Certificates
**arXiv**：[2601.21991v1](https://arxiv.org/abs/2601.21991) · [PDF](https://arxiv.org/pdf/2601.21991.pdf)  
**作者**：Zuyuan Zhang, Mahdi Imani, Tian Lan  

**一句话要点**：提出基于同伦路径几何分析的HT-RL方法，以提升非平稳强化学习中的跟踪性能与稳定性。

**关键词**：非平稳强化学习, 几何分析, 同伦路径, 稳定性证书, 动态遗憾优化

## 3 点简述
- 针对非平稳强化学习中环境漂移、加速和切换导致的跟踪误差问题，提出几何建模方法。
- 通过分析最优贝尔曼不动点的运动，推导路径积分稳定性界和间隙安全可行区域，确保局部稳定性。
- 实验表明HT-RL在振荡和切换场景中优于静态基线，动态遗憾显著降低。

## 摘要（原文）

> Real-world reinforcement learning is often \emph{nonstationary}: rewards and dynamics drift, accelerate, oscillate, and trigger abrupt switches in the optimal action. Existing theory often represents nonstationarity with coarse-scale models that measure \emph{how much} the environment changes, not \emph{how} it changes locally -- even though acceleration and near-ties drive tracking error and policy chattering. We take a geometric view of nonstationary discounted Markov Decision Processes (MDPs) by modeling the environment as a differentiable homotopy path and tracking the induced motion of the optimal Bellman fixed point. This yields a length-curvature-kink signature of intrinsic complexity: cumulative drift, acceleration/oscillation, and action-gap-induced nonsmoothness. We prove a solver-agnostic path-integral stability bound and derive gap-safe feasible regions that certify local stability away from switch regimes. Building on these results, we introduce \textit{Homotopy-Tracking RL (HT-RL)} and \textit{HT-MCTS}, lightweight wrappers that estimate replay-based proxies of length, curvature, and near-tie proximity online and adapt learning or planning intensity accordingly. Experiments show improved tracking and dynamic regret over matched static baselines, with the largest gains in oscillatory and switch-prone regimes.

