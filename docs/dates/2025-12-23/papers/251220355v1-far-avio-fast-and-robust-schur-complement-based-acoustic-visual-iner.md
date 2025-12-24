---
layout: default
title: FAR-AVIO: Fast and Robust Schur-Complement Based Acoustic-Visual-Inertial Fusion Odometry with Sensor Calibration
---

# FAR-AVIO: Fast and Robust Schur-Complement Based Acoustic-Visual-Inertial Fusion Odometry with Sensor Calibration
**arXiv**：[2512.20355v1](https://arxiv.org/abs/2512.20355) · [PDF](https://arxiv.org/pdf/2512.20355.pdf)  
**作者**：Hao Wei, Peiji Wang, Qianhao Wang, Tong Qin, Fei Gao, Yulin Si  

**一句话要点**：提出FAR-AVIO框架，基于舒尔补的声学-视觉-惯性融合里程计，用于水下机器人实时状态估计。

**关键词**：水下机器人, 传感器融合, 舒尔补优化, 扩展卡尔曼滤波, 在线校准, 声学里程计

## 3 点简述
- 水下环境导致视觉-惯性里程计性能下降，声学-视觉-惯性融合可提升精度但计算成本高。
- FAR-AVIO结合舒尔补与扩展卡尔曼滤波，实现恒定时间更新的联合优化，并集成在线传感器健康评估与校准。
- 仿真与真实实验显示，FAR-AVIO在定位精度和计算效率上优于现有方法，适用于低功耗嵌入式平台。

## 摘要（原文）

> Underwater environments impose severe challenges to visual-inertial odometry systems, as strong light attenuation, marine snow and turbidity, together with weakly exciting motions, degrade inertial observability and cause frequent tracking failures over long-term operation. While tightly coupled acoustic-visual-inertial fusion, typically implemented through an acoustic Doppler Velocity Log (DVL) integrated with visual-inertial measurements, can provide accurate state estimation, the associated graph-based optimization is often computationally prohibitive for real-time deployment on resource-constrained platforms. Here we present FAR-AVIO, a Schur-Complement based, tightly coupled acoustic-visual-inertial odometry framework tailored for underwater robots. FAR-AVIO embeds a Schur complement formulation into an Extended Kalman Filter(EKF), enabling joint pose-landmark optimization for accuracy while maintaining constant-time updates by efficiently marginalizing landmark states. On top of this backbone, we introduce Adaptive Weight Adjustment and Reliability Evaluation(AWARE), an online sensor health module that continuously assesses the reliability of visual, inertial and DVL measurements and adaptively regulates their sigma weights, and we develop an efficient online calibration scheme that jointly estimates DVL-IMU extrinsics, without dedicated calibration manoeuvres. Numerical simulations and real-world underwater experiments consistently show that FAR-AVIO outperforms state-of-the-art underwater SLAM baselines in both localization accuracy and computational efficiency, enabling robust operation on low-power embedded platforms. Our implementation has been released as open source software at https://far-vido.gitbook.io/far-vido-docs.

