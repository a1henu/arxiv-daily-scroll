---
layout: default
title: Wid3R: Wide Field-of-View 3D Reconstruction via Camera Model Conditioning
---

# Wid3R: Wide Field-of-View 3D Reconstruction via Camera Model Conditioning
**arXiv**：[2602.05321v1](https://arxiv.org/abs/2602.05321) · [PDF](https://arxiv.org/pdf/2602.05321.pdf)  
**作者**：Dongki Jung, Jaehoon Choi, Adil Qureshi, Somi Jeong, Dinesh Manocha, Suyong Yeon  

**一句话要点**：提出Wid3R以支持广角相机模型的通用多视角三维重建

**关键词**：广角三维重建, 相机模型条件化, 多视角估计, 失真感知, 零样本鲁棒性, 360度图像处理

## 3 点简述
- 核心问题：现有方法依赖针孔相机假设，限制了在鱼眼或全景相机等广角场景的应用。
- 方法要点：利用射线表示、球谐函数和相机模型令牌，实现失真感知的三维重建。
- 实验或效果：在Stanford2D3D上提升达+77.33，展示零样本鲁棒性并支持360度图像直接重建。

## 摘要（原文）

> We present Wid3R, a feed-forward neural network for visual geometry reconstruction that supports wide field-of-view camera models. Prior methods typically assume that input images are rectified or captured with pinhole cameras, since both their architectures and training datasets are tailored to perspective images only. These assumptions limit their applicability in real-world scenarios that use fisheye or panoramic cameras and often require careful calibration and undistortion. In contrast, Wid3R is a generalizable multi-view 3D estimation method that can model wide field-of-view camera types. Our approach leverages a ray representation with spherical harmonics and a novel camera model token within the network, enabling distortion-aware 3D reconstruction. Furthermore, Wid3R is the first multi-view foundation model to support feed-forward 3D reconstruction directly from 360 imagery. It demonstrates strong zero-shot robustness and consistently outperforms prior methods, achieving improvements of up to +77.33 on Stanford2D3D.

