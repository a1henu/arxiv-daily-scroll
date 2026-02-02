---
layout: default
title: A Cross-Domain Graph Learning Protocol for Single-Step Molecular Geometry Refinement
---

# A Cross-Domain Graph Learning Protocol for Single-Step Molecular Geometry Refinement
**arXiv**：[2601.22723v1](https://arxiv.org/abs/2601.22723) · [PDF](https://arxiv.org/pdf/2601.22723.pdf)  
**作者**：Chengchun Liu, Wendi Cai, Boxuan Zhao, Fanyang Mo  

**一句话要点**：提出GeoOpt-Net以单步预测DFT精度分子几何结构，加速量子化学工作流

**关键词**：分子几何优化, SE(3)-等变网络, 密度泛函理论, 高通量筛选, 机器学习势能

## 3 点简述
- 核心问题：DFT优化是分子高通量筛选的瓶颈，需高效获取精确几何结构。
- 方法要点：使用SE(3)-等变网络和两阶段训练，结合保真度感知特征调制机制。
- 实验或效果：在外部药物分子上实现亚毫埃RMSD和近零能量偏差，提升DFT收敛率。

## 摘要（原文）

> Accurate molecular geometries are a prerequisite for reliable quantum-chemical predictions, yet density functional theory (DFT) optimization remains a major bottleneck for high-throughput molecular screening. Here we present GeoOpt-Net, a multi-branch SE(3)-equivariant geometry refinement network that predicts DFT-quality structures at the B3LYP/TZVP level of theory in a single forward pass starting from inexpensive initial conformers generated at a low-cost force-field level. GeoOpt-Net is trained using a two-stage strategy in which a broadly pretrained geometric representation is subsequently fine-tuned to approach B3LYP/TZVP-level accuracy, with theory- and basis-set-aware calibration enabled by a fidelity-aware feature modulation (FAFM) mechanism. Benchmarking against representative approaches spanning classical conformer generation (RDKit), semiempirical quantum methods (xTB), data-driven geometry refinement pipelines (Auto3D), and machine-learning interatomic potentials (UMA) on external drug-like molecules demonstrates that GeoOpt-Net achieves sub-milli-Å all-atom RMSD with near-zero B3LYP/TZVP single-point energy deviations, indicating DFT-ready geometries that closely reproduce both structural and energetic references. Beyond geometric metrics, GeoOpt-Net generates initial guesses intrinsically compatible with DFT convergence criteria, yielding nonzero ``All-YES'' convergence rates (65.0\% under loose and 33.4\% under default thresholds), and substantially reducing re-optimization steps and wall-clock time. GeoOpt-Net further exhibits smooth and predictable energy scaling with molecular complexity while preserving key electronic observables such as dipole moments. Collectively, these results establish GeoOpt-Net as a scalable, physically consistent geometry refinement framework that enables efficient acceleration of DFT-based quantum-chemical workflows.

