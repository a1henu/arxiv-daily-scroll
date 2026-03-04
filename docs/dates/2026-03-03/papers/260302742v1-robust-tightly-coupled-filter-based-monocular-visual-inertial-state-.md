---
layout: default
title: Robust Tightly-Coupled Filter-Based Monocular Visual-Inertial State Estimation and Graph-Based Evaluation for Autonomous Drone Racing
---

# Robust Tightly-Coupled Filter-Based Monocular Visual-Inertial State Estimation and Graph-Based Evaluation for Autonomous Drone Racing
**arXiv**：[2603.02742v1](https://arxiv.org/abs/2603.02742) · [PDF](https://arxiv.org/pdf/2603.02742.pdf)  
**作者**：Maulana Bisyir Azhari, Donghun Han, SungJun Park, David Hyunchul Shim  

**一句话要点**：提出基于误差状态卡尔曼滤波的鲁棒单目视觉惯性状态估计框架，用于自主无人机竞速，并引入因子图优化进行离线评估。

**关键词**：自主无人机竞速, 视觉惯性状态估计, 误差状态卡尔曼滤波, 因子图优化, 鲁棒重加权, 离线评估

## 3 点简述
- 传统视觉惯性框架在高速机动中易受感知退化影响，且依赖四特征可见的PnP求解，导致效率低和鲁棒性差。
- ADR-VINS通过直接像素重投影误差集成到滤波器中，支持最少两个角点更新，并采用鲁棒重加权处理异常值，提升计算效率。
- 在TII-RATM数据集上验证，ADR-VINS平均平移误差0.134米，ADR-FGO为0.060米，并在A2RL竞速赛中成功部署，支持20.9米/秒高速飞行。

## 摘要（原文）

> Autonomous drone racing (ADR) demands state estimation that is simultaneously computationally efficient and resilient to the perceptual degradation experienced during extreme velocity and maneuvers. Traditional frameworks typically rely on conventional visual-inertial pipelines with loosely-coupled gate-based Perspective-n-Points (PnP) corrections that suffer from a rigid requirement for four visible features and information loss in intermediate steps. Furthermore, the absence of GNSS and Motion Capture systems in uninstrumented, competitive racing environments makes the objective evaluation of such systems remarkably difficult. To address these limitations, we propose ADR-VINS, a robust, monocular visual-inertial state estimation framework based on an Error-State Kalman Filter (ESKF) tailored for autonomous drone racing. Our approach integrates direct pixel reprojection errors from gate corners features as innovation terms within the filter. By bypassing intermediate PnP solvers, ADR-VINS maintains valid state updates with as few as two visible corners and utilizes robust reweighting instead of RANSAC-based schemes to handle outliers, enhancing computational efficiency. Furthermore, we introduce ADR-FGO, an offline Factor-Graph Optimization framework to generate high-fidelity reference trajectories that facilitate post-flight performance evaluation and analysis on uninstrumented, GNSS-denied environments. The proposed system is validated using TII-RATM dataset, where ADR-VINS achieves an average RMS translation error of 0.134 m, while ADR-FGO yields 0.060 m as a smoothing-based reference. Finally, ADR-VINS was successfully deployed in the A2RL Drone Championship Season 2, maintaining stable and robust estimation despite noisy detections during high-agility flight at top speeds of 20.9 m/s. We further utilize ADR-FGO for post-flight evaluation in uninstrumented racing environments.

