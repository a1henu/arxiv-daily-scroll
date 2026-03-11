---
layout: default
title: Trajectory Optimization for Self-Wrap-Aware Cable-Towed Planar Object Manipulation under Implicit Tension Constraints
---

# Trajectory Optimization for Self-Wrap-Aware Cable-Towed Planar Object Manipulation under Implicit Tension Constraints
**arXiv**：[2603.09557v1](https://arxiv.org/abs/2603.09557) · [PDF](https://arxiv.org/pdf/2603.09557.pdf)  
**作者**：Yu Li, Amin Fakhari, Hamid Sadeghian  

**一句话要点**：提出基于隐式张力约束的自缠绕感知轨迹优化方法，用于电缆牵引平面物体操纵。

**关键词**：电缆牵引操纵, 轨迹优化, 自缠绕感知, 隐式张力约束, 平面物体操纵, 松弛层次

## 3 点简述
- 研究电缆牵引操纵中自缠绕与张力约束耦合的轨迹优化问题。
- 构建从严格模式到三种可处理松弛的层次化优化框架。
- 实验表明隐式模式松弛能通过状态演化诱导自缠绕，有效利用转向扭矩通道。

## 摘要（原文）

> Cable/rope elements are pervasive in deformable-object manipulation, often serving as a deformable force-transmission medium whose routing and contact determine how wrenches are delivered. In cable-towed manipulation, transmission is unilateral and hybrid: the tether can pull only when taut and becomes force-free when slack; in practice, the tether may also contact the object boundary and self-wrap around edges, which is not merely collision avoidance but a change of the wrench transmission channel by shifting the effective application point and moment arm, thereby coupling routing geometry with rigid-body motion and tensioning. We formulate self-wrap towing as a routing-aware, tensioning-implicit trajectory optimization (TITO) problem that couples (i) a tensioning-implicit taut/slack constraint and (ii) routing-conditioned transmission maps for effective length and wrench, and we build a relaxation hierarchy from a strict mode-conditioned reference to three tractable relaxations: Full-Mode Relaxation (FMR), Binary-Mode Relaxation (BMR), and Implicit-Mode Relaxation (IMR). Across planar towing tasks, we find that making routing an explicit decision often yields conservative solutions that stay near switching boundaries, whereas IMR induces self-wrap through state evolution and exploits the redirected torque channel whenever turning requires it.

