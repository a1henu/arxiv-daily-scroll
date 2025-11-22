---
layout: default
title: Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments
---

# Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments
**arXiv**：[2511.16091v1](https://arxiv.org/abs/2511.16091) · [PDF](https://arxiv.org/pdf/2511.16091.pdf)  
**作者**：Renxiang Xiao, Wei Liu, Yuanfan Zhang, Yushuai Chen, Jinming Chen, Zilu Wang, Liang Hu  

**一句话要点**：提出Rad-GS雷达-视觉SLAM系统，用于大规模户外环境3D重建。

**关键词**：雷达-视觉融合, 3D高斯溅射, SLAM系统, 动态物体掩码, 大规模重建

## 3 点简述
- 核心问题：户外大规模环境中动态物体导致渲染伪影和定位精度下降。
- 方法要点：结合雷达点云和多普勒信息，引导动态物体掩码，优化3D高斯表示。
- 实验或效果：在千米级真实环境中验证，性能媲美相机或LiDAR方法。

## 摘要（原文）

> We present Rad-GS, a 4D radar-camera SLAM system designed for kilometer-scale outdoor environments, utilizing 3D Gaussian as a differentiable spatial representation. Rad-GS combines the advantages of raw radar point cloud with Doppler information and geometrically enhanced point cloud to guide dynamic object masking in synchronized images, thereby alleviating rendering artifacts and improving localization accuracy. Additionally, unsynchronized image frames are leveraged to globally refine the 3D Gaussian representation, enhancing texture consistency and novel view synthesis fidelity. Furthermore, the global octree structure coupled with a targeted Gaussian primitive management strategy further suppresses noise and significantly reduces memory consumption in large-scale environments. Extensive experiments and ablation studies demonstrate that Rad-GS achieves performance comparable to traditional 3D Gaussian methods based on camera or LiDAR inputs, highlighting the feasibility of robust outdoor mapping using 4D mmWave radar. Real-world reconstruction at kilometer scale validates the potential of Rad-GS for large-scale scene reconstruction.

