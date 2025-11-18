---
layout: default
title: Reconstructing 3D Scenes in Native High Dynamic Range
---

# Reconstructing 3D Scenes in Native High Dynamic Range
**arXiv**：[2511.12895v1](https://arxiv.org/abs/2511.12895) · [PDF](https://arxiv.org/pdf/2511.12895.pdf)  
**作者**：Kaixuan Zhang, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  

**一句话要点**：提出原生高动态范围3D高斯泼溅以直接建模HDR数据，提升3D场景重建质量

**关键词**：高动态范围成像, 3D场景重建, 高斯泼溅, 亮度-色度分解, 原生HDR数据, 多视图重建

## 3 点简述
- 核心问题：现有3D重建方法依赖LDR数据，限制专业应用，HDR重建需复杂多曝光或逆色调映射
- 方法要点：引入亮度-色度分解颜色表示，直接从原生HDR相机数据优化，保持全动态范围
- 实验或效果：在合成和真实HDR数据集上，重建质量和动态范围保持显著优于现有方法

## 摘要（原文）

> High Dynamic Range (HDR) imaging is essential for professional digital media creation, e.g., filmmaking, virtual production, and photorealistic rendering. However, 3D scene reconstruction has primarily focused on Low Dynamic Range (LDR) data, limiting its applicability to professional workflows. Existing approaches that reconstruct HDR scenes from LDR observations rely on multi-exposure fusion or inverse tone-mapping, which increase capture complexity and depend on synthetic supervision. With the recent emergence of cameras that directly capture native HDR data in a single exposure, we present the first method for 3D scene reconstruction that directly models native HDR observations. We propose {\bf Native High dynamic range 3D Gaussian Splatting (NH-3DGS)}, which preserves the full dynamic range throughout the reconstruction pipeline. Our key technical contribution is a novel luminance-chromaticity decomposition of the color representation that enables direct optimization from native HDR camera data. We demonstrate on both synthetic and real multi-view HDR datasets that NH-3DGS significantly outperforms existing methods in reconstruction quality and dynamic range preservation, enabling professional-grade 3D reconstruction directly from native HDR captures. Code and datasets will be made available.

