---
layout: default
title: Vision-only UAV State Estimation for Fast Flights Without External Localization Systems: A2RL Drone Racing Finalist Approach
---

# Vision-only UAV State Estimation for Fast Flights Without External Localization Systems: A2RL Drone Racing Finalist Approach
**arXiv**：[2602.01860v1](https://arxiv.org/abs/2602.01860) · [PDF](https://arxiv.org/pdf/2602.01860.pdf)  
**作者**：Filip Novák, Matěj Petrlík, Matej Novosad, Parakh M. Gupta, Robert Pěnička, Martin Saska  

**一句话要点**：提出基于单目相机与IMU的无人机状态估计方法，以解决GNSS拒止环境下快速飞行时的漂移问题。

**关键词**：无人机状态估计, 视觉惯性里程计, 漂移校正, 单目相机, GNSS拒止环境, 快速飞行

## 3 点简述
- 核心问题：在GNSS拒止环境中，快速机动飞行时视觉惯性里程计（VIO）的漂移导致状态估计不准确。
- 方法要点：融合VIO、基于地标的相机测量和IMU数据，通过新颖漂移模型校正所有VIO状态（位置、姿态、线性和角速度）。
- 实验或效果：经1600次仿真和真实实验验证，在A2RL无人机竞速挑战赛中进入前四名并获奖。

## 摘要（原文）

> Fast flights with aggressive maneuvers in cluttered GNSS-denied environments require fast, reliable, and accurate UAV state estimation. In this paper, we present an approach for onboard state estimation of a high-speed UAV using a monocular RGB camera and an IMU. Our approach fuses data from Visual-Inertial Odometry (VIO), an onboard landmark-based camera measurement system, and an IMU to produce an accurate state estimate. Using onboard measurement data, we estimate and compensate for VIO drift through a novel mathematical drift model. State-of-the-art approaches often rely on more complex hardware (e.g., stereo cameras or rangefinders) and use uncorrected drifting VIO velocities, orientation, and angular rates, leading to errors during fast maneuvers. In contrast, our method corrects all VIO states (position, orientation, linear and angular velocity), resulting in accurate state estimation even during rapid and dynamic motion. Our approach was thoroughly validated through 1600 simulations and numerous real-world experiments. Furthermore, we applied the proposed method in the A2RL Drone Racing Challenge 2025, where our team advanced to the final four out of 210 teams and earned a medal.

