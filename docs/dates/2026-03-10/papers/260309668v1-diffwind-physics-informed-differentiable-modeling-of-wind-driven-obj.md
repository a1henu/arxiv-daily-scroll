---
layout: default
title: DiffWind: Physics-Informed Differentiable Modeling of Wind-Driven Object Dynamics
---

# DiffWind: Physics-Informed Differentiable Modeling of Wind-Driven Object Dynamics
**arXiv**：[2603.09668v1](https://arxiv.org/abs/2603.09668) · [PDF](https://arxiv.org/pdf/2603.09668.pdf)  
**作者**：Yuanhang Lei, Boming Zhao, Zesong Yang, Xingxuan Li, Tao Cheng, Haocheng Peng, Ru Zhang, Yang Yang, Siyuan Huang, Yujun Shen, Ruizhen Hu, Hujun Bao, Zhaopeng Cui  

**一句话要点**：提出DiffWind框架，通过物理约束可微分建模解决视频中风驱动物体动态重建与模拟问题

**关键词**：风驱动物体动态建模, 物理约束可微分模拟, 视频重建与仿真, 风场优化, 粒子系统交互

## 3 点简述
- 核心问题：风不可见且时空变化，物体变形复杂，导致从视频建模风驱动动态极具挑战
- 方法要点：统一风场网格表示、物体粒子系统、可微分渲染与模拟，结合LBM物理约束优化
- 实验或效果：在合成与真实数据集上优于现有方法，支持新风条件下的前向模拟和风重定向应用

## 摘要（原文）

> Modeling wind-driven object dynamics from video observations is highly challenging due to the invisibility and spatio-temporal variability of wind, as well as the complex deformations of objects. We present DiffWind, a physics-informed differentiable framework that unifies wind-object interaction modeling, video-based reconstruction, and forward simulation. Specifically, we represent wind as a grid-based physical field and objects as particle systems derived from 3D Gaussian Splatting, with their interaction modeled by the Material Point Method (MPM). To recover wind-driven object dynamics, we introduce a reconstruction framework that jointly optimizes the spatio-temporal wind force field and object motion through differentiable rendering and simulation. To ensure physical validity, we incorporate the Lattice Boltzmann Method (LBM) as a physics-informed constraint, enforcing compliance with fluid dynamics laws. Beyond reconstruction, our method naturally supports forward simulation under novel wind conditions and enables new applications such as wind retargeting. We further introduce WD-Objects, a dataset of synthetic and real-world wind-driven scenes. Extensive experiments demonstrate that our method significantly outperforms prior dynamic scene modeling approaches in both reconstruction accuracy and simulation fidelity, opening a new avenue for video-based wind-object interaction modeling.

