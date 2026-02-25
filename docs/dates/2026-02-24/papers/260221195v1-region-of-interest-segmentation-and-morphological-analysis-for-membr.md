---
layout: default
title: Region of Interest Segmentation and Morphological Analysis for Membranes in Cryo-Electron Tomography
---

# Region of Interest Segmentation and Morphological Analysis for Membranes in Cryo-Electron Tomography
**arXiv**：[2602.21195v1](https://arxiv.org/abs/2602.21195) · [PDF](https://arxiv.org/pdf/2602.21195.pdf)  
**作者**：Xingyi Cheng, Julien Maufront, Aurélie Di Cicco, Daniël M. Pelt, Manuela Dezi, Daniel Lévy  

**一句话要点**：提出TomoROIS-SurfORA框架，用于冷冻电镜断层扫描中膜结构的直接ROI分割与形态分析。

**关键词**：冷冻电镜断层扫描, ROI分割, 形态分析, 深度学习, 表面网格, 膜结构

## 3 点简述
- 核心问题：传统ROI分割依赖全结构分割，对连续复杂膜结构处理不足。
- 方法要点：结合深度学习ROI分割和点云表面分析，支持开放与封闭表面。
- 实验或效果：在体外重构膜系统上验证，自动分析膜接触位点和重塑事件。

## 摘要（原文）

> Cryo-electron tomography (cryo-ET) enables high resolution, three-dimensional reconstruction of biological structures, including membranes and membrane proteins. Identification of regions of interest (ROIs) is central to scientific imaging, as it enables isolation and quantitative analysis of specific structural features within complex datasets. In practice, however, ROIs are typically derived indirectly through full structure segmentation followed by post hoc analysis. This limitation is especially apparent for continuous and geometrically complex structures such as membranes, which are segmented as single entities. Here, we developed TomoROIS-SurfORA, a two step framework for direct, shape-agnostic ROI segmentation and morphological surface analysis. TomoROIS performs deep learning-based ROI segmentation and can be trained from scratch using small annotated datasets, enabling practical application across diverse imaging data. SurfORA processes segmented structures as point clouds and surface meshes to extract quantitative morphological features, including inter-membrane distances, curvature, and surface roughness. It supports both closed and open surfaces, with specific considerations for open surfaces, which are common in cryo-ET due to the missing wedge effect. We demonstrate both tools using in vitro reconstituted membrane systems containing deformable vesicles with complex geometries, enabling automatic quantitative analysis of membrane contact sites and remodeling events such as invagination. While demonstrated here on cryo-ET membrane data, the combined approach is applicable to ROI detection and surface analysis in broader scientific imaging contexts.

