---
layout: default
title: Dynamic-ICP: Doppler-Aware Iterative Closest Point Registration for Dynamic Scenes
---

# Dynamic-ICP: Doppler-Aware Iterative Closest Point Registration for Dynamic Scenes
**arXiv**：[2511.20292v1](https://arxiv.org/abs/2511.20292) · [PDF](https://arxiv.org/pdf/2511.20292.pdf)  
**作者**：Dong Wang, Daniel Casado Herraez, Stefan May, Andreas Nüchter  

**一句话要点**：提出Dynamic-ICP以解决动态场景中ICP注册退化问题

**关键词**：动态场景注册, 多普勒感知ICP, LiDAR里程计, 实时算法, 运动估计

## 3 点简述
- 核心问题：ICP在动态、重复或低纹理场景中性能下降
- 方法要点：利用多普勒速度估计自运动和动态点，结合几何与多普勒残差进行扫描对齐
- 实验或效果：在多个数据集上提升旋转稳定性和平移精度，实时运行

## 摘要（原文）

> Reliable odometry in highly dynamic environments remains challenging when it relies on ICP-based registration: ICP assumes near-static scenes and degrades in repetitive or low-texture geometry. We introduce Dynamic-ICP, a Doppler-aware registration framework. The method (i) estimates ego motion from per-point Doppler velocity via robust regression and builds a velocity filter, (ii) clusters dynamic objects and reconstructs object-wise translational velocities from ego-compensated radial measurements, (iii) predicts dynamic points with a constant-velocity model, and (iv) aligns scans using a compact objective that combines point-to-plane geometry residual with a translation-invariant, rotation-only Doppler residual. The approach requires no external sensors or sensor-vehicle calibration and operates directly on FMCW LiDAR range and Doppler velocities. We evaluate Dynamic-ICP on three datasets-HeRCULES, HeLiPR, AevaScenes-focusing on highly dynamic scenes. Dynamic-ICP consistently improves rotational stability and translation accuracy over the state-of-the-art methods. Our approach is also simple to integrate into existing pipelines, runs in real time, and provides a lightweight solution for robust registration in dynamic environments. To encourage further research, the code is available at: https://github.com/JMUWRobotics/Dynamic-ICP.

