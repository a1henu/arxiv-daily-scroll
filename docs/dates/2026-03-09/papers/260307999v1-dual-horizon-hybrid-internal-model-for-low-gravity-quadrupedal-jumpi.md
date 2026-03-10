---
layout: default
title: Dual-Horizon Hybrid Internal Model for Low-Gravity Quadrupedal Jumping with Hardware-in-the-Loop Validation
---

# Dual-Horizon Hybrid Internal Model for Low-Gravity Quadrupedal Jumping with Hardware-in-the-Loop Validation
**arXiv**：[2603.07999v1](https://arxiv.org/abs/2603.07999) · [PDF](https://arxiv.org/pdf/2603.07999.pdf)  
**作者**：Haozhe Xu, Yifei Zhao, Wenhao Feng, Zhipeng Wang, Hongrui Sang, Cheng Cheng, Xiuxian Li, Zhen Yin, Bin He  

**一句话要点**：提出双时域混合内部模型，用于仅凭本体感知实现月球重力下四足机器人连续跳跃。

**关键词**：四足机器人跳跃, 低重力环境, 混合内部模型, 硬件在环验证, 连续地形运动

## 3 点简述
- 问题：月球重力下连续跳跃因长飞行阶段和稀疏地面接触而困难，现有方法缺乏连续地形解决方案和硬件验证。
- 方法：设计双时域编码器，短时域分支建模快速垂直动力学，长时域分支建模水平运动趋势和质心高度演化。
- 实验：开发MATRIX混合现实平台进行硬件在环验证，在模拟月球地形上展示连续跳跃性能。

## 摘要（原文）

> Locomotion under reduced gravity is commonly realized through jumping, yet continuous pronking in lunar gravity remains challenging due to prolonged flight phases and sparse ground contact. The extended aerial duration increases landing impact sensitivity and makes stable attitude regulation over rough planetary terrain difficult. Existing approaches primarily address single jumps on flat surfaces and lack both continuous-terrain solutions and realistic hardware validation. This work presents a Dual-Horizon Hybrid Internal Model for continuous quadrupedal jumping under lunar gravity using proprioceptive sensing only. Two temporal encoders capture complementary time scales: a short-horizon branch models rapid vertical dynamics with explicit vertical velocity estimation, while a long-horizon branch models horizontal motion trends and center-of-mass height evolution across the jump cycle. The fused representation enables stable and continuous jumping under extended aerial phases characteristic of lunar gravity. To provide hardware-in-the-loop validation, we develop the MATRIX (Mixed-reality Adaptive Testbed for Robotic Integrated eXploration) platform, a digital-twin-driven system that offloads gravity through a pulley-counterweight mechanism and maps Unreal Engine lunar terrain to a motion platform and treadmill in real time. Using MATRIX, we demonstrate continuous jumping of a quadruped robot under lunar-gravity emulation across cratered lunar-like terrain.

