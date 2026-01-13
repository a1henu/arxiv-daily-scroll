---
layout: default
title: LOONG: Online Time-Optimal Autonomous Flight for MAVs in Cluttered Environments
---

# LOONG: Online Time-Optimal Autonomous Flight for MAVs in Cluttered Environments
**arXiv**：[2601.07434v1](https://arxiv.org/abs/2601.07434) · [PDF](https://arxiv.org/pdf/2601.07434.pdf)  
**作者**：Xin Guan, Fangguo Zhao, Qianyi Wang, Chengcheng Zhao, Jiming Chen, Shuo Li  

**一句话要点**：提出LOONG框架，实现MAV在未知杂乱环境中的在线时间最优自主飞行。

**关键词**：自主飞行, 时间最优控制, 模型预测轮廓控制, 安全飞行走廊, 模仿学习, MAV平台

## 3 点简述
- 核心问题：MAV在未知杂乱环境中因保守策略难以满足时间关键任务的高速飞行需求。
- 方法要点：集成规划与控制，通过模仿学习加速时间分配，并采用时间最优MPCC结合SFC约束实现激进安全机动。
- 实验或效果：在仿真中展现优越攻击性，真实实验中峰值速度达18 m/s，10次连续试验成功。

## 摘要（原文）

> Autonomous flight of micro air vehicles (MAVs) in unknown, cluttered environments remains challenging for time-critical missions due to conservative maneuvering strategies. This article presents an integrated planning and control framework for high-speed, time-optimal autonomous flight of MAVs in cluttered environments. In each replanning cycle (100 Hz), a time-optimal trajectory under polynomial presentation is generated as a reference, with the time-allocation process accelerated by imitation learning. Subsequently, a time-optimal model predictive contouring control (MPCC) incorporates safe flight corridor (SFC) constraints at variable horizon steps to enable aggressive yet safe maneuvering, while fully exploiting the MAV's dynamics. We validate the proposed framework extensively on a custom-built LiDAR-based MAV platform. Simulation results demonstrate superior aggressiveness compared to the state of the art, while real-world experiments achieve a peak speed of 18 m/s in a cluttered environment and succeed in 10 consecutive trials from diverse start points. The video is available at the following link: https://youtu.be/vexXXhv99oQ.

