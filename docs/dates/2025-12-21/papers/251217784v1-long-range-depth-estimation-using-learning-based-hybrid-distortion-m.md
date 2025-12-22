---
layout: default
title: Long-Range depth estimation using learning based Hybrid Distortion Model for CCTV cameras
---

# Long-Range depth estimation using learning based Hybrid Distortion Model for CCTV cameras
**arXiv**：[2512.17784v1](https://arxiv.org/abs/2512.17784) · [PDF](https://arxiv.org/pdf/2512.17784.pdf)  
**作者**：Ami Pandat, Punna Rajasekhar, G. Aravamuthan, Gopika Vinod, Rohit Shukla  

**一句话要点**：提出基于学习的混合畸变模型框架，用于提升CCTV相机在长距离深度估计中的性能。

**关键词**：长距离深度估计, 混合畸变模型, 神经网络校正, CCTV相机校准, 3D定位, GIS可视化

## 3 点简述
- 核心问题：传统畸变模型在长距离（如数百米以上）3D定位中因非线性限制导致性能不足。
- 方法要点：结合扩展传统畸变模型与神经网络残差校正，构建混合模型以准确建模镜头畸变。
- 实验或效果：框架在长达5公里的距离内有效估计物体3D位置，并通过GIS坐标可视化验证了鲁棒性。

## 摘要（原文）

> Accurate camera models are essential for photogrammetry applications such as 3D mapping and object localization, particularly for long distances. Various stereo-camera based 3D localization methods are available but are limited to few hundreds of meters' range. This is majorly due to the limitation of the distortion models assumed for the non-linearities present in the camera lens. This paper presents a framework for modeling a suitable distortion model that can be used for localizing the objects at longer distances. It is well known that neural networks can be a better alternative to model a highly complex non-linear lens distortion function; on contrary, it is observed that a direct application of neural networks to distortion models fails to converge to estimate the camera parameters. To resolve this, a hybrid approach is presented in this paper where the conventional distortion models are initially extended to incorporate higher-order terms and then enhanced using neural network based residual correction model. This hybrid approach has substantially improved long-range localization performance and is capable of estimating the 3D position of objects at distances up to 5 kilometres. The estimated 3D coordinates are transformed to GIS coordinates and are plotted on a GIS map for visualization. Experimental validation demonstrates the robustness and effectiveness of proposed framework, offering a practical solution to calibrate CCTV cameras for long-range photogrammetry applications.

