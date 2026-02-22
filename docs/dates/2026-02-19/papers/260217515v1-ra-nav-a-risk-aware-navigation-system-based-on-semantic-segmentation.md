---
layout: default
title: RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments
---

# RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments
**arXiv**：[2602.17515v1](https://arxiv.org/abs/2602.17515) · [PDF](https://arxiv.org/pdf/2602.17515.pdf)  
**作者**：Ziyi Zong, Xin Dong, Jinwu Xiang, Daochun Li, Zhan Tu  

**一句话要点**：提出RA-Nav风险感知导航框架，基于语义分割解决空中机器人在静态障碍物突然移动环境中的适应问题。

**关键词**：空中机器人导航, 语义分割, 风险感知, 路径规划, 动态障碍物, 实时系统

## 3 点简述
- 核心问题：现有导航系统无法适应静态障碍物突然移动，导致安全风险。
- 方法要点：使用轻量级多尺度语义分割网络实时识别障碍物类别，并分类为静止、暂时静态和动态类型，设计风险估计函数构建局部风险地图。
- 实验或效果：在模拟中，RA-Nav在障碍物状态突变场景下比基线方法具有更高成功率，并通过真实世界数据验证有效性。

## 摘要（原文）

> Existing aerial robot navigation systems typically plan paths around static and dynamic obstacles, but fail to adapt when a static obstacle suddenly moves. Integrating environmental semantic awareness enables estimation of potential risks posed by suddenly moving obstacles. In this paper, we propose RA- Nav, a risk-aware navigation framework based on semantic segmentation. A lightweight multi-scale semantic segmentation network identifies obstacle categories in real time. These obstacles are further classified into three types: stationary, temporarily static, and dynamic. For each type, corresponding risk estimation functions are designed to enable real-time risk prediction, based on which a complete local risk map is constructed. Based on this map, the risk-informed path search algorithm is designed to guarantee planning that balances path efficiency and safety. Trajectory optimization is then applied to generate trajectories that are safe, smooth, and dynamically feasible. Comparative simulations demonstrate that RA-Nav achieves higher success rates than baselines in sudden obstacle state transition scenarios. Its effectiveness is further validated in simulations using real- world data.

