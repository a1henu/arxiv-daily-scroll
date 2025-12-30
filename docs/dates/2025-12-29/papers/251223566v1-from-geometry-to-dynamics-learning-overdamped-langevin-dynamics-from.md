---
layout: default
title: From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints
---

# From geometry to dynamics: Learning overdamped Langevin dynamics from sparse observations with geometric constraints
**arXiv**：[2512.23566v1](https://arxiv.org/abs/2512.23566) · [PDF](https://arxiv.org/pdf/2512.23566.pdf)  
**作者**：Dimitra Maoutsa  

**一句话要点**：提出几何约束下从稀疏观测学习过阻尼朗之万动力学的新框架

**关键词**：随机系统识别, 几何约束, 过阻尼朗之万动力学, 稀疏观测, 随机控制, 路径增强

## 3 点简述
- 核心问题：如何从时间稀疏采样的轨迹中学习随机系统的动力学规律，现有方法受限。
- 方法要点：将推断重构为随机控制问题，利用几何驱动的路径增强，基于不变密度几何重建轨迹。
- 实验或效果：在过阻尼朗之万系统中，即使数据极度欠采样，也能准确恢复动力学，优于现有方法。

## 摘要（原文）

> How can we learn the laws underlying the dynamics of stochastic systems when their trajectories are sampled sparsely in time? Existing methods either require temporally resolved high-frequency observations, or rely on geometric arguments that apply only to conservative systems, limiting the range of dynamics they can recover. Here, we present a new framework that reconciles these two perspectives by reformulating inference as a stochastic control problem. Our method uses geometry-driven path augmentation, guided by the geometry in the system's invariant density to reconstruct likely trajectories and infer the underlying dynamics without assuming specific parametric models. Applied to overdamped Langevin systems, our approach accurately recovers stochastic dynamics even from extremely undersampled data, outperforming existing methods in synthetic benchmarks. This work demonstrates the effectiveness of incorporating geometric inductive biases into stochastic system identification methods.

