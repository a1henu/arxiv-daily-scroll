---
layout: default
title: MirrorLimb: Implementing hand pose acquisition and robot teleoperation based on RealMirror
---

# MirrorLimb: Implementing hand pose acquisition and robot teleoperation based on RealMirror
**arXiv**：[2511.08865v1](https://arxiv.org/abs/2511.08865) · [PDF](https://arxiv.org/pdf/2511.08865.pdf)  
**作者**：Cong Tai, Hansheng Wu, Haixu Long, Zhengbin Long, Zhaoyu Zheng, Haodong Xiang, Tao Shen  

**一句话要点**：提出基于RealMirror的低成本手部姿态获取与机器人遥操作框架，以降低上肢机器人操作研究门槛。

**关键词**：手部姿态获取, 机器人遥操作, RealMirror生态, 低成本运动捕捉, VLA数据集构建

## 3 点简述
- 核心问题：传统手部运动捕捉方案成本高，难以实时获取精确姿态数据。
- 方法要点：利用PICO设备实现低成本实时手部运动与姿态数据采集。
- 实验或效果：在Isaac仿真环境中稳定记录机器人轨迹，支持多种末端执行器遥操作。

## 摘要（原文）

> In this work, we present a PICO-based robot remote operating framework that enables low-cost, real-time acquisition of hand motion and pose data, outperforming mainstream visual tracking and motion capture solutions in terms of cost-effectiveness. The framework is natively compatible with the RealMirror ecosystem, offering ready-to-use functionality for stable and precise robotic trajectory recording within the Isaac simulation environment, thereby facilitating the construction of Vision-Language-Action (VLA) datasets. Additionally, the system supports real-time teleoperation of a variety of end-effector-equipped robots, including dexterous hands and robotic grippers. This work aims to lower the technical barriers in the study of upper-limb robotic manipulation, thereby accelerating advancements in VLA-related research.

