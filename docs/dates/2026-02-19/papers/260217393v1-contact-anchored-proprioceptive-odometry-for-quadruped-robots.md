---
layout: default
title: Contact-Anchored Proprioceptive Odometry for Quadruped Robots
---

# Contact-Anchored Proprioceptive Odometry for Quadruped Robots
**arXiv**：[2602.17393v1](https://arxiv.org/abs/2602.17393) · [PDF](https://arxiv.org/pdf/2602.17393.pdf)  
**作者**：Minxing Sun, Yao Mao  

**一句话要点**：提出基于接触锚定的本体感知里程计，用于无外部传感器的腿式机器人位姿估计

**关键词**：本体感知里程计, 腿式机器人定位, 接触状态估计, 运动学约束, 四足机器人, 无外部传感器定位

## 3 点简述
- 核心问题：仅依赖IMU和关节传感器的腿式机器人里程计存在长期漂移和噪声干扰
- 方法要点：将接触腿作为运动学锚点，通过足端力估计筛选可靠接触点，利用足落位置提供世界坐标系约束
- 实验效果：在多种四足机器人平台上测试，水平环路误差在0.16-7.68米，垂直环路误差在0.1-0.54米

## 摘要（原文）

> Reliable odometry for legged robots without cameras or LiDAR remains challenging due to IMU drift and noisy joint velocity sensing. This paper presents a purely proprioceptive state estimator that uses only IMU and motor measurements to jointly estimate body pose and velocity, with a unified formulation applicable to biped, quadruped, and wheel-legged robots. The key idea is to treat each contacting leg as a kinematic anchor: joint-torque--based foot wrench estimation selects reliable contacts, and the corresponding footfall positions provide intermittent world-frame constraints that suppress long-term drift. To prevent elevation drift during extended traversal, we introduce a lightweight height clustering and time-decay correction that snaps newly recorded footfall heights to previously observed support planes. To improve foot velocity observations under encoder quantization, we apply an inverse-kinematics cubature Kalman filter that directly filters foot-end velocities from joint angles and velocities. The implementation further mitigates yaw drift through multi-contact geometric consistency and degrades gracefully to a kinematics-derived heading reference when IMU yaw constraints are unavailable or unreliable. We evaluate the method on four quadruped platforms (three Astrall robots and a Unitree Go2 EDU) using closed-loop trajectories. On Astrall point-foot robot~A, a $\sim$200\,m horizontal loop and a $\sim$15\,m vertical loop return with 0.1638\,m and 0.219\,m error, respectively; on wheel-legged robot~B, the corresponding errors are 0.2264\,m and 0.199\,m. On wheel-legged robot~C, a $\sim$700\,m horizontal loop yields 7.68\,m error and a $\sim$20\,m vertical loop yields 0.540\,m error. Unitree Go2 EDU closes a $\sim$120\,m horizontal loop with 2.2138\,m error and a $\sim$8\,m vertical loop with less than 0.1\,m vertical error. github.com/ShineMinxing/Ros2Go2Estimator.git

