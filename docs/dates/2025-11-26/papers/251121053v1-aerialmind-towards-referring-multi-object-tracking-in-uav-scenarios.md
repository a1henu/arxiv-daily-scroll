---
layout: default
title: AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios
---

# AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios
**arXiv**：[2511.21053v1](https://arxiv.org/abs/2511.21053) · [PDF](https://arxiv.org/pdf/2511.21053.pdf)  
**作者**：Chenglizhao Chen, Shaofeng Liang, Runwei Guan, Xiaolou Sun, Haocheng Zhao, Haiyun Jiang, Tao Huang, Henghui Ding, Qing-Long Han  

**一句话要点**：提出AerialMind基准和HawkEyeTrack方法以解决无人机场景中的指称多目标跟踪问题

**关键词**：指称多目标跟踪, 无人机场景, 视觉-语言学习, 半自动标注, 基准数据集

## 3 点简述
- 核心问题：现有指称多目标跟踪研究局限于地面场景，无法利用无人机广视角进行大范围跟踪
- 方法要点：开发COALA半自动标注框架降低标注成本，提出HETrack方法增强视觉-语言表示学习
- 实验或效果：验证数据集挑战性及方法有效性，提升无人机场景感知能力

## 摘要（原文）

> Referring Multi-Object Tracking (RMOT) aims to achieve precise object detection and tracking through natural language instructions, representing a fundamental capability for intelligent robotic systems. However, current RMOT research remains mostly confined to ground-level scenarios, which constrains their ability to capture broad-scale scene contexts and perform comprehensive tracking and path planning. In contrast, Unmanned Aerial Vehicles (UAVs) leverage their expansive aerial perspectives and superior maneuverability to enable wide-area surveillance. Moreover, UAVs have emerged as critical platforms for Embodied Intelligence, which has given rise to an unprecedented demand for intelligent aerial systems capable of natural language interaction. To this end, we introduce AerialMind, the first large-scale RMOT benchmark in UAV scenarios, which aims to bridge this research gap. To facilitate its construction, we develop an innovative semi-automated collaborative agent-based labeling assistant (COALA) framework that significantly reduces labor costs while maintaining annotation quality. Furthermore, we propose HawkEyeTrack (HETrack), a novel method that collaboratively enhances vision-language representation learning and improves the perception of UAV scenarios. Comprehensive experiments validated the challenging nature of our dataset and the effectiveness of our method.

