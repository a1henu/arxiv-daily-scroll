---
layout: default
title: XGrid-Mapping: Explicit Implicit Hybrid Grid Submaps for Efficient Incremental Neural LiDAR Mapping
---

# XGrid-Mapping: Explicit Implicit Hybrid Grid Submaps for Efficient Incremental Neural LiDAR Mapping
**arXiv**：[2512.20976v1](https://arxiv.org/abs/2512.20976) · [PDF](https://arxiv.org/pdf/2512.20976.pdf)  
**作者**：Zeqing Song, Zhongmiao Yan, Junyuan Deng, Songpengcheng Xia, Xiang Mu, Jingyi Xu, Qi Wu, Ling Pei  

**一句话要点**：提出XGrid-Mapping混合网格框架以解决大规模增量神经LiDAR映射的效率与质量挑战

**关键词**：神经LiDAR映射, 混合网格表示, 增量映射, VDB结构, 蒸馏对齐, 动态移除模块

## 3 点简述
- 核心问题：现有神经LiDAR映射方法依赖密集隐式表示或体素引导，导致效率低或实时性差
- 方法要点：结合稀疏网格提供几何先验与隐式密集网格丰富表示，基于VDB结构和子图组织降低计算负载
- 实验或效果：通过蒸馏对齐和动态移除模块增强一致性，实验显示在映射质量和效率上优于现有方法

## 摘要（原文）

> Large-scale incremental mapping is fundamental to the development of robust and reliable autonomous systems, as it underpins incremental environmental understanding with sequential inputs for navigation and decision-making. LiDAR is widely used for this purpose due to its accuracy and robustness. Recently, neural LiDAR mapping has shown impressive performance; however, most approaches rely on dense implicit representations and underutilize geometric structure, while existing voxel-guided methods struggle to achieve real-time performance. To address these challenges, we propose XGrid-Mapping, a hybrid grid framework that jointly exploits explicit and implicit representations for efficient neural LiDAR mapping. Specifically, the strategy combines a sparse grid, providing geometric priors and structural guidance, with an implicit dense grid that enriches scene representation. By coupling the VDB structure with a submap-based organization, the framework reduces computational load and enables efficient incremental mapping on a large scale. To mitigate discontinuities across submaps, we introduce a distillation-based overlap alignment strategy, in which preceding submaps supervise subsequent ones to ensure consistency in overlapping regions. To further enhance robustness and sampling efficiency, we incorporate a dynamic removal module. Extensive experiments show that our approach delivers superior mapping quality while overcoming the efficiency limitations of voxel-guided methods, thereby outperforming existing state-of-the-art mapping methods.

