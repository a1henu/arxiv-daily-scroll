---
layout: default
title: An Open-Source Robotics Research Platform for Autonomous Laparoscopic Surgery
---

# An Open-Source Robotics Research Platform for Autonomous Laparoscopic Surgery
**arXiv**：[2603.08490v1](https://arxiv.org/abs/2603.08490) · [PDF](https://arxiv.org/pdf/2603.08490.pdf)  
**作者**：Ariel Rodriguez, Lorenzo Mazza, Martin Lelis, Rayan Younis, Sebastian Bodenstedt, Martin Wagner, Stefanie Speidel  

**一句话要点**：提出开源机器人无关远程运动中心控制器，用于自主腹腔镜手术研究平台。

**关键词**：自主手术机器人, 远程运动中心控制, 开源平台, 腹腔镜手术, 机器人无关控制器, ROS集成

## 3 点简述
- 现有达芬奇研究套件存在电缆驱动机械限制，影响状态空间一致性和自主策略训练。
- 基于闭式解析速度求解器，实现确定性套管约束，支持任意工业机械臂作为手术机器人。
- 在幻影、离体和活体猪腹腔镜任务中验证，远程运动中心偏差亚毫米，轨迹平滑度媲美专家演示。

## 摘要（原文）

> Autonomous robot-assisted surgery demands reliable, high-precision platforms that strictly adhere to the safety and kinematic constraints of minimally invasive procedures. Existing research platforms, primarily based on the da Vinci Research Kit, suffer from cable-driven mechanical limitations that degrade state-space consistency and hinder the downstream training of reliable autonomous policies. We present an open-source, robot-agnostic Remote Center of Motion (RCM) controller based on a closed-form analytical velocity solver that enforces the trocar constraint deterministically without iterative optimization. The controller operates in Cartesian space, enabling any industrial manipulator to function as a surgical robot. We provide implementations for the UR5e and Franka Emika Panda manipulators, and integrate stereoscopic 3D perception. We integrate the robot control into a full-stack ROS-based surgical robotics platform supporting teleoperation, demonstration recording, and deployment of learned policies via a decoupled server-client architecture. We validate the system on a bowel grasping and retraction task across phantom, ex vivo, and in vivo porcine laparoscopic procedures. RCM deviations remain sub-millimeter across all conditions, and trajectory smoothness metrics (SPARC, LDLJ) are comparable to expert demonstrations from the JIGSAWS benchmark recorded on the da Vinci system. These results demonstrate that the platform provides the precision and robustness required for teleoperation, data collection and autonomous policy deployment in realistic surgical scenarios.

