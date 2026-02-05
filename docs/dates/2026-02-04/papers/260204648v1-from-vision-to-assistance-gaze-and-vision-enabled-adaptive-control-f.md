---
layout: default
title: From Vision to Assistance: Gaze and Vision-Enabled Adaptive Control for a Back-Support Exoskeleton
---

# From Vision to Assistance: Gaze and Vision-Enabled Adaptive Control for a Back-Support Exoskeleton
**arXiv**：[2602.04648v1](https://arxiv.org/abs/2602.04648) · [PDF](https://arxiv.org/pdf/2602.04648.pdf)  
**作者**：Alessandro Leanza, Paolo Franceschi, Blerina Spahiu, Loris Roveda  

**一句话要点**：提出基于视觉与注视的主动控制框架，以增强腰部支撑外骨骼的辅助响应与用户体验。

**关键词**：腰部支撑外骨骼, 视觉门控控制, 注视跟踪, 自适应辅助, 用户研究, 第一人称感知

## 3 点简述
- 核心问题：现有腰部支撑外骨骼依赖负载估计或视觉系统，但缺乏直接控制信息，影响辅助及时性与情境感知。
- 方法要点：集成第一人称YOLO抓取检测、有限状态机和可变导纳控制器，根据姿态与物体状态自适应调节扭矩。
- 实验或效果：用户研究表明，视觉门控辅助显著降低感知体力需求，提升流畅度、信任度和舒适度，用户偏好该模式。

## 摘要（原文）

> Back-support exoskeletons have been proposed to mitigate spinal loading in industrial handling, yet their effectiveness critically depends on timely and context-aware assistance. Most existing approaches rely either on load-estimation techniques (e.g., EMG, IMU) or on vision systems that do not directly inform control. In this work, we present a vision-gated control framework for an active lumbar occupational exoskeleton that leverages egocentric vision with wearable gaze tracking. The proposed system integrates real-time grasp detection from a first-person YOLO-based perception system, a finite-state machine (FSM) for task progression, and a variable admittance controller to adapt torque delivery to both posture and object state. A user study with 15 participants performing stooping load lifting trials under three conditions (no exoskeleton, exoskeleton without vision, exoskeleton with vision) shows that vision-gated assistance significantly reduces perceived physical demand and improves fluency, trust, and comfort. Quantitative analysis reveals earlier and stronger assistance when vision is enabled, while questionnaire results confirm user preference for the vision-gated mode. These findings highlight the potential of egocentric vision to enhance the responsiveness, ergonomics, safety, and acceptance of back-support exoskeletons.

