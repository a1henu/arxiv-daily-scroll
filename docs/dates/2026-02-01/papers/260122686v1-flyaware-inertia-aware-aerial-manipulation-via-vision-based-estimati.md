---
layout: default
title: FlyAware: Inertia-Aware Aerial Manipulation via Vision-Based Estimation and Post-Grasp Adaptation
---

# FlyAware: Inertia-Aware Aerial Manipulation via Vision-Based Estimation and Post-Grasp Adaptation
**arXiv**：[2601.22686v1](https://arxiv.org/abs/2601.22686) · [PDF](https://arxiv.org/pdf/2601.22686.pdf)  
**作者**：Biyu Ye, Na Fan, Zhengping Fan, Weiliang Deng, Hongming Chen, Qifeng Chen, Ximin Lyu  

**一句话要点**：提出FlyAware框架，通过视觉惯性估计与抓取后适应，解决空中机械臂时变惯性参数挑战。

**关键词**：空中机械臂, 惯性估计, 视觉控制, 自适应控制, 抓取后适应

## 3 点简述
- 核心问题：空中机械臂的时变惯性参数对负载变化和配置敏感，影响稳定操控。
- 方法要点：集成视觉预抓取惯性估计模块与抓取后适应机制，实现实时惯性动态估计与自适应控制。
- 实验或效果：通过频域系统识别评估鲁棒性，真实世界实验验证框架的有效性和可行性。

## 摘要（原文）

> Aerial manipulators (AMs) are gaining increasing attention in automated transportation and emergency services due to their superior dexterity compared to conventional multirotor drones. However, their practical deployment is challenged by the complexity of time-varying inertial parameters, which are highly sensitive to payload variations and manipulator configurations. Inspired by human strategies for interacting with unknown objects, this letter presents a novel onboard framework for robust aerial manipulation. The proposed system integrates a vision-based pre-grasp inertia estimation module with a post-grasp adaptation mechanism, enabling real-time estimation and adaptation of inertial dynamics. For control, we develop an inertia-aware adaptive control strategy based on gain scheduling, and assess its robustness via frequency-domain system identification. Our study provides new insights into post-grasp control for AMs, and real-world experiments validate the effectiveness and feasibility of the proposed framework.

