---
layout: default
title: Urban Neural Surface Reconstruction from Constrained Sparse Aerial Imagery with 3D SAR Fusion
---

# Urban Neural Surface Reconstruction from Constrained Sparse Aerial Imagery with 3D SAR Fusion
**arXiv**：[2601.22045v1](https://arxiv.org/abs/2601.22045) · [PDF](https://arxiv.org/pdf/2601.22045.pdf)  
**作者**：Da Li, Chen Yao, Tong Mao, Jiacheng Bao, Houjun Sun  

**一句话要点**：提出融合3D SAR点云与航拍图像的神经表面重建框架，以解决稀疏视角下城市三维重建的几何模糊问题。

**关键词**：神经表面重建, 3D SAR融合, 稀疏视角重建, 城市三维重建, 多模态遥感, SDF优化

## 3 点简述
- 核心问题：现有神经表面重建方法在稀疏航拍图像下存在几何模糊和不稳定性，影响大规模城市遥感应用。
- 方法要点：首次将3D SAR点云作为空间先验融入SDF-based神经表面重建，通过结构感知光线选择和自适应采样优化重建过程。
- 实验或效果：构建首个多模态基准数据集，实验表明融合3D SAR显著提升稀疏和斜视角条件下的重建精度、完整性和鲁棒性。

## 摘要（原文）

> Neural surface reconstruction (NSR) has recently shown strong potential for urban 3D reconstruction from multi-view aerial imagery. However, existing NSR methods often suffer from geometric ambiguity and instability, particularly under sparse-view conditions. This issue is critical in large-scale urban remote sensing, where aerial image acquisition is limited by flight paths, terrain, and cost. To address this challenge, we present the first urban NSR framework that fuses 3D synthetic aperture radar (SAR) point clouds with aerial imagery for high-fidelity reconstruction under constrained, sparse-view settings. 3D SAR can efficiently capture large-scale geometry even from a single side-looking flight path, providing robust priors that complement photometric cues from images. Our framework integrates radar-derived spatial constraints into an SDF-based NSR backbone, guiding structure-aware ray selection and adaptive sampling for stable and efficient optimization. We also construct the first benchmark dataset with co-registered 3D SAR point clouds and aerial imagery, facilitating systematic evaluation of cross-modal 3D reconstruction. Extensive experiments show that incorporating 3D SAR markedly enhances reconstruction accuracy, completeness, and robustness compared with single-modality baselines under highly sparse and oblique-view conditions, highlighting a viable route toward scalable high-fidelity urban reconstruction with advanced airborne and spaceborne optical-SAR sensing.

