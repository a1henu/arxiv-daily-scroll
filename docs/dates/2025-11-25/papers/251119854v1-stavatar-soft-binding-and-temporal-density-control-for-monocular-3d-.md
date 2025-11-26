---
layout: default
title: STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction
---

# STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction
**arXiv**：[2511.19854v1](https://arxiv.org/abs/2511.19854) · [PDF](https://arxiv.org/pdf/2511.19854.pdf)  
**作者**：Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  

**一句话要点**：提出STAvatar以解决单目视频3D头部重建中的刚性运动和遮挡区域问题

**关键词**：3D头部重建, 单目视频, 高斯溅射, 软绑定, 自适应密度控制, 遮挡处理

## 3 点简述
- 核心问题：现有方法基于3D高斯溅射，绑定网格三角形，仅用线性混合蒙皮导致运动僵硬和表达受限，且缺乏处理遮挡区域的策略。
- 方法要点：引入UV自适应软绑定框架，结合图像和几何先验学习高斯特征偏移；采用时间自适应密度控制策略，聚类相似帧并使用融合感知误差优化细节。
- 实验或效果：在四个基准数据集上实现最先进重建性能，尤其在捕捉细粒度细节和重建频繁遮挡区域方面表现优异。

## 摘要（原文）

> Reconstructing high-fidelity and animatable 3D head avatars from monocular videos remains a challenging yet essential task. Existing methods based on 3D Gaussian Splatting typically bind Gaussians to mesh triangles and model deformations solely via Linear Blend Skinning, which results in rigid motion and limited expressiveness. Moreover, they lack specialized strategies to handle frequently occluded regions (e.g., mouth interiors, eyelids). To address these limitations, we propose STAvatar, which consists of two key components: (1) a UV-Adaptive Soft Binding framework that leverages both image-based and geometric priors to learn per-Gaussian feature offsets within the UV space. This UV representation supports dynamic resampling, ensuring full compatibility with Adaptive Density Control (ADC) and enhanced adaptability to shape and textural variations. (2) a Temporal ADC strategy, which first clusters structurally similar frames to facilitate more targeted computation of the densification criterion. It further introduces a novel fused perceptual error as clone criterion to jointly capture geometric and textural discrepancies, encouraging densification in regions requiring finer details. Extensive experiments on four benchmark datasets demonstrate that STAvatar achieves state-of-the-art reconstruction performance, especially in capturing fine-grained details and reconstructing frequently occluded regions. The code will be publicly available.

