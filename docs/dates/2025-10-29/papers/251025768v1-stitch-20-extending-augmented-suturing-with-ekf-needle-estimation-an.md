---
layout: default
title: STITCH 2.0: Extending Augmented Suturing with EKF Needle Estimation and Thread Management
---

# STITCH 2.0: Extending Augmented Suturing with EKF Needle Estimation and Thread Management
**arXiv**：[2510.25768v1](https://arxiv.org/abs/2510.25768) · [PDF](https://arxiv.org/pdf/2510.25768.pdf)  
**作者**：Kush Hari, Ziyang Chen, Hansoul Kim, Ken Goldberg  

**一句话要点**：提出STITCH 2.0以改进机器人缝合，通过EKF针位估计和线程管理提升伤口闭合效果

**关键词**：机器人缝合, EKF针位估计, 线程管理, 伤口闭合, 增强灵巧性

## 3 点简述
- 核心问题：机器人缝合中针位跟踪不准和线程管理差，导致伤口闭合不完整
- 方法要点：引入EKF针位估计、线程解缠方法和自动3D缝合对齐算法
- 实验或效果：平均74.4%伤口闭合率，比基线多66%缝合，时间减少38%

## 摘要（原文）

> Surgical suturing is a high-precision task that impacts patient healing and
> scarring. Suturing skill varies widely between surgeons, highlighting the need
> for robot assistance. Previous robot suturing works, such as STITCH 1.0 [1],
> struggle to fully close wounds due to inaccurate needle tracking and poor
> thread management. To address these challenges, we present STITCH 2.0, an
> elevated augmented dexterity pipeline with seven improvements including:
> improved EKF needle pose estimation, new thread untangling methods, and an
> automated 3D suture alignment algorithm. Experimental results over 15 trials
> find that STITCH 2.0 on average achieves 74.4% wound closure with 4.87 sutures
> per trial, representing 66% more sutures in 38% less time compared to the
> previous baseline. When two human interventions are allowed, STITCH 2.0
> averages six sutures with 100% wound closure rate. Project website:
> https://stitch-2.github.io/

