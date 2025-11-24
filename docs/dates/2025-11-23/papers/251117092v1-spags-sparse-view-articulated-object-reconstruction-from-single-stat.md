---
layout: default
title: SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting
---

# SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting
**arXiv**：[2511.17092v1](https://arxiv.org/abs/2511.17092) · [PDF](https://arxiv.org/pdf/2511.17092.pdf)  
**作者**：Di Wu, Liu Liu, Xueyu Yuan, Qiaoyu Jun, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  

**一句话要点**：提出基于平面高斯溅射的稀疏视图铰接物体重建框架，仅需单状态图像输入

**关键词**：铰接物体重建, 平面高斯溅射, 稀疏视图, 部件分割, 深度平滑正则化, 少样本扩散

## 3 点简述
- 核心问题：现有铰接物体重建方法需多阶段多视图输入，成本高昂
- 方法要点：引入高斯信息场感知最优视图，压缩3D高斯为平面高斯优化
- 实验效果：在合成和真实数据上实现更高保真度的部件级表面重建

## 摘要（原文）

> Articulated objects are ubiquitous in daily environments, and their 3D reconstruction holds great significance across various fields. However, existing articulated object reconstruction methods typically require costly inputs such as multi-stage and multi-view observations. To address the limitations, we propose a category-agnostic articulated object reconstruction framework via planar Gaussian Splatting, which only uses sparse-view RGB images from a single state. Specifically, we first introduce a Gaussian information field to perceive the optimal sparse viewpoints from candidate camera poses. Then we compress 3D Gaussians into planar Gaussians to facilitate accurate estimation of normal and depth. The planar Gaussians are optimized in a coarse-to-fine manner through depth smooth regularization and few-shot diffusion. Moreover, we introduce a part segmentation probability for each Gaussian primitive and update them by back-projecting part segmentation masks of renderings. Extensive experimental results demonstrate that our method achieves higher-fidelity part-level surface reconstruction on both synthetic and real-world data than existing methods. Codes will be made publicly available.

