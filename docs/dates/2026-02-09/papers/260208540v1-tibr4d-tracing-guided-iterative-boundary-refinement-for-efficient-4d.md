---
layout: default
title: TIBR4D: Tracing-Guided Iterative Boundary Refinement for Efficient 4D Gaussian Segmentation
---

# TIBR4D: Tracing-Guided Iterative Boundary Refinement for Efficient 4D Gaussian Segmentation
**arXiv**：[2602.08540v1](https://arxiv.org/abs/2602.08540) · [PDF](https://arxiv.org/pdf/2602.08540.pdf)  
**作者**：He Wu, Xia Yan, Yanghui Xu, Liegang Xia, Jiazhou Chen  

**一句话要点**：提出TIBR4D框架，通过迭代边界精炼实现高效4D高斯场景分割

**关键词**：4D高斯分割, 迭代边界精炼, 无学习框架, 动态场景, 对象分割

## 3 点简述
- 核心问题：动态4D高斯场景中对象分割面临运动复杂、遮挡和边界模糊的挑战
- 方法要点：采用两阶段迭代边界精炼，包括时间片段级高斯实例追踪和帧级渲染范围控制
- 实验或效果：在HyperNeRF和Neu3D数据集上验证，相比SOTA方法产生更清晰边界和更高效率

## 摘要（原文）

> Object-level segmentation in dynamic 4D Gaussian scenes remains challenging due to complex motion, occlusions, and ambiguous boundaries. In this paper, we present an efficient learning-free 4D Gaussian segmentation framework that lifts video segmentation masks to 4D spaces, whose core is a two-stage iterative boundary refinement, TIBR4D. The first stage is an Iterative Gaussian Instance Tracing (IGIT) at the temporal segment level. It progressively refines Gaussian-to-instance probabilities through iterative tracing, and extracts corresponding Gaussian point clouds that better handle occlusions and preserve completeness of object structures compared to existing one-shot threshold-based methods. The second stage is a frame-wise Gaussian Rendering Range Control (RCC) via suppressing highly uncertain Gaussians near object boundaries while retaining their core contributions for more accurate boundaries. Furthermore, a temporal segmentation merging strategy is proposed for IGIT to balance identity consistency and dynamic awareness. Longer segments enforce stronger multi-frame constraints for stable identities, while shorter segments allow identity changes to be captured promptly. Experiments on HyperNeRF and Neu3D demonstrate that our method produces accurate object Gaussian point clouds with clearer boundaries and higher efficiency compared to SOTA methods.

