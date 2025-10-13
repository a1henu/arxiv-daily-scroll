---
layout: default
title: Minkowski-MambaNet: A Point Cloud Framework with Selective State Space Models for Forest Biomass Quantification
---

# Minkowski-MambaNet: A Point Cloud Framework with Selective State Space Models for Forest Biomass Quantification
**arXiv**：[2510.09367v1](https://arxiv.org/abs/2510.09367) · [PDF](https://arxiv.org/pdf/2510.09367.pdf)  
**作者**：Jinxiang Tu, Dayong Ren, Fei Shi, Zhenhong Jia, Yahong Ren, Jiwei Qin, Fang He  

**一句话要点**：提出Minkowski-MambaNet框架，结合选择性状态空间模型，从LiDAR点云直接估计森林生物量

**关键词**：点云处理, 选择性状态空间模型, 森林生物量估计, LiDAR数据分析, 深度学习框架

## 3 点简述
- 核心问题：点云中长程依赖建模困难，影响树木区分和生物量估计准确性
- 方法要点：集成Mamba的选择性状态空间模型到Minkowski网络，增强全局上下文编码
- 实验或效果：在丹麦国家森林清单数据上，显著优于现有方法，无需DTM且鲁棒

## 摘要（原文）

> Accurate forest biomass quantification is vital for carbon cycle monitoring.
> While airborne LiDAR excels at capturing 3D forest structure, directly
> estimating woody volume and Aboveground Biomass (AGB) from point clouds is
> challenging due to difficulties in modeling long-range dependencies needed to
> distinguish trees.We propose Minkowski-MambaNet, a novel deep learning
> framework that directly estimates volume and AGB from raw LiDAR. Its key
> innovation is integrating the Mamba model's Selective State Space Model (SSM)
> into a Minkowski network, enabling effective encoding of global context and
> long-range dependencies for improved tree differentiation. Skip connections are
> incorporated to enhance features and accelerate convergence.Evaluated on Danish
> National Forest Inventory LiDAR data, Minkowski-MambaNet significantly
> outperforms state-of-the-art methods, providing more accurate and robust
> estimates. Crucially, it requires no Digital Terrain Model (DTM) and is robust
> to boundary artifacts. This work offers a powerful tool for large-scale forest
> biomass analysis, advancing LiDAR-based forest inventories.

