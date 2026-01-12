---
layout: default
title: FlyPose: Towards Robust Human Pose Estimation From Aerial Views
---

# FlyPose: Towards Robust Human Pose Estimation From Aerial Views
**arXiv**：[2601.05747v1](https://arxiv.org/abs/2601.05747) · [PDF](https://arxiv.org/pdf/2601.05747.pdf)  
**作者**：Hassaan Farooq, Marvin Brenner, Peter St\ütz  

**一句话要点**：提出FlyPose轻量级自上而下姿态估计方法，以解决无人机视角下人体姿态估计的挑战。

**关键词**：无人机视角姿态估计, 轻量化模型, 多数据集训练, 实时部署, 自上而下方法

## 3 点简述
- 核心问题：无人机视角下人体姿态估计面临低分辨率、陡视角和遮挡等挑战，需实时可行模型。
- 方法要点：采用多数据集训练，提升检测和姿态估计性能，实现轻量化部署。
- 实验或效果：在多个数据集上平均提升6.8 mAP检测精度，UAV-Human数据集姿态估计提升16.3 mAP，推理延迟约20毫秒。

## 摘要（原文）

> Unmanned Aerial Vehicles (UAVs) are increasingly deployed in close proximity to humans for applications such as parcel delivery, traffic monitoring, disaster response and infrastructure inspections. Ensuring safe and reliable operation in these human-populated environments demands accurate perception of human poses and actions from an aerial viewpoint. This perspective challenges existing methods with low resolution, steep viewing angles and (self-)occlusion, especially if the application demands realtime feasibile models. We train and deploy FlyPose, a lightweight top-down human pose estimation pipeline for aerial imagery. Through multi-dataset training, we achieve an average improvement of 6.8 mAP in person detection across the test-sets of Manipal-UAV, VisDrone, HIT-UAV as well as our custom dataset. For 2D human pose estimation we report an improvement of 16.3 mAP on the challenging UAV-Human dataset. FlyPose runs with an inference latency of ~20 milliseconds including preprocessing on a Jetson Orin AGX Developer Kit and is deployed onboard a quadrotor UAV during flight experiments. We also publish FlyPose-104, a small but challenging aerial human pose estimation dataset, that includes manual annotations from difficult aerial perspectives: https://github.com/farooqhassaan/FlyPose.

