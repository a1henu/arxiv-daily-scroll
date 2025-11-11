---
layout: default
title: Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes
---

# Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes
**arXiv**：[2511.06765v1](https://arxiv.org/abs/2511.06765) · [PDF](https://arxiv.org/pdf/2511.06765.pdf)  
**作者**：Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  

**一句话要点**：提出融合位姿先验与几何约束的3D高斯泼溅方法，以解决纹理缺失户外场景的渲染问题

**关键词**：3D高斯泼溅, 位姿估计, 几何约束, 户外场景渲染, 法向量优化, 秩正则化

## 3 点简述
- 核心问题：户外大场景中纹理弱或重复导致位姿估计不稳定和场景表示失真
- 方法要点：利用LiDAR-IMU里程计提供位姿先验，并引入法向量约束和秩正则化优化高斯基元
- 实验或效果：在公开和自采数据集上，位姿优化时间减少三分之二，渲染质量显著提升

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a key rendering pipeline for
> digital asset creation due to its balance between efficiency and visual
> quality. To address the issues of unstable pose estimation and scene
> representation distortion caused by geometric texture inconsistency in large
> outdoor scenes with weak or repetitive textures, we approach the problem from
> two aspects: pose estimation and scene representation. For pose estimation, we
> leverage LiDAR-IMU Odometry to provide prior poses for cameras in large-scale
> environments. These prior pose constraints are incorporated into COLMAP's
> triangulation process, with pose optimization performed via bundle adjustment.
> Ensuring consistency between pixel data association and prior poses helps
> maintain both robustness and accuracy. For scene representation, we introduce
> normal vector constraints and effective rank regularization to enforce
> consistency in the direction and shape of Gaussian primitives. These
> constraints are jointly optimized with the existing photometric loss to enhance
> the map quality. We evaluate our approach using both public and self-collected
> datasets. In terms of pose optimization, our method requires only one-third of
> the time while maintaining accuracy and robustness across both datasets. In
> terms of scene representation, the results show that our method significantly
> outperforms conventional 3DGS pipelines. Notably, on self-collected datasets
> characterized by weak or repetitive textures, our approach demonstrates
> enhanced visualization capabilities and achieves superior overall performance.
> Codes and data will be publicly available at
> https://github.com/justinyeah/normal_shape.git.

