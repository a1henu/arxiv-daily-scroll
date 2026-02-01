---
layout: default
title: From Implicit Ambiguity to Explicit Solidity: Diagnosing Interior Geometric Degradation in Neural Radiance Fields for Dense 3D Scene Understanding
---

# From Implicit Ambiguity to Explicit Solidity: Diagnosing Interior Geometric Degradation in Neural Radiance Fields for Dense 3D Scene Understanding
**arXiv**：[2601.21421v1](https://arxiv.org/abs/2601.21421) · [PDF](https://arxiv.org/pdf/2601.21421.pdf)  
**作者**：Jiangsan Zhao, Jakob Geipel, Kryzysztof Kusnierek  

**一句话要点**：提出基于稀疏体素栅格化的显式几何方法，以解决NeRF在密集自遮挡场景中的内部几何退化问题

**关键词**：神经辐射场, 三维场景理解, 几何退化, 稀疏体素栅格化, 自遮挡场景, 实例恢复

## 3 点简述
- 核心问题：NeRF在密集自遮挡场景中因隐式密度场优化导致内部几何退化，表现为空心或破碎结构，影响实例计数准确性
- 方法要点：引入基于SfM特征几何的稀疏体素栅格化流程，通过2D实例掩码投影和递归分割强制几何分离，保持物理实体性
- 实验或效果：在合成数据集上，显式方法实现95.8%实例恢复率，比隐式基线高43%，对监督失败更鲁棒

## 摘要（原文）

> Neural Radiance Fields (NeRFs) have emerged as a powerful paradigm for multi-view reconstruction, complementing classical photogrammetric pipelines based on Structure-from-Motion (SfM) and Multi-View Stereo (MVS). However, their reliability for quantitative 3D analysis in dense, self-occluding scenes remains poorly understood. In this study, we identify a fundamental failure mode of implicit density fields under heavy occlusion, which we term Interior Geometric Degradation (IGD). We show that transmittance-based volumetric optimization satisfies photometric supervision by reconstructing hollow or fragmented structures rather than solid interiors, leading to systematic instance undercounting. Through controlled experiments on synthetic datasets with increasing occlusion, we demonstrate that state-of-the-art mask-supervised NeRFs saturate at approximately 89% instance recovery in dense scenes, despite improved surface coherence and mask quality. To overcome this limitation, we introduce an explicit geometric pipeline based on Sparse Voxel Rasterization (SVRaster), initialized from SfM feature geometry. By projecting 2D instance masks onto an explicit voxel grid and enforcing geometric separation via recursive splitting, our approach preserves physical solidity and achieves a 95.8% recovery rate in dense clusters. A sensitivity analysis using degraded segmentation masks further shows that explicit SfM-based geometry is substantially more robust to supervision failure, recovering 43% more instances than implicit baselines. These results demonstrate that explicit geometric priors are a prerequisite for reliable quantitative analysis in highly self-occluding 3D scenes.

