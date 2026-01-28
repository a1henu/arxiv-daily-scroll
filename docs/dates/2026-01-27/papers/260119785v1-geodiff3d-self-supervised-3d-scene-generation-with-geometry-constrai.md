---
layout: default
title: GeoDiff3D: Self-Supervised 3D Scene Generation with Geometry-Constrained 2D Diffusion Guidance
---

# GeoDiff3D: Self-Supervised 3D Scene Generation with Geometry-Constrained 2D Diffusion Guidance
**arXiv**：[2601.19785v1](https://arxiv.org/abs/2601.19785) · [PDF](https://arxiv.org/pdf/2601.19785.pdf)  
**作者**：Haozhi Zhu, Miaomiao Zhao, Dingyao Liu, Runze Tian, Yan Zhang, Jie Guo, Fenggen Yu  

**一句话要点**：提出GeoDiff3D，利用几何约束的2D扩散引导实现自监督3D场景生成

**关键词**：3D场景生成, 自监督学习, 扩散模型, 几何约束, 体素特征聚合

## 3 点简述
- 现有方法存在结构建模弱、依赖大规模标注数据的问题，导致几何不一致和细节退化
- 使用粗几何作为结构锚点，结合几何约束的2D扩散模型提供纹理参考，无需严格多视图一致性
- 通过体素对齐特征聚合和双重自监督，在减少标注依赖下提升场景连贯性和细节质量

## 摘要（原文）

> 3D scene generation is a core technology for gaming, film/VFX, and VR/AR. Growing demand for rapid iteration, high-fidelity detail, and accessible content creation has further increased interest in this area. Existing methods broadly follow two paradigms - indirect 2D-to-3D reconstruction and direct 3D generation - but both are limited by weak structural modeling and heavy reliance on large-scale ground-truth supervision, often producing structural artifacts, geometric inconsistencies, and degraded high-frequency details in complex scenes. We propose GeoDiff3D, an efficient self-supervised framework that uses coarse geometry as a structural anchor and a geometry-constrained 2D diffusion model to provide texture-rich reference images. Importantly, GeoDiff3D does not require strict multi-view consistency of the diffusion-generated references and remains robust to the resulting noisy, inconsistent guidance. We further introduce voxel-aligned 3D feature aggregation and dual self-supervision to maintain scene coherence and fine details while substantially reducing dependence on labeled data. GeoDiff3D also trains with low computational cost and enables fast, high-quality 3D scene generation. Extensive experiments on challenging scenes show improved generalization and generation quality over existing baselines, offering a practical solution for accessible and efficient 3D scene construction.

