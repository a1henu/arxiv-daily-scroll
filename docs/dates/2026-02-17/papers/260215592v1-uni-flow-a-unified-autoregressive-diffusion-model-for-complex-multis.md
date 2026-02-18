---
layout: default
title: Uni-Flow: a unified autoregressive-diffusion model for complex multiscale flows
---

# Uni-Flow: a unified autoregressive-diffusion model for complex multiscale flows
**arXiv**：[2602.15592v1](https://arxiv.org/abs/2602.15592) · [PDF](https://arxiv.org/pdf/2602.15592.pdf)  
**作者**：Xiao Xue, Tianyue Yang, Mingyang Gao, Leyu Pan, Maida Wang, Kewei Zhu, Shuo Wang, Jiuling Li, Marco F. P. ten Eikelder, Peter V. Coveney  

**一句话要点**：提出Uni-Flow统一自回归-扩散模型以解决复杂多尺度流建模中长时演化与细尺度结构兼顾的挑战。

**关键词**：多尺度流建模, 自回归-扩散模型, 时空分离, 高分辨率重建, 快于实时推理, 科学机器学习

## 3 点简述
- 核心问题：现有方法难以同时维持长时演化与解析混沌、湍流等流场的细尺度结构。
- 方法要点：通过自回归组件学习低分辨率潜态动力学，扩散组件重建高分辨率物理场，实现时空分离建模。
- 实验或效果：在二维Kolmogorov流、三维湍流通道生成和主动脉缩窄模拟中验证，心血管场景实现秒级快于实时推理。

## 摘要（原文）

> Spatiotemporal flows govern diverse phenomena across physics, biology, and engineering, yet modelling their multiscale dynamics remains a central challenge. Despite major advances in physics-informed machine learning, existing approaches struggle to simultaneously maintain long-term temporal evolution and resolve fine-scale structure across chaotic, turbulent, and physiological regimes. Here, we introduce Uni-Flow, a unified autoregressive-diffusion framework that explicitly separates temporal evolution from spatial refinement for modelling complex dynamical systems. The autoregressive component learns low-resolution latent dynamics that preserve large-scale structure and ensure stable long-horizon rollouts, while the diffusion component reconstructs high-resolution physical fields, recovering fine-scale features in a small number of denoising steps. We validate Uni-Flow across canonical benchmarks, including two-dimensional Kolmogorov flow, three-dimensional turbulent channel inflow generation with a quantum-informed autoregressive prior, and patient-specific simulations of aortic coarctation derived from high-fidelity lattice Boltzmann hemodynamic solvers. In the cardiovascular setting, Uni-Flow enables task-level faster than real-time inference of pulsatile hemodynamics, reconstructing high-resolution pressure fields over physiologically relevant time horizons in seconds rather than hours. By transforming high-fidelity hemodynamic simulation from an offline, HPC-bound process into a deployable surrogate, Uni-Flow establishes a pathway to faster-than-real-time modelling of complex multiscale flows, with broad implications for scientific machine learning in flow physics.

