---
layout: default
title: HumanMPC - Safe and Efficient MAV Navigation among Humans
---

# HumanMPC - Safe and Efficient MAV Navigation among Humans
**arXiv**：[2510.17525v1](https://arxiv.org/abs/2510.17525) · [PDF](https://arxiv.org/pdf/2510.17525.pdf)  
**作者**：Simon Schaefer, Helen Oleynikova, Sandra Hirche, Stefan Leutenegger  

**一句话要点**：提出HumanMPC框架以安全高效导航MAV于人群中

**关键词**：模型预测控制, 无人机导航, 人体运动预测, 可达性分析, 安全保证

## 3 点简述
- 现有方法多限于2D人群导航，忽略人体动态复杂性。
- 结合可达性安全保证与数据驱动模型，优化控制输入。
- 仿真与真实实验验证安全性和效率优于基线方法。

## 摘要（原文）

> Safe and efficient robotic navigation among humans is essential for
> integrating robots into everyday environments. Most existing approaches focus
> on simplified 2D crowd navigation and fail to account for the full complexity
> of human body dynamics beyond root motion. We present HumanMPC, a Model
> Predictive Control (MPC) framework for 3D Micro Air Vehicle (MAV) navigation
> among humans that combines theoretical safety guarantees with data-driven
> models for realistic human motion forecasting. Our approach introduces a novel
> twist to reachability-based safety formulation that constrains only the initial
> control input for safety while modeling its effects over the entire planning
> horizon, enabling safe yet efficient navigation. We validate HumanMPC in both
> simulated experiments using real human trajectories and in the real-world,
> demonstrating its effectiveness across tasks ranging from goal-directed
> navigation to visual servoing for human tracking. While we apply our method to
> MAVs in this work, it is generic and can be adapted by other platforms. Our
> results show that the method ensures safety without excessive conservatism and
> outperforms baseline approaches in both efficiency and reliability.

