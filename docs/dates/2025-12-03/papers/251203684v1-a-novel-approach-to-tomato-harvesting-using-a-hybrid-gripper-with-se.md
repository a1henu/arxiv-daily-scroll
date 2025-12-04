---
layout: default
title: A Novel Approach to Tomato Harvesting Using a Hybrid Gripper with Semantic Segmentation and Keypoint Detection
---

# A Novel Approach to Tomato Harvesting Using a Hybrid Gripper with Semantic Segmentation and Keypoint Detection
**arXiv**：[2512.03684v1](https://arxiv.org/abs/2512.03684) · [PDF](https://arxiv.org/pdf/2512.03684.pdf)  
**作者**：Shahid Ansari, Mahendra Kumar Gohil, Yusuke Maeda, Bishakh Bhattacharya  

**一句话要点**：提出结合语义分割与关键点检测的混合夹爪系统，用于番茄自主采摘

**关键词**：番茄采摘机器人, 混合夹爪设计, 语义分割, 关键点检测, 抓取力控制, 轨迹规划

## 3 点简述
- 核心问题：在杂乱环境中实现番茄的轻柔、可靠采摘，避免损伤和滑移。
- 方法要点：使用软硬混合夹爪结合视觉感知，通过PID控制器闭环调节抓取力，并基于PSO规划机械臂轨迹。
- 实验效果：平均采摘周期24.34秒，成功率约80%，抓取力保持在0.20–0.50 N的低水平。

## 摘要（原文）

> This paper presents an autonomous tomato-harvesting system built around a hybrid robotic gripper that combines six soft auxetic fingers with a rigid exoskeleton and a latex basket to achieve gentle, cage-like grasping. The gripper is driven by a servo-actuated Scotch--yoke mechanism, and includes separator leaves that form a conical frustum for fruit isolation, with an integrated micro-servo cutter for pedicel cutting. For perception, an RGB--D camera and a Detectron2-based pipeline perform semantic segmentation of ripe/unripe tomatoes and keypoint localization of the pedicel and fruit center under occlusion and variable illumination. An analytical model derived using the principle of virtual work relates servo torque to grasp force, enabling design-level reasoning about actuation requirements. During execution, closed-loop grasp-force regulation is achieved using a proportional--integral--derivative controller with feedback from force-sensitive resistors mounted on selected fingers to prevent slip and bruising. Motion execution is supported by Particle Swarm Optimization (PSO)--based trajectory planning for a 5-DOF manipulator. Experiments demonstrate complete picking cycles (approach, separation, cutting, grasping, transport, release) with an average cycle time of 24.34~s and an overall success rate of approximately 80\%, while maintaining low grasp forces (0.20--0.50~N). These results validate the proposed hybrid gripper and integrated vision--control pipeline for reliable harvesting in cluttered environments.

