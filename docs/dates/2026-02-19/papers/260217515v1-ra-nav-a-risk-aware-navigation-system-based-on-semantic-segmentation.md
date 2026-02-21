---
layout: default
title: RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments
---

# RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments
**arXiv**：[2602.17515v1](https://arxiv.org/abs/2602.17515) · [PDF](https://arxiv.org/pdf/2602.17515.pdf)  
**作者**：Ziyi Zong, Xin Dong, Jinwu Xiang, Daochun Li, Zhan Tu  

**一句话要点**：提出基于语义分割的风险感知导航框架RA-Nav，以应对空中机器人在不可预测环境中静态障碍物突然移动的问题。

**关键词**：风险感知导航, 语义分割, 空中机器人, 局部风险图, 路径规划

## 3 点简述
- 现有导航系统难以适应静态障碍物突然移动，导致安全风险。
- 通过轻量级语义分割网络实时识别障碍物类型，并设计风险估计函数构建局部风险图。
- 在模拟中验证了RA-Nav在障碍物状态突变场景下比基线方法具有更高成功率。

## 摘要（原文）

> Existing aerial robot navigation systems typically plan paths around static and dynamic obstacles, but fail to adapt when a static obstacle suddenly moves. Integrating environmental semantic awareness enables estimation of potential risks posed by suddenly moving obstacles. In this paper, we propose RA- Nav, a risk-aware navigation framework based on semantic segmentation. A lightweight multi-scale semantic segmentation network identifies obstacle categories in real time. These obstacles are further classified into three types: stationary, temporarily static, and dynamic. For each type, corresponding risk estimation functions are designed to enable real-time risk prediction, based on which a complete local risk map is constructed. Based on this map, the risk-informed path search algorithm is designed to guarantee planning that balances path efficiency and safety. Trajectory optimization is then applied to generate trajectories that are safe, smooth, and dynamically feasible. Comparative simulations demonstrate that RA-Nav achieves higher success rates than baselines in sudden obstacle state transition scenarios. Its effectiveness is further validated in simulations using real- world data.

