---
layout: default
title: Real-Time Loop Closure Detection in Visual SLAM via NetVLAD and Faiss
---

# Real-Time Loop Closure Detection in Visual SLAM via NetVLAD and Faiss
**arXiv**：[2602.01673v1](https://arxiv.org/abs/2602.01673) · [PDF](https://arxiv.org/pdf/2602.01673.pdf)  
**作者**：Enguang Fan  

**一句话要点**：提出基于NetVLAD和Faiss的实时闭环检测方法，以提升视觉SLAM的准确性和鲁棒性。

**关键词**：视觉SLAM, 闭环检测, NetVLAD, Faiss, 实时系统, 视觉地点识别

## 3 点简述
- 核心问题：传统词袋方法在视觉变化和感知混淆下性能下降，深度学习描述符计算成本高，难以实时应用。
- 方法要点：采用NetVLAD作为描述符，结合Faiss加速最近邻搜索，实现实时查询速度。
- 实验或效果：在KITTI数据集上评估，NetVLAD相比DBoW提高了准确性和鲁棒性，并引入细粒度Top-K精度-召回曲线以更好反映闭环检测场景。

## 摘要（原文）

> Loop closure detection (LCD) is a core component of simultaneous localization and mapping (SLAM): it identifies revisited places and enables pose-graph constraints that correct accumulated drift. Classic bag-of-words approaches such as DBoW are efficient but often degrade under appearance change and perceptual aliasing. In parallel, deep learning-based visual place recognition (VPR) descriptors (e.g., NetVLAD and Transformer-based models) offer stronger robustness, but their computational cost is often viewed as a barrier to real-time SLAM. In this paper, we empirically evaluate NetVLAD as an LCD module and compare it against DBoW on the KITTI dataset. We introduce a Fine-Grained Top-K precision-recall curve that better reflects LCD settings where a query may have zero or multiple valid matches. With Faiss-accelerated nearestneighbor search, NetVLAD achieves real-time query speed while improving accuracy and robustness over DBoW, making it a practical drop-in alternative for LCD in SLAM.

