---
layout: default
title: FlowCalib: LiDAR-to-Vehicle Miscalibration Detection using Scene Flows
---

# FlowCalib: LiDAR-to-Vehicle Miscalibration Detection using Scene Flows
**arXiv**：[2601.23107v1](https://arxiv.org/abs/2601.23107) · [PDF](https://arxiv.org/pdf/2601.23107.pdf)  
**作者**：Ilir Tahiraj, Peter Wittal, Markus Lienkamp  

**一句话要点**：提出FlowCalib框架，利用静态物体场景流检测LiDAR与车辆间的标定误差。

**关键词**：LiDAR标定, 场景流, 自动驾驶安全, 神经网络检测, 点云处理

## 3 点简述
- 核心问题：LiDAR传感器角度标定误差可能导致自动驾驶安全问题，现有方法多关注传感器间校正而非源头误差。
- 方法要点：基于序列点云生成场景流，通过旋转误差引起的系统性偏差，结合神经网络与手工特征进行双分支分类检测。
- 实验或效果：在nuScenes数据集上验证了鲁棒性，为传感器-车辆标定误差检测建立了基准。

## 摘要（原文）

> Accurate sensor-to-vehicle calibration is essential for safe autonomous driving. Angular misalignments of LiDAR sensors can lead to safety-critical issues during autonomous operation. However, current methods primarily focus on correcting sensor-to-sensor errors without considering the miscalibration of individual sensors that cause these errors in the first place. We introduce FlowCalib, the first framework that detects LiDAR-to-vehicle miscalibration using motion cues from the scene flow of static objects. Our approach leverages the systematic bias induced by rotational misalignment in the flow field generated from sequential 3D point clouds, eliminating the need for additional sensors. The architecture integrates a neural scene flow prior for flow estimation and incorporates a dual-branch detection network that fuses learned global flow features with handcrafted geometric descriptors. These combined representations allow the system to perform two complementary binary classification tasks: a global binary decision indicating whether misalignment is present and separate, axis-specific binary decisions indicating whether each rotational axis is misaligned. Experiments on the nuScenes dataset demonstrate FlowCalib's ability to robustly detect miscalibration, establishing a benchmark for sensor-to-vehicle miscalibration detection.

