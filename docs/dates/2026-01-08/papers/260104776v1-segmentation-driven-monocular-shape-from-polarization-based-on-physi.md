---
layout: default
title: Segmentation-Driven Monocular Shape from Polarization based on Physical Model
---

# Segmentation-Driven Monocular Shape from Polarization based on Physical Model
**arXiv**：[2601.04776v1](https://arxiv.org/abs/2601.04776) · [PDF](https://arxiv.org/pdf/2601.04776.pdf)  
**作者**：Jinyu Zhang, Xu Ma, Weili Chen, Gonzalo R. Arce  

**一句话要点**：提出分割驱动的单目偏振形状恢复框架，通过局部重建解决方位角歧义问题。

**关键词**：单目偏振形状恢复, 方位角歧义, 自适应区域分割, 凸性先验, 三维重建

## 3 点简述
- 核心问题：单目偏振形状恢复存在方位角歧义，影响重建精度和稳定性。
- 方法要点：采用偏振辅助自适应区域生长分割，将全局凸性假设分解为局部凸区域，并引入多尺度融合凸性先验约束。
- 实验或效果：在合成和真实数据集上验证，相比现有方法在歧义消除和几何保真度方面有显著提升。

## 摘要（原文）

> Monocular shape-from-polarization (SfP) leverages the intrinsic relationship between light polarization properties and surface geometry to recover surface normals from single-view polarized images, providing a compact and robust approach for three-dimensional (3D) reconstruction. Despite its potential, existing monocular SfP methods suffer from azimuth angle ambiguity, an inherent limitation of polarization analysis, that severely compromises reconstruction accuracy and stability. This paper introduces a novel segmentation-driven monocular SfP (SMSfP) framework that reformulates global shape recovery into a set of local reconstructions over adaptively segmented convex sub-regions. Specifically, a polarization-aided adaptive region growing (PARG) segmentation strategy is proposed to decompose the global convexity assumption into locally convex regions, effectively suppressing azimuth ambiguities and preserving surface continuity. Furthermore, a multi-scale fusion convexity prior (MFCP) constraint is developed to ensure local surface consistency and enhance the recovery of fine textural and structural details. Extensive experiments on both synthetic and real-world datasets validate the proposed approach, showing significant improvements in disambiguation accuracy and geometric fidelity compared with existing physics-based monocular SfP techniques.

