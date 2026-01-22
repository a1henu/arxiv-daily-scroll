---
layout: default
title: MonoRace: Winning Champion-Level Drone Racing with Robust Monocular AI
---

# MonoRace: Winning Champion-Level Drone Racing with Robust Monocular AI
**arXiv**：[2601.15222v1](https://arxiv.org/abs/2601.15222) · [PDF](https://arxiv.org/pdf/2601.15222.pdf)  
**作者**：Stavrow A. Bahnam, Robin Ferede, Till M. Blaha, Anton E. Lang, Erin Lucassen, Quentin Missinne, Aderik E. C. Verraest, Christophe De Wagter, Guido C. H. E. de Croon  

**一句话要点**：提出MonoRace方法，在无人机竞速中仅用单目相机和IMU实现冠军级自主飞行。

**关键词**：自主无人机竞速, 单目视觉状态估计, 神经网络控制, 离线参数优化, 高速飞行

## 3 点简述
- 核心问题：在资源受限的无人机上实现高速自主竞速，需鲁棒状态估计和实时控制。
- 方法要点：结合神经网络门分割与无人机模型进行状态估计，并离线优化相机校准参数。
- 实验或效果：在2025年阿布扎比比赛中击败所有AI团队和人类冠军，速度达100 km/h。

## 摘要（原文）

> Autonomous drone racing represents a major frontier in robotics research. It requires an Artificial Intelligence (AI) that can run on board light-weight flying robots under tight resource and time constraints, while pushing the physical system to its limits. The state of the art in this area consists of a system with a stereo camera and an inertial measurement unit (IMU) that beat human drone racing champions in a controlled indoor environment. Here, we present MonoRace: an onboard drone racing approach that uses a monocular, rolling-shutter camera and IMU that generalizes to a competition environment without any external motion tracking system. The approach features robust state estimation that combines neural-network-based gate segmentation with a drone model. Moreover, it includes an offline optimization procedure that leverages the known geometry of gates to refine any state estimation parameter. This offline optimization is based purely on onboard flight data and is important for fine-tuning the vital external camera calibration parameters. Furthermore, the guidance and control are performed by a neural network that foregoes inner loop controllers by directly sending motor commands. This small network runs on the flight controller at 500Hz. The proposed approach won the 2025 Abu Dhabi Autonomous Drone Racing Competition (A2RL), outperforming all competing AI teams and three human world champion pilots in a direct knockout tournament. It set a new milestone in autonomous drone racing research, reaching speeds up to 100 km/h on the competition track and successfully coping with problems such as camera interference and IMU saturation.

