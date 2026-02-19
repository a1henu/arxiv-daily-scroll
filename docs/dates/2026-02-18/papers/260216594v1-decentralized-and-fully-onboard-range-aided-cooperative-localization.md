---
layout: default
title: Decentralized and Fully Onboard: Range-Aided Cooperative Localization and Navigation on Micro Aerial Vehicles
---

# Decentralized and Fully Onboard: Range-Aided Cooperative Localization and Navigation on Micro Aerial Vehicles
**arXiv**：[2602.16594v1](https://arxiv.org/abs/2602.16594) · [PDF](https://arxiv.org/pdf/2602.16594.pdf)  
**作者**：Abhishek Goudar, Angela P. Schoellig  

**一句话要点**：提出基于块坐标下降和因子图的去中心化范围辅助定位与编队控制方法，用于微型飞行器协同导航。

**关键词**：去中心化定位, 编队控制, 范围辅助导航, 因子图推理, 微型飞行器, 协同机器人

## 3 点简述
- 核心问题：去中心化协同定位与编队控制，避免集中式计算和外部定位依赖，仅利用机载里程计和机器人间距离测量。
- 方法要点：采用块坐标下降进行定位，无需严格协调；将编队控制建模为因子图推理，考虑状态估计不确定性，高效求解。
- 实验或效果：在多样室内外环境中进行编队飞行实验，实现分米级定位和编队控制精度，无需专用轨迹维持编队。

## 摘要（原文）

> Controlling a team of robots in a coordinated manner is challenging because centralized approaches (where all computation is performed on a central machine) scale poorly, and globally referenced external localization systems may not always be available. In this work, we consider the problem of range-aided decentralized localization and formation control. In such a setting, each robot estimates its relative pose by combining data only from onboard odometry sensors and distance measurements to other robots in the team. Additionally, each robot calculates the control inputs necessary to collaboratively navigate an environment to accomplish a specific task, for example, moving in a desired formation while monitoring an area. We present a block coordinate descent approach to localization that does not require strict coordination between the robots. We present a novel formulation for formation control as inference on factor graphs that takes into account the state estimation uncertainty and can be solved efficiently. Our approach to range-aided localization and formation-based navigation is completely decentralized, does not require specialized trajectories to maintain formation, and achieves decimeter-level positioning and formation control accuracy. We demonstrate our approach through multiple real experiments involving formation flights in diverse indoor and outdoor environments.

