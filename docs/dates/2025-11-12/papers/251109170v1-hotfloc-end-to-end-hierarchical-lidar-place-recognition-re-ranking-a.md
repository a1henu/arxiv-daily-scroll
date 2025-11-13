---
layout: default
title: HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests
---

# HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests
**arXiv**：[2511.09170v1](https://arxiv.org/abs/2511.09170) · [PDF](https://arxiv.org/pdf/2511.09170.pdf)  
**作者**：Ethan Griffiths, Maryam Haghighat, Simon Denman, Clinton Fookes, Milad Ramezani  

**一句话要点**：提出HOTFLoc++框架，用于森林环境中的LiDAR地点识别与6-DoF定位

**关键词**：LiDAR地点识别, 6-DoF定位, 八叉树变换器, 多尺度几何验证, 森林环境, 端到端框架

## 3 点简述
- 核心问题：森林环境中LiDAR地点识别易受杂乱、自相似和视角变化影响
- 方法要点：使用八叉树变换器提取分层局部描述符，并引入多尺度几何验证模块
- 实验效果：在CS-Wild-Places数据集上Recall@1达90.7%，定位误差平均降低约2倍

## 摘要（原文）

> This article presents HOTFLoc++, an end-to-end framework for LiDAR place recognition, re-ranking, and 6-DoF metric localisation in forests. Leveraging an octree-based transformer, our approach extracts hierarchical local descriptors at multiple granularities to increase robustness to clutter, self-similarity, and viewpoint changes in challenging scenarios, including ground-to-ground and ground-to-aerial in forest and urban environments. We propose a learnable multi-scale geometric verification module to reduce re-ranking failures in the presence of degraded single-scale correspondences. Our coarse-to-fine registration approach achieves comparable or lower localisation errors to baselines, with runtime improvements of two orders of magnitude over RANSAC for dense point clouds. Experimental results on public datasets show the superiority of our approach compared to state-of-the-art methods, achieving an average Recall@1 of 90.7% on CS-Wild-Places: an improvement of 29.6 percentage points over baselines, while maintaining high performance on single-source benchmarks with an average Recall@1 of 91.7% and 96.0% on Wild-Places and MulRan, respectively. Our method achieves under 2 m and 5 degrees error for 97.2% of 6-DoF registration attempts, with our multi-scale re-ranking module reducing localisation errors by ~2$\times$ on average. The code will be available upon acceptance.

