---
layout: default
title: FoMo: A Multi-Season Dataset for Robot Navigation in Forêt Montmorency
---

# FoMo: A Multi-Season Dataset for Robot Navigation in Forêt Montmorency
**arXiv**：[2603.08433v1](https://arxiv.org/abs/2603.08433) · [PDF](https://arxiv.org/pdf/2603.08433.pdf)  
**作者**：Matěj Boxan, Gabriel Jeanson, Alexander Krawciw, Effie Daum, Xinyuan Qiao, Sven Lilge, Timothy D. Barfoot, François Pomerleau  

**一句话要点**：提出FoMo多季节数据集以挑战机器人导航在北方森林中的环境变化问题

**关键词**：多季节数据集, 机器人导航, 传感器融合, 环境变化, 定位与建图, 北方森林

## 3 点简述
- 核心问题：多季节环境变化（如积雪、植被生长）对机器人定位与建图技术构成挑战
- 方法要点：收集一年内12次部署的64公里轨迹数据，包含激光雷达、雷达、相机和IMU等多种传感器
- 实验或效果：初步评估显示季节变化严重影响先进方法的重新定位能力

## 摘要（原文）

> The Forêt Montmorency (FoMo) dataset is a comprehensive multi-season data collection, recorded over the span of one year in a boreal forest. Featuring a unique combination of on- and off-pavement environments with significant environmental changes, the dataset challenges established odometry and SLAM pipelines. Some highlights of the data include the accumulation of snow exceeding 1 m, significant vegetation growth in front of sensors, and operations at the traction limits of the platform. In total, the FoMo dataset includes over 64 km of six diverse trajectories, repeated during 12 deployments throughout the year. The dataset features data from one rotating and one hybrid solid-state lidar, a Frequency Modulated Continuous Wave (FMCW) radar, full-HD images from a stereo camera and a wide lens monocular camera, as well as data from two IMUs. Ground Truth is calculated by post-processing three GNSS receivers mounted on the Uncrewed Ground Vehicle (UGV) and a static GNSS base station. Additional metadata, such as one measurement per minute from an on-site weather station, camera calibration intrinsics, and vehicle power consumption, is available for all sequences. To highlight the relevance of the dataset, we performed a preliminary evaluation of the robustness of a lidar-inertial, radar-gyro, and a visual-inertial localization and mapping techniques to seasonal changes. We show that seasonal changes have serious effects on the re-localization capabilities of the state-of-the-art methods. The dataset and development kit are available at https://fomo.norlab.ulaval.ca.

