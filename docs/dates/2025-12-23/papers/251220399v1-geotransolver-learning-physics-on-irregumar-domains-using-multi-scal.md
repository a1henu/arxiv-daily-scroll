---
layout: default
title: GeoTransolver: Learning Physics on Irregumar Domains Using Multi-scale Geometry Aware Physics Attention Transformer
---

# GeoTransolver: Learning Physics on Irregumar Domains Using Multi-scale Geometry Aware Physics Attention Transformer
**arXiv**：[2512.20399v1](https://arxiv.org/abs/2512.20399) · [PDF](https://arxiv.org/pdf/2512.20399.pdf)  
**作者**：Corey Adams, Rishikesh Ranade, Ram Cherukuri, Sanjay Choudhry  

**一句话要点**：提出GeoTransolver，通过多尺度几何感知物理注意力Transformer解决不规则域高保真代理建模问题。

**关键词**：几何感知注意力, 物理注意力Transformer, 不规则域建模, 多尺度查询, 代理建模, CAE应用

## 3 点简述
- 核心问题：不规则域和非线性物理机制下的高保真代理建模挑战。
- 方法要点：用GALE替代标准注意力，结合物理感知自注意力和多尺度球查询的交叉注意力。
- 实验或效果：在多个基准测试中优于现有方法，提升精度、鲁棒性和数据效率。

## 摘要（原文）

> We present GeoTransolver, a Multiscale Geometry-Aware Physics Attention Transformer for CAE that replaces standard attention with GALE, coupling physics-aware self-attention on learned state slices with cross-attention to a shared geometry/global/boundary-condition context computed from multi-scale ball queries (inspired by DoMINO) and reused in every block. Implemented and released in NVIDIA PhysicsNeMo, GeoTransolver persistently projects geometry, global and boundary condition parameters into physical state spaces to anchor latent computations to domain structure and operating regimes. We benchmark GeoTransolver on DrivAerML, Luminary SHIFT-SUV, and Luminary SHIFT-Wing, comparing against Domino, Transolver (as released in PhysicsNeMo), and literature-reported AB-UPT, and evaluate drag/lift R2 and Relative L1 errors for field variables. GeoTransolver delivers better accuracy, improved robustness to geometry/regime shifts, and favorable data efficiency; we include ablations on DrivAerML and qualitative results such as contour plots and design trends for the best GeoTransolver models. By unifying multiscale geometry-aware context with physics-based attention in a scalable transformer, GeoTransolver advances operator learning for high-fidelity surrogate modeling across complex, irregular domains and non-linear physical regimes.

