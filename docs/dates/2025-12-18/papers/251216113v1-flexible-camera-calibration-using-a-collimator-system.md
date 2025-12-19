---
layout: default
title: Flexible Camera Calibration using a Collimator System
---

# Flexible Camera Calibration using a Collimator System
**arXiv**：[2512.16113v1](https://arxiv.org/abs/2512.16113) · [PDF](https://arxiv.org/pdf/2512.16113.pdf)  
**作者**：Shunkun Liang, Banglei Guan, Zhenbao Yu, Dongcai Tan, Pengju Sun, Zibin Liu, Qifeng Yu, Yang Shang  

**一句话要点**：提出基于准直仪系统的相机标定方法，实现灵活快速标定

**关键词**：相机标定, 准直仪系统, 角度不变性约束, 球形运动模型, 单图像标定, 摄影测量

## 3 点简述
- 核心问题：相机标定在摄影测量和3D视觉中至关重要，传统方法可能依赖复杂运动或环境
- 方法要点：利用准直仪系统引入角度不变性约束，将相对运动简化为3自由度纯旋转，提出线性求解器和单图像标定算法
- 实验或效果：合成和真实实验验证可行性，性能优于基线方法，代码开源

## 摘要（原文）

> Camera calibration is a crucial step in photogrammetry and 3D vision applications. This paper introduces a novel camera calibration method using a designed collimator system. Our collimator system provides a reliable and controllable calibration environment for the camera. Exploiting the unique optical geometry property of our collimator system, we introduce an angle invariance constraint and further prove that the relative motion between the calibration target and camera conforms to a spherical motion model. This constraint reduces the original 6DOF relative motion between target and camera to a 3DOF pure rotation motion. Using spherical motion constraint, a closed-form linear solver for multiple images and a minimal solver for two images are proposed for camera calibration. Furthermore, we propose a single collimator image calibration algorithm based on the angle invariance constraint. This algorithm eliminates the requirement for camera motion, providing a novel solution for flexible and fast calibration. The performance of our method is evaluated in both synthetic and real-world experiments, which verify the feasibility of calibration using the collimator system and demonstrate that our method is superior to existing baseline methods. Demo code is available at https://github.com/LiangSK98/CollimatorCalibration

