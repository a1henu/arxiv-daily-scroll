---
layout: default
title: SP-VINS: A Hybrid Stereo Visual Inertial Navigation System based on Implicit Environmental Map
---

# SP-VINS: A Hybrid Stereo Visual Inertial Navigation System based on Implicit Environmental Map
**arXiv**：[2511.18756v1](https://arxiv.org/abs/2511.18756) · [PDF](https://arxiv.org/pdf/2511.18756.pdf)  
**作者**：Xueyu Du, Lilian Zhang, Fuan Duan, Xincan Luo, Maosong Wang, Wenqi Wu, JunMao  

**一句话要点**：提出SP-VINS混合立体视觉惯性导航系统，基于隐式环境地图解决长期高精度定位问题

**关键词**：立体视觉惯性导航, 隐式环境地图, 混合残差滤波, 在线校准, 状态估计

## 3 点简述
- 核心问题：基于滤波的VINS在长期高精度状态估计中受限于地图质量不足
- 方法要点：结合地标重投影和射线约束的混合残差滤波框架，实现高效闭环
- 实验效果：在基准测试中，SP-VINS在计算效率和定位精度上优于现有SOTA方法

## 摘要（原文）

> Filter-based visual inertial navigation system (VINS) has attracted mobile-robot researchers for the good balance between accuracy and efficiency, but its limited mapping quality hampers long-term high-accuracy state estimation. To this end, we first propose a novel filter-based stereo VINS, differing from traditional simultaneous localization and mapping (SLAM) systems based on 3D map, which performs efficient loop closure constraints with implicit environmental map composed of keyframes and 2D keypoints. Secondly, we proposed a hybrid residual filter framework that combines landmark reprojection and ray constraints to construct a unified Jacobian matrix for measurement updates. Finally, considering the degraded environment, we incorporated the camera-IMU extrinsic parameters into visual description to achieve online calibration. Benchmark experiments demonstrate that the proposed SP-VINS achieves high computational efficiency while maintaining long-term high-accuracy localization performance, and is superior to existing state-of-the-art (SOTA) methods.

