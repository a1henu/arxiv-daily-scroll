---
layout: default
title: Spherical Leech Quantization for Visual Tokenization and Generation
---

# Spherical Leech Quantization for Visual Tokenization and Generation
**arXiv**：[2512.14697v1](https://arxiv.org/abs/2512.14697) · [PDF](https://arxiv.org/pdf/2512.14697.pdf)  
**作者**：Yue Zhao, Hanwen Jiang, Zhenlin Xu, Chutong Yang, Ehsan Adeli, Philipp Krähenbühl  

**一句话要点**：提出基于Leech晶格的球面量化方法，以改进视觉标记化与生成中的重建-压缩权衡。

**关键词**：非参数量化, 晶格编码, Leech晶格, 视觉标记化, 图像压缩, 自回归生成

## 3 点简述
- 核心问题：非参数量化方法在训练自编码器时需辅助损失项，影响效率与性能。
- 方法要点：通过晶格编码统一非参数量化，探索Leech晶格的高对称性实现简化训练。
- 实验或效果：在图像标记化和压缩任务中，优于BSQ，重建质量更高且比特消耗略少。

## 摘要（原文）

> Non-parametric quantization has received much attention due to its efficiency on parameters and scalability to a large codebook. In this paper, we present a unified formulation of different non-parametric quantization methods through the lens of lattice coding. The geometry of lattice codes explains the necessity of auxiliary loss terms when training auto-encoders with certain existing lookup-free quantization variants such as BSQ. As a step forward, we explore a few possible candidates, including random lattices, generalized Fibonacci lattices, and densest sphere packing lattices. Among all, we find the Leech lattice-based quantization method, which is dubbed as Spherical Leech Quantization ($Λ_{24}$-SQ), leads to both a simplified training recipe and an improved reconstruction-compression tradeoff thanks to its high symmetry and even distribution on the hypersphere. In image tokenization and compression tasks, this quantization approach achieves better reconstruction quality across all metrics than BSQ, the best prior art, while consuming slightly fewer bits. The improvement also extends to state-of-the-art auto-regressive image generation frameworks.

