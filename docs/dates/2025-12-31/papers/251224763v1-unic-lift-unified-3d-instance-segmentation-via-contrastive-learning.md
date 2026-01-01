---
layout: default
title: UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning
---

# UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning
**arXiv**：[2512.24763v1](https://arxiv.org/abs/2512.24763) · [PDF](https://arxiv.org/pdf/2512.24763.pdf)  
**作者**：Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan  

**一句话要点**：提出UniC-Lift框架，通过统一对比学习解决3D实例分割中多视图标签不一致问题。

**关键词**：3D实例分割, 对比学习, 高斯基元, 多视图一致性, 边界优化

## 3 点简述
- 核心问题：多视图2D实例标签不一致导致3D分割性能差。
- 方法要点：引入可学习特征嵌入，结合Embedding-to-Label解码和边界硬挖掘优化。
- 实验或效果：在ScanNet等数据集上优于基线，提升训练效率和分割质量。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) have advanced novel-view synthesis. Recent methods extend multi-view 2D segmentation to 3D, enabling instance/semantic segmentation for better scene understanding. A key challenge is the inconsistency of 2D instance labels across views, leading to poor 3D predictions. Existing methods use a two-stage approach in which some rely on contrastive learning with hyperparameter-sensitive clustering, while others preprocess labels for consistency. We propose a unified framework that merges these steps, reducing training time and improving performance by introducing a learnable feature embedding for segmentation in Gaussian primitives. This embedding is then efficiently decoded into instance labels through a novel "Embedding-to-Label" process, effectively integrating the optimization. While this unified framework offers substantial benefits, we observed artifacts at the object boundaries. To address the object boundary issues, we propose hard-mining samples along these boundaries. However, directly applying hard mining to the feature embeddings proved unstable. Therefore, we apply a linear layer to the rasterized feature embeddings before calculating the triplet loss, which stabilizes training and significantly improves performance. Our method outperforms baselines qualitatively and quantitatively on the ScanNet, Replica3D, and Messy-Rooms datasets.

