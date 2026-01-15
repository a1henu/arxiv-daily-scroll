---
layout: default
title: Multimodal Signal Processing For Thermo-Visible-Lidar Fusion In Real-time 3D Semantic Mapping
---

# Multimodal Signal Processing For Thermo-Visible-Lidar Fusion In Real-time 3D Semantic Mapping
**arXiv**：[2601.09578v1](https://arxiv.org/abs/2601.09578) · [PDF](https://arxiv.org/pdf/2601.09578.pdf)  
**作者**：Jiajun Sun, Yangyi Ou, Haoyuan Zheng, Chao yang, Yue Ma  

**一句话要点**：提出基于热-可见光-LiDAR融合的实时3D语义建图方法，用于增强环境感知能力。

**关键词**：多模态信号处理, 3D语义建图, 热-可见光-LiDAR融合, 实时SLAM, 热源分割, 环境感知

## 3 点简述
- 核心问题：复杂环境中自主机器人导航对环境感知提出更高要求，需提升SLAM技术的语义理解能力。
- 方法要点：通过像素级融合可见光与红外图像，将LiDAR点云投影到融合图像流，分割热源特征以识别高温目标。
- 实验或效果：生成具有精确几何和温度语义层的3D地图，适用于快速灾害评估和工业预防性维护等应用。

## 摘要（原文）

> In complex environments, autonomous robot navigation and environmental perception pose higher requirements for SLAM technology. This paper presents a novel method for semantically enhancing 3D point cloud maps with thermal information. By first performing pixel-level fusion of visible and infrared images, the system projects real-time LiDAR point clouds onto this fused image stream. It then segments heat source features in the thermal channel to instantly identify high temperature targets and applies this temperature information as a semantic layer on the final 3D map. This approach generates maps that not only have accurate geometry but also possess a critical semantic understanding of the environment, making it highly valuable for specific applications like rapid disaster assessment and industrial preventive maintenance.

