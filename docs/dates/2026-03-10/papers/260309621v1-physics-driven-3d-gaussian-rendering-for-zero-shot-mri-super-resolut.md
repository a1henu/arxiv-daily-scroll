---
layout: default
title: Physics-Driven 3D Gaussian Rendering for Zero-Shot MRI Super-Resolution
---

# Physics-Driven 3D Gaussian Rendering for Zero-Shot MRI Super-Resolution
**arXiv**：[2603.09621v1](https://arxiv.org/abs/2603.09621) · [PDF](https://arxiv.org/pdf/2603.09621.pdf)  
**作者**：Shuting Liu, Lei Zhang, Wei Huang, Zhao Zhang, Zizhou Wang  

**一句话要点**：提出基于物理驱动的3D高斯渲染框架，用于零样本MRI超分辨率以平衡数据需求与效率。

**关键词**：MRI超分辨率, 零样本学习, 3D高斯渲染, 物理驱动建模, 体积渲染, 并行计算

## 3 点简述
- 核心问题：现有MRI超分辨率方法在数据对齐需求与计算效率间存在权衡，限制临床应用。
- 方法要点：采用显式高斯表示嵌入组织物理属性，结合物理基础体积渲染和砖块化光栅化，降低参数与计算成本。
- 实验或效果：在公开MRI数据集上验证，展示优越的重建质量和效率，具备临床潜力。

## 摘要（原文）

> High-resolution Magnetic Resonance Imaging (MRI) is vital for clinical diagnosis but limited by long acquisition times and motion artifacts. Super-resolution (SR) reconstructs low-resolution scans into high-resolution images, yet existing methods are mutually constrained: paired-data methods achieve efficiency only by relying on costly aligned datasets, while implicit neural representation approaches avoid such data needs at the expense of heavy computation. We propose a zero-shot MRI SR framework using explicit Gaussian representation to balance data requirements and efficiency. MRI-tailored Gaussian parameters embed tissue physical properties, reducing learnable parameters while preserving MR signal fidelity. A physics-grounded volume rendering strategy models MRI signal formation via normalized Gaussian aggregation. Additionally, a brick-based order-independent rasterization scheme enables highly parallel 3D computation, lowering training and inference costs. Experiments on two public MRI datasets show superior reconstruction quality and efficiency, demonstrating the method's potential for clinical MRI SR.

