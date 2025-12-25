---
layout: default
title: Wireless Center of Pressure Feedback System for Humanoid Robot Balance Control using ESP32-C3
---

# Wireless Center of Pressure Feedback System for Humanoid Robot Balance Control using ESP32-C3
**arXiv**：[2512.21219v1](https://arxiv.org/abs/2512.21219) · [PDF](https://arxiv.org/pdf/2512.21219.pdf)  
**作者**：Muhtadin, Faris Rafi Pramana, Dion Hayu Fandiantoro, Moh Ismarintan Zazuli, Atar Fuady Babgei  

**一句话要点**：提出基于ESP32-C3的无线压力中心反馈系统，以增强人形机器人单腿支撑阶段的平衡控制。

**关键词**：人形机器人平衡控制, 无线压力中心反馈, ESP32-C3嵌入式系统, PID控制策略, 负载单元传感器, 单腿支撑稳定性

## 3 点简述
- 核心问题：人形机器人单腿支撑阶段稳定性差，传统有线传感器限制关节运动并引入机械噪声。
- 方法要点：设计集成四负载单元的足部模块，通过ESP32-C3实时估计压力中心，无线传输数据并采用PID控制调整躯干、髋部和踝关节。
- 实验或效果：传感器平均误差14.8克，在3度倾斜单腿提升任务中平衡成功率100%，验证了无线反馈对机械灵活性的提升。

## 摘要（原文）

> Maintaining stability during the single-support phase is a fundamental challenge in humanoid robotics, particularly in dance robots that require complex maneuvers and high mechanical freedom. Traditional tethered sensor configurations often restrict joint movement and introduce mechanical noises. This study proposes a wireless embedded balance system designed to maintain stability on uneven surfaces. The system utilizes a custom-designed foot unit integrated with four load cells and an ESP32-C3 microcontroller to estimate the Center of Pressure (CoP) in real time. The CoP data were transmitted wirelessly to the main controller to minimize the wiring complexity of the 29-DoF VI-ROSE humanoid robot. A PID control strategy is implemented to adjust the torso, hip, and ankle roll joints based on CoP feedback. Experimental characterization demonstrated high sensor precision with an average measurement error of 14.8 g. Furthermore, the proposed control system achieved a 100% success rate in maintaining balance during single-leg lifting tasks at a 3-degree inclination with optimized PID parameters (Kp=0.10, Kd=0.005). These results validate the efficacy of wireless CoP feedback in enhancing the postural stability of humanoid robots, without compromising their mechanical flexibility.

