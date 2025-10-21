---
layout: default
title: Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS
---

# Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS
**arXiv**：[2510.17479v1](https://arxiv.org/abs/2510.17479) · [PDF](https://arxiv.org/pdf/2510.17479.pdf)  
**作者**：Feng Zhou, Wenkai Guo, Pu Cao, Zhicheng Zhang, Jianqin Yin  

**一句话要点**：提出更强初始化管道以解决稀疏视图3D高斯溅射的过拟合问题

**关键词**：稀疏视图3D重建, 高斯溅射初始化, 结构从运动增强, 点云正则化, 新视图合成

## 3 点简述
- 核心问题：稀疏视图3DGS易过拟合训练视图，导致新视图渲染模糊。
- 方法要点：基于SfM，设计频率感知SfM、3DGS自初始化和点云正则化。
- 实验效果：在LLFF和Mip-NeRF360数据集上，稀疏视图设置下性能一致提升。

## 摘要（原文）

> Sparse-view 3D Gaussian Splatting (3DGS) often overfits to the training
> views, leading to artifacts like blurring in novel view rendering. Prior work
> addresses it either by enhancing the initialization (\emph{i.e.}, the point
> cloud from Structure-from-Motion (SfM)) or by adding training-time constraints
> (regularization) to the 3DGS optimization. Yet our controlled ablations reveal
> that initialization is the decisive factor: it determines the attainable
> performance band in sparse-view 3DGS, while training-time constraints yield
> only modest within-band improvements at extra cost. Given initialization's
> primacy, we focus our design there. Although SfM performs poorly under sparse
> views due to its reliance on feature matching, it still provides reliable seed
> points. Thus, building on SfM, our effort aims to supplement the regions it
> fails to cover as comprehensively as possible. Specifically, we design: (i)
> frequency-aware SfM that improves low-texture coverage via low-frequency view
> augmentation and relaxed multi-view correspondences; (ii) 3DGS
> self-initialization that lifts photometric supervision into additional points,
> compensating SfM-sparse regions with learned Gaussian centers; and (iii)
> point-cloud regularization that enforces multi-view consistency and uniform
> spatial coverage through simple geometric/visibility priors, yielding a clean
> and reliable point cloud. Our experiments on LLFF and Mip-NeRF360 demonstrate
> consistent gains in sparse-view settings, establishing our approach as a
> stronger initialization strategy. Code is available at
> https://github.com/zss171999645/ItG-GS.

