---
layout: default
title: UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction
---

# UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction
**arXiv**：[2602.02089v1](https://arxiv.org/abs/2602.02089) · [PDF](https://arxiv.org/pdf/2602.02089.pdf)  
**作者**：Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan, Baochang Zhang  

**一句话要点**：提出UrbanGS框架以解决大规模城市场景重建中的几何一致性和可扩展性问题

**关键词**：大规模场景重建, 3D高斯溅射, 几何一致性, 深度正则化, 自适应剪枝, 城市建模

## 3 点简述
- 核心问题：3D高斯溅射扩展至大规模城市场景时面临几何不一致、内存效率低和计算可扩展性差。
- 方法要点：结合深度一致D-正态正则化和自适应高斯剪枝，提升几何精度并减少冗余。
- 实验或效果：在多个城市数据集上验证了渲染质量、几何准确性和内存效率的优越性能。

## 摘要（原文）

> While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical challenges in terms of geometric consistency, memory efficiency, and computational scalability. To address these issues, we present UrbanGS, a scalable reconstruction framework that effectively tackles these challenges for city-scale applications. First, we propose a Depth-Consistent D-Normal Regularization module. Unlike existing approaches that rely solely on monocular normal estimators, which can effectively update rotation parameters yet struggle to update position parameters, our method integrates D-Normal constraints with external depth supervision. This allows for comprehensive updates of all geometric parameters. By further incorporating an adaptive confidence weighting mechanism based on gradient consistency and inverse depth deviation, our approach significantly enhances multi-view depth alignment and geometric coherence, which effectively resolves the issue of geometric accuracy in complex large-scale scenes. To improve scalability, we introduce a Spatially Adaptive Gaussian Pruning (SAGP) strategy, which dynamically adjusts Gaussian density based on local geometric complexity and visibility to reduce redundancy. Additionally, a unified partitioning and view assignment scheme is designed to eliminate boundary artifacts and optimize computational load. Extensive experiments on multiple urban datasets demonstrate that UrbanGS achieves superior performance in rendering quality, geometric accuracy, and memory efficiency, providing a systematic solution for high-fidelity large-scale scene reconstruction.

