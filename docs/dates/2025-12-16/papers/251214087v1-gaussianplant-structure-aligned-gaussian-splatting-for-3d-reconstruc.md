---
layout: default
title: GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants
---

# GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants
**arXiv**：[2512.14087v1](https://arxiv.org/abs/2512.14087) · [PDF](https://arxiv.org/pdf/2512.14087.pdf)  
**作者**：Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  

**一句话要点**：提出GaussianPlant以解决植物三维重建中外观与结构分离的难题

**关键词**：三维高斯泼溅, 植物三维重建, 结构外观解耦, 多视图图像, 表型分析, 联合优化

## 3 点简述
- 核心问题：3D高斯泼溅缺乏植物分支结构表示，限制表型分析应用。
- 方法要点：使用结构基元表示分支和叶子几何，外观基元绑定结构基元进行外观重建。
- 实验效果：通过联合优化实现高保真外观和准确结构重建，支持分支和叶子实例提取。

## 摘要（原文）

> We present a method for jointly recovering the appearance and internal structure of botanical plants from multi-view images based on 3D Gaussian Splatting (3DGS). While 3DGS exhibits robust reconstruction of scene appearance for novel-view synthesis, it lacks structural representations underlying those appearances (e.g., branching patterns of plants), which limits its applicability to tasks such as plant phenotyping. To achieve both high-fidelity appearance and structural reconstruction, we introduce GaussianPlant, a hierarchical 3DGS representation, which disentangles structure and appearance. Specifically, we employ structure primitives (StPs) to explicitly represent branch and leaf geometry, and appearance primitives (ApPs) to the plants' appearance using 3D Gaussians. StPs represent a simplified structure of the plant, i.e., modeling branches as cylinders and leaves as disks. To accurately distinguish the branches and leaves, StP's attributes (i.e., branches or leaves) are optimized in a self-organized manner. ApPs are bound to each StP to represent the appearance of branches or leaves as in conventional 3DGS. StPs and ApPs are jointly optimized using a re-rendering loss on the input multi-view images, as well as the gradient flow from ApP to StP using the binding correspondence information. We conduct experiments to qualitatively evaluate the reconstruction accuracy of both appearance and structure, as well as real-world experiments to qualitatively validate the practical performance. Experiments show that the GaussianPlant achieves both high-fidelity appearance reconstruction via ApPs and accurate structural reconstruction via StPs, enabling the extraction of branch structure and leaf instances.

