---
layout: default
title: Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting
---

# Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting
**arXiv**：[2603.02893v1](https://arxiv.org/abs/2603.02893) · [PDF](https://arxiv.org/pdf/2603.02893.pdf)  
**作者**：Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  

**一句话要点**：提出MVD-HuGaS方法，通过多视图扩散模型实现单图像自由视角3D人体渲染。

**关键词**：3D人体重建, 高斯溅射, 多视图扩散, 单图像渲染, 相机姿态优化

## 3 点简述
- 核心问题：单图像3D人体重建存在伪影和泛化困难，如结构扁平化或视图不一致。
- 方法要点：使用增强多视图扩散模型生成多视图图像，结合对齐模块优化3D高斯和相机姿态。
- 实验或效果：在Thuman2.0和2K2K数据集上实现最先进的单视图3D人体渲染性能。

## 摘要（原文）

> 3D human reconstruction from a single image is a challenging problem and has been exclusively studied in the literature. Recently, some methods have resorted to diffusion models for guidance, optimizing a 3D representation via Score Distillation Sampling(SDS) or generating a back-view image for facilitating reconstruction. However, these methods tend to produce unsatisfactory artifacts (\textit{e.g.} flattened human structure or over-smoothing results caused by inconsistent priors from multiple views) and struggle with real-world generalization in the wild. In this work, we present \emph{MVD-HuGaS}, enabling free-view 3D human rendering from a single image via a multi-view human diffusion model. We first generate multi-view images from the single reference image with an enhanced multi-view diffusion model, which is well fine-tuned on high-quality 3D human datasets to incorporate 3D geometry priors and human structure priors. To infer accurate camera poses from the sparse generated multi-view images for reconstruction, an alignment module is introduced to facilitate joint optimization of 3D Gaussians and camera poses. Furthermore, we propose a depth-based Facial Distortion Mitigation module to refine the generated facial regions, thereby improving the overall fidelity of the reconstruction. Finally, leveraging the refined multi-view images, along with their accurate camera poses, MVD-HuGaS optimizes the 3D Gaussians of the target human for high-fidelity free-view renderings. Extensive experiments on Thuman2.0 and 2K2K datasets show that the proposed MVD-HuGaS achieves state-of-the-art performance on single-view 3D human rendering.

