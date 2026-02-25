---
layout: default
title: WeirNet: A Large-Scale 3D CFD Benchmark for Geometric Surrogate Modeling of Piano Key Weirs
---

# WeirNet: A Large-Scale 3D CFD Benchmark for Geometric Surrogate Modeling of Piano Key Weirs
**arXiv**：[2602.20714v1](https://arxiv.org/abs/2602.20714) · [PDF](https://arxiv.org/pdf/2602.20714.pdf)  
**作者**：Lisa Lüddecke, Michael Hohmann, Sebastian Eilermann, Jan Tillmann-Mumm, Pezhman Pourabdollah, Mario Oertel, Oliver Niggemann  

**一句话要点**：提出WeirNet数据集以解决钢琴键堰几何代理建模中缺乏大规模基准数据的问题

**关键词**：钢琴键堰, 几何代理建模, CFD基准数据集, 参数化设计, 水力性能预测, 机器学习基准

## 3 点简述
- 核心问题：钢琴键堰水力性能预测依赖三维几何和工况，但现有数据集稀缺，限制代理模型发展。
- 方法要点：构建包含3,794个参数化几何和71,387个CFD模拟的大规模基准数据集，提供多模态数据和标准化任务。
- 实验或效果：基准测试显示基于参数描述符的树回归器精度最高，所有代理模型实现毫秒级推理，大幅加速设计探索。

## 摘要（原文）

> Reliable prediction of hydraulic performance is challenging for Piano Key Weir (PKW) design because discharge capacity depends on three-dimensional geometry and operating conditions. Surrogate models can accelerate hydraulic-structure design, but progress is limited by scarce large, well-documented datasets that jointly capture geometric variation, operating conditions, and functional performance. This study presents WeirNet, a large 3D CFD benchmark dataset for geometric surrogate modeling of PKWs. WeirNet contains 3,794 parametric, feasibility-constrained rectangular and trapezoidal PKW geometries, each scheduled at 19 discharge conditions using a consistent free-surface OpenFOAM workflow, resulting in 71,387 completed simulations that form the benchmark and with complete discharge coefficient labels. The dataset is released as multiple modalities compact parametric descriptors, watertight surface meshes and high-resolution point clouds together with standardized tasks and in-distribution and out-of-distribution splits. Representative surrogate families are benchmarked for discharge coefficient prediction. Tree-based regressors on parametric descriptors achieve the best overall accuracy, while point- and mesh-based models remain competitive and offer parameterization-agnostic inference. All surrogates evaluate in milliseconds per sample, providing orders-of-magnitude speedups over CFD runtimes. Out-of-distribution results identify geometry shift as the dominant failure mode compared to unseen discharge values, and data-efficiency experiments show diminishing returns beyond roughly 60% of the training data. By publicly releasing the dataset together with simulation setups and evaluation pipelines, WeirNet establishes a reproducible framework for data-driven hydraulic modeling and enables faster exploration of PKW designs during the early stages of hydraulic planning.

