---
layout: default
title: iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion
---

# iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion
**arXiv**：[2511.14149v1](https://arxiv.org/abs/2511.14149) · [PDF](https://arxiv.org/pdf/2511.14149.pdf)  
**作者**：Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  

**一句话要点**：提出iGaussian通过前馈3D高斯反演实现实时相机位姿估计

**关键词**：相机位姿估计, 3D高斯反演, 前馈框架, 实时SLAM, 特征匹配, 多模型融合

## 3 点简述
- 现有方法依赖迭代渲染比较循环，计算开销大，难以实时应用
- 采用两阶段前馈框架，先粗回归位姿，再通过特征匹配和多模型融合精炼
- 实验显示显著降低旋转误差至0.2°，速度提升10倍，达2.87 FPS

## 摘要（原文）

> Recent trends in SLAM and visual navigation have embraced 3D Gaussians as the preferred scene representation, highlighting the importance of estimating camera poses from a single image using a pre-built Gaussian model. However, existing approaches typically rely on an iterative \textit{render-compare-refine} loop, where candidate views are first rendered using NeRF or Gaussian Splatting, then compared against the target image, and finally, discrepancies are used to update the pose. This multi-round process incurs significant computational overhead, hindering real-time performance in robotics. In this paper, we propose iGaussian, a two-stage feed-forward framework that achieves real-time camera pose estimation through direct 3D Gaussian inversion. Our method first regresses a coarse 6DoF pose using a Gaussian Scene Prior-based Pose Regression Network with spatial uniform sampling and guided attention mechanisms, then refines it through feature matching and multi-model fusion. The key contribution lies in our cross-correlation module that aligns image embeddings with 3D Gaussian attributes without differentiable rendering, coupled with a Weighted Multiview Predictor that fuses features from Multiple strategically sampled viewpoints. Experimental results on the NeRF Synthetic, Mip-NeRF 360, and T\&T+DB datasets demonstrate a significant performance improvement over previous methods, reducing median rotation errors to 0.2° while achieving 2.87 FPS tracking on mobile robots, which is an impressive 10 times speedup compared to optimization-based approaches. Code: https://github.com/pythongod-exe/iGaussian

