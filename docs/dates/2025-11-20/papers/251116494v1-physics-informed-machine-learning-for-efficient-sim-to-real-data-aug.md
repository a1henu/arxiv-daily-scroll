---
layout: default
title: Physics-Informed Machine Learning for Efficient Sim-to-Real Data Augmentation in Micro-Object Pose Estimation
---

# Physics-Informed Machine Learning for Efficient Sim-to-Real Data Augmentation in Micro-Object Pose Estimation
**arXiv**：[2511.16494v1](https://arxiv.org/abs/2511.16494) · [PDF](https://arxiv.org/pdf/2511.16494.pdf)  
**作者**：Zongcai Tan, Lan Wei, Dandan Zhang  

**一句话要点**：提出物理信息深度生成学习框架，以高效合成显微镜图像用于微物体姿态估计

**关键词**：物理信息机器学习, 模拟到真实数据增强, 微物体姿态估计, 生成对抗网络, 波光学渲染, 深度对齐

## 3 点简述
- 微物体姿态估计依赖高质量显微镜图像，但数据获取困难且成本高
- 集成波光学物理渲染和深度对齐到GAN，合成高保真图像
- 合成数据训练的姿态估计器精度接近真实数据，泛化至未知姿态

## 摘要（原文）

> Precise pose estimation of optical microrobots is essential for enabling high-precision object tracking and autonomous biological studies. However, current methods rely heavily on large, high-quality microscope image datasets, which are difficult and costly to acquire due to the complexity of microrobot fabrication and the labour-intensive labelling. Digital twin systems offer a promising path for sim-to-real data augmentation, yet existing techniques struggle to replicate complex optical microscopy phenomena, such as diffraction artifacts and depth-dependent imaging.This work proposes a novel physics-informed deep generative learning framework that, for the first time, integrates wave optics-based physical rendering and depth alignment into a generative adversarial network (GAN), to synthesise high-fidelity microscope images for microrobot pose estimation efficiently. Our method improves the structural similarity index (SSIM) by 35.6% compared to purely AI-driven methods, while maintaining real-time rendering speeds (0.022 s/frame).The pose estimator (CNN backbone) trained on our synthetic data achieves 93.9%/91.9% (pitch/roll) accuracy, just 5.0%/5.4% (pitch/roll) below that of an estimator trained exclusively on real data. Furthermore, our framework generalises to unseen poses, enabling data augmentation and robust pose estimation for novel microrobot configurations without additional training data.

