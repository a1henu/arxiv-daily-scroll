---
layout: default
title: U-OBCA: Uncertainty-Aware Optimization-Based Collision Avoidance via Wasserstein Distributionally Robust Chance Constraints
---

# U-OBCA: Uncertainty-Aware Optimization-Based Collision Avoidance via Wasserstein Distributionally Robust Chance Constraints
**arXiv**：[2603.04914v1](https://arxiv.org/abs/2603.04914) · [PDF](https://arxiv.org/pdf/2603.04914.pdf)  
**作者**：Zehao Wang, Yuxuan Tang, Han Zhang, Jingchuan Wang, Weidong Chen  

**一句话要点**：提出U-OBCA方法，通过分布鲁棒机会约束解决多边形机器人导航中的不确定性避障问题。

**关键词**：机器人导航, 避障规划, 不确定性处理, 机会约束, 分布鲁棒优化, 多边形碰撞检测

## 3 点简述
- 核心问题：定位误差、障碍物轨迹预测误差等不确定性导致现有方法在狭窄环境中过于保守或失败。
- 方法要点：基于OBCA框架，引入机会约束避免几何简化，并转化为确定性约束以高效求解。
- 实验或效果：理论分析、仿真和真实实验验证，在狭窄拥挤环境中减少保守性并提高导航效率。

## 摘要（原文）

> Uncertainties arising from localization error, trajectory prediction errors of the moving obstacles and environmental disturbances pose significant challenges to robot's safe navigation. Existing uncertainty-aware planners often approximate polygon-shaped robots and obstacles using simple geometric primitives such as circles or ellipses. Though computationally convenient, these approximations substantially shrink the feasible space, leading to overly conservative trajectories and even planning failure in narrow environments. In addition, many such methods rely on specific assumptions about noise distributions, which may not hold in practice and thus limit their performance guarantees. To address these limitations, we extend the Optimization-Based Collision Avoidance (OBCA) framework to an uncertainty-aware formulation, termed \emph{U-OBCA}. The proposed method explicitly accounts for the collision risk between polygon-shaped robots and obstacles by formulating OBCA-based chance constraints, and hence avoiding geometric simplifications and reducing unnecessary conservatism. These probabilistic constraints are further tightened into deterministic nonlinear constraints under mild distributional assumptions, which can be solved efficiently by standard numerical optimization solvers. The proposed approach is validated through theoretical analysis, numerical simulations and real-world experiments. The results demonstrate that U-OBCA significantly mitigates the conservatism in trajectory planning and achieves higher navigation efficiency compared to existing baseline methods, particularly in narrow and cluttered environments.

