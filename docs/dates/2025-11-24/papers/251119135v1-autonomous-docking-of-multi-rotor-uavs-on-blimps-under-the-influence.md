---
layout: default
title: Autonomous Docking of Multi-Rotor UAVs on Blimps under the Influence of Wind Gusts
---

# Autonomous Docking of Multi-Rotor UAVs on Blimps under the Influence of Wind Gusts
**arXiv**：[2511.19135v1](https://arxiv.org/abs/2511.19135) · [PDF](https://arxiv.org/pdf/2511.19135.pdf)  
**作者**：Pascal Goldschmid, Aamir Ahmad  

**一句话要点**：提出基于TCN和MPC的自主对接方法，解决多旋翼无人机在风扰下对接飞艇问题。

**关键词**：自主对接, 多旋翼无人机, 飞艇, 风扰预测, 模型预测控制, 障碍物避免

## 3 点简述
- 核心问题：风扰导致飞艇轨迹偏移，影响无人机自主对接的精确性和安全性。
- 方法要点：使用TCN预测飞艇对风扰的响应，MPC结合预测计算无碰撞对接轨迹。
- 实验或效果：仿真和真实实验验证方法优于基线，首次实现仿真外自主对接。

## 摘要（原文）

> Multi-rotor UAVs face limited flight time due to battery constraints. Autonomous docking on blimps with onboard battery recharging and data offloading offers a promising solution for extended UAV missions. However, the vulnerability of blimps to wind gusts causes trajectory deviations, requiring precise, obstacle-aware docking strategies. To this end, this work introduces two key novelties: (i) a temporal convolutional network that predicts blimp responses to wind gusts, enabling rapid gust detection and estimation of points where the wind gust effect has subsided; (ii) a model predictive controller (MPC) that leverages these predictions to compute collision-free trajectories for docking, enabled by a novel obstacle avoidance method for close-range manoeuvres near the blimp. Simulation results show our method outperforms a baseline constant-velocity model of the blimp significantly across different scenarios. We further validate the approach in real-world experiments, demonstrating the first autonomous multi-rotor docking control strategy on blimps shown outside simulation. Source code is available here https://github.com/robot-perception-group/multi_rotor_airship_docking.

