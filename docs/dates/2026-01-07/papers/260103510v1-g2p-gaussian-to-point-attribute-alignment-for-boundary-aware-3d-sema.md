---
layout: default
title: G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation
---

# G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation
**arXiv**：[2601.03510v1](https://arxiv.org/abs/2601.03510) · [PDF](https://arxiv.org/pdf/2601.03510.pdf)  
**作者**：Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  

**一句话要点**：提出G2P方法，通过高斯到点属性对齐解决点云语义分割中几何相似物体的外观区分问题。

**关键词**：点云语义分割, 3D高斯泼溅, 属性对齐, 边界定位, 几何歧义解决

## 3 点简述
- 核心问题：点云稀疏不规则，几何特征不足以区分形状相似但外观不同的物体。
- 方法要点：从3D高斯泼溅转移外观属性到点云，利用不透明度和尺度属性对齐几何并定位边界。
- 实验或效果：在标准基准测试中表现优异，对几何挑战类有显著改进，无需2D或语言监督。

## 摘要（原文）

> Semantic segmentation on point clouds is critical for 3D scene understanding. However, sparse and irregular point distributions provide limited appearance evidence, making geometry-only features insufficient to distinguish objects with similar shapes but distinct appearances (e.g., color, texture, material). We propose Gaussian-to-Point (G2P), which transfers appearance-aware attributes from 3D Gaussian Splatting to point clouds for more discriminative and appearance-consistent segmentation. Our G2P address the misalignment between optimized Gaussians and original point geometry by establishing point-wise correspondences. By leveraging Gaussian opacity attributes, we resolve the geometric ambiguity that limits existing models. Additionally, Gaussian scale attributes enable precise boundary localization in complex 3D scenes. Extensive experiments demonstrate that our approach achieves superior performance on standard benchmarks and shows significant improvements on geometrically challenging classes, all without any 2D or language supervision.

