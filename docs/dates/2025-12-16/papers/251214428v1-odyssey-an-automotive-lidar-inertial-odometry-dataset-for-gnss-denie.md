---
layout: default
title: Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
---

# Odyssey: An Automotive Lidar-Inertial Odometry Dataset for GNSS-denied situations
**arXiv**：[2512.14428v1](https://arxiv.org/abs/2512.14428) · [PDF](https://arxiv.org/pdf/2512.14428.pdf)  
**作者**：Aaron Kurda, Simon Steuernagel, Lukas Jung, Marcus Baum  

**一句话要点**：提出Odyssey数据集，基于RLG-INS提供GNSS缺失环境下的激光雷达-惯性里程计基准数据

**关键词**：激光雷达-惯性里程计, GNSS缺失环境, 环形激光陀螺仪, 数据集, 地面真值, 地点识别

## 3 点简述
- 核心问题：现有数据集因IMU限制，难以支持GNSS信号长期缺失环境（如隧道、停车场）的LIO/SLAM研究。
- 方法要点：使用导航级INS配备环形激光陀螺仪（RLG），提供高偏置稳定性的地面真值，覆盖多种代表性场景。
- 实验或效果：数据集公开可用，支持LIO、地点识别等任务，通过轨迹重复和地理坐标集成增强实用性。

## 摘要（原文）

> The development and evaluation of Lidar-Inertial Odometry (LIO) and Simultaneous Localization and Mapping (SLAM) systems requires a precise ground truth. The Global Navigation Satellite System (GNSS) is often used as a foundation for this, but its signals can be unreliable in obstructed environments due to multi-path effects or loss-of-signal. While existing datasets compensate for the sporadic loss of GNSS signals by incorporating Inertial Measurement Unit (IMU) measurements, the commonly used Micro-Electro-Mechanical Systems (MEMS) or Fiber Optic Gyroscope (FOG)-based systems do not permit the prolonged study of GNSS-denied environments. To close this gap, we present Odyssey, a LIO dataset with a focus on GNSS-denied environments such as tunnels and parking garages as well as other underrepresented, yet ubiquitous situations such as stop-and-go-traffic, bumpy roads and wide open fields. Our ground truth is derived from a navigation-grade Inertial Navigation System (INS) equipped with a Ring Laser Gyroscope (RLG), offering exceptional bias stability characteristics compared to IMUs used in existing datasets and enabling the prolonged and accurate study of GNSS-denied environments. This makes Odyssey the first publicly available dataset featuring a RLG-based INS. Besides providing data for LIO, we also support other tasks, such as place recognition, through the threefold repetition of all trajectories as well as the integration of external mapping data by providing precise geodetic coordinates. All data, dataloader and other material is available online at https://odyssey.uni-goettingen.de/ .

