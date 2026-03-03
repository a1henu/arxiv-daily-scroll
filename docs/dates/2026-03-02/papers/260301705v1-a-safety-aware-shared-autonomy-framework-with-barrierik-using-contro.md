---
layout: default
title: A Safety-Aware Shared Autonomy Framework with BarrierIK Using Control Barrier Functions
---

# A Safety-Aware Shared Autonomy Framework with BarrierIK Using Control Barrier Functions
**arXiv**：[2603.01705v1](https://arxiv.org/abs/2603.01705) · [PDF](https://arxiv.org/pdf/2603.01705.pdf)  
**作者**：Berk Guler, Kay Pompetzki, Yuanzheng Sun, Simon Manschitz, Jan Peters  

**一句话要点**：提出基于控制屏障函数的BarrierIK框架，在共享自主中确保混合后安全

**关键词**：共享自主, 控制屏障函数, 逆运动学, 安全关键控制, 障碍物避让, 人机交互

## 3 点简述
- 共享自主中线性混合在杂乱环境下可能产生不安全命令，现有方法仅软约束安全
- 在逆运动学层使用控制屏障函数，提供硬安全保证同时保持任务性能
- 仿真和VR用户研究表明，该方法减少违规时间、提高最小间隙，提升感知安全和信任

## 摘要（原文）

> Shared autonomy blends operator intent with autonomous assistance. In cluttered environments, linear blending can produce unsafe commands even when each source is individually collision-free. Many existing approaches model obstacle avoidance through potentials or cost terms, which only enforce safety as a soft constraint. In contrast, safety-critical control requires hard guarantees. We investigate the use of control barrier functions (CBFs) at the inverse kinematics (IK) layer of shared autonomy, targeting post-blend safety while preserving task performance. Our approach is evaluated in simulation on representative cluttered environments and in a VR teleoperation study comparing pure teleoperation with shared autonomy. Across conditions, employing CBFs at the IK layer reduces violation time and increases minimum clearance while maintaining task performance. In the user study, participants reported higher perceived safety and trust, lower interference, and an overall preference for shared autonomy with our safety filter. Additional materials available at https://berkguler.github.io/barrierik.

