---
layout: default
title: Flow Field Reconstruction via Voronoi-Enhanced Physics-Informed Neural Networks with End-to-End Sensor Placement Optimization
---

# Flow Field Reconstruction via Voronoi-Enhanced Physics-Informed Neural Networks with End-to-End Sensor Placement Optimization
**arXiv**：[2603.09371v1](https://arxiv.org/abs/2603.09371) · [PDF](https://arxiv.org/pdf/2603.09371.pdf)  
**作者**：Renjie Xiao, Bingteng Sun, Yiling Chen, Lin Lu, Qiang Du, Junqiang Zhu  

**一句话要点**：提出Voronoi增强物理信息神经网络，通过端到端传感器布局优化实现高精度流场重建

**关键词**：流场重建, 物理信息神经网络, 传感器布局优化, Voronoi剖分, 端到端学习, 流体动力学

## 3 点简述
- 核心问题：稀疏传感器测量和传感器失效挑战流场重建精度与鲁棒性
- 方法要点：结合可微分软Voronoi构造和质心Voronoi剖分，实现传感器布局与PINN的端到端融合
- 实验或效果：在腔流、血管流和环形旋转流中验证，显著提升重建精度并适应传感器失效

## 摘要（原文）

> (short version abstract, full in article)High-fidelity flow field reconstruction is important in fluid dynamics, but it is challenged by sparse and spatiotemporally incomplete sensor measurements, as well as failures of pre-deployed measurement points that can invalidate pre-trained reconstruction models. Physics-informed neural networks (PINNs) alleviate dependence on large labeled datasets by incorporating governing physics, yet sensor placement optimization, a key factor in reconstruction accuracy and robustness, remains underexplored. In this study, we propose a PINN with Voronoi-enhanced Sensor Optimization (VSOPINN). VSOPINN enables differentiable soft Voronoi construction for sparse sensor data rasterization, end-to-end fusion of centroidal Voronoi tessellation (CVT) with PINNs for adaptive sensor placement, and unified layout optimization for multi-condition flow reconstruction through a shared encoder-multi-decoder architecture. We validate VSOPINN on three representative problems: lid-driven cavity flow, vascular flow, and annular rotating flow. Results show that VSOPINN significantly improves reconstruction accuracy across different Reynolds numbers, adaptively learns effective sensor layouts, and remains robust under partial sensor failure. The study clarifies the intrinsic relationship between sensor placement and reconstruction precision in PINN-based flow field reconstruction.

