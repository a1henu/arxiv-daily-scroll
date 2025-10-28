---
layout: default
title: Payload trajectory tracking control for aerial transportation systems with cable length online optimization
---

# Payload trajectory tracking control for aerial transportation systems with cable length online optimization
**arXiv**：[2510.23296v1](https://arxiv.org/abs/2510.23296) · [PDF](https://arxiv.org/pdf/2510.23296.pdf)  
**作者**：Hai Yu, Zhichao Yang, Wei He, Jianda Han, Yongchun Fang, Xiao Liang  

**一句话要点**：提出基于反步控制与缆长在线优化的方法，用于可变缆长空中运输系统的载荷轨迹跟踪。

**关键词**：空中运输系统, 反步控制, 缆长优化, 轨迹跟踪, 非线性控制, 动态耦合

## 3 点简述
- 核心问题：可变缆长引入非线性与动态耦合，增加控制设计难度。
- 方法要点：采用反步控制策略，结合缆长生成器在线优化缆长。
- 实验或效果：仿真验证方法有效管理轨迹跟踪与缆长调整。

## 摘要（原文）

> Cable-suspended aerial transportation systems are employed extensively across
> various industries. The capability to flexibly adjust the relative position
> between the multirotor and the payload has spurred growing interest in the
> system equipped with variable-length cable, promising broader application
> potential. Compared to systems with fixed-length cables, introducing the
> variable-length cable adds a new degree of freedom. However, it also results in
> increased nonlinearity and more complex dynamic coupling among the multirotor,
> the cable and the payload, posing significant challenges in control design.
> This paper introduces a backstepping control strategy tailored for aerial
> transportation systems with variable-length cable, designed to precisely track
> the payload trajectory while dynamically adjusting cable length. Then, a cable
> length generator has been developed that achieves online optimization of the
> cable length while satisfying state constraints, thus balancing the
> multirotor's motion and cable length changes without the need for manual
> trajectory planning. The asymptotic stability of the closed-loop system is
> guaranteed through Lyapunov techniques and the growth restriction condition.
> Finally, simulation results confirm the efficacy of the proposed method in
> managing trajectory tracking and cable length adjustments effectively.

