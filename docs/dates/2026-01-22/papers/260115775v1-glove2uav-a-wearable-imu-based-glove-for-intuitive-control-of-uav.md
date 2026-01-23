---
layout: default
title: Glove2UAV: A Wearable IMU-Based Glove for Intuitive Control of UAV
---

# Glove2UAV: A Wearable IMU-Based Glove for Intuitive Control of UAV
**arXiv**：[2601.15775v1](https://arxiv.org/abs/2601.15775) · [PDF](https://arxiv.org/pdf/2601.15775.pdf)  
**作者**：Amir Habel, Ivan Snegirev, Elizaveta Semenyakina, Miguel Altamirano Cabrera, Jeffrin Sam, Fawad Mehboob, Roohan Ahmed Khan, Muhammad Ahsan Mustafa, Dzmitry Tsetserukou  

**一句话要点**：提出Glove2UAV，一种基于IMU的手套，用于通过手势直观控制无人机，并集成振动触觉警告。

**关键词**：可穿戴设备, 无人机控制, 手势识别, 振动触觉反馈, 实时系统

## 3 点简述
- 核心问题：设计轻量可穿戴界面，实现无人机在动态飞行中的安全直观控制。
- 方法要点：使用中值滤波和Madgwick算法实时估计手部姿态，映射为飞行控制指令，并加入速度超限振动反馈。
- 实验或效果：在仿真和真实飞行中验证实时性，展示快速命令执行、稳定手势-运动耦合及警告及时性。

## 摘要（原文）

> This paper presents Glove2UAV, a wearable IMU-glove interface for intuitive UAV control through hand and finger gestures, augmented with vibrotactile warnings for exceeding predefined speed thresholds. To promote safer and more predictable interaction in dynamic flight, Glove2UAV is designed as a lightweight and easily deployable wearable interface intended for real-time operation. Glove2UAV streams inertial measurements in real time and estimates palm and finger orientations using a compact processing pipeline that combines median-based outlier suppression with Madgwick-based orientation estimation. The resulting motion estimations are mapped to a small set of control primitives for directional flight (forward/backward and lateral motion) and, when supported by the platform, to object-interaction commands. Vibrotactile feedback is triggered when flight speed exceeds predefined threshold values, providing an additional alert channel during operation. We validate real-time feasibility by synchronizing glove signals with UAV telemetry in both simulation and real-world flights. The results show fast gesture-based command execution, stable coupling between gesture dynamics and platform motion, correct operation of the core command set in our trials, and timely delivery of vibratile warning cues.

