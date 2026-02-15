---
layout: default
title: WorldTree: Towards 4D Dynamic Worlds from Monocular Video using Tree-Chains
---

# WorldTree: Towards 4D Dynamic Worlds from Monocular Video using Tree-Chains
**arXiv**：[2602.11845v1](https://arxiv.org/abs/2602.11845) · [PDF](https://arxiv.org/pdf/2602.11845.pdf)  
**作者**：Qisen Wang, Yifan Zhao, Jia Li  

**一句话要点**：提出WorldTree框架，通过树链结构从单目视频构建4D动态世界

**关键词**：单目视频重建, 4D动态世界, 时空分解, 树链结构, 层次化优化

## 3 点简述
- 核心问题：单目动态重建缺乏统一的时空分解框架，现有方法在整体时间优化或耦合空间组合上存在局限
- 方法要点：结合时间分割树和空间祖先链，实现从粗到细的层次化时空分解与运动表示
- 实验或效果：在NVIDIA-LS和DyCheck数据集上，LPIPS和mLPIPS指标分别提升8.26%和9.09%

## 摘要（原文）

> Dynamic reconstruction has achieved remarkable progress, but there remain challenges in monocular input for more practical applications. The prevailing works attempt to construct efficient motion representations, but lack a unified spatiotemporal decomposition framework, suffering from either holistic temporal optimization or coupled hierarchical spatial composition. To this end, we propose WorldTree, a unified framework comprising Temporal Partition Tree (TPT) that enables coarse-to-fine optimization based on the inheritance-based partition tree structure for hierarchical temporal decomposition, and Spatial Ancestral Chains (SAC) that recursively query ancestral hierarchical structure to provide complementary spatial dynamics while specializing motion representations across ancestral nodes. Experimental results on different datasets indicate that our proposed method achieves 8.26% improvement of LPIPS on NVIDIA-LS and 9.09% improvement of mLPIPS on DyCheck compared to the second-best method. Code: https://github.com/iCVTEAM/WorldTree.

