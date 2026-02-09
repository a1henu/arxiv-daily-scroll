---
layout: default
title: TFusionOcc: Student's t-Distribution Based Object-Centric Multi-Sensor Fusion Framework for 3D Occupancy Prediction
---

# TFusionOcc: Student's t-Distribution Based Object-Centric Multi-Sensor Fusion Framework for 3D Occupancy Prediction
**arXiv**：[2602.06400v1](https://arxiv.org/abs/2602.06400) · [PDF](https://arxiv.org/pdf/2602.06400.pdf)  
**作者**：Zhenxing Ming, Julie Stephany Berrio, Mao Shan, Stewart Worrall  

**一句话要点**：提出TFusionOcc，基于学生t分布的对象中心多传感器融合框架，用于3D占用预测。

**关键词**：3D语义占用预测, 多传感器融合, 学生t分布, 对象中心表示, 自动驾驶感知, 几何建模

## 3 点简述
- 核心问题：现有3D语义占用预测方法依赖3D体素或高斯分布，难以高效捕捉精细几何细节。
- 方法要点：采用对象中心多传感器融合、学生t分布和T混合模型，结合可变形超二次曲面等几何基元。
- 实验或效果：在nuScenes基准上实现SOTA性能，并在nuScenes-C数据集上验证了鲁棒性。

## 摘要（原文）

> 3D semantic occupancy prediction enables autonomous vehicles (AVs) to perceive fine-grained geometric and semantic structure of their surroundings from onboard sensors, which is essential for safe decision-making and navigation. Recent models for 3D semantic occupancy prediction have successfully addressed the challenge of describing real-world objects with varied shapes and classes. However, the intermediate representations used by existing methods for 3D semantic occupancy prediction rely heavily on 3D voxel volumes or a set of 3D Gaussians, hindering the model's ability to efficiently and effectively capture fine-grained geometric details in the 3D driving environment. This paper introduces TFusionOcc, a novel object-centric multi-sensor fusion framework for predicting 3D semantic occupancy. By leveraging multi-stage multi-sensor fusion, Student's t-distribution, and the T-Mixture model (TMM), together with more geometrically flexible primitives, such as the deformable superquadric (superquadric with inverse warp), the proposed method achieved state-of-the-art (SOTA) performance on the nuScenes benchmark. In addition, extensive experiments were conducted on the nuScenes-C dataset to demonstrate the robustness of the proposed method in different camera and lidar corruption scenarios. The code will be available at: https://github.com/DanielMing123/TFusionOcc

