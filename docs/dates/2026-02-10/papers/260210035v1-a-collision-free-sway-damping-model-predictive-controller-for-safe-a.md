---
layout: default
title: A Collision-Free Sway Damping Model Predictive Controller for Safe and Reactive Forestry Crane Navigation
---

# A Collision-Free Sway Damping Model Predictive Controller for Safe and Reactive Forestry Crane Navigation
**arXiv**：[2602.10035v1](https://arxiv.org/abs/2602.10035) · [PDF](https://arxiv.org/pdf/2602.10035.pdf)  
**作者**：Marc-Philip Ecker, Christoph Fröhlich, Johannes Huemer, David Gruber, Bernhard Bischof, Tobias Glück, Wolfgang Kemmetmüller  

**一句话要点**：提出碰撞无扰摆抑制模型预测控制器，以解决林业起重机在动态环境中同时避障和载荷摆动的安全导航问题。

**关键词**：林业起重机控制, 模型预测控制, 碰撞避免, 载荷摆动抑制, 在线环境映射, 欧几里得距离场

## 3 点简述
- 核心问题：林业起重机在动态非结构化环境中需同时实现碰撞避免和载荷摆动控制，现有方法常分离处理。
- 方法要点：集成基于LiDAR的环境映射到MPC，使用在线欧几里得距离场，统一避障和摆抑制目标。
- 实验或效果：在真实林业起重机上验证，有效抑制摆动并成功避障，支持实时环境适应和安全停止。

## 摘要（原文）

> Forestry cranes operate in dynamic, unstructured outdoor environments where simultaneous collision avoidance and payload sway control are critical for safe navigation. Existing approaches address these challenges separately, either focusing on sway damping with predefined collision-free paths or performing collision avoidance only at the global planning level. We present the first collision-free, sway-damping model predictive controller (MPC) for a forestry crane that unifies both objectives in a single control framework. Our approach integrates LiDAR-based environment mapping directly into the MPC using online Euclidean distance fields (EDF), enabling real-time environmental adaptation. The controller simultaneously enforces collision constraints while damping payload sway, allowing it to (i) replan upon quasi-static environmental changes, (ii) maintain collision-free operation under disturbances, and (iii) provide safe stopping when no bypass exists. Experimental validation on a real forestry crane demonstrates effective sway damping and successful obstacle avoidance. A video can be found at https://youtu.be/tEXDoeLLTxA.

