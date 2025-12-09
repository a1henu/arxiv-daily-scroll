---
layout: default
title: Multi-view Pyramid Transformer: Look Coarser to See Broader
---

# Multi-view Pyramid Transformer: Look Coarser to See Broader
**arXiv**：[2512.07806v1](https://arxiv.org/abs/2512.07806) · [PDF](https://arxiv.org/pdf/2512.07806.pdf)  
**作者**：Gyeongjin Kang, Seungkwon Yang, Seungtae Nam, Younggeun Lee, Jungwoo Kim, Eunbyung Park  

**一句话要点**：提出多视图金字塔变换器，通过双层次结构从多图像高效重建大3D场景。

**关键词**：多视图3D重建, 变换器架构, 层次化表示, 计算效率, 可扩展性, 3D高斯泼溅

## 3 点简述
- 核心问题：从数十至数百张图像直接重建大规模3D场景，需平衡计算效率与表示丰富性。
- 方法要点：结合局部到全局的视图间层次和细到粗的视图内层次，实现视角扩展与信息聚合。
- 实验或效果：在多样化数据集上验证，结合3D高斯泼溅实现高效、可扩展的先进重建质量。

## 摘要（原文）

> We propose Multi-view Pyramid Transformer (MVP), a scalable multi-view transformer architecture that directly reconstructs large 3D scenes from tens to hundreds of images in a single forward pass. Drawing on the idea of ``looking broader to see the whole, looking finer to see the details," MVP is built on two core design principles: 1) a local-to-global inter-view hierarchy that gradually broadens the model's perspective from local views to groups and ultimately the full scene, and 2) a fine-to-coarse intra-view hierarchy that starts from detailed spatial representations and progressively aggregates them into compact, information-dense tokens. This dual hierarchy achieves both computational efficiency and representational richness, enabling fast reconstruction of large and complex scenes. We validate MVP on diverse datasets and show that, when coupled with 3D Gaussian Splatting as the underlying 3D representation, it achieves state-of-the-art generalizable reconstruction quality while maintaining high efficiency and scalability across a wide range of view configurations.

