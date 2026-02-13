---
layout: default
title: Decentralized Multi-Robot Obstacle Detection and Tracking in a Maritime Scenario
---

# Decentralized Multi-Robot Obstacle Detection and Tracking in a Maritime Scenario
**arXiv**：[2602.12012v1](https://arxiv.org/abs/2602.12012) · [PDF](https://arxiv.org/pdf/2602.12012.pdf)  
**作者**：Muhammad Farhan Ahmed, Vincent Frémont  

**一句话要点**：提出去中心化多机器人框架，用于海上场景中漂浮容器的检测与跟踪。

**关键词**：多机器人系统, 目标检测与跟踪, 去中心化协调, 海上监控, 不确定性融合

## 3 点简述
- 核心问题：在反射水面和有限通信下，实现多机器人可靠感知与可扩展协调。
- 方法要点：结合YOLOv8和立体视觉检测，使用不确定性感知数据关联与协方差交集融合轨迹。
- 实验或效果：仿真显示提升覆盖范围、定位精度和跟踪一致性，通信需求适中。

## 摘要（原文）

> Autonomous aerial-surface robot teams are promising for maritime monitoring. Robust deployment requires reliable perception over reflective water and scalable coordination under limited communication. We present a decentralized multi-robot framework for detecting and tracking floating containers using multiple UAVs cooperating with an autonomous surface vessel. Each UAV performs YOLOv8 and stereo-disparity-based visual detection, then tracks targets with per-object EKFs using uncertainty-aware data association. Compact track summaries are exchanged and fused conservatively via covariance intersection, ensuring consistency under unknown correlations. An information-driven assignment module allocates targets and selects UAV hover viewpoints by trading expected uncertainty reduction against travel effort and safety separation. Simulation results in a maritime scenario demonstrate improved coverage, localization accuracy, and tracking consistency while maintaining modest communication requirements.

