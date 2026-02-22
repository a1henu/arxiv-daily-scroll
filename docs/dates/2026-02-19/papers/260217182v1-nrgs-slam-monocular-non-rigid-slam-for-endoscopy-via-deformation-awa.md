---
layout: default
title: NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting
---

# NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting
**arXiv**：[2602.17182v1](https://arxiv.org/abs/2602.17182) · [PDF](https://arxiv.org/pdf/2602.17182.pdf)  
**作者**：Jiwei Shan, Zeyu Cai, Yirui Li, Yongbo Chen, Lijun Han, Yun-hui Liu, Hesheng Wang, Shing Shin Cheng  

**一句话要点**：提出NRGS-SLAM，基于变形感知3D高斯泼溅的内窥镜单目非刚性SLAM系统，以解决变形耦合与重建质量低的问题。

**关键词**：非刚性SLAM, 3D高斯泼溅, 内窥镜视觉, 变形感知, 单目视觉, 几何先验

## 3 点简述
- 核心问题：内窥镜场景因软组织持续变形违反刚性假设，导致相机运动与变形耦合模糊，现有方法缺乏有效解耦机制和高质量场景表示。
- 方法要点：引入变形感知3D高斯地图，通过贝叶斯自监督学习变形概率；设计变形跟踪模块优先低变形区域进行姿态估计，并更新变形；结合几何先验损失缓解病态性。
- 实验或效果：在多个公开内窥镜数据集上，相比先进方法，相机姿态估计误差降低达50%，实现更高质量的光照真实重建，消融研究验证关键设计有效性。

## 摘要（原文）

> Visual simultaneous localization and mapping (V-SLAM) is a fundamental capability for autonomous perception and navigation. However, endoscopic scenes violate the rigidity assumption due to persistent soft-tissue deformations, creating a strong coupling ambiguity between camera ego-motion and intrinsic deformation. Although recent monocular non-rigid SLAM methods have made notable progress, they often lack effective decoupling mechanisms and rely on sparse or low-fidelity scene representations, which leads to tracking drift and limited reconstruction quality. To address these limitations, we propose NRGS-SLAM, a monocular non-rigid SLAM system for endoscopy based on 3D Gaussian Splatting. To resolve the coupling ambiguity, we introduce a deformation-aware 3D Gaussian map that augments each Gaussian primitive with a learnable deformation probability, optimized via a Bayesian self-supervision strategy without requiring external non-rigidity labels. Building on this representation, we design a deformable tracking module that performs robust coarse-to-fine pose estimation by prioritizing low-deformation regions, followed by efficient per-frame deformation updates. A carefully designed deformable mapping module progressively expands and refines the map, balancing representational capacity and computational efficiency. In addition, a unified robust geometric loss incorporates external geometric priors to mitigate the inherent ill-posedness of monocular non-rigid SLAM. Extensive experiments on multiple public endoscopic datasets demonstrate that NRGS-SLAM achieves more accurate camera pose estimation (up to 50\% reduction in RMSE) and higher-quality photo-realistic reconstructions than state-of-the-art methods. Comprehensive ablation studies further validate the effectiveness of our key design choices. Source code will be publicly available upon paper acceptance.

