---
layout: default
title: Acceleration-Based Control of Fixed-Wing UAVs for Guidance Applications
---

# Acceleration-Based Control of Fixed-Wing UAVs for Guidance Applications
**arXiv**：[2602.23821v1](https://arxiv.org/abs/2602.23821) · [PDF](https://arxiv.org/pdf/2602.23821.pdf)  
**作者**：Jixiang Wang, Siyuan Yang, Ziyi Wu, Siqi Wei, Ashay Wakode, Agata Barcis, Hung Nguyen, Shaoming He  

**一句话要点**：提出固定翼无人机加速度级外环控制框架，实现比例导引等加速度指令的实用部署。

**关键词**：固定翼无人机控制, 加速度指令, 外环控制, 比例导引, 能量法, 实飞验证

## 3 点简述
- 核心问题：固定翼无人机无法直接执行加速度指令，需在飞行包线约束下通过姿态和推力间接实现。
- 方法要点：推导法向加速度到滚转/俯仰速率的工程映射，基于能量法建立切向加速度与推力关系，避免复杂建模。
- 实验或效果：在VTOL固定翼平台上进行大量实飞实验，验证了加速度跟踪精度和比例导引的可行性。

## 摘要（原文）

> Acceleration-commanded guidance laws (e.g., proportional navigation) are attractive for high-level decision making, but their direct deployment on fixed-wing UAVs is challenging because accelerations are not directly actuated and must be realized through attitude and thrust under flight-envelope constraints. This paper presents an acceleration-level outer-loop control framework that converts commanded tangential and normal accelerations into executable body-rate and normalized thrust commands compatible with mainstream autopilots (e.g., PX4/APM). For the normal channel, we derive an engineering mapping from the desired normal acceleration to roll- and pitch-rate commands that regulate the direction and magnitude of the lift vector under small-angle assumptions. For the tangential channel, we introduce an energy-based formulation inspired by total energy control and identify an empirical thrust-energy acceleration relationship directly from flight data, avoiding explicit propulsion modeling or thrust bench calibration. We further discuss priority handling between normal and tangential accelerations under saturation and non-level maneuvers. Extensive real-flight experiments on a VTOL fixed-wing platform demonstrate accurate acceleration tracking and enable practical implementation of proportional navigation using only body-rate and normalized thrust interfaces.

