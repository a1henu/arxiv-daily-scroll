---
layout: default
title: BuildMamba: A Visual State-Space Based Model for Multi-Task Building Segmentation and Height Estimation from Satellite Images
---

# BuildMamba: A Visual State-Space Based Model for Multi-Task Building Segmentation and Height Estimation from Satellite Images
**arXiv**：[2603.08523v1](https://arxiv.org/abs/2603.08523) · [PDF](https://arxiv.org/pdf/2603.08523.pdf)  
**作者**：Sinan U. Ulu, A. Enes Doruk, I. Can Yagmur, Bahadir K. Gunturk, Oguz Hanoglu, Hasan F. Ates  

**一句话要点**：提出BuildMamba模型，利用视觉状态空间模型实现卫星图像多任务建筑分割与高度估计

**关键词**：建筑分割, 高度估计, 视觉状态空间模型, 卫星图像, 多任务学习, 城市重建

## 3 点简述
- 核心问题：单视图RGB卫星图像中建筑分割和高度估计因结构多变和全局上下文建模计算成本高而困难，现有方法存在边界模糊和高层建筑低估问题。
- 方法要点：引入Mamba注意力模块、空间感知Mamba-FPN和掩码感知高度细化模块，通过状态空间扫描增强结构耦合与计算效率。
- 实验或效果：在DFC23基准测试中达到IoU 0.93和RMSE 1.77米，高度估计性能超越现有最佳方法0.82米，验证了模型在大规模3D城市重建中的鲁棒性和可扩展性。

## 摘要（原文）

> Accurate building segmentation and height estimation from single-view RGB satellite imagery are fundamental for urban analytics, yet remain ill-posed due to structural variability and the high computational cost of global context modeling. While current approaches typically adapt monocular depth architectures, they often suffer from boundary bleeding and systematic underestimation of high-rise structures. To address these limitations, we propose BuildMamba, a unified multi-task framework designed to exploit the linear-time global modeling of visual state-space models. Motivated by the need for stronger structural coupling and computational efficiency, we introduce three modules: a Mamba Attention Module for dynamic spatial recalibration, a Spatial-Aware Mamba-FPN for multi-scale feature aggregation via gated state-space scans, and a Mask-Aware Height Refinement module using semantic priors to suppress height artifacts. Extensive experiments demonstrate that BuildMamba establishes a new performance upper bound across three benchmarks. Specifically, it achieves an IoU of 0.93 and RMSE of 1.77~m on DFC23 benchmark, surpassing state-of-the-art by 0.82~m in height estimation. Simulation results confirm the model's superior robustness and scalability for large-scale 3D urban reconstruction.

