---
layout: default
title: CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth
---

# CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth
**arXiv**：[2512.14001v1](https://arxiv.org/abs/2512.14001) · [PDF](https://arxiv.org/pdf/2512.14001.pdf)  
**作者**：Zhuo Zhang, Yonghui Liu, Meijie Zhang, Feiyang Tan, Yikang Ding  

**一句话要点**：提出CLAIM方法，利用单目深度模型优化相机与LiDAR数据对齐。

**关键词**：相机-LiDAR对齐, 单目深度模型, 损失函数优化, 多模态校准, 点云处理

## 3 点简述
- 核心问题：相机与LiDAR数据对齐需精确校准，传统方法依赖复杂特征处理。
- 方法要点：采用粗到精搜索，结合基于皮尔逊相关的结构损失和基于互信息的纹理损失。
- 实验或效果：在KITTI、Waymo和MIAS-LCEC数据集上验证，性能优于现有方法。

## 摘要（原文）

> In this paper, we unleash the potential of the powerful monodepth model in camera-LiDAR calibration and propose CLAIM, a novel method of aligning data from the camera and LiDAR. Given the initial guess and pairs of images and LiDAR point clouds, CLAIM utilizes a coarse-to-fine searching method to find the optimal transformation minimizing a patched Pearson correlation-based structure loss and a mutual information-based texture loss. These two losses serve as good metrics for camera-LiDAR alignment results and require no complicated steps of data processing, feature extraction, or feature matching like most methods, rendering our method simple and adaptive to most scenes. We validate CLAIM on public KITTI, Waymo, and MIAS-LCEC datasets, and the experimental results demonstrate its superior performance compared with the state-of-the-art methods. The code is available at https://github.com/Tompson11/claim.

