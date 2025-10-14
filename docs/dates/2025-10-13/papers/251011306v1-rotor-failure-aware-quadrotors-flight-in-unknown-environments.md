---
layout: default
title: Rotor-Failure-Aware Quadrotors Flight in Unknown Environments
---

# Rotor-Failure-Aware Quadrotors Flight in Unknown Environments
**arXiv**：[2510.11306v1](https://arxiv.org/abs/2510.11306) · [PDF](https://arxiv.org/pdf/2510.11306.pdf)  
**作者**：Xiaobin Zhou, Miao Wang, Chengao Li, Can Cui, Ruibin Zhang, Yongchao Wang, Chao Xu, Fei Gao  

**一句话要点**：提出转子故障感知四旋翼导航系统，以在未知环境中实现自主飞行

**关键词**：四旋翼导航, 转子故障检测, 非线性模型预测控制, 时空优化, LiDAR感知, 故障容错控制

## 3 点简述
- 核心问题：转子故障导致高速旋转和振动，挑战未知环境自主飞行
- 方法要点：结合故障检测诊断、非线性模型预测控制和时空联合优化规划
- 实验效果：在杂乱房间和未知森林中首次实现转子故障下的自主飞行

## 摘要（原文）

> Rotor failures in quadrotors may result in high-speed rotation and vibration
> due to rotor imbalance, which introduces significant challenges for autonomous
> flight in unknown environments. The mainstream approaches against rotor
> failures rely on fault-tolerant control (FTC) and predefined trajectory
> tracking. To the best of our knowledge, online failure detection and diagnosis
> (FDD), trajectory planning, and FTC of the post-failure quadrotors in unknown
> and complex environments have not yet been achieved. This paper presents a
> rotor-failure-aware quadrotor navigation system designed to mitigate the
> impacts of rotor imbalance. First, a composite FDD-based nonlinear model
> predictive controller (NMPC), incorporating motor dynamics, is designed to
> ensure fast failure detection and flight stability. Second, a
> rotor-failure-aware planner is designed to leverage FDD results and
> spatial-temporal joint optimization, while a LiDAR-based quadrotor platform
> with four anti-torque plates is designed to enable reliable perception under
> high-speed rotation. Lastly, extensive benchmarks against state-of-the-art
> methods highlight the superior performance of the proposed approach in
> addressing rotor failures, including propeller unloading and motor stoppage.
> The experimental results demonstrate, for the first time, that our approach
> enables autonomous quadrotor flight with rotor failures in challenging
> environments, including cluttered rooms and unknown forests.

