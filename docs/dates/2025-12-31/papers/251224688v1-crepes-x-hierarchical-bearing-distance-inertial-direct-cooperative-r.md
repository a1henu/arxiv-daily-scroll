---
layout: default
title: CREPES-X: Hierarchical Bearing-Distance-Inertial Direct Cooperative Relative Pose Estimation System
---

# CREPES-X: Hierarchical Bearing-Distance-Inertial Direct Cooperative Relative Pose Estimation System
**arXiv**：[2512.24688v1](https://arxiv.org/abs/2512.24688) · [PDF](https://arxiv.org/pdf/2512.24688.pdf)  
**作者**：Zhehan Li, Zheng Wang, Jiadong Lu, Qi Liu, Zhiren Xun, Yue Wang, Fei Gao, Chao Xu, Yanjun Cao  

**一句话要点**：提出CREPES-X分层框架，通过融合方位-距离-惯性测量实现多机器人鲁棒相对位姿估计

**关键词**：相对位姿估计, 多机器人系统, 传感器融合, 分层估计, 鲁棒优化, 紧凑硬件

## 3 点简述
- 核心问题：多机器人系统中，现有方法依赖环境特征或惯性假设，在复杂环境下易受非视距和异常值影响，鲁棒高效融合测量仍具挑战
- 方法要点：采用紧凑硬件设计，结合单帧和多帧分层估计器，通过闭式解和优化提升速度、精度与鲁棒性
- 实验或效果：仿真与真实实验验证，在高达90%方位异常值下保持鲁棒，真实数据集RMSE达0.073米和1.817度

## 摘要（原文）

> Relative localization is critical for cooperation in autonomous multi-robot systems. Existing approaches either rely on shared environmental features or inertial assumptions or suffer from non-line-of-sight degradation and outliers in complex environments. Robust and efficient fusion of inter-robot measurements such as bearings, distances, and inertials for tens of robots remains challenging. We present CREPES-X (Cooperative RElative Pose Estimation System with multiple eXtended features), a hierarchical relative localization framework that enhances speed, accuracy, and robustness under challenging conditions, without requiring any global information. CREPES-X starts with a compact hardware design: InfraRed (IR) LEDs, an IR camera, an ultra-wideband module, and an IMU housed in a cube no larger than 6cm on each side. Then CREPES-X implements a two-stage hierarchical estimator to meet different requirements, considering speed, accuracy, and robustness. First, we propose a single-frame relative estimator that provides instant relative poses for multi-robot setups through a closed-form solution and robust bearing outlier rejection. Then a multi-frame relative estimator is designed to offer accurate and robust relative states by exploring IMU pre-integration via robocentric relative kinematics with loosely- and tightly-coupled optimization. Extensive simulations and real-world experiments validate the effectiveness of CREPES-X, showing robustness to up to 90% bearing outliers, proving resilience in challenging conditions, and achieving RMSE of 0.073m and 1.817° in real-world datasets.

