---
layout: default
title: Towards Terrain-Aware Safe Locomotion for Quadrupedal Robots Using Proprioceptive Sensing
---

# Towards Terrain-Aware Safe Locomotion for Quadrupedal Robots Using Proprioceptive Sensing
**arXiv**：[2603.09585v1](https://arxiv.org/abs/2603.09585) · [PDF](https://arxiv.org/pdf/2603.09585.pdf)  
**作者**：Peiyu Yang, Jiatao Ding, Wei Pan, Claudio Semini, Cosimo Della Santina  

**一句话要点**：提出基于本体感知的地形估计与安全控制框架，以提升四足机器人在不平坦地形中的安全运动能力。

**关键词**：四足机器人, 地形估计, 本体感知, 安全控制, 控制障碍函数, 状态估计

## 3 点简述
- 核心问题：四足机器人在不平坦地形中，仅依赖本体感知传感器（如IMU、关节编码器）实现可靠估计与安全控制仍具挑战。
- 方法要点：开发地形估计框架生成2.5维地图，提取支撑面参数，并集成到接触与状态估计中，结合控制障碍函数确保安全。
- 实验效果：地形估计平滑，耦合框架相比解耦框架，基座位置估计平均绝对误差降低64.8%，方差减少47.2%，接触估计鲁棒性提升。

## 摘要（原文）

> Achieving safe quadrupedal locomotion in real-world environments has attracted much attention in recent years. When walking over uneven terrain, achieving reliable estimation and realising safety-critical control based on the obtained information is still an open question. To address this challenge, especially for low-cost robots equipped solely with proprioceptive sensors (e.g., IMUs, joint encoders, and contact force sensors), this work first presents an estimation framework that generates a 2.5-D terrain map and extracts support plane parameters, which are then integrated into contact and state estimation. Then, we integrate this estimation framework into a safety-critical control pipeline by formulating control barrier functions that provide rigorous safety guarantees. Experiments demonstrate that the proposed terrain estimation method provides smooth terrain representations. Moreover, the coupled estimation framework of terrain, state, and contact reduces the mean absolute error of base position estimation by 64.8%, decreases the estimation variance by 47.2%, and improves the robustness of contact estimation compared to a decoupled framework. The terrain-informed CBFs integrate historical terrain information and current proprioceptive measurements to ensure global safety by keeping the robot out of hazardous areas and local safety by preventing body-terrain collision, relying solely on proprioceptive sensing.

