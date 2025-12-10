---
layout: default
title: Zero-Splat TeleAssist: A Zero-Shot Pose Estimation Framework for Semantic Teleoperation
---

# Zero-Splat TeleAssist: A Zero-Shot Pose Estimation Framework for Semantic Teleoperation
**arXiv**：[2512.08271v1](https://arxiv.org/abs/2512.08271) · [PDF](https://arxiv.org/pdf/2512.08271.pdf)  
**作者**：Srijan Dokania, Dharini Raghavan  

**一句话要点**：提出Zero-Splat TeleAssist框架，通过零样本传感器融合实现基于CCTV流的语义远程操作姿态估计。

**关键词**：零样本姿态估计, 传感器融合, 远程操作, 3D高斯泼溅, 视觉语言分割, 单目深度估计

## 3 点简述
- 核心问题：在无标记或深度传感器的交互式远程操作中，实时估计多机器人的全局6自由度姿态。
- 方法要点：集成视觉语言分割、单目深度、加权PCA姿态提取和3D高斯泼溅，构建共享世界模型。
- 实验或效果：提供实时姿态信息，支持多边远程操作，无需额外传感器或标记。

## 摘要（原文）

> We introduce Zero-Splat TeleAssist, a zero-shot sensor-fusion pipeline that transforms commodity CCTV streams into a shared, 6-DoF world model for multilateral teleoperation. By integrating vision-language segmentation, monocular depth, weighted-PCA pose extraction, and 3D Gaussian Splatting (3DGS), TeleAssist provides every operator with real-time global positions and orientations of multiple robots without fiducials or depth sensors in an interaction-centric teleoperation setup.

