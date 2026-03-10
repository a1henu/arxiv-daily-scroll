---
layout: default
title: Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction
---

# Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction
**arXiv**：[2603.08503v1](https://arxiv.org/abs/2603.08503) · [PDF](https://arxiv.org/pdf/2603.08503.pdf)  
**作者**：Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  

**一句话要点**：提出Spherical-GOF以解决全景相机模型下3D高斯溅射的几何失真问题

**关键词**：全景渲染, 3D高斯溅射, 几何一致性, 球面射线采样, 机器人视觉, 数据集发布

## 3 点简述
- 核心问题：现有3D高斯溅射方法基于透视投影，直接应用于全景图像时易产生失真和几何不一致。
- 方法要点：在球面射线空间直接采样高斯不透明度场，引入保守球面边界规则和球面滤波方案以优化渲染。
- 实验或效果：在标准全景基准测试中，深度重投影误差降低57%，循环内点率提升21%，几何一致性显著改善。

## 摘要（原文）

> Omnidirectional images are increasingly used in robotics and vision due to their wide field of view. However, extending 3D Gaussian Splatting (3DGS) to panoramic camera models remains challenging, as existing formulations are designed for perspective projections and naive adaptations often introduce distortion and geometric inconsistencies. We present Spherical-GOF, an omnidirectional Gaussian rendering framework built upon Gaussian Opacity Fields (GOF). Unlike projection-based rasterization, Spherical-GOF performs GOF ray sampling directly on the unit sphere in spherical ray space, enabling consistent ray-Gaussian interactions for panoramic rendering. To make the spherical ray casting efficient and robust, we derive a conservative spherical bounding rule for fast ray-Gaussian culling and introduce a spherical filtering scheme that adapts Gaussian footprints to distortion-varying panoramic pixel sampling. Extensive experiments on standard panoramic benchmarks (OmniBlender and OmniPhotos) demonstrate competitive photometric quality and substantially improved geometric consistency. Compared with the strongest baseline, Spherical-GOF reduces depth reprojection error by 57% and improves cycle inlier ratio by 21%. Qualitative results show cleaner depth and more coherent normal maps, with strong robustness to global panorama rotations. We further validate generalization on OmniRob, a real-world robotic omnidirectional dataset introduced in this work, featuring UAV and quadruped platforms. The source code and the OmniRob dataset will be released at https://github.com/1170632760/Spherical-GOF.

